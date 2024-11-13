import os
import requests
import zipfile

# TO DO:
#   - get ACS_language_spoken_at_home data via API
#   - adapt code to download both data sets

def download_and_extract_csv(data_set, url, data_dir, save_as):
    # 1 - download the file from the URL
    print(f'Downloading data set "{data_set}" from: {url}')
    if url != None:
        response = requests.get(url)
    else: pass

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
        # TO DO: What happens if there are many csv-files in the zip?
        # print(zip_folder.namelist())
        for file in zip_folder.namelist():     
            if file.endswith('.csv'):
                zip_folder.extract(file, data_dir)
                os.replace(os.path.join(data_dir, file), save_as)  # Save to the desired name/location

    # 4 - remove temp zip-file
    os.remove(file_path)
    print(f'CSV file saved as "{save_as}"')

data_set_dict = {'PIAAC':'https://www.oecd.org/content/dam/oecd/en/about/programmes/edu/piaac/data-materials/CSV-prgusap1-Combined-2012-2014-U.S-International-PUF.zip',
                 'ACS_language_spoken_at_home':'https://api.census.gov/data/2012/acs/acs5/subject?get=group(S1601)&ucgid=0100000US'}

if __name__ == '__main__':
    for item in data_set_dict.items():
        data_set, url = item[0], item[1]
        data_dir = os.path.join('..', 'data')  # Folder to extract to; go back to made-wise2425 from "project" and into "data"
        save_as=os.path.join(data_dir, f'{data_set}.csv')
        download_and_extract_csv(data_set, url, data_dir, save_as)
