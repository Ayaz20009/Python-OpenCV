import cv2
import numpy as np

#VideoCapture(0) is the first Webcam in the system. 
cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0 ,(650,480))

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#	out.write(frame)	
	cv2.imshow('Frame',frame)
	cv2.imshow('Gray',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
#out.release()
cv2.destroyAllWindows()
