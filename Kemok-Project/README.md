# scrapper_and_ms
script to get data by scraping along with a django api

STEP 1 (CREATE ENV TO SCRAPPER):

Create a virtual environment for the scrapper application, in the scrapper directory with:

* python3 -m venv venv

Then activate this venv with any terminal, bash or any built in app like pycharm visual studio code. The following must be executed:

* source venv/bin/activate


STEP 2 (CREATE ENV TO MICROSERVICE):

Create a virtual environment for the microservice application, in the scrapper directory with:

* python3 -m venv venv

Then activate this venv with any terminal, bash or any built in app like pycharm visual studio code. The following must be executed:

* source venv/bin/activate

STEP 3 (CONFIGURATE AND RUNNING DJANGO MICROSERVICE):

You use bash in project folder for configurate django microservice, first execute:

* setup.sh setup_microservice  

Then:

* setup.sh makemigrations 

Next:

* setup.sh migrate 

Finally:

* setup.sh microservice

With this, the server that will handle the extracted data and save it in the database is running.


STEP 4 (CONFIGURATE):

You use bash in project folder for configurate scrapper, first execute:

* setup.sh setup_scrapper  

With this you can run the main script

STEP 5 (RUN MAIN SCRIPT):

Then, in order to run the main script that performs the webscrapping, the following command is used:

* setup.sh runscrapper


This completes the entire process required for this project.