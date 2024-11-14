import os
import requests
import zipfile

# NOTE: I am having trouble with getting the ACS data via API - it is all very confusing and I am still working on it.
# I will manage, but it takes more time than expected, because I need to understand a whole bunch of things that are new to me.

# TO DO:
#   - get ACS_language_spoken_at_home data via API
#   - adapt code to download both data sets
#   - add error-handling if url does not work
#   - What happens if there are many csv-files in the zip? (Maybe not necessary to consider)

def download_and_extract_csv(data_set, url, data_dir, save_as):
    # 1 - download the file from the URL
    print(f'Downloading data set "{data_set}" from: {url}')
    response = requests.get(url)

    # 2 - save file (temporarily)
    file_path = os.path.join(data_dir, f'{data_set}_temp.zip')
    print(file_path)
    # w = write -> create file if it does not exist, overwrite if it exists
    # b = binary -> zip-file is (always) in binary format
    with open(file_path, "wb") as df:
        # write() -> write binary content into the file
        # response.content -> holds raw binary content downloaded from URL (by requests.get())
        df.write(response.content)
    
    # 3 - unzip and extract csv-file
    with zipfile.ZipFile(file_path, 'r') as zip_folder:     # open temporarily saved zip as zip_folder
        for file in zip_folder.namelist():     
            if file.endswith('.csv'):
                zip_folder.extract(file, data_dir)
                os.replace(os.path.join(data_dir, file), save_as)  # Save to the desired name/location

    # 4 - remove temp zip-file
    os.remove(file_path)
    print(f'CSV file saved as "{save_as}"')

if __name__ == '__main__':
    data_set = 'PIAAC'
    url = 'https://www.oecd.org/content/dam/oecd/en/about/programmes/edu/piaac/data-materials/CSV-prgusap1-Combined-2012-2014-U.S-International-PUF.zip'
    data_dir = os.path.join('..', 'data')  # Folder to extract to; if script is started from made-wise2425\project, go back to made-wise2425 from "project" and into "data"
    if not os.path.exists(data_dir):       
        data_dir = os.path.join('.', 'data')  # Folder to extract to; if script is started from made-wise2425 folder, do directly into "data"
    save_as=os.path.join(data_dir, f'{data_set}.csv')
    download_and_extract_csv(data_set, url, data_dir, save_as)
