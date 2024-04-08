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

## Example Bitcoin

- Search term: 'bitcoin'
- Desired time span: 2000 to 2015
- Command: `python ./extract_occurrences.py 'bitcoin' 2000 2015`
- Output: `out.csv`, with the following contents:

| year | bitcoin  | 
|------|--------- |
| ...  |    ...   |
| 2011 |    141   |
| 2012 |    292   |
| 2013 |    889   |
| 2014 |    2370  |
| 2015 |    2580  |

## Example Compare Smart City Terms

- Search term: Various Smart City terms
- Desired time span: 1990 to 2022
- Command: `python ./extract_occurrences.py '"Smart City", "Digital City", "Intelligent City", Resilient City"' 1990 2022`
- Command: `python ./extract_occurrences.py '"Wired City", "Connected City", "Sustainable City"' 1990 2022`
- Output: `out.csv`, with the following contents:

| year  | "Smart City"  |  "Digital City"  | "Intelligent City"  |  "Resilient City"  |
|------|--------- | ------|--------- |------|
| 1990  | 19  | 2  | 10  | 1  |
| 1991  | 19  | 2  | 7  | 2  |
| 1992  | 31  | 4  | 12  | 1  |
| 1993  | 24  | 4  | 9  | 0  |
| 1994  | 31  | 6  | 12  | 1  |
| 1995  | 31  | 19  | 10  | 5  |
| 1996  | 51  | 30  | 14  | 3  |
| 1997  | 60  | 53  | 33  | 1  |
| 1998  | 83  | 68  | 23  | 0  |
| 1999  | 77  | 116  | 31  | 4  |
| 2000  | 103  | 151  | 47  | 6  |
| 2001  | 100  | 237  | 39  | 8  |
| 2002  | 90  | 208  | 60  | 9  |
| 2003  | 155  | 366  | 51  | 13  |
| 2004  | 169  | 327  | 56  | 11  |
| 2005  | 184  | 338  | 61  | 57  |
| 2006  | 188  | 286  | 74  | 84  |
| 2007  | 251  | 328  | 76  | 86  |
| 2008  | 272  | 404  | 69  | 106  |
| ...   | ...  | ...  | ... | ... |

![Smart City chart](https://raw.githubusercontent.com/philkisters/academic-keyword-occurrence/master/smart_city_terminology.png "Smart City chart")

## Credits
Created by Volker Strobel - volker.strobel87@gmail.com
adapted by Philipp Kisters - philkisters@gmail.com

If you use this code in academic papers, please cite this repository via Zenodo (http://doi.org/10.5281/zenodo.1218409):

Volker Strobel. (2018, April 14). Pold87/academic-keyword-occurrence: First release (Version v1.0.0). Zenodo. http://doi.org/10.5281/zenodo.1218409
