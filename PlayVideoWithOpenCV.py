import cv2

videoFile = ("/Users/georgedamoulakis/Desktop/mesh 40 single 1.cine")
imagesFolder = "/Users/georgedamoulakis/Desktop/mesh40single1splits"

cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
print("the frame rate is", frameRate)

while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    print(frameId)
    if (ret != True):
        break
    if (frameId % 2 == 0):
        filename = imagesFolder + "/image_" +  str(int(frameId)) + ".jpg"
        cv2.imwrite(filename, frame)
cap.release()
print("Done!")