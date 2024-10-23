import cv2

# create a video capture object
imgcapture= cv2.VideoCapture(0)
result= True

while (result):
    #read the frame
    ret,  frame= imgcapture.read()
     # save the captured frame as an image
    cv2.imwrite("NewPicture.jpg", frame)
    result =False
    print ("Image captured...")

imgcapture.release()