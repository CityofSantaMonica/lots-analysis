# lots-analysis

A project to analyze parking lot data in Santa Monica. 

The primary data source is the [City of Santa Monica's Open Data Portal](https://data.smgov.net),
and specifically the [Parking Lot Counts](https://data.smgov.net/Transportation/Parking-Lot-Counts/ng8m-khuz) dataset.

This dataset is fed a snapshot of the [current state of the parking lots](https://parking.api.smgov.net/lots) every 5 minutes, 24 hours a day.

## Getting Started

[Conda](http://conda.pydata.org/docs/) is required to get a local environment setup (Miniconda works just fine).

Assuming you have `conda` available at the command line, setup is very simple

First, clone the repo down:

    $ git clone git@github.com:CityofSantaMonica/lots-analysis.git <your-path>
    $ ...
    $ cd <your-path>
    
Next, create the `conda` environment (named *datascience*) from the environment descriptor file:

    $ conda env create -f env.yml

Activate the environment

    $ source activate datascience
    
Finally, launch Jupyter Notebook

    (datascience)$ jupyter notebook