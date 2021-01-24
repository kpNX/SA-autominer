import pyautogui
import time

#img must be .png
#conf must be >=1
def recherche(img, conf) :
	location = pyautogui.locateCenterOnScreen(img, confidence=conf)
	return location

def pause(img,conf) :
	pos = recherche(img,conf)
	if pos == None :
		pos = recherche(img,conf)
	return pos

def minage() :
	error = 0
	#click on the red button mine tritium
	minetritium = pause("minetritium.png",0.7)
	pyautogui.moveTo(minetritium)
	pyautogui.click()
	#wait for the new window to open
	miner = pause("miner.png",0.9)
	#write the number of ship you send
	pyautogui.moveTo(miner)
	pyautogui.click()
	pyautogui.write(Mperfleet)
	#next
	suivant = recherche("next.png",0.8)
	pyautogui.moveTo(suivant)
	pyautogui.click()
	#Mine
	mine = pause("mine.png",0.8)
	pyautogui.moveTo(mine)
	pyautogui.click()

#verification for the right window
def verificationRightwindow() :
	Flybutton = recherche("Flybutton.png", 0.9)
	Planetbutton = recherche("Planetbutton.png", 0.9)
	pyautogui.moveTo(Flybutton)
	pyautogui.click()
	pyautogui.moveTo(Planetbutton)
	pyautogui.click()
	time.sleep(0.25)
	Gas_Giant = pause("Gas_Giant.png",0.8)
	pyautogui.moveTo(Gas_Giant)
	pyautogui.click()
	posx, posy = Gas_Giant
	return posx, posy

#descendre 
def descendre(posx, posy, p, r)	:
	

	p = p + 1
	if (p % 2) == 0 :
		r = r + 1
	else :
		r = r
	pyautogui.moveTo(posx, posy + r)
	pyautogui.click()
	pyautogui.scroll(-23)
	time.sleep(0.7)
	pyautogui.click()
	return p, r

###################################################################################

#mode 1 = basic mining function work whitout preferences 
def mode1(Mfleet,Mperfleet) :
	i = 0
	#verification for the right window

	posx, posy = verificationRightwindow()

	while i != Mfleet :
		Gas_Giant_Vert = recherche("Gas_Giant_Vert.png",0.83)
		time.sleep(0.4)
		queue = recherche("queue.png",0.8)
		colonise = recherche("colonise.png",0.5)
		sendfleet = recherche("sendfleet.png",0.8)
		if Gas_Giant_Vert == None :
			print("No gas giant found !")
			break
		elif colonise != None :
			pass
		elif sendfleet != None :
			pass
		elif queue == None  :
			minage()
			i = i + 1
		else :
			pass
		descendre(posx, posy, 0, 0)

#advanced mining work exclusively whit preference
def mode2(Mfleet,Mperfleet) :
	x = 0
	p = 0
	r = 0
	

	def check(left,top,width,height, f) :
		nom = "GSsave"
		number = 1
		png = ".png"
		

		while number <= f :
			number = str(number)
			try :
				re = pyautogui.locateOnScreen(nom+number+png,region=(left,top, width+50, height), confidence = 0.99)
			except :
				re = None

			if re != None :
				re = 1
				return re
				break
			else :
				number = int(number)
				number = number + 1
				
	f = open("option.txt", "r")
	f = f.read()
	f = int(f)
	print(f)				
	posx, posy = verificationRightwindow()
	time.sleep(1)
	left,top,width,height = pyautogui.locateOnScreen("hashtag.png", confidence=0.75)

	while x != Mfleet :
		p, r = descendre(posx, posy,p ,r)
		re = check(left,top,width,height,f)
		if re == 1 :
			queue = recherche("queue.png", 0.8)
			if queue == None :
				minage()
				x = x + 1
				print(x,'Fleet sent')

			else :
				pass

#used to put gas giant of a system to use for advanced mining
def mode3() :
	print("_________________________")
	print("/!\ ctrl + c to shut /!\\")
	print("This mode is used to save \ngas giant of interest")
	print("How to : \n1 : Select a gas giant on the galaxy page\n2 : Enter Y on the cmd tab")
	print("_________________________")
	screen = 0
	name = "GSsave"
	png = ".png"
	r = 0
	p = 0
	arret = 0
	while True :
		try :
			bal = str(input("Save (Y) :"))
			if bal == "Y" or "y" :
				screen = screen + 1
				screen = str(screen)
				left,top,width,height = pyautogui.locateOnScreen("hashtag.png", confidence=0.75)
				print(left,top,width,height)
				im = pyautogui.screenshot(region=(left,top, width+50, height))
				im.save(name+screen+png)
				screen = int(screen)
				f = open("option.txt", "w+")
				
				
		except :
			screen = str(screen)
			f.write(screen)
			f.close()
			break

###################################################################################

choice = input("1. Basic mining\n2. Advanced mining\n3. Save Gas Giant\n")
print(choice)

if choice == "1" :
	Mfleet = int(input("Number of mining fleet : "))
	Mperfleet = str(input("Number of miner per fleet : "))
	mode1(Mfleet,Mperfleet)
if choice == "2" :
	Mfleet = int(input("Number of mining fleet : "))
	Mperfleet = str(input("Number of miner per fleet : "))
	mode2(Mfleet,Mperfleet)
if choice == "3" :
	mode3()