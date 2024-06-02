import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
                    
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "app.py",
]                 

for f in list_of_files:
    print('original: ', f)
    print('new: ', Path(f))                             ## Path converts the '\' or'/' according to correct OS path. For windows, it is backslash '\'
    dir, file = os.path.split(Path(f))                  ## split the path into directory and file name
    print('Dir : ', dir, ' : ', 'File : ', file)
    
    if dir != "":
        os.makedirs(dir, exist_ok=True)                  ## create the directory if it does not
        logging.info(f'Directory created: {dir}')
        
    if not os.path.exists(f) or os.path.getsize(f) == 0: ## create the file if it does not exist or is empty
        with open(f, 'w') as file:
            pass
        logging.info(f'File created: {f}')
    else:                                               ## if the file already exists, do nothing.
        logging.info(f'File already exists: {f}') 
        
        