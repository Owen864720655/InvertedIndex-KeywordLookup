'''
Created on Feb 20, 2015

@author: Siddartha.Reddy
'''

import re
from collections import defaultdict
from nltk import PorterStemmer
from array import array

p = PorterStemmer()

class invertedindex:

    def __init__(self):
        self.index=defaultdict(list) 

    def createindex(self):
        with open('C:/Users/Siddartha.Reddy/Desktop/testfiles/testfile.txt','r') as fd:
            for row in fd:
                demotext = row.split('$')[1]
                lineid = row.split('$')[0]
                self.getStopwords()
                terms = self.getTerms(demotext)
                
                termindex = {}
                
                for position, term in enumerate(terms):
                        try:
                            termindex[term][1].append(position)
                        except:
                            termindex[term]=[lineid, array('I',[position])]
                
                for termpage, postingpage in termindex.iteritems():
                        self.index[termpage].append(postingpage)
                    
                ##print(self.index)
        self.searchword()

    def getStopwords(self):
        f = open('C:/Users/Siddartha.Reddy/Downloads/InvertedIndex/stopwords.dat','r')
        stopwords = [line.rstrip() for line in f]
        self.sw = dict.fromkeys(stopwords)
        f.close()
    
    def getTerms(self,demotext):
        line = demotext.lower()
        line=re.sub(r'[^a-z0-9 ]',' ',line) # puts spaces instead of alpha numeric obj
        line = line.split()
        line = [x for x in line if x not in self.sw]
        # line = [p.stem(word) for word in line]
        return line

    def writeindex(self):
        f = open('indexfile','w')
        for term in self.index.iterkeys():
            postinglist=[]
            for p in self.index[term]:
                docID=p[0]
                positions=p[1]
                postinglist.append(':'.join([str(docID) ,','.join(map(str,positions))]))
            print >> f,''.join((term,'|',';'.join(postinglist)))
    
    def searchword(self):
        searchword = 'antivirus'
        for term in self.index.iterkeys():
            if term == searchword:
                for p in self.index[term]:
                    print(term,p[0],map(str,p[1]))

c = invertedindex()
c.createindex()
    
