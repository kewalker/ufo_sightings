var width = 960,
    height = 500;

var projection = d3.geo.mercator()
    .center([0, 5 ])
    .scale(200)
    .rotate([-180,0]);

var map = d3.select("#map").append("svg")
    .attr("width", width)
    .attr("height", height);

var path = d3.geo.path()
    .projection(projection);

var g2 = map.append("g");

// load and display the World
d3.json("data/world-50m.json", function(error, topology) {

// load and display the cities
// d3.csv("cities.csv", function(error, data) {
//     g.selectAll("circle")
//        .data(data)
//        .enter()
//        .append("a")
//           .attr("xlink:href", function(d) {
//             return "https://www.google.com/search?q="+d.city;}
//           )
//        .append("circle")
//        .attr("cx", function(d) {
//                return projection([d.lon, d.lat])[0];
//        })
//        .attr("cy", function(d) {
//                return projection([d.lon, d.lat])[1];
//        })
//        .attr("r", 5)
//        .style("fill", "red");
// });

g2.selectAll("path")
      .data(topojson.object(topology, topology.objects.countries)
          .geometries)
    .enter()
      .append("path")
      .attr("d", path)
});

// zoom and pan
var zoom = d3.behavior.zoom()
    .on("zoom",function() {
        // g2.attr("transform","translate("+ 
        //     d3.event.translate.join(",")+")scale("+d3.event.scale+")");
        // g2.selectAll("circle")
        //     .attr("d", path.projection(projection));
        // g2.selectAll("path")  
        //     .attr("d", path.projection(projection)); 
        g2.attr("transform",
          "translate("+d3.event.translate+")"
          + " scale("+d3.event.scale+")");

  });

map.call(zoom)