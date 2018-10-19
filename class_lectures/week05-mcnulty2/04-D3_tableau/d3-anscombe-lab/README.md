##Lab part I

1. Again we'll start by creating a new folder for our index.html file.

2. When using D3, we can create our HTML template as follows:

  ```
  <!DOCTYPE html>
  <html>
  <head>
    <meta charset="utf-8">

    <style type="text/css">
      /*css to go here*/
    </style>
  </head>
  <body>

    <script src="https://d3js.org/d3.v4.min.js"></script>
    <script>
      //JS to go here
    </script>
  </body>
  </html>
  ```

3. Fire up a local server and open the page in the console. Test and see if your version loaded.  Make sure you are in the new local folder where you created the index.html.

  ```
  # for Python 2
  python -m SimpleHTTPServer 8000

  # for Python 3
  python -m http.server 8000
  ```

4. Open `index.html` in a text editor, and append an `h1` to the page via d3.select("body").append("h1").text("some text")

5. Let's also add some styles 
```
    body {
      /*hex color*/
      background-color: #ddf;
      
      /*css color picker*/
      color: #4542f4;
      /* font-family: family-name|generic-family|initial|inherit;*/
      font-family:"Times New Roman", Georgia, Serif;
      font-size: 30px;
      font-weight: bold; 
    }

    p { 
      font-family: Calibri,Candara,Segoe,Segoe UI,Optima,Arial,sans-serif; 
      font-size: 20px;
      color: #ce42f4;
    }
    
    
```

Or add style via a class:

```
.first-class {

    background-color: #ddf;
    color: #4542f4;
    font-family:"Times New Roman", Georgia, Serif;
    font-size: 30px;
    font-weight: bold; 
  }
  
.second-class { 
  font-family: Calibri,Candara,Segoe,Segoe UI,Optima,Arial,sans-serif; 
  font-size: 20px;
}

// update our js: 
d3.select("body")
    .append("h1").text("Some wonderful new text").classed("first-class",true)
    ;

// More efficiently, D3 lets you "chain" your code. Handy!

```


Now do a data join. Make an array called parts and create a new `p` element for each.

  ```
    var parts = ["This is", "my first", "data join!"]

    var sentence = d3.select("body").selectAll("p")
        .data(parts)
      .enter()
        .append("p")
        .text(function(d) { return d; });
  ```
  
  
Lets break that down:

line 1) selectAll: will select all matching elements on our page:    
line 2) data(parts): ~ identity function: for each element within our data, return a row of data     
line 3) .enter() ~ "virtual selection": all the stuff after .enter() will happen for the case where we have a data element 
but no corresponding page element    
...




[first check-point](first_data_join.html)


That's a data join! Selecting elements you haven't created yet is a little strange, and we'll discuss it (and get plenty more experience in the next six weeks). For more details, Scott Murray has [a great explanation](http://alignedleft.com/tutorials/d3/binding-data) and Mike Bostock Goes charactistically deep in [Thinking With Joins](http://bost.ocks.org/mike/join/).

As mundane as that was, that's the building block of every D3 chart you see on the internet.

##Lab part 2.
We're going to make the famous Anscombe plot using D3:

1. Clear out or start a new `index.html`.

2. Make a Javascript object out of your tabular data in (quartet.tsv) and make sure you know how to manipulate it. (This is an annoying but useful exercise in getting useful in a text editor.) Choose One Group Data only (I, II, III or IV).  There are only 11 data rows per group, so this will build the muscle memory in writing Javascript Object arrays.  You only need X, Y attribute values in this data variable.

  ```
  // Group II data
  var data = [
  {"group": "II", "x":10, "y" : 9.14},
  {"group": "II", "x":8, "y" : 8.14},
  {"group": "II", "x":13, "y" : 8.74},
  {"group": "II", "x":9, "y" : 8.77},
  {"group": "II", "x":11, "y" : 9.26},
  {"group": "II", "x":14, "y" : 8.1},
  {"group": "II", "x":6, "y" : 6.13},
  {"group": "II", "x":4, "y" : 3.1},
  {"group": "II", "x":12, "y" : 9.13},
  {"group": "II", "x":7, "y" : 7.26},
  {"group": "II", "x":5, "y" : 4.74}
];

  ```

3. Now let's try to code this using D3 and produce a Scatter plot. Add an SVG element of width 600 and height 400.

```
var height = 400;
var width = 600; 

var svg = d3.select("body").append("svg")
.attr("height",height)
.attr("width", width );

```
[checkpoint](02-svg.html)

4. Using a data join, add a circle for every element of our array. Give it a radius 5 and a class, `anscombe-circle'. Inspect it in the browser. To start, I like to put a pink border around the SVG to make sure I knew it drew:

    ```
    /* Add CSS Styles in Header section of the html */
    svg {
      border: 1px solid #f0f;
    }
    ```

5. Position the circles based on their `x` and `y` attributes. How does SVG interpret these positions?

```
svg.selectAll("circle")
  .data(data)
  .enter()
  .append("circle")
  .attr("cx",function(d) {return d.x})
  .attr("cy",function(d) {return d.y})
  .attr("r",5)
  .attr("class","anscombe-cirlce");

```

Also add a another class for our circles:   

```
.anscombe-circle { 
    color: #ddd;
    font-size: 11px;
    fill: red;}
```
[3rd checkpoint](03-data_join.html)    

6. We need a [scale](https://github.com/mbostock/d3/wiki/Quantitative-Scales#linear-scales). Let's add one.    

```
var x = d3.scaleLinear()
.domain([4,13])
.range([0,width]);

var y= d3.scaleLinear()
.domain([3,10])
.range([height,0]);
```

Update your Data Join: 
```
d3.select("svg").selectAll("circle")
.data(data)
.enter()
.append("circle")
.attr("cx",function(d) {return x(d.x)})
.attr("cy",function(d) {return y(d.y)})
.attr("r",5)
.attr("class","anscombe-cirlce");
```

[check it!](04-simple_scale.html)   

But we will want to add margins:   

```
var margin = {top: 20, right: 40, bottom:20, left:20}
	 var height = 400 - margin.top - margin.bottom;
	 var width = 600 -margin.left -margin.right;

	 var svg = d3.select("body").append("svg")
	 .attr("height",height +margin.top + margin.bottom)
	 .attr("width", width +margin.left +margin.right )
	 .append("g")
	 .attr("transform","translate(" +margin.left+ ","+ margin.top +")");
```


```
var circleGroup= svg.selectAll("circle")
    .data(data)
    .enter()
      .append("g")
      .attr("class","anscombe-circle")
      .attr("transform",function(d) {return "translate(" +x(d.x) + "," + y(d.y) + ")";});

circleGroup.append("circle")
      .attr("r",5);
 ```

[transform, translate?!]( https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Basic_Transformations)




Checkpoint is [here](05-scale_via_transform.html).  

7. Let's label the coordinate positions of each using text. Is another data join really necessary?

 - Redo the original join, using groups first, then appending circles and text. Note SVG [transformation](http://www.w3.org/TR/SVG/coords.html) documentation, which is not that fun. Scott Murray [does better](http://chimera.labs.oreilly.com/books/1230000000345/ch08.html#_cleaning_it_up).

Add:   

```
circleGroup
.append("text")
.text(function(d) { return "(" + d.x + "," + d.y + ")"; })
.attr("dx", 6);
```


Checkpoint is [here](06-add_label.html).   

8.  Maybe [axes](https://github.com/mbostock/d3/wiki/SVG-Axes) are in order? The built-in components are a little clunky, and [Gregor](https://twitter.com/driven_by_data) prefers not to use them at all, but you have to know the rules before you break them, so let's use them for now.

Lets add axes:   

```
var xAxis=d3.axisBottom()
     .scale(x)
     .tickSize(-height)
     .tickPadding(8);

var yAxis=d3.axisRight()
 .scale(y)
 .tickSize(-width)
 .tickPadding(8);
 
 svg.append("g")
.attr("class", "x axis")
.attr("transform","translate(0,"+height+")")
.call(xAxis);

 svg.append("g")
.attr("class", "y axis")
.attr("transform","translate("+width+",0)")
.call(yAxis);
 ```
 
 and lets add some css:   
```
.axis text {
font-size: 12px;
fill: #777;
}

.axis path {
display: none;
}

.axis line {
stroke-width:1px;
stroke: #ccc;
stroke-dasharray: 3px 3px;
}
```

Checkpoint is [here](08-axes.html)


(On your own: checkout out this nice reference with transitions [here)](09-anscombe-transition.html)

Congratulations for making this far!  
