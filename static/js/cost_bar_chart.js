$(function () {
    $('#cost_bar_chart').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'Average Cost for Ad Set'
        },
        subtitle: {
            
        },
        xAxis: {
            categories: [
                'ABSOLUTE_OCPM',
                'MULTI_PREMIUM',
                'CPA',
                'CPC',
                'CPM',
                'None'
            ],
            crosshair: true
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Cost (USD)'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f} USD </b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: 'Per Result',
            data: [1.451900, 0.232911, 1.348726, 0.821144, 1.899272, 1.439996]

        }, {
            name: 'Per Total Action',
            data: [0.608176, 0.169653, 0.366932, 0.197947, 0.766964, 0.592445]

        }]
    });
});
