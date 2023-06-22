import os
import zipfile
import kaggle


# Download dataset from Kaggle
if not os.path.exists('dataset/instacart-market-basket-analysis.zip'):
    os.system('kaggle competitions download -c instacart-market-basket-analysis -p dataset/')

# Unzip download
ZIPFILE_PATH = os.path.join('dataset', 'instacart-market-basket-analysis.zip')

with zipfile.ZipFile(ZIPFILE_PATH, 'r') as main_zipfile:
    main_zipfile.extractall(path=os.path.join('dataset', 'zip'))

# Unzip all wanted csv files 
EXTRACTED_ZIPFILES_DIRECTORY = os.path.join('dataset', 'zip')

for filename in os.listdir(EXTRACTED_ZIPFILES_DIRECTORY):
    individual_zipfile_path = os.path.join(EXTRACTED_ZIPFILES_DIRECTORY, filename)
    if filename.endswith('.zip') and filename != 'sample_submission.csv.zip':
        with zipfile.ZipFile(individual_zipfile_path, 'r') as individual_zipfile:
            individual_zipfile.extractall(path=os.path.join('dataset', 'csv'))

os.remove(ZIPFILE_PATH)