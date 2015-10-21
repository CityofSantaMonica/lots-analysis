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

def munge(historical_data, static_data):
    # read in the sources
    hdf = pd.read_csv(historical_data)
    sdf = pd.read_csv(static_data)

    # renaming some funky columns
    hdf.rename(
        columns = { "Date/Time": "DateTime", "Map Point": "MapPoint" },
        inplace = True
    )

    sdf.rename(
        columns = { "Total Spaces": "Total" },
        inplace = True
    )

    # clean up addresses in historical data to match those in static data
    hdf.Address = hdf.Address.replace(
        [r", Santa Monica", r"\.", r"\bSt\b", r"\sat 4th Street"],
        [               "",    "",  "Street",                 ""],
        regex = True
    )

    # merge the DataFrames on the Address columns
    # this is an 'inner join' => any Addresses missing in the static data
    # will have their corresponding records removed
    # then select out only the columns we are interested in
    df = hdf.merge(sdf, on = "Address")[[
        "DateTime",
        "Lot",
        "Address",
        "Zip",
        "Available",
        "Total",
        "Latitude",
        "Longitude"
    ]]

    # convert strings to datetime64[ns] objects
    df.DateTime = pd.to_datetime(df.DateTime, format = "%m/%d/%Y %H:%M:%S %p")

    return df

if __name__ == "__main__":
    historical_data = "./data.csv"
    static_data = "./static.csv"

    refresh(historical_data)
    data = munge(historical_data, static_data)
