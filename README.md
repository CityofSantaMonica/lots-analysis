# lots-analysis

A project to analyze parking lot data in Santa Monica.

The primary data source is the [City of Santa Monica's Open Data Portal](https://data.smgov.net),
and specifically the [Parking Lot Counts](https://data.smgov.net/Transportation/Parking-Lot-Counts/ng8m-khuz) dataset.

This dataset is fed a snapshot of the [current state of the parking lots](https://parking.api.smgov.net/lots) every 5 minutes, 24 hours a day.

## Setup

This project uses [Vagrant](https://www.vagrantup.com/) (and [VirtualBox](https://www.virtualbox.org/)) - you must install these first (Windows, OSX, Linux). We use a customized [Data Science Toolbox](http://datasciencetoolbox.org/) for the environment setup.

*Windows users*: use [Git BASH](https://git-for-windows.github.io/) for the commands below.

### Clone the repo

```bash
~$ git clone git@github.com:CityofSantaMonica/lots-analysis.git
Cloning into 'lots-analysis'...
...
~$ cd lots-analysis
```

### Setup and login to the vm

```bash
~/lots-analysis$ vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
...
~/lots-analysis$ vagrant ssh
Welcome to Ubuntu...
...
vagrant@data-science-toolbox:~$
```

### Setup the ipython environment and run the notebook server

```bash
vagrant@data-science-toolbox:~$ dst setup base
IPython notebook password: <enter a password>
confirm IPython notebook password: <enter password again>
...
vagrant@data-science-toolbox:~$ sudo ipython notebook --profile=dst
```

Now you should be able to run the notebook in a browser: `https://localhost:8888/notebooks/lots-analysis/main.ipynb`.
