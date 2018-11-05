### Game of life

Let's tie it all together. *I know you'll find this frustrating. I'll be around to help.*

1) Move your pair.html from last Thursday to this folder and add these code pieces to it. The first goes at the beginning of your "body" block. And the second goes to the end of the "script" block. You also need this line in your <head>: <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>. Alternately, you can use this file: [pair.html](pair.html)

```javascript
      <div>
        <button type="button" onClick="getnextframe()">Evolve!</button>
      </div>
```

```javascript
       function getnextframe(){
         $.ajax({
           type: "POST",
           contentType: "application/json; charset=utf-8",
           url: "/gof",
           dataType: "json",
           async: true,
           data: "{\"grid\": ["+dataset+"]}",
           success: function (d) {

           }
         })
       }
 ```
 
2) If you pasted into your file, make sure to change the "dataset" variable to your variable that contains the information on which cells are alive.

3) You have goflife.ipynb in the folder. Just run that and it will serve up the pair.html and you can access it in the browser at http://0.0.0.0:5000/.

4) Currently, nothing will happen. In Python, you are getting the board (as a 1-d list) and just sending it back. First, set everything to 0 before sending back.

5) What Python returns comes to the "success" function (stored in the variable 'd'). First just print that to see if you get all 0s. You can use console.log().

6) Write code to update the D3 grid using the returned values. It's similar to the creation statement, without the "enter" and "create" and with just the attribute you are updating.

7) In that python notebook, add code to do the actual evolution of the board (instead of sending all 0s).
