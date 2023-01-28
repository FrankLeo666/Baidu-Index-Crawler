import time
import pandas as pd
from qdata.baidu_index import get_search_index


keywords = [['张艺兴', '汪峰'], ['百度'], ['疫情', '杭州'], ['北京', '疫情'], ['猫粮'], ['流浪猫']]
# If a keyword itself is a list,e.g. ['张艺兴', '汪峰'], the sum of the Baidu Index of each keyword in the list would be calculated.  

cookie = 'enter your cookie here'

for j in keywords:
    keywords_list = [j]
    start_date = '2022-01-01'
    end_date = '2022-07-31'
    res_list = list(get_search_index(keywords_list=keywords_list, start_date=start_date, end_date=end_date, cookies=cookie))
    data = pd.DataFrame(res_list).head()
    for i in res_list:
        if i.get("type")=="all":
            print(i.get("index"),end="\t")
    print("")
