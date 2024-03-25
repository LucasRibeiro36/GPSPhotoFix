from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory
from GPSPhoto import gpsphoto
import os
import datetime
import threading
import time
from PIL import Image

app = Flask(__name__)

# Store the creation time of each uploaded image
image_creation_times = {}

def change_location(image_path, coordinates):
    photo = gpsphoto.GPSPhoto(image_path)
    timestamp = datetime.datetime.now().strftime('%Y:%m:%d %H:%M:%S')
    
    info = gpsphoto.GPSInfo((coordinates["latitude"], coordinates["longitude"]), timeStamp=timestamp)
    photo.modGPSData(info, image_path)

def changeFileName(image_path, new_name):
    os.rename(image_path, new_name)
    return new_name

def delete_old_images():
    while True:
        time.sleep(60 * 60)  # Sleep for 1 hour (adjust as needed)
        current_time = time.time()
        
        for filename, creation_time in list(image_creation_times.items()):
            if current_time - creation_time > 24 * 60 * 60:  # Check if older than 24 hours
                image_path = os.path.join('uploads', filename)
                os.remove(image_path)
                del image_creation_times[filename]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        latitude = float(request.form['latitude'])
        longitude = float(request.form['longitude'])
        name = request.form['name']
        coordinates = {'latitude': latitude, 'longitude': longitude}
        
        image = request.files['image']
        image_path = os.path.join('uploads', image.filename)
        image.save(image_path)
        image_path = changeFileName(image_path, os.path.join('uploads', name + '.jpg'))
        
        if image_path.lower().endswith(".png"):
            jpeg_path = image_path.replace(".png", ".jpg")
            with Image.open(image_path) as img:
                img.convert("RGB").save(jpeg_path, "JPEG")
            os.remove(image_path)
            image_path = jpeg_path
            change_location(image_path, coordinates)
            image_creation_times[image_path] = time.time()
        else:
            change_location(image_path, coordinates)

        # Record the creation time of the uploaded image
        image_creation_times[image.filename] = time.time()

        return render_template('index.html', image_path=image_path, os=os)

    return render_template('index.html')

@app.route('/download/<filename>')
def download(filename):
    image_path = os.path.join('uploads', filename)
    return send_file(image_path, as_attachment=True)

@app.route("/uploads/<filename>")
def uploads(filename):
    return send_from_directory("uploads", filename)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


# Start the thread to delete old images
delete_thread = threading.Thread(target=delete_old_images)
delete_thread.start()

if __name__ == '__main__':
    app.run(debug=True)
