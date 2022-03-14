import bs4
import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        R = requests.get(url, timeout=30)
        R.raise_for_status()  # 若不是200，则表示异常
        R.encoding = R.apparent_encoding
        return R.text
    except:
        return "产生异常"


def main():
    url = "https://news.sina.com.cn/w/2022-03-04/doc-imcwiwss4155836.shtml?qq-pf-to=pcqq.c2c"
    txt = get_html(url)

    html = BeautifulSoup(txt, "html.parser")
    new_title = html.select('.second-title')[0].text
    new = []
    for i in html.select('.article p')[:-1]:
        new.append(i.text.strip())

    f = open('new_text.txt', 'w', encoding='utf-8')
    f.write('        ' + new_title + '\n')
    for i in new:
        f.write('        ' + i + '\n')


if __name__ == '__main__':
    main()
