
# encoding=utf8  
# coding=UTF-8



CONTEUDO_JS = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.3.0/Chart.bundle.js"></script>
<div class="container">
  <canvas id="examChart"></canvas>
</div>

<script>
    var options = {month: 'numeric', day: 'numeric', year:'numeric' };
    var ctx = document.getElementById("examChart").getContext("2d");
    var yLabels = {
            0 : 'Aberta', 1 : 'Em Análise', 2 : 'Em Atendimento', 3 : 'Entregue', 4 : 'Em Homologação',
            5 : 'Homologada e Aguardando Implantação', 6 : 'Em Implantação'
        }
    var myChart = new Chart(ctx, {
      type: 'line',        
      data: {
        labels: [],
        datasets: [{
          label: 'Demo',          
          data: [{
                x: new Date("2018-05-17"),
                y: 0 
              },
              {
                x: new Date("2018-05-22"),
                y: 1
              },
              {
                x: new Date("2018-05-25"),
                y: 1
              },
              {
                x: new Date("2018-05-28"),
                y: 2
              }
          ],
          borderColor: [
          '#4dc9f6'
          ],
          fill: false,
          borderWidth: 1
        }]
      },
      options: { 
        elements: {
          line: {
              tension: 0
          },              
        },
        scales: {
            yAxes: [{
                ticks: {
                    callback: function(value, index, values) {
                        // for a value (tick) equals to 8
                        return yLabels[value];
                        // 'junior-dev' will be returned instead and displayed on your chart
                    }
                }
            }],
            xAxes: [{
                type: 'time'}],
        }
}
    });
</script>

"""