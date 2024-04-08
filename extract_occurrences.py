# By: Volker Strobel, improved by Patrick Hofmann
from bs4 import BeautifulSoup
from urllib.request import Request, build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
from http.cookiejar import MozillaCookieJar
import re, time, sys, urllib

def get_num_results(search_term, start_date, end_date):
    """
    Helper method, sends HTTP request and returns response payload.
    """

    # Open website and read html
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
    query_params = { 'q' : search_term, 'as_ylo' : start_date, 'as_yhi' : end_date}
    url = "https://scholar.google.com/scholar?as_vis=1&hl=en&as_sdt=1,5&" + urllib.parse.urlencode(query_params)
    opener = build_opener()
    request = Request(url=url, headers={'User-Agent': user_agent})
    handler = opener.open(request)
    html = handler.read() 

    # Create soup for parsing HTML and extracting the relevant information
    soup = BeautifulSoup(html, 'html.parser')
    div_results = soup.find("div", {"id": "gs_ab_md"}) # find line 'About x results (y sec)

    if div_results != None:

        res = re.findall(r'(\d+).?(\d+)?.?(\d+)?\s', div_results.text) # extract number of search results
        
        if res == []:
            num_results = '0'
            success = True
        else:
            num_results = ''.join(res[0]) # convert string to numbe
            success = True

    else:
        success = False
        num_results = 0

    return num_results, success

def get_range(search_terms, start_date, end_date):

    fp = open("out.csv", 'w')
    fp.write("year," + ",".join(search_terms)+ "\n")
    print("year," + ",".join(search_terms)+ "\n")

    for date in range(start_date, end_date + 1):
        results = []
        for search_term in search_terms:
            num_results, success = get_num_results(search_term, date, date)
            if not(success):
                print("It seems that you made to many requests to Google Scholar. Please wait a couple of hours and try again.")
                break
            results.append(num_results)
            time.sleep(5)
        year_results = "{0},{1}".format(date, ",".join(results))
        print(year_results)
        fp.write(year_results + '\n')
        time.sleep(5)

    fp.close()

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("******")
        print("Academic word relevance")
        print("******")
        print("")
        print("Usage: python extract_occurences.py '<search term 1>, <search term 2>, ...' <start date> <end date>")
        
    else:
        search_term_list = sys.argv[1]
        search_terms = search_term_list.split(',')
        start_date = int(sys.argv[2])
        end_date = int(sys.argv[3])
        html = get_range(search_terms, start_date, end_date)
