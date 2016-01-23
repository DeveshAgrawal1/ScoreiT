from BeautifulSoup import BeautifulSoup
import requests

def getscore():
    url='http://www.cricbuzz.com/cricket-match/live-scores'
    response=requests.get(url)
    source=response.text.encode('ascii','ignore')
    soup=BeautifulSoup(source)
    for score in soup.findAll('div',{'class':'list-group-item-text pad-0 margin0 cb-match-state'}):
        count,i,j=0,0,0
        x=score.find('a')
        print x.get('title')
        y=x.findAll('div')
        z=y[0].findAll('span')
        p= str(y[0].text)
        r=str(z[2].text)
        q=str(z[0].text)
        while  i!=len(q)-1 or j!=len(r)-1 :
            if i!=len(q)-1 and p[i]==q[i]:
                i+=1
            if p[count]==r[j] and j!=len(r)-1:
                j+=1
            count+=1
        print q, p[i+1:count-len(r)+1].replace('&nbsp;&#8226;&nbsp;',' '),r,p[count+1:],str(y[1].text)
        print "\n"
        
getscore()
