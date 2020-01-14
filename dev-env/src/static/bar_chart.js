new Chart(document.getElementById("bar-chart"), {
  type: 'bar',
  data: {
    labels: barData.labels,
    datasets: [
      {
        label: "Time (minutes)",
        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850", "#ff0", "#f02e85"],
        data: barData.data
      }
    ]
  },
  options: {
    legend: {
      display: false,
    },
    title: {
      display: true,
      text: 'Raspberry PI LED time on',
      fontColor: "#FFFFFF"
    },
    responsive: true,
    scales: {
      yAxes: [{
        scaleLabel: {
          display: true,
          labelString: "Minutes",
          fontColor: "#FFFFFF"
        },
        ticks: {
          beginAtZero: true,
          fontColor: "#ffffff"
        }
      }],
    xAxes: [{
      scaleLabel: {
        display: true,
        labelString: "Days of the week",
        fontColor: "#FFFFFF"
      },
      ticks: {
        fontColor: "#ffffff"
      }}]
    }
  }
});


<canvas id="bar-chart" width="600" height="400"></canvas>
<script>


barData = {
  labels : [
       {% for item in labels %}
        "{{ item }}",
       {% endfor %}
     ],
     data : [
            {% for item in values %}
               "{{ item }}",
              {% endfor %} ]
   }


</script>
