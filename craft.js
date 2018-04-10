var svg1 = d3.select("#svg1"),
    margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = +svg1.attr("width") - margin.left - margin.right,
    height = +svg1.attr("height") - margin.top - margin.bottom;

var x1 = d3.scaleBand().rangeRound([0, width]).padding(0.1),
    y1 = d3.scaleLinear().rangeRound([height, 0]);

var g1 = svg1.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.csv("data/craft_frequency.csv", function(d) {
  d.count = +d.count;
  return d;
}, function(error, data) {
  if (error) throw error;

  x1.domain(data.map(function(d) { return d.craft_type; }));
  y1.domain([0, d3.max(data, function(d) { return d.count; })]);

  g1.append("g")
      .attr("class", "axis axis--x")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x1));

  g1.append("g")
      .attr("class", "axis axis--y")
      .call(d3.axisLeft(y1).ticks(10))
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", "0.71em")
      .attr("text-anchor", "end")
      .text("Frequency");

  g1.selectAll(".bar")
    .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x1(d.craft_type); })
      .attr("y", function(d) { return y1(d.count); })
      .attr("width", x1.bandwidth())
      .attr("height", function(d) { return height - y1(d.count); });
});
