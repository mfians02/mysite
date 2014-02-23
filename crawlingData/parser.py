import urllib2
import string
from bs4 import BeautifulSoup
from crawlingData.models import * 

xth = 1
isLatest = True
url = 'http://www.betman.co.kr/gameSchedule.so?method=basic&gameId=G101&gameRound='

html = urllib2.urlopen(url+str(xth+140000)) 
gameData = BeautifulSoup(html).find(id='tblSort').find('tbody').find_all('tr')

a = Xth(number=xth)
a.save()

def remove_escape_sequence(a):
    keyList = a.keys()
    for i in keyList:
        a[i] = a[i].replace('\n','')
        a[i] = a[i].replace('\t','')
        a[i] = a[i].replace('\r','')
        a[i] = a[i].replace(' ','')
    return a

for i in range(0,len(gameData)):
    gameInfo = {
        'num' : '',
        'league' : '',
        'date' : '',
        'home' : '',
        'away' : '',
        'win' : '',
        'draw' : '',
        'lose' : ''
    }
    gameInfo['num'] = gameData[i].find(class_='num').get_text()
    gameInfo['league'] = gameData[i].find(class_='league').get_text()
    gameInfo['date'] = gameData[i].find(class_='date').get_text()
    gameInfo['home'] = gameData[i].find(class_='home').get_text()
    gameInfo['away'] = gameData[i].find(class_='away').get_text()
    gameInfo['win'] = gameData[i].find(class_='win').get_text()
    gameInfo['draw'] = gameData[i].find(class_='same').get_text()
    gameInfo['lose'] = gameData[i].find(class_='lose').get_text()
    gameInfo = remove_escape_sequence(gameInfo)
    b = Game(gameNumber=gameInfo['num'],league=gameInfo['league'])
    c = Odd(serviceProvider='sportstoto',winP=gameInfo['win'],drawP=gameInfo['draw'],loseP=gameInfo['lose'])
    b.save()
    c.save()