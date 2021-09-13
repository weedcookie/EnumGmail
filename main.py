






### a gmail enumerator 

## target server { https://mail.google.com/mail/gxlu?email=<target_mail> 

import requests 
from clint.textui import puts , colored , indent 
import argparse 
import names 
import concurrent.futures 
from random_username.generate import generate_username
from user_agent import generate_user_agent

lst = [] 
tmp = []

def mail_gen2(n):
	''' A function to generate mails  '''
	
	lst = [ item+"@gmail.com" for item in generate_username(n) ]

	return lst 


def check_mail(mail): 
	''' A function to check if email is valid  ''' 
	## if the server return cookies then the email is valid else it is not 


	#try:
	payload = {"User-Agent":generate_user_agent()}

	resp = requests.get(f"https://mail.google.com/mail/gxlu?email={mail}", headers=payload )
	
	if resp.cookies:
			
		puts(colored.green(f" [ {mail} ] is valid"))
		lst.append(mail)

		return True

	else:
			
		puts(colored.red(f" [ {mail} ] is not valid"))
			#print ("Didn't find cookies ")
		return False

	#except :
	#	print (f"Failed to check {mail} ")
	#	return False



def mail_gen():
	''' a function to generate emails  '''
	full_name = names.get_full_name()
	first , last = full_name.split()

	
	tmp = [ first+str(i)+"@gmail.com" for i in range (0 , 1000) ]

	return tmp







def load_emails(file_name):
	with open(file_name, 'r') as handler:
		return list(handler)

def create_output(lst):
	''' writes found emails to a txt file'''
	with open('output.txt' , 'a') as f:
		for item in lst:
			f.write(item+"\n")


if __name__ == "__main__":
	

#  -s single email check 
#  -m multi email check  using a txt file as an input 
#  -g generate emails and check them without user interference
#  -t  threaded  takes a number as an input 


	parser = argparse.ArgumentParser()
	parser.add_argument("-s",  help="single email check ")
	parser.add_argument("-m", help="multiple email check")

	parser.add_argument("-g", help="generate and check without user interference")

	parser.add_argument("-g2", help="generate and check without user interference")

	parser.add_argument("-t", help="threaded ")


	args = parser.parse_args()

	if args.s :
		check_mail(args.s)



	if args.m: 
		file_name = args.m
		try:

			with open(args.m , 'r') as handler:
				for item in handler:
					check_mail(item)
		except FileNotFoundError as no_file:
			print (f"{args.m} not found !!!")


	if args.g:
		
		tmp = mail_gen()
		if not args.t:

			
			print (f" Total generated mails : {len(tmp)} ")
			for item in tmp:
				check_mail(item)
		else:
			with concurrent.futures.ThreadPoolExecutor(max_workers=int(args.t)) as executor:
				results = {executor.submit(check_mail , item ): item for item in tmp }
				for future in concurrent.futures.as_completed(results):
					out = results[future]

	if args.g2:
		tmp = mail_gen2(int(args.g2))
		if not args.t:

			
			
			print (f" Total generated mails : {len(tmp)} ")
			for item in tmp:
				check_mail(item)
		else:
			with concurrent.futures.ThreadPoolExecutor(max_workers=int(args.t)) as executor:
				resutls = {executor.submit(check_mail , item ): item for item in tmp}
				for future in concurrent.futures.as_completed(resutls):
					out = resutls[future]




	print (f"Found {len(lst)} valid emails out of {len(tmp)}")


	create_output(lst)

















