#
# This is the server logic of a Shiny web application. You can run the 
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#  
library(readr)
library(tidyverse)
library(fmsb)
library(shiny)
library(shinydashboard)
library(DT)

shinyServer(function(input, output, session){
  setwd('/Users/andreewerner/Documents/DataScience/SpeedDating')
  print(getwd())
  print(list.files(getwd()))
  SD_df <- read_csv('SDClean .csv')
  
  activities_reactive <- reactive({
    activities_df %>% 
      filter(gender == input$sex)
  })
  

 #Logistic Regression

  ML_data <- reactive({
    SD_df[SD_df$gender == input$sex,]
  })
  
  train <- reactive({
    ML_data() %>% 
      select(dec:shar) %>% 
      slice(1:(nrow(ML_data())/2))
  })
  
  test <- reactive({
    ML_data() %>% 
      select(dec:shar) %>% 
      slice((nrow(ML_data())/2+1):nrow(ML_data()))
  })
  
  user_df <- eventReactive(input$calc, {
    data.frame(attr = as.integer(input$attr), sinc = as.integer(input$sinc),  
               intel = as.integer(input$intel), fun = as.integer(input$fun), 
               amb = as.integer(input$amb), shar = as.integer(input$shar))
  })
  
  pred <- eventReactive(input$calc, {
    model <- glm(dec ~ ., family = binomial(link = "logit"), data = train())
    paste(round((predict(model, user_df(), type='response') * 100), 0), '%')
  })
  
  #render SpiderChart
  output$spiderchart <- renderPlot({
    
    user_df_initial <- data.frame(attr = 0, sinc = 0, 
                                  intel = 0, fun = 0, 
                                  amb = 0, shar = 0)
    
    #adding upper/lower bounds to radarchart and initial state of action button
    user_df_bounds <- if(input$calc == 0) {
      rbind(rep(10,6) , rep(0,6) , user_df_initial)
    } else (rbind(rep(10,6) , rep(0,6) , user_df()))
    
    #renaming columns to better match descriptions for final chart
    colnames(user_df_bounds) <- c('Attractiveness','Sincerity','Intellect',
                                  'Fun','Ambition','Shared Hobbies')
    
    radarchart(user_df_bounds, axistype = 1,
               #custom the grid
               cglcol="grey", cglty=1, axislabcol="grey", caxislabels=seq(0,10,2.5),
               #custom polygon
               pcol=rgb(0.2,0.8,0,0.9), pfcol=rgb(0.2,0.8,0,0.4) , plwd= , plty=1)
  })
  
  output$date_prob <-  renderText({
    if (input$calc == 0) {
      as.character('?')
    } else (pred()) 
  })
  
})