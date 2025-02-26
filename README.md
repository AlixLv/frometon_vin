# FROMETON

### Description
Are you about to enjoy a good cheese and want to find a wine to go with it? 

Frometon offers a range of cheese and wine pairings. After registering on the site, you can search by cheese name or wine name for suggested pairings.


### Main features of the app:
- create a account
- search for a cheese or a wine name
- add a pairing to favourites
- delete a pairing from favourites
- update user’s informations


### Tech Stack:
Python, Django, TailwindCSS, HTML


### Setup:
This setup assumes you have already Python installed on your machine.

First clone the Github repository: `git clone git@github.com:AlixLv/frometon_vin.git` 

Enter the newly created folder: cd frometon_vin 

Execute the command to create your virtual environment: `python3 -m myvenv env` // you can replace "myvenv" by another name that suits you best

Execute the command to activate your virtual environment: source myvenv/bin/activate // on Windows: myvenv\Scripts\activate
Now, you can see your virtual environment is activated with the (myvenv) displayed at the beginning of your command line.

In your virtual environment (myvenv) install the dependancies listed in the requirements: `pip install -r requirements/local.txt`

Migrate the models of the database: `python3 manage.py makemigrations`

Load the data already available into the database: `python3 manage.py loaddata  vins-aop.json` 
Then `python3 manage.py loaddata fromages-aop.json` 
And last `python3 manage.py loaddata accords.json` 

Apply the migrations: `python3 manage.py migrate`

Run the server to start using the website: `python3 manage.py runserver`
and navigate to the link displayed in your terminal
