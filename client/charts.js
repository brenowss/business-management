var chart_width = 265;
var chart_height = 245;
// Load the Visualization API and the corechart package.
google.charts.load("current", { packages: ["corechart"] });

// Set a callback to run when the Google Visualization API is loaded.
// Each chart will have its own callback function
google.charts.setOnLoadCallback(drawPieChart);

google.charts.setOnLoadCallback(drawBarChart);

google.charts.setOnLoadCallback(drawColumnChart);

google.charts.setOnLoadCallback(drawTrendlineChart);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.

//Pie Chart
function drawPieChart() {
  // Create the data table.
  var data = new google.visualization.DataTable();
  data.addColumn("string", "Topping");
  data.addColumn("number", "Slices");
  data.addRows([
    ["Mushrooms", 3],
    ["Onions", 1],
    ["Olives", 1],
    ["Zucchini", 1],
    ["Pepperoni", 2]
  ]);

  // Set chart options
  var options = {
    title: "How Much Pizza I Ate Last Night",
    width: chart_width,
    height: chart_height,
    is3D: true,
    legend: { alignment: "start" },
    pieSliceTextStyle: { color: "#f5f5f5" },
    fontName: "Montserrat",
    tooltip: { isHtml: true }
  };

  // Instantiate and draw our chart, passing in some options.
  var chart = new google.visualization.PieChart(
    document.getElementById("pie_chart_div")
  );
  chart.draw(data, options);
}

// Bar chart
function drawBarChart() {
  // Create the data table.
  var data = google.visualization.arrayToDataTable([
    ["Element", "Density", { role: "style" }],
    ["Copper", 8.94, "#b87333"],
    ["Silver", 10.49, "silver"],
    ["Gold", 19.3, "gold"],
    ["Platinum", 21.45, "color: #e5e4e2"]
  ]);

  var view = new google.visualization.DataView(data);
  view.setColumns([
    0,
    1,
    { calc: "stringify", sourceColumn: 1, type: "string", role: "annotation" },
    2
  ]);

  var options = {
    title: "Density of Precious Metals",
    width: chart_width,
    height: chart_height,
    bar: { groupWidth: "95%" },
    legend: { position: "none" },
    fontName: "Montserrat",
    tooltip: { isHtml: true }
  };
  var chart = new google.visualization.BarChart(
    document.getElementById("bar_chart_div")
  );
  chart.draw(view, options);
}

// Column chart
function drawColumnChart() {
  var data = google.visualization.arrayToDataTable([
    ["Element", "Density", { role: "style" }],
    ["Copper", 8.94, "#b87333"],
    ["Silver", 10.49, "silver"],
    ["Gold", 19.3, "gold"],
    ["Platinum", 21.45, "color: #e5e4e2"]
  ]);

  var view = new google.visualization.DataView(data);
  view.setColumns([
    0,
    1,
    { calc: "stringify", sourceColumn: 1, type: "string", role: "annotation" },
    2
  ]);

  var options = {
    title: "Density of Precious Metals",
    width: chart_width,
    height: chart_height,
    bar: { groupWidth: "95%" },
    legend: { position: "none" },
    fontName: "Montserrat",
    tooltip: { isHtml: true }
  };
  var chart = new google.visualization.ColumnChart(
    document.getElementById("column_chart_div")
  );
  chart.draw(view, options);
}

//Trendline chart
function drawTrendlineChart() {
    var data = google.visualization.arrayToDataTable([
        ['X', 'Y', 'Z'],
        [0, 4, 5],
        [1, 2, 6],
        [2, 4, 8],
        [3, 6, 10],
        [4, 4, 11],
        [5, 8, 13],
        [6, 12, 15],
        [7, 15, 19],
        [8, 25, 21],
        [9, 34, 23],
        [10, 50, 27]
      ]);

      var options = {
        title: "Trendline of something",
        height: chart_height,
        width: chart_width,
        fontName: "Montserrat",
        legend: 'none',
        colors: ['#9575cd', '#33ac71'],
        pointShape: 'diamond',
        trendlines: {
          0: {
            type: 'exponential',
            pointSize: 20,
            opacity: 0.6,
            pointsVisible: false
          },
          1: {
            type: 'linear',
            pointSize: 10,
            pointsVisible: true
          }
        }
      };

      var chart = new google.visualization.ScatterChart(document.getElementById('trendline_chart_div'));

      chart.draw(data, options);
}
