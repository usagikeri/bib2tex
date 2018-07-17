from flask import Flask, request
import bibtexparser

app = Flask(__name__)


@app.route("/", methods=['POST'])
def bib2tex():
    return_text = ''
    items = bibtexparser.loads(request.json['items']).entries

    num = 9 if len(items) < 10 else 99
    return_text += '\\begin{{thebibliography}}{{{}}}\n'.format(num)

    for item in items:
        author = item['author'].replace('and', '，')
        title = item['title']
        journal = item['journal']
        year = item['year']

        return_text += '\t\\bibitem{{}} {}，``{}\'\'，{}，{}．\n' .format(author, title, journal, year)

    return_text += '\\end{thebibliography}'

    return return_text


if __name__ == "__main__":
    app.run(host='0.0.0.0',port="80")
