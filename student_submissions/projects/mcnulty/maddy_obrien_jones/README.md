# Welcome to my 'Project McNulty' repo!   

For this project at Metis, I used supervised learning (classification), Amazon Web Services, PostgreSQL, Flask, and HTML/CSS to create a web app that consolidates data on housing throughout the city. Users can find information on complaints about the building and area, crime rates, as well as the 'Sketchy Landlord' index, created by a classification model trained on data where tenants ended up suing their landlords.

In this repo, I've uploaded my code, the data I used, and the presentation I gave at Metis on this project.  

Blog post is currently a work in progress.

## Repo Contents:   

### Data
* All data is available on [NYC Open Data]. The datasets used in this project are up-to-date as of October 17th, 2018.

### Data Cleaning
* [data_cleaning.py](https://github.com/maddyobrienjones/project_mcnulty/blob/master/data_cleaning.py) - cleaning of NYC open data and PLUTO data
* all performed on AWS

### Modeling
* [mvp_maddy_obrien_jones.ipynb](https://github.com/maddyobrienjones/project_mcnulty/blob/master/mvp_maddy_obrien_jones.ipynb) - minimum viable product
* [baseline.ipynb](https://github.com/maddyobrienjones/project_mcnulty/blob/master/baseline.ipynb) - baseline model built on DOB complaints only
* [model_testing.ipynb](https://github.com/maddyobrienjones/project_mcnulty/blob/master/model_testing.ipynb) - feature engineering and model testing
* [final_modeling.ipynb](https://github.com/maddyobrienjones/project_mcnulty/blob/master/final_modeling.ipynb) - building XGBoost model and scoring on data

### Web App Building
* [flaskapp.py](https://github.com/maddyobrienjones/project_mcnulty/blob/master/flaskapp.py) - Flask app to look up building information
* [page.html](https://github.com/maddyobrienjones/project_mcnulty/blob/master/page.html) - first page of Flask app (search bar)
* [template2.html](https://github.com/maddyobrienjones/project_mcnulty/blob/master/template2.html) - second page of Flask app (building information)
* [xgb.pkl](https://github.com/maddyobrienjones/project_mcnulty/blob/master/xgb.pkl) - pickled model to predict risk of litigation

### Presentation
* [predicting_housing_litigation.pdf](https://github.com/maddyobrienjones/project_mcnulty/blob/master/predicting_housing_litigation.pdf) - powerpoint
* [screen_recording.mov](https://github.com/maddyobrienjones/project_mcnulty/blob/master/screen_recording.mov) - demonstration of Flask app


*work in progress

[NYC Open Data]: https://opendata.cityofnewyork.us/
