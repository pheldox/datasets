Road safety in Europe encompasses transportation safety among road users in Europe, including automobile accidents, pedestrian or cycling accidents, motor-coach accidents, and other incidents occurring within the European Union or within the European region of the World Health Organization (49 countries). Road traffic safety refers to the methods and measures used to prevent road users from being killed or seriously injured.

## Data
Features within the data are:
* Country
* Area
* Population
* Population Density
* Total Deaths
* GDP per capita
* Vehicle Ownership, etc 


[Retreived from Wikipedia](https://en.wikipedia.org/wiki/Road_safety_in_Europe)

## Preparation


Install the required python libraries :

    cd scripts
    pip install -r requirements.txt

The scrape.py script scrapes data from wikipedia and saves into data folder i.e data/roadsafety.csv

Run script:

    python scrape.py
        
## Visualization

Charts deployed on heroku: 

    https://roaddataviz.herokuapp.com/