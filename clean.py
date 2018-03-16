

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 01:09:13 2018

@author: santh_000
"""
import json
import sys
def clean(fname):
	content=open(fname,'r').readlines()
	L={}
	
	newfile=set(content)
	for line in newfile:
			
			read = line.strip()
			a,word = read.split(" - ")
			a=a.strip()
			if ',' in a:
				b = a.split(',')
				c = b[0]
			elif '.' in a and ' ' in a:
				b = a.split(' ')
				d = a.count(' ')
				c=b[d]
			elif '.' in a:
				b = a.split('.')
				c=b[1]  
			elif ' ' in a:
				b = a.split(' ')
				d = a.count(' ')
				c=b[d]
			elif ',' not in a and '.' not in a and ' ' not in a:
				c=a
			#print(c)
			
			name=c.capitalize()
			l=[]
			class_name = word.strip()
			l = class_name.split('|')
			l=sorted(l,key=lambda x: (x.upper(), x[0].islower()))
			#print(l)
			#print(l)
			if name in L:
				L[name].append(l)
			else:
				L[name] = l
			#print(L)
			
			result = {}
			for key,value in L.items():
				leftdata = []
				for x in value:
					if(type(x)==list):
						for y in x:
							leftdata.append(y)	
							leftdata[-1] = leftdata[-1].strip()
					else:
						leftdata.append(x)
						leftdata[-1] = leftdata[-1].strip()
			
						
				result[key] = sorted(leftdata,key=lambda x: x.upper())
			for key, value in result.items():
				str2 = "|".join(str(x) for x in value)
				result[key] = str2
				
			
			json.dump(result, open('cleaned.txt', 'w'),sort_keys=True,indent=10)


if __name__ == '__main__':
    fname=sys.argv[1]
    clean(fname)
    			
    

		
    
