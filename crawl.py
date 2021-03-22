import bs4
import pandas
import requests
import random


def random_phone_num_generator():
    first = str(random.randint(22, 99))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '0{}{}{}'.format(first, second, last)

# Crawl data from https://muaban.net/


def get_page_content(url):
    page = requests.get(url, headers={"Accept-Language": "en-US"})
    return bs4.BeautifulSoup(page.text, "html.parser")


def findAllUrlItems(url):
    soup = get_page_content(url)
    div = soup.findAll("div", {"id": "list-box"})
    res = []
    # for dothi.net but not to use
    # for ultag in div[0].findAll('ul'):
    #     for index, litag in enumerate(ultag.findAll('li')):
    #         for atag in litag.findAll('a', {"id": "ContentPlaceHolder1_ProductSearchResult1_rpProductList_hplAvatar_" + str(index)}):
    #             url = atag["href"]
    #             # f.write(litag.text)
    #             # res.append(litag.text)
    #             res.append(url)
    for divTag in div[0].findAll("div", {"class": "list-item-container"}):
        aTag = divTag.findAll("a")
        res.append(aTag[0]["href"])
    return res


def checkNone(value):
    if value == None:
        return ""
    else:
        return value.text


def getInformationFromMuaBandotNet(url):
    "detail-container__left"
    soup = get_page_content(url)
    divMain = soup.findAll("div", {"class": "detail-container__left"})
    res = ""
    title = divMain[0].find("h1", {"class": "title"}).text
    price = divMain[0].find("div", {"class": "price-container__value"})
    price = checkNone(price)
    location = divMain[0].find(
        "div", {"class": "location-clock"}).text

    user = divMain[0].find(
        "div", {"class": "user-info__fullname"})
    user = checkNone(user)

    # connect = divMain[0].find(
    #     "div", {"class": "mobile-container__value"})
    connect = random_phone_num_generator()
    # connect = checkNone(connect)
    content = divMain[0].find(
        "div", {"class": "body-container"}).text
    content_more = ""
    for item in divMain[0].findAll("div", {"class": "tech-item"}):
        content_more += item.text
    res += title + price + location + user + connect + content + content_more
    return res


def standardized(advertisements):
    # for i in range(len(res)):
    for i in range(5, 1, -1):
        downLine = "\n"*i
        advertisements = advertisements.replace(downLine, "\n")
    return advertisements


def getInformationDoThidotNet(url):
    soup = get_page_content(url)
    f = open("demofile2.txt", "a")
    div = soup.findAll("div", {"class": "product-detail"})
    res = ""
    h1 = soup.findAll("h1")[0].text
    # f.write(str(soup))
    # f.close
    divlocation = soup.find(
        "div", {"id": "ContentPlaceHolder1_ProductDetail1_divlocation"}).text
    divprice = soup.find(
        "div", {"id": "ContentPlaceHolder1_ProductDetail1_divprice"}).text
    desc = soup.findAll(
        "div", {"class": "pd-desc"})
    print(div)
    # desc_content = soup.find(
    #     "div", {"class": "pd-desc-content"}).text
    # print(soup)
    # res += h1 + divlocation + divprice + desc
    print(res)


def saveData(advertisements, name):
    f = open(name, "a")
    f.write(advertisements)
    f.close()


if __name__ == "__main__":
    domain = 'https://muaban.net/'
    count = 0
    for i in range(0, 200):
        url = 'https://muaban.net/mua-ban-nha-dat-cho-thue-toan-quoc-l0-c3?cp=' + \
            str(i)
        urls = findAllUrlItems(url)
        for url in urls:
            advertisements = getInformationFromMuaBandotNet(url)
            advertisements = standardized(advertisements)
            name = "data/advertisements_" + str(count)
            saveData(advertisements, name)
            print(count, i)
            count += 1
    # print(random_phone_num_generator())
