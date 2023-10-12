var stats_year = {};
var font_size = 16;

var chart = init(dataGlobal);

function init(data) {
    stats_ref = refactor_stats(data);
    x = stats_ref[0];
    stats = stats_ref[1];
    stats_year[current_school_year] = stats;
    chart = chart_stats(x, stats);
    return chart;
}

function update_stats(year) {
    setSmallLoading(true);
    var stats = {};
    if (year in stats_year) {
        stats = stats_year[year];
        let dts = make_datasets(stats);
        chart.data.datasets = dts;
        chart.update();
        setSmallLoading(false);
    } else {
        $.ajax({
            url: "/get-stats?year=" + year + "-" + (parseInt(year) + 1) + "&tab=" + JSON.stringify(tab_id_nameType),
            type: "GET",
            success: function (data) {
                data = refactor_stats(data);
                stats = data[1];
                stats_year[year] = stats;
                let dts = make_datasets(stats);
                chart.data.datasets = dts;
                chart.update();
                setSmallLoading(false);
            },
            error: function (error_data) {
                console.log("error");
                console.log(error_data);
                return false;
            }
        });
    }
    return true;
}

function refactor_stats(stats_name_T_size) {
    var stats_T_sizes = {};
    var x = [];
    for (let name in stats_name_T_size) {
        x.push(name);

        stats_T_size_extracted = stats_name_T_size[name];
        for (T in stats_T_size_extracted) {
            if (!(T in stats_T_sizes)) {
                stats_T_sizes[T] = [];
            }
            stats_T_sizes[T].push(stats_T_size_extracted[T]);
        }
    }
    return [x, stats_T_sizes];
}

function make_datasets(stats) {

    var dts = [];
    var colors = [
        'rgba(255, 99, 132, 0.5)',
        'rgba(54, 162, 235, 0.5)',
        'rgba(255, 206, 86, 0.5)',
        'rgba(75, 192, 192, 0.5)',
        'rgba(153, 102, 255, 0.5)',
        'rgba(255, 159, 64, 0.5)'
    ];

    for (T in stats) {
        dt = {
            label: T,
            data: stats[T],
            backgroundColor: [colors[T]],
            borderColor: [colors[T]],
            borderWidth: 2,
            spanGaps: true
          };
        dts.push(dt);
    }

    return dts;
}

function chart_stats(x, stats) {
    var ctx = document.getElementById('myChart').getContext('2d');
    var dts = make_datasets(stats);
    var chartConfig = {
        type: 'line',
        data: {
            labels: x,
            datasets: dts
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    ticks: {
                        font: {
                            size: font_size
                        }
                    }
                },
                y: {
                    type: 'logarithmic',
                    min: .9
                }
            },
            plugins: {
                legend: {
                    position: "top",
                    align: "start",
                    labels: {
                        font: {
                            size: font_size
                        }
                    }
                }
            }
        }
    }

    var myChart = new Chart(ctx, chartConfig);
    return myChart;
}

function getSmallLoader() {
    return document.getElementById("small-loader");
}

function setSmallLoading(change) {
    var smallLoader = getSmallLoader();
    if (change) {
        smallLoader.style.display = "block";
    } else {
        smallLoader.style.display = "none";
    }
}
