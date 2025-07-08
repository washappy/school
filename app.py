from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import datetime

app = Flask(__name__)

def get_today():
    today = datetime.date.today()
    
    month = today.month
    day = today.day
    weekday = today.weekday()

    weekdays = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    weekday_str = weekdays[weekday]

    result = f"{month}월 {day}일 {weekday_str}"
    
    return result

def get_lunch():
    #url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EA%B2%BD%EA%B8%B0%EA%B3%A0+%EA%B8%89%EC%8B%9D&ackey=vwcnif47"

    #url = "https://m.search.naver.com/search.naver?query=경기고+급식&sm=mtp_hty.top&where=m"
    url = "https://school.koreacharts.com/school/meals/B000012060/contents.html"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    
    soup = BeautifulSoup(html, 'html.parser')

    """
    k=1
    for i in range(1,11):
        if soup.select_one("#main_pack > div.sc_new.cs_common_module.case_normal.color_5._school.cs_kindergarten._edu_list > div.cm_content_wrap > div > div.timeline_list.open > ul > li:nth-child({}) > div > strong".format(i)) is None:
            continue
        if "TODAY" in soup.select_one("#main_pack > div.sc_new.cs_common_module.case_normal.color_5._school.cs_kindergarten._edu_list > div.cm_content_wrap > div > div.timeline_list.open > ul > li:nth-child({}) > div > strong".format(i)).text:
            k = i
            break
    day = soup.select_one("#main_pack > div.sc_new.cs_common_module.case_normal.color_5._school.cs_kindergarten._edu_list > div.cm_content_wrap > div > div.timeline_list.open > ul > li:nth-child({}) > div > strong".format(k))

    source = soup.select_one("#main_pack > div.sc_new.cs_common_module.case_normal.color_5._school.cs_kindergarten._edu_list > div.cm_content_wrap > div > div.timeline_list.open > ul > li:nth-child({}) > div > div > ul".format(k))
    """

    today = datetime.date.today()
    tday = str(today.day)

    k = 0
    i = 2
    while True:
        if soup.select_one("body > div > div > div > section.content > div:nth-child(6) > div > div > div.box-body > table > tbody > tr:nth-child({}) > td:nth-child(1)".format(i)) is None:
            break
        if tday = soup.select_one("body > div > div > div > section.content > div:nth-child(6) > div > div > div.box-body > table > tbody > tr:nth-child({}) > td:nth-child(1)".format(i)):
            k = i
            break

        i+=1
        
    a = ""
    if k != 0:
        a = "TODAY"
    else:
        k = 2
    day = soup.select_one("body > div > div > div > section.content > div:nth-child(6) > div > div > div.box-body > table > tbody > tr:nth-child({}) > td:nth-child(2)".format(k))

    source = soup.select_one("body > div > div > div > section.content > div:nth-child(6) > div > div > div.box-body > table > tbody > tr:nth-child({}) > td:nth-child(3) > p:nth-child(1)".format(k))
    
    text = source.text
    text = text.replace("""[중식]

																	""","[중식]\n")
    text = text.replace("*","\n*")
    
    #if ("TODAY" in text):
    return (get_today+a+"\n\n"+text)
    #else:
    #return("오늘 중식은 없습니다")

    """
    found = False
    t = ""
    for tag in soup.find_all(True):
        # tag.get_text()가 아니라 tag 자체의 html로 찾음
        tag_html = str(tag)
        t+=tag_html

        if re.search(r"TODAY", tag_html):
            t+=tag_html+"\n"
            found = True
            
    return t
    if not found:
        return("없음")
    """

def get_dinner():
    #url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EA%B2%BD%EA%B8%B0%EA%B3%A0+%EA%B8%89%EC%8B%9D&ac"

    #url = "https://m.search.naver.com/search.naver?query=경기고+급식&sm=mtp_hty.top&where=m"

    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blBI&pkid=682&os=24929299&qvt=0&query=경기고등학교 급식식단"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    
    soup = BeautifulSoup(html, 'html.parser')

    k=2
    for i in range(1,11):
        if soup.select_one("#main_pack > div.sc_new.cs_common_module.case_normal.color_5._school.cs_kindergarten._edu_list > div.cm_content_wrap > div > div.timeline_list.open > ul > li:nth-child({}) > div > strong".format(i)) is None:
            continue
        if "TODAY" in soup.select_one("#main_pack > div.sc_new.cs_common_module.case_normal.color_5._school.cs_kindergarten._edu_list > div.cm_content_wrap > div > div.timeline_list.open > ul > li:nth-child({}) > div > strong".format(i)).text:
            k = i + 1
            break
    day = soup.select_one("#main_pack > div.sc_new.cs_common_module.case_normal.color_5._school.cs_kindergarten._edu_list > div.cm_content_wrap > div > div.timeline_list.open > ul > li:nth-child({}) > div > strong".format(k))

    source = soup.select_one("#main_pack > div.sc_new.cs_common_module.case_normal.color_5._school.cs_kindergarten._edu_list > div.cm_content_wrap > div > div.timeline_list.open > ul > li:nth-child({}) > div > div > ul".format(k))
    
    text = source.text
    text = text.replace(" ","\n*").rstrip("*")
    
    #if ("TODAY" in text):
    return (day.text+"\n"+text)
    #else:
        #return("오늘 석식은 없습니다")

@app.route("/")
def index():
    return "서버 작동 중! :D"

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
