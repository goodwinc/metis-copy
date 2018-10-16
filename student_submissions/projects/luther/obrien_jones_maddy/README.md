# Welcome to my 'Project Luther' repo!   

For this project at Metis, I used web scraping with BeautifulSoup and Selenium to gather information on films from IMDB. Then, I tested linear regression and decision tree models to try and predict the proportion of revenue movies get from the USA versus the rest of the world.   

In this repo, I've uploaded my code, the data I used, and the presentation I gave at Metis on this project.  
  
Read my blog post [here]!*
  
## Repo Contents:   

### Data
* [codes.csv](codes.csv) - list of IMDB movie codes
* [codes.pkl](codes.pkl) - codes.csv in pickled format for ease of use
* [df.csv](df.csv) - cleaned data for modeling
* [imdb.csv](imdb.csv) - raw IMDB data
* [imdb.pkl](imdb.pkl) - raw IMDB data in pickled format for ease of use
* [money_df.csv](money_df.csv) - supplementary data on budgets and box office grosses from The Numbers
  
### Web Scraping and Data Cleaning
* [cleaning.py](cleaning.py) - cleaning of raw IMDB data
* [moneyscraping.py](moneyscraping.py) - scraper used to get supplementary budget and revenue information from The Numbers
* [scraper.py](scraper.py) - scraper used to gather data from each movie
* [selenium_link_scraper.py](selenium_link_scraper.py) - scraper used to gather IMDB movie codes
  
### Model Testing
* [final_models.ipynb](final_models.ipynb) - cleaned notebook of models tested
* [model_test.ipynb](model_test.ipynb) - miscellaneous model testing
* [poly_model.ipynb](poly_model.ipynb) - building of polynomial model
* [trees_model.ipynb](trees_model.ipynb) - building of trees models
* [modeling.py](modeling.py) - modeling notes

### Presentation
* [luther.pdf](luther.pdf) - presentation in PDF format

*work in progress


[here]: https://medium.com/@obrienjonesm2013/predicting-us-share-of-box-office-revenue-with-web-scraping-and-regression-9aa82bca4cfd
