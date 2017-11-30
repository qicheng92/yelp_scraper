#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 17:33:50 2017

@author: Cheng Qi
"""
from bs4 import BeautifulSoup
import re
import time
import requests

def run(url):
    for i in range(5): # try 5 times
        try:
            response=requests.get(url,headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36', })
            html=response.content 
            break
        except Exception as e:
            print ('failed attempt',i)
            time.sleep(2) 		
		
    soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 
    reviews=soup.findAll('div', {'class':re.compile('review_table_row')}) # get all the reviews
    return reviews
    
    
def getCritic(rul):
    lst1 = [] 
    for review in run(rul):
        critic='NA'# initialize critic and text 
        criticChunk=review.find('a',{'href':re.compile('/critic/')})
        if criticChunk: 
            critic=criticChunk.text#.encode('ascii','ignore')
        lst1.append(critic)
    return lst1
  
def getRating(url):
    lst2 = []
    for review in run(url):
        rate='NA' # initialize critic and text
        allrate=review.find('div',{'class':re.compile('review_icon icon')})
        Tap = allrate.attrs# get a dictionary about its tag,such as {'class': ['review_icon', 'icon', 'small', 'fresh']}
        if Tap:
            val = Tap['class']
            rate = val[3]
        lst2.append(rate)
    return lst2

def getSource(url):
    lst3 = []   
    for review in run(url):
        source='NA' # initialize critic and text 
        allsource=review.find('a',{'href':re.compile('/source-')})
        if allsource:
            source=allsource.text#.encode('ascii','ignore')
        lst3.append(source)
    return lst3

def getDate(url):
    lst4 = []      
    for review in run(url):
        date='NA' 
        alldate=review.find('div',{'class':'review_date subtle small'})
        if alldate: 
            date=alldate.text#.encode('ascii','ignore')
        lst4.append(date)
    return lst4

def getTextLen(url):
    lst5 = []
    for review in run(url):
        lenth='NA' 
        content = review.find('div',{'class':'the_review'})
        if content: 
            lenth = len(content.text)#.encode('ascii','ignore')         
        lst5.append(lenth)
    return lst5

if __name__=='__main__':
    url='https://www.rottentomatoes.com/m/space_jam/reviews/'
    print('Critic: ',getCritic(url),'\n')
    print('Rating: ',getRating(url),'\n')
    print('Source: ',getSource(url),'\n')
    print('Date: ',getDate(url),'\n')
    print('TextLen: ',getTextLen(url))
