from json import loads
from requests import get
request_result = get("https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=en&tl=bn&q=you are a piece of shit")
translated_text = loads(request_result.text)[0][0][0]
print(translated_text)

# https://github.com/ssut/py-googletrans/issues/268
# https://analyticsindiamag.com/10-popular-datasets-for-sentiment-analysis/
