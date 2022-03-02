from json import loads, dumps
from requests import get
import csv
import time
import os

#request_result = get("https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=en&tl=bn&q=life has no meaning")
#translated_text = loads(request_result.text)[0][0][0]
#print(translated_text)

def translate_function(text):
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=en&tl=bn&q="+text
    try:
        request_result = get(url)
        print(request_result.text)
        print(type(request_result.text))
        str = ""
        _list = loads(request_result.text)
        print(len(_list))
        print(_list)
        _list = _list[0]
        trans_sen = []
        for i in range(0, len(_list)):
            # print ("i = ",i,  _list[i][0])
            sen = _list[i][0]
            trans_sen.append(sen)
            # print("sen = ", sen)
        #translated_text = loads(request_result.text)[0][0][0]
        #print(translated_text)
        return trans_sen
    except Exception as e:
        print(e)
        return []

# https://github.com/ssut/py-googletrans/issues/268
# https://analyticsindiamag.com/10-popular-datasets-for-sentiment-analysis/


def read_csv_file(file_name):
    w = open(os.path.join('.', 'IMDB_Dataset', 'bangla_IMDB_dataset.csv'), 'w', encoding='utf-8', errors='ignore')
    writer = csv.writer(w)
    writer.writerow(['review', 'sentiment'])
    with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
        csv_lines = csv.DictReader(f)
        idx = 0
        for row in csv_lines:
            review = row['review']
            sentiment = row['sentiment']
            bn_review = translate_function(text=review)
            bn_review = dumps(bn_review)
            writer.writerow([bn_review, sentiment])
            idx = idx + 1
            if idx < 1:
                print(review)
                print(bn_review)
                break
            print('done ', idx)
            if idx%100 == 0:
                time.sleep(10)
                print("sleeping")
            if idx == 2:
                break
        w.close()


trans_sen = translate_function(text="you are useless rizvee.")
#print(trans_sen)
# read_csv_file(file_name=os.path.join('.', 'IMDB_Dataset', 'IMDB Dataset.csv'))