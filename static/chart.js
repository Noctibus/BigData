var genres = Object.keys(genre_number);
var counts = Object.values(genre_number);
var danse =  Object.values(genre_danse);
console.log(genre_danse);
var ctx1 = document.getElementById('myChart1').getContext('2d');
var ctx2 = document.getElementById('myChart2').getContext('2d');

    
var myChart = new Chart(ctx1, {
    type: 'bar',
    data: {
        labels: genres,
        datasets: [{
            label: 'Nombre de musiques par genre',
            data: counts,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
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

var myChart = new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: genres,
        datasets: [{
            label: 'Nombre de musiques par genre',
            data: danse,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
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