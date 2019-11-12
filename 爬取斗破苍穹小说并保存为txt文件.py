import requests
from bs4 import BeautifulSoup
import os
import re

# newlis = []

def getHtml(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    r = r.text
    soup = BeautifulSoup(r, 'lxml')
    return soup


def main(url):
    soup = getHtml(url)
    lis = soup.find('ul').find_all('li')
    #     print（lis）
    path = os.getcwd() + u'/斗破苍穹文章保存/'  # 在源文件同个目录下新建
    if not os.path.isdir(path):
        os.mkdir(path)

    # 问题：爬取所有的小说，但是没能控制在五个
    #     for i in range(5):
    #         newlis.append(lis[i])
    #         print(newlis)

    for i in lis[:5]:
        newurl = i.find('a')['href'].replace('/doupocangqiong', 'http://www.doupoxs.com/doupocangqiong')
        result = getHtml(newurl)  # 每篇文章
        title = result.find('div', {'class': 'entry-tit'}).find('h1').get_text()

        filename = path + title + '.txt'
        print(filename)

        new = open(filename, 'w')
        new.write('<<' + title + '>>\n\n')
        # content = result.find('div', {'class': 'm-post'}).find('p').get_text()
        # content = re.findall(r'<p>(.*?)</p>',result.text,re.S)
        # for i in content:
        #     new.write(i + '\n')
        content = result.select("div[class='m-post'] p").join(content)
        # 问题：多个p标签文本不能全部爬取，有空值，去空值也不对
        #       换成select写法保存为列表不是字符串，不会转换写不进txt
        new.write(content)
        new.close()


if __name__ == '__main__':
    firsturl = 'http://www.doupoxs.com/doupocangqiong'
    main(firsturl)
