var map = L.map('map').setView([35.49697602037354, 51.22930290094908], 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
var marker = L.marker([35.49697602037354, 51.22930290094908]).addTo(map);