# Predicting crime in London

I used a gradient boosted tree to predict whether a certain type of crime is or is not going to happen for a LSOA in a certain month. 

For this, I collected data from the London Data Store on crime rates along with census data to include demographic and economical information in the model.

Using a time series approach, I found that the main predictors so far are the crime frequency of the previous 12 months, and the ID (index of deprivation) of each LSOA. 	

![image-20181025185612150](/Users/lailasprejer/Library/Application Support/typora-user-images/image-20181025185612150.png)



The graph shows the ROC curve for the model.

