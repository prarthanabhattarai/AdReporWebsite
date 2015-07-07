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
            categories: ['CPC','CPM','CPA','ABSOLUTE_OCPM','MULTI_PREMIUM'],
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
            data: cost_per_result

        }, {
            name: 'Per Total Action',
            data: cost_per_action

        }]
    });
});
