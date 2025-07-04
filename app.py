from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_lunch():
    url = "https://school.koreacharts.com/school/meals/B000012060/contents.html"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    
    soup = BeautifulSoup(html, 'html.parser')
    
    source = soup.select_one("body > div > div > div > section.content > div:nth-child(6) > div > div > div.box-body > table > tbody > tr:nth-child(2) > td:nth-child(3) > p:nth-child(1)")
    
    text = source.text
    text = text.replace("""[중식]
    
    																	""","[중식]\n")
    text = text.replace("*","\n*")

    return text

def get_dinner():
    url = "https://school.koreacharts.com/school/meals/B000012060/contents.html"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    
    soup = BeautifulSoup(html, 'html.parser')
    
    source = soup.select_one("body > div > div > div > section.content > div:nth-child(6) > div > div > div.box-body > table > tbody > tr:nth-child(2) > td:nth-child(3) > p:nth-child(2)")
    
    text = source.text
    text = text.replace("""[석식]
    
    																	""","[석식]\n")
    text = text.replace("*","\n*")

    return text

@app.route("/")
def index():
    return "챗봇 서버 작동 중!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    user_input = data["userRequest"]["utterance"]

    if "중식" in user_input:
        meal_info = get_lunch()
    elif "석식" in user_input:
        meal_info = get_dinner()

    return jsonify({
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": meal_info
                    }
                }
            ]
        }
    })

if __name__ == "__main__":
    app.run()
