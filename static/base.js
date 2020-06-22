var dynamicColors = function() {
    var r = Math.floor(Math.random() * 255);
    var g = Math.floor(Math.random() * 255);
    var b = Math.floor(Math.random() * 255);
    return "rgb(" + r + "," + g + "," + b + ")";
 };

var currentCtx = document.getElementById('currentchart').getContext('2d');
var tickers = ['AAPL', 'MSFT', 'AMZN', 'NFLX', 'USD'];
var percentages = [];
var colors = [];

for (var i in tickers) {
    percentages.push(20);
    colors.push(dynamicColors());
}
var currentChart = new Chart(currentCtx, {
    type: 'doughnut',
    data: {
        labels: tickers,
        datasets: [{
            label: 'Current Portfolio',
            backgroundColor: colors,
            borderColor: 'rgb(255, 99, 132)',
            data: percentages
        }]
    },
    options: {}
});

var nextCtx = document.getElementById('nextchart').getContext('2d');
var nextChart = new Chart(nextCtx, {
    type: 'doughnut',
    data: {
        labels: tickers,
        datasets: [{
            label: 'Current Portfolio',
            backgroundColor: colors,
            borderColor: 'rgb(255, 99, 132)',
            data: percentages
        }]
    },
    options: {}
});