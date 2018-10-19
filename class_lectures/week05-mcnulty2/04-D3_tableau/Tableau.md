# Intro to Tableau - Seattle Home Prices Walkthrough

This walkthrough will introduce you to some of Tableau's core functionality, getting you up and running with a starting dashboard visualization. Start by downloading the free [Tableau Public](https://public.tableau.com/en-us/s/) app and setting up an account.

Connect to the “SeattleHomePrices.csv” text file, you'll see that Tableau will automatically populate "dimensions" (discrete variables) and "measures" (continuous variables) from the data set.

As you play around with worksheets and follow these steps, note that the "Show Me" tab shows you a bunch of options of visualizations you could potentially construct, and tells you what dimensions/measures would be needed to create that visual.

OPEN SHEET 1

Display the Number of Houses in the dataset.

* Drag the mls# directly onto the sheet. Notice that the variable is automatically aggregated by sum, click on this aggregation and switch it to count (you should get 350).

* Play around with the formatting - make the number bigger, change the color etc., change the title

OPEN SHEET 2

Plot the Price Vs Square footage. 

* Drag the square feet measure to columns, and the price measure to rows. Note again that Tableau will automatically aggregate the measures. Disaggregate them by pressing analysis and unselecting "aggregate measures"

* Change the dot marks to circles. Make the size of the dots proportional to the number of bedrooms by dragging the beds measure to the size label under marks. Add transparency by adjusting the color settings. 
    
* Add a linear trend line by going to analysis, clicking trend line, and clicking to show.

OPEN SHEET 3

Create a histogram of the number of bedrooms, and highlight the mode. 

* Create bins of bedrooms by right clicking beds measure, clicking create then bins, select bin size = 1.

* Set the count of beds to rows, and Beds(bin) to columns to get a histogram.

* Create a calculated field for color. Tableau allows you to write your own formulas to create new variables such as a filter variable in this case. Once you've created it, drag the new field to colors to filter the histogram. 

    BarColor: 
``` 
    IF COUNT([Beds])==WINDOW_MAX(COUNT([Beds])) 
    THEN 1  
    ELSE 0 
    END 
```

OPEN SHEET 4

Create a map visualization of each house, colored by zip code

* Drag latitude to rows, and longitude to columns. Use the analysis tab to disaggregate measures again.

* Drag zipcode to color (click add all members)

* Hover over each point, notice that a tooltip pops up with the coordinates and the zip code. We can edit what this tooltip displays. Drag the Year Built dimension to tooltip, and see that this new info shows up when you hover over points.

OPEN SHEET 5 

Create a bar chart that shows average days on the market broken out by property type.

* Make the bars horizontal instead of vertical. Click above the bars to sort in descending order.

* As in Sheet 3, create a calculated field that will highlight the highest average days on the market property type.

OPEN A DASHBOARD

* Drag all 5 sheets we've created onto the dashboard, format the dashboard in a visually pleasing way.

* Add a filter by clicking Dashboard, Actions, Filter, ... and select sheet 5 as the source and all sheets as targets. Set it so that clearing the selection will show all values.

SAVE WORKBOOK

* Save your work to Tableau Public! You'll have to create a profile. Note that the dashboard will be visible to anyone on the internet.

* Once it's on Tableau Public, we can click the share button at the bottom and get an HTML embed code - you can add this to a blog to get an awesome interactive visualization! The example below isn't interactive (missing the javascript part), but many blogs should be able to accomodate this. 

<div class='tableauPlaceholder' id='viz1518672936006' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;De&#47;Demo1_188&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Demo1_188&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;De&#47;Demo1_188&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='filter' value='publish=yes' /></object></div>                

