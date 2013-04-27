#coding:utf-8
import urllib2
import BeautifulSoup
import sys
import re
word = sys.argv[1]
check = re.compile(r'^[a-z]*$')
try:
    a = urllib2.urlopen("http://www.iciba.com/"+word)
    soup = BeautifulSoup.BeautifulSoup(a.read())
    result = soup.find("div",{'class':'group_pos'}).findAll("label")
    for i in result:
        if check.match(word) is not  None:
            print i.string
        else:
            print i.a.string
except:
    print "could not find"
