#coding=UTF-8
from bs4 import BeautifulSoup
import re
 
with open(r'./r.html', 'r', encoding='utf-8') as f:
    text = f.read()
    # print(text)
    soup = BeautifulSoup(text, 'lxml')
    text_n = str(soup.find_all('pre')[0].text).replace('#', '').replace('\n', '')
    l = []
    for t in text_n:
        l.append(t)
    print(','.join(l).replace(',', ''))