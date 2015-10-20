import os, os.path
import urllib
import time

def refreshData(file_path):
    url = "https://data.smgov.net/api/views/ng8m-khuz/rows.csv?accessType=DOWNLOAD"

    def _refreshData():
        print "retrieving data file"
        urllib.urlretrieve(url, file_path)

    if os.path.isfile(file_path):
        # refresh the file at most once per hour
        mtime = os.stat(file_path).st_mtime
        now = time.time()
        if ((now - mtime) / 60) > 60:
            _refreshData(file_path)
        else:
            print "file is fresh"
    else:
        _refreshData(file_path)

if __name__ == "__main__":
    data_file = "./data.csv"
    refreshData(data_file)
