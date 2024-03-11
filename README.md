# Github Repos Analyser

This is a simple programm for counting total number of additional and deletional rows in the self projects.

Before usage create a `.env` file with the following structure:

```
ACCESS_TOKEN_GITHUB=<Your personal github access token>
```

At this moment only the `.py` extension supports.

## Setup and run

```
pipenv install
pipenv shell
python app.py
```
 ### Arguments

 ```
 python app.py -h

 usage: app.py [-h] [--date_from DATE_FROM]

options:
  -h, --help            show this help message and exit
  --date_from DATE_FROM The Start Date - format YYYY-MM-DD
 ```
 If the date_from parameter is not passed, the date will be calculated as the current date minus one day.
