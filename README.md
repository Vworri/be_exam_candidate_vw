# SCOIR Technical Interview for Back-End Engineers
This repo contains an exercise intended for Back-End Engineers.

## How To:
After you pull the repo to your local machine,
 and with  with [python 3.6](https://www.python.org/downloads/release/python-360/) installed,
and your path properly set on [windows](https://docs.python.org/3.6/using/windows.html) or [mac](https://docs.python.org/3.6/using/mac.html)
 pip install the requirements
    
```commandline
    pip3 install -r requirements.txt
```
This will go very easily if you also use a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

Now that the environment is set up, all you have to do is run:
```bash
    python app.py
```

if you have multiple versions of Python downloaded and have gotten an error while trying to run app.py, try:
```commandline
    python3 app.py
```
The app will prompt the user for some information:
Where to find the input file and where to place the output file

If given an invalid filepath for the input, the program will error

###Testing:
 In the command line:
```commandline
python test_recordValidation.py 
```

## Assumptions
1. The headers for the input file are exactly: INTERNAL_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME,PHONE_NUM
2. The user has access to the original file and has given python adequate permissions
3. All paths given will be relative to app.py or absolute
