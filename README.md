# How to run
## Requirements
1. Python 3
2. virtualenv
## Set enviroment
Run this three commands
```console
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Run Code
```console
python solution.py input.txt
```
## Run Tests
```console
pytest tests.py
```
# Notes about this code
## Linter
Pylama - https://github.com/klen/pylama
## Input file format
```
time_of_start;time_of_finish;call_from;call_to
```
## Implemented rules
### Rule 1
The first 5 minutes of each call are billed at 5 cents per minute
### Rule 2
The remainer of the call is billed at 2 cents per minute
### Rule 3
The caller with the highest total call duration of the day will not be charged (i.e., the caller that has the highest total call duration among all of its calls)
