import json
from sentimentanalyzer import *
from keywordextractor import *

#sentiment analysis on data in json file
with open('data/caller1.json') as f:
    data = json.load(f)
    for caller1 in data['caller1']:
        #print(caller1)
        #print(caller1['sentence'])
        sentenceorder = caller1['sentenceorder']
        callerresp = caller1['sentence']
        sentimentscore = caller1['sentimentscore']
        sentimentCateg = caller1['sentimentCateg']
        resp=sentiment_scores(callerresp)
        extract_keyword(sentenceorder,callerresp,sentimentscore,sentimentCateg,resp)





