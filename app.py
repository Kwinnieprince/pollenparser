import sys
from flask import Flask
from datetime import date
import requests
from bs4 import BeautifulSoup

pollen_url = "https://www.meteo.be/nl/weer/verwachtingen/stuifmeelallergie-en-hooikoorts"
column1_header = "column_1"
column2_header = "column_2"
column3_header = "allergie"

app = Flask(__name__)

def get_current_day():
    return str(date.today())

@app.route("/")
def parse_results():
    page = get_page()
    results = parse_page(page.content)
    return results[0]

def get_page():
    page = None
    url = pollen_url
    try:
        page = requests.get(url)
        if page.status_code != 200:
            print("Unable to retrieve page (returncode != 200):\n%s", url)
            sys.exit(1)
    except:
        print("Unable to retrieve page:\n%s", url)
        sys.exit(-1)
    return page

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    header_above_table = soup.find("h3", id="grassenstuifmeel")
    table = header_above_table.find_next("table")
    results = []
    for row in table.findAll('tr'):
        item = {}
        if row.findAll("th"):
            column1_header = row.findAll("th")[0].string
            column2_header = row.findAll("th")[1].string
            continue
        item[column1_header] = row.findAll("td")[0].string
        item[column2_header] = row.findAll("td")[1].string
        item[column3_header] = row.findAll("td")[0].string
        # Add a * behind the current date row
        if item[column1_header].startswith(get_current_day()):
            item[column2_header] = item[column2_header] + " (today)"
        results.append(item)
    print("The following results were retrieved:\n%s", repr(results))
    return results

@app.after_request
def after_request(response):
    header = response.headers
    # header['Access-Control-Allow-Origin'] = 'https://weg.kwinten.me'
    return response

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)