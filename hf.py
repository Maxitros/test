a1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',\
'А', 'а' , 'Б', 'б', 'В', 'в', 'Г' ,'г', 'Д', 'д','Е', 'е', 'Ё', 'ё', 'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й',\
'й', 'К', 'к','Л', 'л','М', 'м', 'Н', 'н', 'О', 'о', 'П', 'п', 'Р',\
'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц',\
'Ч', 'ч', 'Ш', 'ш', 'Щ', 'щ', 'Ъ', 'ъ', 'Ы', 'ы', 'Ь', 'ь', 'Э', 'э', 'Ю', 'ю', 'Я', 'я','і', 'ї',"є",'э']

def f1(stroka) :
	out = ""
	for n in stroka :
		for i in range(len(a1)) :	
			if n == a1[i] :
				out += a1[i]
	out1  = out.split(" ")
	out2 = "" .join(out1)
	out3 = len(out2)
	print(out3)
def f2(stroka) : 
	output = []
	for n in stroka : 
		if n not in output : 
			output.append(n)
	return output
		
t = ''
while t != "exit" :
	print('1.Output letters /n 2.Delete dublicate')
	t = input("What?>>" )
	inp = input("Text>> ")
	if t == "1" :
		f1(inp)
	elif t == '2' :
		inp  = ' '.join(f2(inp.split()))
		print(inp)
		