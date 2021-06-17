import requests
from bs4 import BeautifulSoup

# su dung data tu trang bongda.com.vn
url = "http://www.bongda.com.vn/"
page = requests.get(url)
coverpage = page.content
soup = BeautifulSoup(coverpage, 'html5lib')

# tim tat ca bai bao trong muc doc nhieu nhat
articles = soup.find_all('a', class_='thumb140x90 thumbblock')
data_tit = []
data_url = []
# lay title va duong link toi bai bao
for article in articles:
    title = article.get('title')
    link = article.get('href')
    data_tit.append (title)
    data_url.append (link)
    #print ('title: {} - link: {}'.format(title, link))

url1 = data_url
cont = []
index = 0
for i in url1:
    print (i)
    r1 = requests.get(i)
    page_content = r1.content
    soup1 = BeautifulSoup (page_content, 'html5lib')
    # lay text nam trong the chu thich anh
    capt_text = soup1.find_all ('h2', class_='expEdit')
    # lay text trong the van ban
    cont_text = soup1.find ("div", class_='exp_content news_details').find_all('p')
    for j in capt_text:
        cont.append(j.get_text())
    for k in cont_text:
        cont.append(k.get_text())
    # tao file txt 
    f= open("file"+str(index)+'.txt',"w+")
    with open(r'C:\Users\Admin\Desktop\boolean\file'+str(index)+'.txt', 'w', encoding="utf-8") as writefile:
        for y in range(len(cont)):
            writefile.write(cont[y])
    index=str(int(index)+1)
    cont.clear()