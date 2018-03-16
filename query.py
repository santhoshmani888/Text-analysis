# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:28:18 2018

@author: santh_000
"""

import json
import sys
fname=sys.argv[1]
data=json.load(open(fname))

def Q1():
    count=0
    d=[]
    for k,v in data.items():
        course_list=v.split('|')
        
        for a in course_list:
            if a not in d:
                d.append(a)
                count=count+1
                
    print(count)
    #print(d)
    



def Q2(name):
    if ',' in name:
        name2=name.split(',')[0]
    else:
        name2=name.split()[1]
    if name2 in data:
        course_name=data[name2]
        course_name=course_name.split('|')
        cor=','.join(sorted(course_name,key=lambda x: (x.upper(), x[0].islower())))
        print(cor)

def Q3():
    total={}
    prof=[]
    max_jaccard=0
    

    for k,v in data.items():
        course_list=v.split('|')
        total[k]=len(course_list)
    #print(total)
    for k,v in total.items():
        if(v>=5):
            prof.append(k)
    #print(prof)
    for i in range(len(prof)):
        for j in range(i+1,len(prof)):
            first=data[prof[i]]
            second=data[prof[j]]
            first=first.split('|')
            #print(first)
            second=second.split('|')
            r=set(first)
            #print(r)
            s=set(second)
            #print(s)
            common = r.intersection(s)
            #print(common)
            jaccard= float(len(common)) / (len(r) + len(s) - len(common))
            #print(prof[i],prof[j],jaccard)
            if jaccard>max_jaccard:
                        lect1=prof[i]
                        lect2=prof[j]
                        max_jaccard=jaccard
                        
    print("professor1-",lect1,"professor2-",lect2,"jaccard dist-",max_jaccard)
                        

if __name__ == '__main__':
    Q1()
    pname=sys.argv[2]
    Q2(pname)
    Q3()