"""
Utils for dealing with arxiv API and related processing
"""

import time
import logging
import urllib.request
import feedparser
from collections import OrderedDict
import pandas as pd
import requests

logger = logging.getLogger(__name__)

def get_response(search_query, start_index=0):
    import requests
    # """ pings arxiv.org API to fetch a batch of 100 papers """
    # # fetch raw response
    # base_url = 'http://export.arxiv.org/api/query?'
    # add_url = 'search_query=%s&sortBy=lastUpdatedDate&start=%d&max_results=100' % (search_query, start_index)
    # #add_url = 'search_query=%s&sortBy=submittedDate&start=%d&max_results=100' % (search_query, start_index)
    # search_query = base_url + add_url
    # logger.debug(f"Searching arxiv for {search_query}")
    # with urllib.request.urlopen(search_query) as url:
    #     response = url.read()

    # if url.status != 200:
    #     logger.error(f"arxiv did not return status 200 response")

    
    startdate = "01/06/2022"
    end_date = pd.to_datetime(startdate) + pd.DateOffset(days=start_index)
    
    url = ('https://newsapi.org/v2/everything?'
        'q=News&'
        'from={startdate}&'
        'to={end_date}&'
        'domains=bbc.co.uk&'           
        'language=en&'
        'sortBy=publishedAt&'
        'apiKey=ee48498e46f04eb38a222ad5170fbe8b')
    response2 = requests.get(url).json()
    return response2['articles']

# def encode_feedparser_dict(d):
#     """ helper function to strip feedparser objects using a deep copy """
#     if isinstance(d, feedparser.FeedParserDict) or isinstance(d, dict):
#         return {k: encode_feedparser_dict(d[k]) for k in d.keys()}
#     elif isinstance(d, list):
#         return [encode_feedparser_dict(k) for k in d]
#     else:
#         return d

# def parse_arxiv_url(url):
#     """
#     examples is http://arxiv.org/abs/1512.08756v2
#     we want to extract the raw id (1512.08756) and the version (2)
#     """
#     ix = url.rfind('/')
#     assert ix >= 0, 'bad url: ' + url
#     idv = url[ix+1:] # extract just the id (and the version)
#     parts = idv.split('v')
#     assert len(parts) == 2, 'error splitting id and version in idv string: ' + idv
#     return idv, parts[0], int(parts[1])

def parse_response(response):

    out = []
    # parse = feedparser.parse(response)
    for e in response:
    #     j = encode_feedparser_dict(e)
    #     # extract / parse id information
    #     idv, rawid, version = parse_arxiv_url(j['id'])
    #     j['_idv']= idv
    #     j['_id'] = rawid
    #     j['_version'] = version
    #     j['_time'] = time.mktime(j['updated_parsed'])
    #     j['_time_str'] = time.strftime('%b %d %Y', j['updated_parsed'])
    #     # delete apparently spurious and redundant information
    #     del j['summary_detail']
    #     del j['title_detail']
    #     out.append(j)+
        del e['urlToImage']
        del e['source']
        
        e['tags']=''
        
        del e['content']
        if e['author'] is None:
            e['author']=''
            
            
            
        e['_id']=  e['url']
        e['_time_str']=  pd.to_datetime(e['publishedAt']).ctime()
        e['_time']= pd.to_datetime(e['publishedAt']).value
        e['content']=  e['description']
        e['summary']=  e['description']
        e['authors']=  e['author']
        
        
            
    

        out.append(e)

    return response

# def filter_latest_version(idvs):
#     """
#     for each idv filter the list down to only the most recent version
#     """

#     pid_to_v = OrderedDict()
#     for idv in idvs:
#         pid, v = idv.split('v')
#         pid_to_v[pid] = max(int(v), pid_to_v.get(pid, 0))

#     filt = [f"{pid}v{v}" for pid, v in pid_to_v.items()]
#     return filt