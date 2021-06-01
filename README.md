**Objective for code**: This is a news crawling code to collect news articles from NAVER, one of Korea's biggest portal. This code has been set in a way that makes it possible to collect data in a chronological order (news articles' publication) within a set time frame. This code has been modified from Kihoon Kim and Creator Jo's code. They can be accessed here: https://creatorjo.tistory.com/87 (It is in Korean so please let me know if there are areas that require translations)


**Instructions**:

Install all necessary packages and web driver. These are all needed for scrapping and later saving scrapped articles into an excel file.

```

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

headers = {  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36", "Accept-Language":"ko-KR,ko" }


def create_soup(url):
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
return soup

```

Now here is the code. Write the url of the articles you want to collect. I included the dates and the query in mine. Since NAVER updates its page frequently, it is important to be able to find and select the elements you want to scrape. In this code, I scrapped the title, link, press name, date of publication, and description of the article. One thing to note here is that I made sure to scrape data in a chronological order by setting up the url query search in a way that would collect news from 05-07 to 05-09

#main_pack > section > div > div.group_news > ul > li

```


def scrape__news():
    # print("news")
    wb = Workbook()
    ws1 = wb.active
    ws1.title = "news scraping"
    ws1.append(["title", "url", "press", "date", "desc"])
    for page in range(50):
        url = "https://search.naver.com/search.naver?where=news&query=%EC%9D%B4%ED%83%9C%EC%9B%90%20%ED%81%B4%EB%9F%BD%20%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2020.05.07&de=2020.05.07&docid=&nso=so%3Ar%2Cp%3Afrom20200507to20200509%2Ca%3Aall&mynews=0&refresh_start={}&related=0".format(str(1 + 10 * page))
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

```
