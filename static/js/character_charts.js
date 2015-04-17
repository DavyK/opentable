$(function () {
    $('#games-played-chart').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: 0,
            plotShadow: false,
            spacingTop:0,
        },
        title: {
            text: 'Games<br>Played',
            style: {'font-size': '12px;'},
            align: 'center',
            verticalAlign: 'middle',
            y: 20
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                dataLabels: {
                    enabled: true,
                    distance: 0,
                    style: {
                        fontWeight: 'bold',
                        color: 'black',

                    }
                },
                startAngle: -90,
                endAngle: 90,
                center: ['50%', '75%']
            }
        },
        series: [{
            type: 'pie',
            name: 'games',
            innerSize: '40%',
            data: [
                ['Not Played',  sessions_out],
                ['Played',      sessions_in]
            ]
        }]
    });
});