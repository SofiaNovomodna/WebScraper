import os
import json
import requests
from bs4 import BeautifulSoup


product_code = input("Provide product code:")
page = 1
next=True
headers = {
    'Host': 'www.ceneo.pl',
    'Cookie': 'sv3=1.0_6dca811d-3ccc-11f1-989d-c722ed84714f; userCeneo=ID=c0f8ff09-d09b-4d8e-8a09-34677276dac2; __RequestVerificationToken=lULItM5cBuNr88qDMRK3sgp8f_OadPzAY4h3oIy4OGVpt0QLcAGFOLPQU3HiLG63LgnICSb-cpwdHa3eOFrK3bEXy0Qp0dKDaKubZMt_GIg1; ai_user=nOIGY|2026-04-20T15:20:16.354Z; __utmf=b005f137479d61dcd846fea07a2e7c2c_Dsgqi6QMc9CtX7buqOpcIw%3D%3D; appType=%7B%22Value%22%3A1%7D; cProdCompare_v2=; browserBlStatus=0; ga4_ga=GA1.2.6dca811d-3ccc-11f1-989d-c722ed84714f; _gcl_au=1.1.39132276.1776698419; consentcookie=eyJBZ3JlZUFsbCI6dHJ1ZSwiQ29uc2VudHMiOlsxLDMsNCwyXSwiVENTdHJpbmciOiJDUWk5ajBBUWk5ajBBR3lBQkJQTENiRXNBUF9nQUFBQUFCNVlLTHREN0Q3ZExXRmd3SHhuWUtzUU1JMWY4ZUNBWW9RQUJBYUJBU0FCU0FLUUlJUUdra0FRSkFTZ0JBQUNBQUlBS0NSQklRQU1BQUNBQ0VBQVFJQUFJUUFFQUFDUUFRZ0tBQUFFaUFBUUFBQVlBQUFpQ0lBQUFRQUlnRUlFRUJFQW1RaEFBQUlBRUZBQWpBQUVJQUFBQUFBQUFBQUFBd0FBQUFBQ0FBSUFBQUFBZ0NBQUFJQUFBQUFBQUVBQVFCZ0lFQUFBQUFFQUFBQUFBQUFBQVFBQUFCQUFBQUFJS0xnQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUJZS0FEQUFFRkZ3a0FHQUFJS0xob0FNQUFRVVhFUUFZQUFnb3VLZ0F3QUJCUmNaQUJnQUNDaTQ2QURBQUVGRnlFQUdBQUlLTGtvQU1BQVFVWEtRQVlBQWdvdVdnQXdBQkJSY0EuSUtMdEQ3RDdkTFdGZ3dIeG5ZS3NRTUkxZjhlQ0FZb1FBQkFhQkFTQUJTQUtRSUlRR2trQVFKQVNnQkFBQ0FBSUFLQ1JCSVFBTUFBQ0FDRUFBUUlBQUlRQUVBQUNRQVFnS0FBQUVpQUFRQUFBWUFBQWlDSUFBQVFBSWdFSUVFQkVBbVFoQUFBSUFFRkFBakFBRUlBQUFBQUFBQUFBQUF3QUFBQUFDQUFJQUFBQUFnQ0FBQUlBQUFBQUFBRUFBUUJnSUVBQUFBQUVBQUFBQUFBQUFBUUFBQUJBQUFBQUlBIiwiVmVyc2lvbiI6InYzIn0=; FPID=FPID2.2.9oh%2F7a5XhKn4rY%2FP6ThpuTUEt6JTsI%2FnEpcDYsL%2F8VU%3D; FPLC=81YG97iT%2BibxRC6kCqwafOoUh2TbvMjlliA9%2FmmWk8W%2FEGpVKQBfnbqtvRInha6xZ62lnFDRLlMF9O0i65W%2F3LWznP6WDT8hZQOam9W2HfLPGMs%3D; nps3=SessionStartTime=1776698467,SurveyId=68; _fbp=fb.1.1776698468845.69781328962113362; _tt_enable_cookie=1; _ttp=01KPNQPB8KQ3MYDMAN6N15VSN2_.tt.1; st2=_gd%3dwww.google.com%2csref%3dhttps%3a%2f%2fwww.google.com%2f%2c_t%3d63912302498%2cencode%3dtrue; urdsc=1; ai_session=yBMXG|1776698417010|1776698521262.9; ga4_ga_K2N2M0CBQ6=GS2.2.s1776698416$o1$g1$t1776698521$j38$l0$h1048071043; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%2C%22expiryDate%22%3A%222027-04-20T15%3A22%3A01.591Z%22%7D; __rtbh.aid=%7B%22eventType%22%3A%22aid%22%2C%22id%22%3A%226dca811d-3ccc-11f1-989d-c722ed84714f%22%2C%22expiryDate%22%3A%222027-04-20T15%3A22%3A01.591Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%225Zsgn1EQXlvdI2P3EBZI%22%2C%22expiryDate%22%3A%222027-04-20T15%3A22%3A01.594Z%22%7D; ttcsid_CNK74OBC77U1PP7E4UR0=1776698469655::Dx4-y1o7C09OQSl4Ly8w.1.1776698521680.1; ttcsid=1776698469658::Z-NBH8s49qDTwBY9PS3R.1.1776698521681.0::1.50787.52023::0.0.0.0::0.0.0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'
}
all_opinions0 = []

while next:
    url = f'https://www.ceneo.pl/{product_code}/opinie-{page}'
    print(url)

    response = requests.get(url, headers= headers)
    if response.status_code == 200:


        page_dom = BeautifulSoup(response.text, 'html.parser')

        if page == 1:
            product_name = page_dom.select_one("h1.product-top__product-info__name").get_text()
            print(product_name)


        opinions = page_dom.select("div.js_product-review:not(.user-post--highlight)")


        all_opinions = page_dom.find_all('div', class_='js_product-review')
        opinions = [r for r in all_opinions if 'user-post--highlight' not in r.get('class', [])]


        for opinion in opinions:
            single_opinion = {
                'opinion_id': opinion['data-entry-id'],
                'author': opinion.select_one('span.user-post__author-name').get_text().strip(),
                'recommendation': opinion.select_one('span.user-post__author-recomendation > em').get_text().strip() if opinion.select_one('span.user-post__author-recomendation > em') else None,
                'score': opinion.select_one('span.user-post__score-count').get_text().strip(),
                'content': opinion.select_one('div.user-post__text').get_text().strip(),
                'pros': [p.get_text() for p in opinion.select('div.review-feature__item--positive')],
                'cons': [c.get_text() for c in opinion.select('div.review-feature__item--negative')],
                'like': opinion.select_one('span[id^="votes-yes"]').get_text().strip() if opinion.select_one('span[id^="votes-yes"]') else None,
                'dislike': opinion.select_one('button.vote-no > span').get_text().strip() if opinion.select_one('button.vote-no > span') else None,
                'publishing_date': opinion.select_one('span.user-post__published > time:nth-child(1)')['datetime'] if opinion.select_one('span.user-post__published > time:nth-child(1)')['datetime'] else None,
                'purchase_date': opinion.select_one('span.user-post__published > time:nth-child(2)')['datetime'].strip() if opinion.select_one('span.user-post__published > time:nth-child(2)[datetime]') else None
            }
            all_opinions0.append(single_opinion)


        next = True if page_dom.select_one('button.pagination__next') else False
        if next: page +=1


if not os.path.exists("./opinions"):
    os.mkdir("./opinions")


with open(f"./opinions/{product_code}.json", "w", encoding="UTF-8") as jf:
    json.dump(all_opinions0, jf, indent=4,ensure_ascii=False)