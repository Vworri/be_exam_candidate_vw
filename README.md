# SCOIR Technical Interview for Back-End Engineers
This repo contains an exercise intended for Back-End Engineers.

## How To:
After you pull the repo to your local machine,
 and with  with [python 3.6](https://www.python.org/downloads/release/python-360/) installed,
and your path properly set on [windows](https://docs.python.org/3.6/using/windows.html) or [mac](https://docs.python.org/3.6/using/mac.html)
 pip install the requirements
    
```bash
    pip3 install -r requirements.txt
```
This will go very easily if you also use a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

Now that the environment is set up, all you have to do is run:
```bash
    python app.py
```

if you have multiple versions of Python downloaded and have gotten an error while trying to run app.py, try:
```bash
    python3 app.py
```
The app will prompt the user for some information:
Where to find the input file and where to place the output file

If given an invalid filepath for the input, the program will error

## Assumptions
1. The headers for the input file are exactly: INTERNAL_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME,PHONE_NUM
2. The user has access to the original file and has given python adequate permissions
3. All paths given will be relative to app.py or absolute
## Instructions

1. Fork this repo.
1. Using technology of your choice, complete [the assignment](./Assignment.md).
1. Update this README with
    * a `How-To` section containing any instructions needed to execute your program.
    * an `Assumptions` section containing documentation on any assumptions made while interpreting the requirements.
1. Before the deadline, submit a pull request with your solution.

## Expectations
1. Please take no more than 8 hours to work on this exercise. Complete as much as possible and then submit your solution.
1. This exercise is meant to showcase how you work. With consideration to the time limit, do your best to treat it like a production system.
