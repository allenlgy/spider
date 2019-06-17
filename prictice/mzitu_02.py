import requests
import os
import time
import threading
from bs4 import BeautifulSoup
# 下载界面的函数，利用requests就可以实现
def download_page(url):
    '''
    用于下载页面
    :param url:
    :return:
    '''

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)
    r.encoding = 'gb2312'
    return r.text

# 获取图一所有套图列表，函数 link 表示套图的链接，text 表示套图的名字
def get_pic_list(html):
    '''
    获取每个页面的套图列表，之后循环用gei_pic函数获取图片
    :param html:
    :return:
    '''
    soup = BeautifulSoup(html,'html.parser')
    pic_list = soup.find_all('li',class_='wp-item')
    for i in pic_list:
        a_tag = i.find('h3',class_='tit').find('a')
        link = a_tag.get('href')  # 套图链接
        text = a_tag.get_text()  #套图名字
        get_pic(link,text)

    # 传入上一步获取到的套图链接及套图名字，获取魅族套图里面的图片并保存
    def get_pic(link,text):
        '''
        获取当前页面的图片，保存
        :param link:
        :param text:
        :return:
        '''

        html = download_page(link)  #下载界面
        soup = BeautifulSoup(html,'html.parser')
        pic_list = soup.find('div',id='picture'.find_all('img'))  # 找到界面所有图片
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Geck0/20100101 Firefox/61.0"}
        create_dir('pic/{}'.format(text))
        for i in pic_list:
            pic_link = i.get('src')  # 拿到图片的具体 url
            r= requests.get(pic_link,headers=headers)  # 下载图片，之后保存图片
            with open('pic/{}/{}'.format(text,link.split('/')[-1]),'wb') as f:
                f.write(r.content)
                time.sleep(1)  # 休息一下，避免被封


        def create_dir(name):
            if not os.path.exests(name):
                os.makedirs(name)

        def execute(url):
            page_html = download_page(url)
            get_pic_list(page_html)

        def main():
            create_dir('pic')
            queue = [i for i in range(1, 20)]  # 构造 url 链接页码
            threads = []
            while len(queue) > 0:
                for thread in threads:
                    if not thread.is_alive():
                        threads.remove(thread)
                while len(threads) < 5 and len(queue) >0:  # 最大线程设置5
                    cur_page = queue.pop(0)
                    url = 'http://mzitu.com/a/more_{}.html'.format(cur_page)
                    thread = threading.Thread(target=execute,args=(url,))
                    thread.setDaemon(True)
                    thread.start()
                    print('{}正在下载{}页'.format(threading.current_thread().name, cur_page))
                    threads.append(thread)

                if __name__== '__main__':
                    main()