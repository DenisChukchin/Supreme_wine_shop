# Supreme wine shop
Wine shop website "Новое русское вино".
Choose from a wide range of red wine, white wine, and another drinks.
## Installing:
Install Python3 latest version. Install PyCharm IDE, if you need it.
> To isolate the project, I'd recommend to use a virtual environment model. [vertualenv/venv](https://docs.python.org/3/library/venv.html).
 ## Preparing to run the script.
+ Create a virtualenv and activate it.
+ Then use pip (or pip3, there is a conflict with Python2) to install the dependencies (use the requirements.txt file):
```bash
% pip install -r requirements.txt
```
+ You will need an .xlsx (excel) file with a table. The table must looks like the example below.
<img width="877" alt="image" src="https://github.com/DenisChukchin/Supreme_wine_shop/assets/125466667/f2c41d6a-e973-4973-bbae-9f881d0d3a65">

> For permanent set, create .env file inside project folder and add variable like this:
```python
FILE_PATH = "/Users/denis/documents/my_shop/wine3.xlsx"
```
> If you don't want to create .env file, then for a quick test run, export your variable "FILE_PATH" with path to file by this command:
``` bash
% export FILE_PATH="YOUR_PATH_TO_FILE_WITH_TABLE"
```
## Run the script.
Use command:
``` bash
% python3 main.py  
```
Also, you can use this command to choose another .xlsx file without setting  variable.
``` bash
% python3 main.py -user_path "/Users/anton/documents/work/w.xlsx" 
```
Go to the website: http://127.0.0.1:8000
## Project goals.
*The program was designed by a student from online web development courses for educational purposes [Devman](https://dvmn.org).*
