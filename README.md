**Objective for code**: This is a news crawling code to collect news articles from NAVER, one of Korea's biggest portal. This code has been modified from Kihoon Kim and Creator Jo's code. They can be accessed here:https://creatorjo.tistory.com/87


**Instructions**:

Install all necessary packages and web driver.

> import requests
> from bs4 import BeautifulSoup
> headers = {  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36", "Accept-Language":"ko-KR,ko"}


> def create_soup(url):
> res = requests.get(url, headers=headers)
> res.raise_for_status()
> soup = BeautifulSoup(res.text, "lxml")
>> return soup
