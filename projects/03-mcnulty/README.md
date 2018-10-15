## Project McNulty
###### Week 4 - Week 6.5

![](mcnulty.jpg)

#### Back story:

Using either data from the web (API or scraped) or one of the optional supplied data sets (possibly in conjunction with your own data), what can we learn via supervised learning techniques? Ground your work in a hypothetical business application by putting emphasis on **data infrastructure** (SQL), **data size/computational scale** (AWS), or **business quality visualization/production** (Tableau, D3, flask website).

Note you can work within a 'company' (with other folks working on the same data source as you) for 
brainstorming, design, additional data and code sharing will be highly encouraged.  However, the final projects will be individual.


#### Data:

Ideally **Relational Data** with multiple tables, for familiarity with this structure and working with SQL.

 * **acquisition**: download, api's, scraping, etc.
 * **storage**: PostgreSQL
 * **sources**:  (see [sql_data_sets](sql_data_sets.md) for descriptions and links to data.)
  - Kaggle Instacart data
  - NYC Transportation
  - Traffic Fatalities
  - US Health Insurance Marketplace
  - Militarized Interstate Disputes
  - Sports, Sports, and More Sports!
  - The Simpson's
  - Climate Change
  - Python StackOverflow Questions 


#### Skills & Tools

You should use **at least one** and preferably more of the optional tools like SQL, AWS, tableau -- cover at least 1 of **data infrastructure**, **size/scale**, **business visualization/production**. You should also spend extra time thinking about **feature engineering** - how can you come up with representations of the data that are really relevant to the business / the predictive problem, and demonstrate that the features you've engineered add predictive value.

* supervised learning
* SQL
* AWS and large scale computing
* tableau
* javascript/D3
* flask


#### Analysis:

 * Supervised classification is required


#### Deliverable/communication:

Project / Presentation due Wednesday 10/31

  * organized project repository
  * slide presentation
  * visual and oral communication in presentations

**Status Updates**: All submitted to the teaching staff

* Wednesday 10/17: Project Proposal Submission
* Monday 10/22: Status Update: What are you working on, have you started modeling, what are the main challenges you're currently facing?
* Thursday 10/25: MVP submission: Minimum Viable Products! Just do it!

    * Which of the business functions have you started to tackle? Show us evidence.
    * Show us some initial results with models (they can be simple models on a subset of your data). Tell us about the feature       engineering you've done so far.
    * [How to](../../class_lectures/week03-luther2/02-null_hypo_eval/mvp_instructions.md) make an MVP.
    * [Example](../../class_lectures/week03-luther2/02-null_hypo_eval/mvp_example.md) MVP.
 
* Monday 10/29: Status Update: Where are you at, what are the final challenges you're facing, do you need extra help?

#### Design:

   * iterative design process
   * "MVP"s and building outward


#### More information:

Data sources for this project are all about options. We can choose from a number of [pre-selected](sql_data_sets.md) data sets. We can also use our own data (either scraped from the web or pulled from api's) or supplement the pre-selected data with some of our own. Either way, we will be honing our database skills by storing data in PostgreSQL and doing some of our analysis there.[^1]

[^1]: If the project does not have a significant SQL component, then additional (intermediate and advanced) [SQL challenges](../../challenges/challenges_questions/09-sql) should be completed.

We'll also learn about many supervised learning methods that can be used to predict outcomes for our projects. And we can showcase those results with a tableau or D3 visualization or a flask website.


