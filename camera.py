import cv2,time,random,os
import numpy as np
print('Starting CAMERA')
video= cv2.VideoCapture(0)
os.system('cls')
def start():
	video= cv2.VideoCapture(0)
	print('\t\t\t\t\tHI THERE, I aM YOUR CAMERA')
	print('\t\t\t\t\t---------------------------')
	print()
	print(" WHAT Can I Do For You : " , end='')
	print()
	while True :
		print('1. Click a Picture')
		print('2. Start Face Detection')
		print('3. Start Pedestian Detection')
		print('4. To Exit')
		print()
		print(' Enter Your Choice : ' , end='')
		choice = input()
		if int(choice) == 1 :
			def click():
				print('Say Cheese...')
				time.sleep(2)
				status , photo = video.read()
				cv2.imshow('Your Photo',photo)
				cv2.waitKey()
				cv2.destroyAllWindows()
				print('1.Want To Save')
				print('2.Click Again')
				print('3.Go Back')
				choice = input()
				if int(choice)==1:
					cv2.imwrite('1.jpg',photo)
					print('Photo Saved At ' , end='')
					print(os.getcwd())
					input('Enter to Continue...')
					os.system('cls')
				elif int(choice)==2 :
					os.system('cls')
					click()
				else :
					os.system('cls')
					start()
			click()
		elif int(choice)==2:
				face_model = cv2.CascadeClassifier('HaarCascade\haarcascade_frontalface_default.xml')
				print('PRESS ENTER TO STOP THE CAMERA')
				time.sleep(2)
				while True:
					status , photo = video.read()
					grey = cv2.cvtColor(photo , cv2.COLOR_BGR2GRAY)
					face_corr = face_model.detectMultiScale(grey)
					if len(face_corr) == 0:
						pass
					else:
						for (x,y,w,h) in face_corr:
							cv2.rectangle(photo, (x,y), (x+w,y+h), (127,0,255), 3)
							cv2.imshow("Live" , photo)
						if cv2.waitKey(10)==13:
								break
				cv2.destroyAllWindows()
				video.release()
				input('Enter to Go Back...')
				os.system('cls')
				start()
		elif int(choice)==3 :
			body_detect = cv2.CascadeClassifier('HaarCascade\haarcascade_fullbody.xml')
			print('PRESS ENTER TO STOP THE CAMERA')
			time.sleep(2)
			while True:
				status , photo = video.read()
				grey = cv2.cvtColor(photo , cv2.COLOR_BGR2GRAY)
				body_corr = body_detect.detectMultiScale(grey)
				if len(body_corr) == 0:
					pass
				else:
					for (x,y,w,h) in body_corr:
						cv2.rectangle(photo, (x,y), (x+w,y+h), (127,0,255), 3)
						cv2.imshow("Live" , photo)
					if cv2.waitKey(10)==13:
							break
			cv2.destroyAllWindows()
			video.release()
			input('Enter to Go Back...')
			os.system('cls')
			start()
		elif int(choice)==4 :
			exit()


		else:
			print('Enter Valid No')
			print()
			input('Enter To GoBack...')
			os.system('cls')





start()
