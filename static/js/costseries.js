$(function () {
    $('#costseries').highcharts({
        chart: {
            zoomType: 'x'
        },
        title: {
            text: 'Cost per unique click for Ad Set'
        },
        subtitle: {
            text: document.ontouchstart === undefined ?
                    'Click and drag in the plot area to zoom in' :
                    'Pinch the chart to zoom in'
        },
        xAxis: {
            type: 'datetime',
            minRange: 1 * 24 * 3600000 // fourteen days
        },
        yAxis: {
            title: {
                text: 'Cost in USD'
            }
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            area: {
                fillColor: {
                    linearGradient: { x1: 0, y1: 0, x2: 0, y2: 1},
                    stops: [
                        [0, Highcharts.getOptions().colors[0]],
                        [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                    ]
                },
                marker: {
                    radius: 2
                },
                lineWidth: 1,
                states: {
                    hover: {
                        lineWidth: 1
                    }
                },
                threshold: null
            }
        },

        series: [{
            type: 'line',
            name: 'Cost Per Unique Click',
            pointInterval: 24 * 3600 * 1000,
            pointStart: Date.UTC(2015, 5, 2),
            data: cost_data
        }]
    });
});
