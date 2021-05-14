# Election 2021

The folder contains all the work that is done for 2021 Assembly Elections.

1. Assam
2. Kerala
3. Puducherry
4. Tamil Nadu
5. West Bengal

## Looking for just the data?

Download the ZIP file and look inside the `may2021/<state-code>` folder for CSV files of all constituencies stored by their constituency number.
There is also a `all_candidate.csv` file each of the state folders which is the combined file of all the constituencies

## Using the software

### Pre-requisites

- Python 3.7 or higher installed in your computer

### Install Dependencies

```
pip install -r requirements.txt
```

### Running the scapper

```
cd may2021
scrapy crawl eci
```

### Software License

The content is MIT Licensed. You are free to copy and distribute.
