#importing modules
import numpy as np
from PIL import ImageGrab
import cv2

fourcc = cv2.VideoWriter_fourcc(*"XVID") #the file encoding

size = (ImageGrab.grab()).size #Getting screen resolution

#output format = (output_name,encoding,fps,screen_size)
output = cv2.VideoWriter("output.mp4",fourcc,25.0,size) 
#saving/stacking the screenshots using loops 
while True:
	img = np.array(ImageGrab.grab())
	frame = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#converts the frame from bgr to rgb
	#bgr is default color scheme

	#cv2.imshow("screen", frame)-->can be used to show the screen
	output.write(frame)	#outputting the frame
	if cv2.waitKey(1) == 27: #27 is esc key..or stop the program to stop recording
		break
output.release()
cv2.destroyAllWindows() 

