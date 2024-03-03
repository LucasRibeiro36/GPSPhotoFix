# GPSPhotoFix

# Image GeoTagging Web Application

This is a simple Flask web application for uploading images and updating their GPS coordinates (latitude and longitude). The application utilizes the [GPSPhoto](https://pypi.org/project/gpsphoto/) library for extracting and modifying GPS data in images.

## Features

1. **Image Upload**: Users can upload images through the web interface.

2. **GPS Coordinates**: Users can input GPS coordinates (latitude and longitude) for the uploaded image.

3. **Image Processing**: The application processes uploaded images, updates their GPS data, and stores them in the 'uploads' directory.

4. **Download**: Users can download the processed images with updated GPS information.

5. **Automatic Deletion**: An automatic background thread runs to delete images older than 24 hours to manage storage.

## Prerequisites

Make sure you have the necessary Python packages installed. You can install them using the following:

```bash
pip install Flask GPSPhoto pillow
```

## Usage

1. Run the application using the following command:

    ```bash
    python app.py
    ```

2. Open your browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Upload an image and provide the GPS coordinates.

4. The application will process the image, update the GPS information, and display the result.

5. You can download the processed image by clicking on the download link.

## Important Note

Ensure that the 'uploads' directory exists in the same directory as your script. This directory is used to store the processed images.

## Dependencies

- [Flask](https://flask.palletsprojects.com/): Web framework for Python.
- [GPSPhoto](https://pypi.org/project/gpsphoto/): Library for accessing and modifying GPS information in photos.
- [Pillow](https://pillow.readthedocs.io/): Python Imaging Library fork for opening, manipulating, and saving many different image file formats.

## Author

Your Name

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
