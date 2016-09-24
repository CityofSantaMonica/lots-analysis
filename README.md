# lots-analysis

A project to analyze parking lot data in Santa Monica.

The primary data source is the [City of Santa Monica's Open Data Portal](https://data.smgov.net),
and specifically the [Parking Lot Counts](https://data.smgov.net/Transportation/Parking-Lot-Counts/ng8m-khuz)
dataset.

This dataset is fed a snapshot of the [current state of the parking lots](https://parking.api.smgov.net/lots)
every 5 minutes, 24 hours a day.

## Setup

This project uses the [Data Science Toolbox](http://datasciencetoolbox.org/) to
quickly get an environment going.

### Prerequisites

First install the latest [Vagrant](https://www.vagrantup.com/) (at least `1.8.5`)
and [VirtualBox](https://www.virtualbox.org/) (at least `5.0.26`); these applications
support Linux, OSX, and Windows.

*Windows users*: use [Git BASH](https://git-for-windows.github.io/) for the commands below.

### Clone the repo

```bash
~$ git clone git@github.com:CityofSantaMonica/lots-analysis.git
...
~$ cd lots-analysis
```

### Setup and login to the vm

```bash
~/lots-analysis$ vagrant up
...
~/lots-analysis$ vagrant ssh
...
vagrant@data-science-toolbox:~$
```

### Setup environment and run the notebook server

```bash
vagrant@data-science-toolbox:~$ dst setup base
<enter any password>
<confirm the password>
vagrant@data-science-toolbox:~$ sudo ipython notebook --profile=dst
```

Now you should be able to run the notebook in a browser (on the host machine):
[https://localhost:8888](https://localhost:8888) using the password you provided above.
You can safely ignore certificate warnings (the notebook server uses a self-signed cert.)

### Cleanup

When you are finished, release any resources used by the vm

```bash
vagrant@data-science-toolbox:~$ logout
...
~/lots-analysis$ vagrant destroy
```
