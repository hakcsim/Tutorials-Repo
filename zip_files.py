import zipfile
import shutil


def zip_compressed():
    with zipfile.ZipFile('test_files/files.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
        my_zip.write('test_files/ages.csv')
        my_zip.write('test_files/plot.png')

def unzip_all():
    with zipfile.ZipFile('test_files/files.zip', 'r') as my_zip:
        print(my_zip.namelist())
        my_zip.extractall('exfiles') # directory for extracted files and

def unzip_selected():
    with zipfile.ZipFile('test_files/files.zip', 'r') as my_zip:
        print(my_zip.namelist())
        my_zip.extract('test_files/plot.png')

# can only zip whole folder
def shutil_compress():
    # options: zip, tar, gztar, bztar, xztar
    shutil.make_archive('another', 'zip', 'test_files')        

def shutil_extract():
    shutil.unpack_archive('another.zip', 'another')        

def download_from_web():
    import requests

    r = requests.get('https://github.com/hakcsim/Test-Repo/archive/master.zip')

    with open('test_files/survey.zip', 'wb') as f:
        f.write(r.content)

    with zipfile.ZipFile('test_files/survey.zip', 'r') as survey_zip:
        print(survey_zip.namelist())
        survey_zip.extractall()

if __name__ == '__main__':
    download_from_web()