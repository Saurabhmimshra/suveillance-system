from datetime import datetime
import cv2, time
import pandas
import boto3

s3 = boto3.client('s3')

#import way2sms
#q=way2sms.sms('9891496927',"cracktheaiims")

first_frame = None
status_list = [None,None]
time_list = []
df = pandas.DataFrame(columns = ["Start", "End"])
#face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)
current_frame = 0

while True:
    check,frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)
    if first_frame is None:
        first_frame = gray
        continue
    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 35, 255,
    cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
    (_,cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
    	if cv2.contourArea(contour)<500:
    		continue
        
    name = str(current_frame) + '.jpg'
    
    cv2.imwrite(name, frame)
        
    fileName = name
        
    bucket= 'amanmausam'
    
    s3.upload_file(fileName, bucket, fileName)
        
    #client= boto3.client('rekognition','us-east-1')
    
    #response = client.detect_labels(Image={'S3Object': {'Bucket':bucket,'Name':fileName}},MinConfidence=75)
    #lis = []
    #for label in response['Labels']:
    	#	lis.append(label['Name'])
    #lis = set(lis)
    
    #flag_lis = set(['Human', 'Person', 'People'])
    #if len(flag_lis.intersection(lis))!=0:
    	#	q.send('7042548961','Alert!!...Some object has entered the territory.')
    	#	n=q.msgSentToday()
            
    current_frame += 1
    status = 1

    status_list.append(status)
    if status_list[-1]==1 and status_list[-2]==0:
        time_list.append(datetime.now())
        #q.send('7042548961','Alert!!...Some object has entered the territory.')
        #n=q.msgSentToday()
    if status_list[-1]==0 and status_list[-2]==1:
        time_list.append(datetime.now())
        #q.send('7042548961','Object has left the territory.')
        #n=q.msgSentToday()
    #faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1,
    #minNeighbors = 10)
    #for X,Y,W,H in faces:
    #    frame = cv2.rectangle(frame, (X,Y), (X+W, Y+H), (0,255,0), 3)
    #cv2.imshow("Gray", gray)
    #cv2.imshow("Delta", delta_frame)
    #cv2.imshow("Threshold", thresh_frame)
    cv2.imshow("Color Frame", frame)
    key = cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
    #if key == 1048689:
        if status==1:
            time_list.append(datetime.now())
        break
    time.sleep(5)
q.logout()
for i in range(0, len(time_list), 2):
    df = df.append({"Start": time_list[i], "End": time_list[i+1]},
    ignore_index = True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()
