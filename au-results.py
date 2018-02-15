from colorama import init, Fore, Back, Style
from termcolor import colored
import requests
import bs4

print("")
regno = input("Enter Your Register Number: ")
req = requests.get('http://aucoe.annauniv.edu/cgi-bin/result/cgrade.pl?regno='+regno)
soup = bs4.BeautifulSoup(req.text, 'lxml')
font = soup.select('font')
strong=soup.select('strong')
init()

if ((req.status_code == 200) and (not strong[0].getText())) or (req.status_code!=200):
	print("")
	print(colored('Oops! Invalid Register Number','red'))
else:
	print("")
	print(Style.BRIGHT + font[0].getText(),end="")
	print(font[1].getText(),end="")
	print(font[2].getText())
	print(" ")
	print(Style.BRIGHT + "Register Number: "+strong[0].getText())
	print("Name           : "+strong[1].getText())
	print("Department     : "+strong[2].getText())
	print(colored("Subject Code       Grade       Result",'green'))
	print(Style.BRIGHT + strong[6].getText()+'%16s'%strong[7].getText()+'%16s'%strong[8].getText(), end="")
	print(strong[9].getText()+'%16s'%strong[10].getText()+'%16s'%strong[11].getText(), end="")
	print(strong[12].getText()+'%16s'%strong[13].getText()+'%16s'%strong[14].getText(), end="")
	print(strong[15].getText()+'%16s'%strong[16].getText()+'%16s'%strong[17].getText(), end="")
	print(strong[18].getText()+'%16s'%strong[19].getText()+'%16s'%strong[20].getText(), end="")
	print(strong[21].getText()+'%16s'%strong[22].getText()+'%16s'%strong[23].getText(), end="")
	print(strong[24].getText()+'%16s'%strong[25].getText()+'%16s'%strong[26].getText(), end="")
	print(strong[27].getText()+'%16s'%strong[28].getText()+'%16s'%strong[29].getText(), end="")
print("")	

print(Style.BRIGHT+colored('>>>>>>>>>>>>>>>>>>>>> Made with ♫ by Kishore Kumar <<<<<<<<<<<<<<<<<<<<<', 'red', 'on_white'))	