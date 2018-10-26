# MVP

1. **HomeCredit Kaggle dataset** https://www.kaggle.com/c/home-credit-default-risk

   1. **Target**: 
      1. 1 - client with payment difficulties: he/she had late payment more than X days on at least one of the first Y installments of the loan in our sample
      2. 0 - all other cases
   2. **Features:**
      1. Home Credit application info: income, job history etc.
      2. Previous Home Credit applications, balances, payment histories
      3. Credit bureau info

2. **Initial ETL, baseline (complete)**

   1. Load into SQL (helped by http://www.convertcsv.com/csv-to-sql.htm )

      1. Binarize 0/1, Y/N, F/M, etc.
      2. Label-encode categorical
      3. Impute missing numerical data (mean)

   2. XGboost, Lightgbm, Catboost model (with application data only)

   3. | Metric                        | XGBoost                     | LightGBM                    | CatBoost                    |
      | ----------------------------- | --------------------------- | --------------------------- | --------------------------- |
      | **Accuracy<br />F1<br />AUC** | 0.860<br />0.305<br />0.753 | 0.861<br />0.311<br />0.760 | 0.861<br />0.311<br />0.757 |

      <intentionally left blank>

3. Feature engineering, modeling (not complete)

   1. Enrich application with summary data from historical tables
   2. Engineer ratios e.g. debt/income
   3. Tune hyperparameters for 1 algo (prob XGboost)
   4. Improvement: ??? TBD

4. Visualize results:

   1. Feature importance (Plotly)
   2. Compare to Kaggle contest winner (much better no doubt)
   3. Further improvements and conclusion
