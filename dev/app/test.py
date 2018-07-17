"""
$python test.py https://bib2tex.arukascloud.io                                                                                                                                   +[master]
\begin{thebibliography}{9}
        \bibitem{} 
\end{thebibliography}
"""

import requests
import json
import sys

if __name__ == '__main__':

    args = sys.argv

    hearder = {'content-type': 'application/json'}
    url = args[1]
    data = json.dumps({'items': '''@article{170000088750,
                    author="usagikeri",
                    title="論文タイトル",
                    journal="Github",
                    ISSN="",
                    publisher="",
                    year="2018",
                    month="mar",
                    volume="2018",
                    number="1",
                    pages="01-08",
                    URL="https://github.com/usagikeri",
                    DOI="",
                    }'''})
    
    r = requests.post(headers=hearder, url=url, data=data)
    print(r.content.decode())
