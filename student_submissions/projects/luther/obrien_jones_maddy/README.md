# Welcome to my 'Project Luther' repo!   

For this project at Metis, I used web scraping with BeautifulSoup and Selenium to gather information on films from IMDB. Then, I tested linear regression and decision tree models to try and predict the proportion of revenue movies get from the USA versus the rest of the world.   

In this repo, I've uploaded my code, the data I used, and the presentation I gave at Metis on this project.  
  
Read my blog post [here]!*
  
## Repo Contents:   

### Data
* [codes.csv](https://github.com/maddyobrienjones/project_luther/blob/master/codes.csv) - list of IMDB movie codes
* [codes.pkl](https://github.com/maddyobrienjones/project_luther/blob/master/codes.pkl) - codes.csv in pickled format for ease of use
* [df.csv](https://github.com/maddyobrienjones/project_luther/blob/master/df.csv) - cleaned data for modeling
* [imdb.csv](https://github.com/maddyobrienjones/project_luther/blob/master/imdb.csv) - raw IMDB data
* [imdb.pkl](https://github.com/maddyobrienjones/project_luther/blob/master/imdb.pkl) - raw IMDB data in pickled format for ease of use
* [money_df.csv](https://github.com/maddyobrienjones/project_luther/blob/master/money_df.csv) - supplementary data on budgets and box office grosses from The Numbers
  
### Web Scraping and Data Cleaning
* [cleaning.py](https://github.com/maddyobrienjones/project_luther/blob/master/cleaning.py) - cleaning of raw IMDB data
* [moneyscraping.py](https://github.com/maddyobrienjones/project_luther/blob/master/moneyscraping.py) - scraper used to get supplementary budget and revenue information from The Numbers
* [scraper.py](https://github.com/maddyobrienjones/project_luther/blob/master/scraper.py) - scraper used to gather data from each movie
* [selenium_link_scraper.py](https://github.com/maddyobrienjones/project_luther/blob/master/selenium_link_scraper.py) - scraper used to gather IMDB movie codes
  
### Model Testing
* [final_models.ipynb](https://github.com/maddyobrienjones/project_luther/blob/master/final_models.ipynb) - cleaned notebook of models tested
* [model_test.ipynb](https://github.com/maddyobrienjones/project_luther/blob/master/model_test.ipynb) - miscellaneous model testing
* [poly_model.ipynb](https://github.com/maddyobrienjones/project_luther/blob/master/poly_model.ipynb) - building of polynomial model
* [trees_model.ipynb](https://github.com/maddyobrienjones/project_luther/blob/master/trees_model.ipynb) - building of trees models
* [modeling.py](https://github.com/maddyobrienjones/project_luther/blob/master/modeling.py) - modeling notes

### Presentation
* [luther.pdf](https://github.com/maddyobrienjones/project_luther/blob/master/luther.pdf) - presentation in PDF format

*work in progress


[here]: https://medium.com/@obrienjonesm2013/predicting-us-share-of-box-office-revenue-with-web-scraping-and-regression-9aa82bca4cfd
