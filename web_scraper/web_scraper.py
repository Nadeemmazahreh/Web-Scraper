import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    url_page = requests.get(url)
    soup = BeautifulSoup(url_page.content, 'html.parser')
    result = soup.findAll('a',title='Wikipedia:Citation needed')
    return len(result)

def get_citations_needed_report(url):
    url_page = requests.get(url)
    soup = BeautifulSoup(url_page.content, 'html.parser')
    pTags = soup.findAll('p')
    ptagsCitations=[]
    for p in pTags:
        citations = p.findAll('a',title='Wikipedia:Citation needed')
        if len(citations)>0:
              for i in citations:
                txt=''
                for i in range(len(p.text.strip())) :
                    if p.text.strip()[i]=='[':
                        break
                    else:
                        txt+=p.text.strip()[i]
                if not txt in  ptagsCitations:
                   ptagsCitations.append(txt)
                else: 
                    txt=''
                    for d in range(len(p.text.strip())) :
                      if p.text.strip()[d]==']':
                        for z in range(d+1,len(p.text.strip())) :
                            if p.text.strip()[z]=='[':
                              break
                            else:
                                txt+=p.text.strip()[z]
                        break
                    ptagsCitations.append(txt)
                                 

    return "\n".join(ptagsCitations)


if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))