import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"
    , "Accept-Language": "ko-KR,ko"
}

def create_soup(url):
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape__news():
    # print("news")
    wb = Workbook()
    ws1 = wb.active
    ws1.title = "news scraping"
    ws1.append(["title", "url", "press", "date", "desc"])
    for page in range(50):
        url = "https://search.naver.com/search.naver?where=news&query=%EC%9D%B4%ED%83%9C%EC%9B%90%20%ED%81%B4%EB%9F%BD%20%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2020.05.07&de=2020.05.07&docid=&nso=so%3Ar%2Cp%3Afrom20200507to20200507%2Ca%3Aall&mynews=0&refresh_start={}&related=0".format(str(1 + 10 * page))
        soup = create_soup(url)

        articles = soup.select("#main_pack > section > div > div.group_news > ul > li")
        for art in articles:
            # print(art)
            a_tag = art.select_one("div.news_wrap.api_ani_send > div > a")
            title = a_tag.text
            link = a_tag["href"]
            press = art.select_one("div.news_wrap.api_ani_send > div > div.news_info > div > a.info.press").text.split(' ')[0].replace('언론사', '')
            date = art.select_one("div.news_wrap.api_ani_send > div > div.news_info > div > span").text
            desc = art.select_one("div > div > div.news_dsc > div > a").text

            ws1.append([title, link, press, date, desc])

    wb.save(filename='my_naver_news_scraping.xlsx')

if __name__ == "__main__":
    scrape__news()