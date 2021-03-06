import cv2
cascPath = "C:\\Users\\OMEN\\anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
# Read the image
vid = cv2.VideoCapture(0)

while(True):
    ret,image = vid.read()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
        )
    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("Faces found", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
# Destroy all the windows
cv2.destroyAllWindows()