import yake
import json

language = "en"
max_ngram_size = 3
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 8


def extract_keyword(sentenceorder,sentence,sentimentscore,sentimentCateg,resp):

    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(sentence)

    if resp == 99 or sentimentscore <= 5:
        print("Unhappy customer, Invoke Agent recommendation Service")
        with open('data/datafile.txt', 'w', encoding='utf-8') as f:
            line = ' '.join(str(kw) for kw in keywords)
            f.write(line + '\n')
            f.close()

if __name__ == "__main__":
    print("\n1st statement :")
    text = "Your site is not working when I try to upload documents.\
     I contacted support and they could not help me. \
      They left me on hold for 56 min prior to me hanging up and calling again."
    positive="positive"
    resp=99
    extract_keyword(1,text,8,positive,resp)
