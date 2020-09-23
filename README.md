# Baby_Names_Visualization :

## Project Goal <hr/>

The goal is to give a clear visualization of the most popular babies' names in the USA (by state or per year) from 1980 to 2018.

## Work Process <hr/>

#### ETL: EXTRACT - TRANSFORM - LOAD

* Extraction:
  We extracted our first tables from the social security websites as text files. The tables were dispatched by state and were all in text format. We ended up working with roughly 52 tables in total. Our second table was the USA latitude and longitude for each state that we extracted from Kaggle.


    + Sources:
  
        https://www.kaggle.com/washimahmed/usa-latlong-for-state-abbreviations

        https://www.ssa.gov/oact/babynames/decades/century.html

* Transform:
  
Our data was a report of the US babies' names by state from 1910 to 2018, and hopefully, we didn't have empty rows. The work consisted of cleaning the data by converting the text files to CSV, removing unnecessary columns, combining the table, and selecting the desired data.

* Load:
we used PostgreSQL as our database

### Heroku-Postgres <hr/>

This step consisted of uploading our data in the cloud through the connection of Heroku with Postgres. 


### Working with Python and Flash-Sqlalchemy <hr/>
