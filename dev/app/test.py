import requests
import json

hearder = {'content-type': 'application/json'}
url = 'http://127.0.0.1:5000'
data = json.dumps({'items': '''@article{170000088750,
                author="藤井雄太郎 and 安藤哲志 and 伊藤孝行",
                title="複数単語間の距離情報及び共起情報を利用した文書分類手法の提案",
                journal="第73回全国大会講演論文集",
                ISSN="",
                publisher="",
                year="2011",
                month="mar",
                volume="2011",
                number="1",
                pages="397-398",
                URL="https://ci.nii.ac.jp/naid/170000088750/",
                DOI="",
                }'''})

r = requests.post(headers=hearder, url=url, data=data)
print(r.content.decode())
