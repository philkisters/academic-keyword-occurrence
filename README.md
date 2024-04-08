# Historic word occurrence in academic papers

## Summary

This script extracts the historical word occurrence of a search term in
academic papers (from Google Scholar). It allows for spotting trends
in research and analyzing the relevance of a topic over time.

There is a Python 3 branch (master) and a Python 2 branch (python2).

## Usage

`python extract_occurrences.py '<keyword1, keyword2, ...>' <start date> <end date>`

This command lists the number of publications for every year using
this keyword. Using multiple keywords lists the number of publication for each keyword, allowing to compare different keywords and their significance. The script just searches for articles and excludes
patents and citations.


### Alternative: Usage with Docker

You can use [Docker](https://www.docker.com/) to run this script, without the need of having Python or its dependencies installed.

1. Update the `command` with your search term and time range in `docker-compose.yml`
2. run `docker-compose up`

## Example

- Search term: 'bitcoin'
- Desired time span: 2000 to 2015
- Command: `python ./extract_occurrences.py 'bitcoin' 1990 2022`
- Command: `python ./extract_occurrences.py '"Smart City", "Digital City", "Intelligent City", "Resilient City"' 1990 2022`
- Command: `python ./extract_occurrences.py '"Wired City", "Connected City", "Sustainable City"' 1990 2022`
- Output: `out.csv`, with the following contents:

| year | keyword1 | keyword2 |
|------|--------- |----------|
| ...  |    ...   |	  ...    |
| 2011 |    141   |   141    |   
| 2012 |    292   |   122    |
| 2013 |    889   |   209    |
| 2014 |    2370  |   354    |
| 2015 |    2580  |   280    |


![bitcoin chart](https://raw.githubusercontent.com/Pold87/academic-keyword-occurrence/master/bitcoin_chart.png "bitcoin chart")

## Credits
Created by Volker Strobel - volker.strobel87@gmail.com
adapted by Philipp Kisters - philkisters@gmail.com

If you use this code in academic papers, please cite this repository via Zenodo (http://doi.org/10.5281/zenodo.1218409):

Volker Strobel. (2018, April 14). Pold87/academic-keyword-occurrence: First release (Version v1.0.0). Zenodo. http://doi.org/10.5281/zenodo.1218409
