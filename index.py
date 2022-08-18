from bs4 import BeautifulSoup
import urllib.request
import requests
from selenium import webdriver
import time
import csv

# with open('groups.csv', 'w', newline='') as f_object:
#     tup1 = ("Name of Facebook Group", "Group URL", "Number of followers (nearest 1000)")
#     writer = csv.writer(f_object)
#     writer.writerow(tup1)
#     f_object.close()

def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0

with open('groups.txt') as group_file:

    # FOR EVERY LINE IN TEXT FILE
    for line in group_file:

        # GO TO PAGE AND COPY ALL HTML IN BODY TAG
        url = line
        # soup = BeautifulSoup(page, 'html.parser')

        # url = "http://www.facebook.com/groups/MidwestGenealogyResearchCommunity"
        driver = webdriver.Chrome('/Users/eliotshort/Downloads/chromedriver')
        driver.get(url)

        # # Give the javascript time to render
        time.sleep(1)

        # # Now we have the page, let BeautifulSoup do the rest!
        soup = BeautifulSoup(driver.page_source)

        nameDivs = soup.find_all("a", class_="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 hnhda86s")
        memberCountDivs = soup.find_all("a", class_="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 m9osqain lrazzd5p")
        print("HITTING THE PAGE " + url)

        if (any(nameDivs) and any(memberCountDivs)):
            first_word = memberCountDivs[0].text.split()[0]
            print(first_word + " is the first word")
            print(f'{nameDivs[0].text} HAS {value_to_float(first_word)}')

            if (nameDivs[0].text is not None and first_word is not None):
                with open('groups.csv', 'a', newline='') as f_object:
                    tup1 = (nameDivs[0].text, url, value_to_float(first_word))
                    writer = csv.writer(f_object)
                    writer.writerow(tup1)
                    f_object.close()