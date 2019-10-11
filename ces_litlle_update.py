a1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


a2=[]

key = int(input('Key>> '))
for i in range(len(a1)) :
	a2.append(a1[i])

for i in range(key) :
	a2.append(a2[0])
	a2.remove(a2[0])

inp = input("Write the text>> ")

out = '' 

for n in inp :
	for i in range(len(a1)) :
		if n == a1[i] :
			out += a2[i]
	else : 
		out += n

out_sp = out.split(' ')
out_sp1 = []
out_sp2 = []
for integer in out_sp : 
	try :
		integer = int(integer)
		integer += key
		out_sp1.append(integer)
	except :
		out_sp1.append(integer)


for n in out_sp1 : 
	l = str(n)
	out_sp2.append(l)

out_final = ' '.join(out_sp2)
 

print(out_final)
