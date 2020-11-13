from random import *

size=200
times=50
rev=[]
def setRules(rules):
	rules[(0,0,0)]=randint(0,1)
	rules[(0,0,1)]=randint(0,1)
	rules[(0,1,0)]=randint(0,1)
	rules[(0,1,1)]=randint(0,1)
	rules[(1,0,0)]=randint(0,1)
	rules[(1,0,1)]=randint(0,1)
	rules[(1,1,0)]=randint(0,1)
	rules[(1,1,1)]=0

def fillList(l):
	for i in range(size):
		l.append(randint(0,1))
	return l

def checkRules(l,rules):
	child = []
	for i in range(size): 
		res = 0
		try:
			res += rules[(l[i-1],l[i],l[i+1])]
		except:
			pass
		try :
			res += rules[(l[i-2],l[i-1],l[i])]
		except:
			pass
		try:
			res += rules[(l[i],l[i+1],l[i+2])]
		except:
			pass
		if res:	
			child.append(1)
		else:
			child.append(0)
	return child

def display(l):
	s = ""
	for i in l:
		if i :
			s+="#"
		else:
			s+=" "
	rev.append(s)
	print(s)

def revDisplay():
	rev.reverse()
	for i in rev:
		print(i)

def main():
	l=[]
	rules={}
	setRules(rules)
	l=fillList(l)
	for k,v in rules.items():
		print(k,v)
	display(l)
	for _ in range(times):
		l=checkRules(l,rules)
		display(l)

if __name__=="__main__":
	main()