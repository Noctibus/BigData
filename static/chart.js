var genres = Object.keys(genre_number);
var counts = Object.values(genre_number);
var danse =  Object.values(genre_danse);
console.log(genre_danse);
var ctx1 = document.getElementById('myChart1').getContext('2d');
var ctx2 = document.getElementById('myChart2').getContext('2d');
var color = 'rgba(42,18,138, 1)';


var myChart = new Chart(ctx1, {
    type: 'bar',
    data: {
        labels: genres,
        datasets: [{
            label: 'Nombre de musiques par genre',
            data: counts,
            backgroundColor: color,
            borderColor: color,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
            }
        }
    }
});

var myChart = new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: genres,
        datasets: [{
            label: 'Nombre de musiques par genre',
            data: danse,
            backgroundColor: color,
            borderColor: color,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});