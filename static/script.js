function performReverseGeocoding() {
    var addressInput = document.getElementById('address');
    var longitudeInput = document.querySelector("body > div.row > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > input");
    var latitudeInput = document.querySelector("body > div.row > div:nth-child(1) > form:nth-child(3) > div:nth-child(2) > input");

    
    var address = addressInput.value;

    var apiUrl = `https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(address)}&format=json&polygon=1&addressdetails=1`;

    var xhr = new XMLHttpRequest();
    xhr.open('GET', apiUrl, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var results = JSON.parse(xhr.responseText);

            if (results.length > 0) {
                var latitude = results[0].lat;
                var longitude = results[0].lon;

                // Exibir os resultados (substitua isso pelo que desejar)
                latitudeInput.value = latitude;
                longitudeInput.value = longitude;

            } else {
                alert('Nenhum resultado encontrado para o endereço fornecido.');
            }
        }
    };
    xhr.send();
}

document.getElementById('search').addEventListener('click', performReverseGeocoding);
