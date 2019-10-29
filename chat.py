import tkinter as tk
from  tkinter import ttk
from  tkinter import scrolledtext
import socket 
from threading import Thread
from tkinter import messagebox
##################################

def crypt(m,k) : 
	a1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
	'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


	a2=[]

	key = int(k)
	for i in range(len(a1)) :
		a2.append(a1[i])

	for i in range(key) :
		a2.append(a2[0])
		a2.remove(a2[0])

	inp = m

	out = '' 

	for n in inp :
		for i in range(len(a1)) :
			if n == a1[i] :
				out += a2[i]
				break
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
 

	return out_final



def s() : 
	textbox1.insert(tk.INSERT,uservar.get() +':'+ textbox.get('1.0','end-1c') + '\n')

def send() : 
	message = str(uservar.get() +':'+ textbox.get('1.0','end-1c') + '\n')
	messagebytes = message.encode('UTF-8')
	soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	soc.sendto(messagebytes,(ipvar.get(),int(l_portvar.get())))

def listen() :
	while True	:
		hostname = socket.gethostname()    
		IPAddr = socket.gethostbyname(hostname)    
		soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		soc.bind((IPAddr,int(l_portvar.get())))
		print(IPAddr)
		result = soc.recv(1024)
		resultdec = str(result.decode('UTF-8'))
		msbox = messagebox.askyesno('Do,you want to crypt message?')
		if msbox == True :
			key = keyvar.get()
			resultdec = crypt(resultdec,key)
			textbox1.insert(tk.INSERT,resultdec + '\n')
		else :
			textbox1.insert(tk.INSERT,resultdec + '\n')

w = tk.Tk()
w.title('Chat')
w.geometry('340x200')

note = ttk.Notebook(w)
tab1 = ttk.Frame(note) 
tab2 = ttk.Frame(note)		
tab3 = ttk.Frame(note) 

note.add(tab1,text='Input')
note.add(tab2,text='Output')
note.add(tab3,text='Settings')

note.pack(expand=1,fill='both')

uservar = tk.StringVar()
userinput = tk.Entry(tab1,textvariable=uservar)
userinput.grid(column=0,row=0)
userinput.insert(tk.INSERT,'Nick')

label = tk.Label(tab1,text='Message input')
label.grid(column=0,row=1)

textbox = scrolledtext.ScrolledText(tab1,height=5,width=40)
textbox.grid(column=0,row=2)

button = tk.Button(tab1,text='Send message',command=send)
button.grid(column=0,row=3)

label1 = tk.Label(tab2,text='Message output')
label1.grid(column=0)

textbox1 = scrolledtext.ScrolledText(tab2,height=5,width=40)
textbox1.grid(column=0,row=1)

###Settings

ipvar =	tk.StringVar()
portvar = tk.StringVar()

l_portvar = tk.StringVar()
l_portvar.set('11111')

keyvar = tk.StringVar()
keyvar.set('0')

labelip = tk.Label(tab3,text='Client IP input')
labelip.grid(column=0,row=0)

ipinput = tk.Entry(tab3,textvariable=ipvar)
ipinput.grid(column=0,row=1)

labelport = tk.Label(tab3,text='Client Port input')
labelport.grid(column=0,row=2)

portinput = tk.Entry(tab3,textvariable=portvar)
portinput.grid(column=0,row=3)

keylabel = tk.Label(tab3,text='Key')
keylabel.grid(column=1,row=0)


keyinput = tk.Entry(tab3,textvariable=keyvar)
keyinput.grid(column=1,row=1)

l_labelip = tk.Label(tab3,text='Server Port input')
l_labelip.grid(column=1,row=2)

l_portinput = tk.Entry(tab3,textvariable=l_portvar)
l_portinput.grid(column=1,row=3)


###Thread
thread_ = Thread(target=listen)
thread_.start()


w.mainloop()
