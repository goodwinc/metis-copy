# D3 Transitions and Events

### Transitions

Transitions are functions within the D3 library that allow for seamless transitions between changes. They're a great way to add more pizzazz to your visualization.

Let's go to [work.html](work.html) and try adding some transitions while we make changes:

```javascript
var dataset = [10,20,30,40];

var svg = d3.select("body").append("svg")
  .attr("width",700)
  .attr("height", 700);

var circles = svg.selectAll("circle");

circles.data(dataset)
  .enter().append("circle")
  .attr("r", function(d) { return d*2; })
  .attr("cx", function(d,i) { return (i + 1) *100; } )
  .attr("cy", function(d,i) { return (i + 1) *100; } )
  .attr("fill", function(d) { if( d == '10' ) { return "red"; }
                          else if( d == '20' ) { return "blue"; }
                          else if( d == '30' ) { return "green"; }
                          else if( d == '40' ) { return "orange"; }
      })
  .style("fill-opacity", .7)
  .style("stroke-width",".2em")
  .style("stroke",function(d) { if( d == '10' ) { return "red"; }
                          else if( d == '20' ) { return "blue"; }
                          else if( d == '30' ) { return "green"; }
                          else if( d == '40' ) { return "orange"; }
      });
```

Let's reload and try that with a transition:

```javascript
var dataset = [10,20,30,40];

var svg = d3.select("body").append("svg")
  .attr("width",700)
  .attr("height", 700);

var circles = svg.selectAll("circle");

circles.data(dataset)
  .enter().append("circle")
  .attr("r", function(d) { return 0; })
  .attr("cx", function(d,i) { return (i + 1) *100; } )
  .attr("cy", function(d,i) { return (i + 1) *100; } )
  .attr("fill", function(d) { if( d == '10' ) { return "red"; }
                          else if( d == '20' ) { return "blue"; }
                          else if( d == '30' ) { return "green"; }
                          else if( d == '40' ) { return "orange"; }
                          })
  .style("fill-opacity", .7)
  .style("stroke-width",".2em")
  .style("stroke",function(d) { if( d == '10' ) { return "red"; }
                          else if( d == '20' ) { return "blue"; }
                          else if( d == '30' ) { return "green"; }
                          else if( d == '40' ) { return "orange"; }
                          })
    .transition()
    .duration(2000)
    .attr("r", function(d) { return d*2; });
```

See what happened?

Let's play with some of the transition parameters to change our transitions:

 * `ease()`
 * `delay()`
 * `duration()`

```javascript
var newdata = [30,10,20,40];

d3.select("svg").selectAll("circle")
  .data(newdata)
  .transition()
  .duration(2000)
  .ease("elastic")
  .delay(200)
  .attr("r", function(d) { return d*2; })
  .attr("cx", function(d,i) { return (i + 1) *100; } )
  .attr("cy", function(d,i) { return (i + 1) *100; } )
  .attr("fill", function(d) { if( d == '10' ) { return "red"; }
                          else if( d == '20' ) { return "blue"; }
                          else if( d == '30' ) { return "green"; }
                          else if( d == '40' ) { return "orange"; }
      })
  .style("fill-opacity", .7)
  .style("stroke-width",".2em")
  .style("stroke",function(d) { if( d == '10' ) { return "red"; }
                          else if( d == '20' ) { return "blue"; }
                          else if( d == '30' ) { return "green"; }
                          else if( d == '40' ) { return "orange"; }
      });
```

 * `ease()`: choose one of [various](https://github.com/mbostock/d3/wiki/Transitions#d3_ease) functions that change how the transition moves between states
 * `delay()`: add a delay
 * `duration()`: say how long you want it to be

For more transition parameters, [check out the API](https://github.com/mbostock/d3/wiki/API-Reference).

---

### Events

Because D3 is a Javascript framework, we can use the different [Javascript Events](http://www.w3schools.com/js/js_events.asp) to add interaction to our visualization.

Javascript Events are things that either user or the browser to does that affects HTML elements. Some common events are "onclick" or "onmouseover"

```javascript
function somethingCool() {
  d3.select(this).style("fill", "red");
}

d3.selectAll("circle").on("mouseover",somethingCool);
```
What's going on here?

 * We defined the event function.
 * We specified where and when it should occur.

That `select(this)` is important, as it says that we're doing it to just this matched element not all of them, even though we allowed any to be selected with the `selectAll()`.

You can add transitions to this to make even cooler events

```javascript
function somethingCool() {
  d3.select(this)
    .transition()
    .duration(5000)
    .ease("elastic")
    .delay(100)
      .style("fill", "black")
      .style("stroke-width","0em");
}

d3.selectAll("circle").on("mouseover",somethingCool);
```

We didn't cover this with transitions before, but you can chain transitions, which are fun to do with events:

```javascript
function somethingCool() {
  d3.select(this)
    .transition()
    .duration(2000)
    .ease("elastic")
    .delay(100)
      .style("fill", "black")
      .style("stroke-width","0em")
    .transition()
    .duration(2000)
    .ease("elastic")
    .style("fill", function(d) { if( d == '10' ) { return "red"; }
                        else if( d == '20' ) { return "blue"; }
                        else if( d == '30' ) { return "green"; }
                        else if( d == '40' ) { return "orange"; }
         })
    .style("fill-opacity", .7)
    .style("stroke-width",".2em")
    .style("stroke",function(d) { if( d == '10' ) { return "red"; }
                        else if( d == '20' ) { return "blue"; }
                        else if( d == '30' ) { return "green"; }
                        else if( d == '40' ) { return "orange"; }
        });

}

d3.selectAll("circle").on("mouseover", somethingCool);
```

Here's another one for fun:

```javascript
function somethingCool() {
  d3.select(this)
    .transition()
    .duration(2000)
    .ease("elastic")
    .attr("r", function(d) { return d * 0.5; })
    .attr("cx", function(d) { return Math.random() * 400; } )
    .attr("cy", function(d) { return Math.random() * 400; } )
    .transition()
    .duration(2000)
    .ease("elastic")
    .attr("r", function(d) { return d * 2; })
    .attr("cx", function(d) { return (d) * 10; } )
    .attr("cy", function(d) { return (d) * 10; } );
}

d3.selectAll("circle").on("mouseover",somethingCool);
```
