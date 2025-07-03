import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

list_of_paths = {
    'app/__init__.py',
    'app/routes/__init__.py',
    'app/routes/flights.py',
    'app/services/skyscanner.py',
    'config.py',
    'run.py',
    'requirements.txt'

}

for filepath in list_of_paths:
    filepath = Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir !='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Create Dicrectory; {filedir} for the file {filename}")
    if (not os.path.exists(filepath) or os.path.getsize(filepath) is 0):
        with open(filepath,'w') as f:
            pass
            logging.info('create empty file: {filepath}')
    else:
        logging.info(f'{filepath} already exists')