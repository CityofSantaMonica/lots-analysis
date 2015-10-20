import os, os.path
import pandas as pd
import urllib
import time

def refresh(file_path):
    url = "https://data.smgov.net/api/views/ng8m-khuz/rows.csv?accessType=DOWNLOAD"

    def _refresh():
        print "retrieving data file"
        urllib.urlretrieve(url, file_path)

    if os.path.isfile(file_path):
        # refresh the file at most once per hour
        mtime = os.stat(file_path).st_mtime
        now = time.time()
        if ((now - mtime) / 60) > 60:
            _refresh()
        else:
            print "file is fresh"
    else:
        _refresh()

def munge(file_path):
    # read in the latest source data
    df = pd.read_csv(file_path).head(100000)

    # renaming some funky columns
    df.rename(
        columns = { "Date/Time": "DateTime", "Map Point": "MapPoint" },
        inplace = True
    )

    # clean up the addresses to match the static data
    df.Address = df.Address.replace(
        [r", Santa Monica", r"\.", r"\bSt\b", r"\sat 4th Street"],
        [               "",    "",  "Street",                 ""],
        regex = True
    )

    # convert strings to datetime64[ns] objects
    df.DateTime = pd.to_datetime(df.DateTime, format = "%m/%d/%Y %H:%M:%S %p")

if __name__ == "__main__":
    data_file = "./data.csv"
    refresh(data_file)
    munge(data_file)
