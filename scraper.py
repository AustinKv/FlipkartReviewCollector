import json
import requests_html
from requests_html import HTMLSession, HTML
from typing import List, Tuple, Any, Dict


class FlipkartScraper:

    def __init__(self, pages: int, url: str):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/116.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'
        }

        self.pages = pages
        self.url = url
        self.session = HTMLSession()

    def iterate_over_pages(self) -> List[dict]:
        reviews = []
        print(f"Page: {pages}")
        r = self.session.get(f'{self.url}&page={pages}', headers=self.headers)
        if self.has_reviews(r.html):
            new_reviews = self.get_reviews_from_page(r.html)
            print("New reviews!")
            print(new_reviews)
            reviews += new_reviews
        else:
            print("No reviews!")

        return reviews

    def has_reviews(self, page_content: HTML) -> bool:
        if page_content.find('div.t-ZTKy'):
            return True
        return False

    def get_reviews_from_page(self, page_content: int) -> list[dict[str, Any]]:

        reviews = []

        user0 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(3) > div > div > div > div.row._3n8db9 > div.row > p._2sc7ZR._2V5EHH',
            first=True).text
        title0 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(3) > div > div > div > div:nth-child(1) > p',
            first=True).text
        date0 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(3) > div > div > div > div.row._3n8db9 > div.row > p:nth-child(5)',
            first=True).text
        review0 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(3) > div > div > div > div:nth-child(2) > div > div > div',
            first=True).text.replace('\n', '')
        reviews.append({
            'user': user0,
            'title': title0,
            'date': date0,
            'review': review0
        })

        user1 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(4) > div > div > div > div.row._3n8db9 > div.row > p._2sc7ZR._2V5EHH',
            first=True).text
        title1 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(4) > div > div > div > div:nth-child(1) > p',
            first=True).text
        date1 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(4) > div > div > div > div.row._3n8db9 > div.row > p:nth-child(5)',
            first=True).text
        review1 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(4) > div > div > div > div:nth-child(2) > div > div > div',
            first=True).text.replace('\n', '')
        reviews.append({
            'user': user1,
            'title': title1,
            'date': date1,
            'review': review1
        })

        user2 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(5) > div > div > div > div.row._3n8db9 > div.row > p._2sc7ZR._2V5EHH',
            first=True).text
        title2 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(5) > div > div > div > div:nth-child(1) > p',
            first=True).text
        date2 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(5) > div > div > div > div.row._3n8db9 > div.row > p:nth-child(5)',
            first=True).text
        review2 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(5) > div > div > div > div:nth-child(2) > div > div > div',
            first=True).text.replace('\n', '')
        reviews.append({
            'user': user2,
            'title': title2,
            'date': date2,
            'review': review2
        })

        user3 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(6) > div > div > div > div.row._3n8db9 > div.row > p._2sc7ZR._2V5EHH',
            first=True).text
        title3 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(6) > div > div > div > div:nth-child(1) > p',
            first=True).text
        date3 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(6) > div > div > div > div.row._3n8db9 > div.row > p:nth-child(5)',
            first=True).text
        review3 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(6) > div > div > div > div:nth-child(2) > div > div > div',
            first=True).text.replace('\n', '')
        reviews.append({
            'user': user1,
            'title': title1,
            'date': date1,
            'review': review1
        })

        user4 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(7) > div > div > div > div.row._3n8db9 > div.row > p._2sc7ZR._2V5EHH',
            first=True).text
        title4 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(7) > div > div > div > div:nth-child(1) > p',
            first=True).text
        date4 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(7) > div > div > div > div.row._3n8db9 > div.row > p:nth-child(5)',
            first=True).text
        review4 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(7) > div > div > div > div:nth-child(2) > div > div > div',
            first=True).text.replace('\n', '')
        reviews.append({
            'user': user4,
            'title': title4,
            'date': date4,
            'review': review4
        })

        user5 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(8) > div > div > div > div.row._3n8db9 > div.row > p._2sc7ZR._2V5EHH',
            first=True).text
        title5 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(8) > div > div > div > div:nth-child(1) > p',
            first=True).text
        date5 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(8) > div > div > div > div.row._3n8db9 > div.row > p:nth-child(5)',
            first=True).text
        review5 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(8) > div > div > div > div:nth-child(2) > div > div > div',
            first=True).text.replace('\n', '')
        reviews.append({
            'user': user5,
            'title': title5,
            'date': date5,
            'review': review5
        })

        user6 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(9) > div > div > div > div.row._3n8db9 > div.row > p._2sc7ZR._2V5EHH',
            first=True).text
        title6 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(9) > div > div > div > div:nth-child(1) > p',
            first=True).text
        date6 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(9) > div > div > div > div.row._3n8db9 > div.row > p:nth-child(5)',
            first=True).text
        review6 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(9) > div > div > div > div:nth-child(2) > div > div > div',
            first=True).text.replace('\n', '')
        reviews.append({
            'user': user6,
            'title': title6,
            'date': date6,
            'review': review6
        })

        user7 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(10) > div > div > div > div.row._3n8db9 > div.row > p._2sc7ZR._2V5EHH',
            first=True).text
        title7 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(10) > div > div > div > div:nth-child(1) > p',
            first=True).text
        date7 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(10) > div > div > div > div.row._3n8db9 > div.row > p:nth-child(5)',
            first=True).text
        review7 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(10) > div > div > div > div:nth-child(2) > div > div > div',
            first=True).text.replace('\n', '')
        reviews.append({
            'user': user7,
            'title': title7,
            'date': date7,
            'review': review7
        })

        user8 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(11) > div > div > div > div.row._3n8db9 > div.row > p._2sc7ZR._2V5EHH',
            first=True).text
        title8 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(11) > div > div > div > div:nth-child(1) > p',
            first=True).text
        date8 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(11) > div > div > div > div.row._3n8db9 > div.row > p:nth-child(5)',
            first=True).text
        review8 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(11) > div > div > div > div:nth-child(2) > div > div > div',
            first=True).text.replace('\n', '')
        reviews.append({
            'user': user8,
            'title': title8,
            'date': date8,
            'review': review8
        })

        user9 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(12) > div > div > div > div.row._3n8db9 > div.row > p._2sc7ZR._2V5EHH',
            first=True).text
        title9 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(12) > div > div > div > div:nth-child(1) > p',
            first=True).text
        date9 = page_content.find(
            '#container > div > div._2tsNFb > div > div > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(12) > div > div > div > div.row._3n8db9 > div.row > p:nth-child(5)',
            first=True).text
        review9 = page_content.find(
            '#container > div > div._2tsNFb > div > div._1YokD2._2GoDe3.col-12-12 > div._1YokD2._3Mn1Gg.col-9-12 > div:nth-child(12) > div > div > div > div:nth-child(2) > div > div > div',
            first=True).text.replace('\n', '')
        reviews.append({
            'user': user9,
            'title': title9,
            'date': date9,
            'review': review9
        })

        return reviews


if __name__ == '__main__':
    url = input("Paste Product Review Page URL here: ")
    print(url)
    pagesstr = input("Enter Page Number of Review Page: ")
    pages = int(pagesstr)
    print(pages)
    scraper = FlipkartScraper(pages, url)
    all_reviews = scraper.iterate_over_pages()
    print("Done")
    print(all_reviews)

with open('flipkartData.json', 'w') as f:
    json.dump(all_reviews, f)
