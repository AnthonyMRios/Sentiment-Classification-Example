import sys
import os
import pickle
import BeautifulSoup

def extractsms(htmlsms) :
    msgitems = []
    tree = BeautifulSoup.BeautifulSoup(htmlsms)
    conversations = tree.findAll("div", attrs={"class" : "message"})
    for conversation in conversations:
        bDate = conversation.find("abbr", attrs={"class" : "dt"})
        date = bDate['title']
        bSender = conversation.find(attrs={"class" : "fn"})
        sender = bSender.text
        bMessage = conversation.find("q")
        message= bMessage.text
        msgitems.append({"datetime": date, "sender": sender, "message": message})
    return msgitems

if __name__ == '__main__':
    allTexts = []
    cnt = 0
    for i in os.listdir('./gabbyTexts'):
        with open('./gabbyTexts/'+i, 'r') as iFile:
            allTexts += extractsms(iFile.read())
        if cnt == 10:
            break
    print len(allTexts)
    pickle.dump(allTexts, open('allTexts.pkl','wb'), pickle.HIGHEST_PROTOCOL)
