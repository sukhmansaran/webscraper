from bs4 import BeautifulSoup
import requests

a = input("enter url: ")
r = requests.get(a)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,"html.parser")
d = dict()

# to update dictionary
def update_dict(name,txt):
        if name not in d:
            s = set()
            s.add(txt)
            d[name] = s
        else:
            v = d[name]
            v.add(txt)


# to find title
def title():
    if soup.find('title'):
        t = soup.find('title')
        t_name = t.name
        t_txt = t.get_text()
        update_dict(t_name,t_txt)
    else:
        d.update({'title': 'not found'})

title()


# to find meta description
def meta_des():
    if soup.find('meta', attrs={'name':'description'}):
        m = soup.find_all('meta', attrs={'name': 'description'})
        for i in m:
            m_name = 'meta_description'
            m_txt = i['content']
            update_dict(m_name,m_txt)
    else:
        d.update({'meta_description': 'not found'})

meta_des()


# to find meta keyword
def meta_key():
    if soup.find('meta', attrs={'name':'keywords'}):
        m = soup.find_all('meta', attrs={'name': 'keywords'})
        for i in m:
            m_name = 'meta_keywords'
            m_txt = i['content']
            update_dict(m_name,m_txt)
    else:
        d.update({'meta_keywords': 'not found'})

meta_key()


# to find all images
def img():
    if soup.find('img'):
        img = soup.find_all('img')
        for i in img:
            i_txt = i.get('alt')
            update_dict('image',i_txt)
    else:
        d.update({'image':'not found'})

img()


# to find headers
def headers():
    h = ['h1','h2','h3','h4','h5','h6']
    for i in h:
        if soup.find(i):
            j = soup.find_all(i)
            for x in j:
                h_name = i
                h_txt = x.get_text()
                update_dict(h_name, h_txt)
        else:
            d.update({i:'not found'})

headers()


def body():
    if soup.find('meta', attrs={'name': 'keywords'}):
        m_key = soup.find('meta', attrs={'name': 'keywords'})
        m_txt = m_key['content']
        body = soup.find('body')
        b_txt = body.get_text()
        if m_txt in b_txt:
            update_dict('body','keywords found in body')
        else:
            update_dict('body','keywords not found in body')

body()


# to print dictionary
def print_d():
    for x,y in d.items():
        print(x,':',y)

print_d()

