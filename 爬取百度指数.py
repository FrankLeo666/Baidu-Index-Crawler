import time
from qdata.baidu_index.common import split_keywords
import pandas as pd
from qdata.baidu_index import get_search_index


keywords = [['张艺兴', '汪峰'], ['百度'], ['疫情', '杭州'], ['北京', '疫情'], ['猫粮'], ['流浪猫']]

# keywords = []
#
# f = open("C:\\Users\liufengqi\Desktop\\Nw.txt", "r", encoding="UTF-8")
# content = f.readlines()
# for i in content:
#     a = i.strip("\n")
#     b = a.split("\t")
#     keywords.append(b)
# print(keywords)

cookie = 'BIDUPSID=2D84AB012DEEEDBAE9BA1C642BC960C7; PSTM=1627214544; __yjs_duid=1_a377baa735ee6ff6c6e4af7ab8e128731627214565115; BDUSS=kloTTl4VWFNTm1zaXhMUmoxeXlSaTlmUXFCeXRFNmJLbGlNT2J3Zk1TZ1kyaVJpSVFBQUFBJCQAAAAAAAAAAAEAAADy-aYaz6--7dK7vL63sbuoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABhN~WEYTf1hY; BAIDUID=655153E438BF1B61F34AF2709886B904:SL=0:NR=10:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BA_HECTOR=8kak058kak212ha0012k6o3e1he2fie17; ZFY=UB9xxpCa56CHHJZd11lkC6F1H2fbW1PLYVeke13AWXc:C; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc=%7B%22uid_%22%3A%7B%22value%22%3A%22447150578%22%2C%22scope%22%3A1%7D%7D; bdindexid=rkuiqsgmnor8hcunfj0grg4kh1; BDRCVFR[bIKc3BPCk_C]=LpDQ8KNdUpDUhGBrHT8mvqV; H_PS_PSSID=26350; delPer=0; PSINO=5; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1658971026,1658973730,1658973825; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1658973829; ab_sr=1.0.1_MWIyNDQ2MDRkNDA2MzdlZTdhMmZlZWE5MWJiOTA0MTFkYTliZmYxMDBhNDY4NjZlYjk0MWEwZDVhOTI4MTgzM2ZhYzE2ZjljZDI0NjYzYjVlM2MxMzNkYTRhZTNkYTg5MGNhYzI5NTA5OTg1ZjU3MDc2Y2YyMDNlN2U4NjdlM2JhMmI4NjNkNDljNDY3NzlkZTY1Zjc4ZmZjM2Y1OTQ5ZQ==; BDUSS_BFESS=kloTTl4VWFNTm1zaXhMUmoxeXlSaTlmUXFCeXRFNmJLbGlNT2J3Zk1TZ1kyaVJpSVFBQUFBJCQAAAAAAAAAAAEAAADy-aYaz6--7dK7vL63sbuoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABhN~WEYTf1hY; RT="z=1&dm=baidu.com&si=57d38e81-811d-462a-a461-ca629ad13805&ss=l64ciiv7&sl=r&tt=t73&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=1o5fo"'

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
