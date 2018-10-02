var year = [20,30];
var africa = [100,200];

var ctx = document.getElementById('myChart');
var myChart = new Chart(ctx,
  type: 'line',
  data: {
    labels: years,
    datasets: [
      {
        data: africa
      }
    ]
  }
});
