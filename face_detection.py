
# install opencv-python and import cv2
# OpenCV already contains many pre-trained classifiers for face, eyes, smile, etc.
import cv2

#  feel free to copy the code from the link below and paste it into a text document and save it as “face_detector.xml”
# After saving the file in your current folder, let’s load it to our program.

face_cascade = cv2.CascadeClassifier('face_detector.xml')

# Make sure there is at least one face in the image so that our program can find one
img = cv2.imread('test.png')

# the code that detects faces in an image:
faces = face_cascade.detectMultiScale(img, 1.1, 4)

# To draw rectangles around the faces detected is possible with the following code:
for (x, y, w, h) in faces:
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# we will use a method from cv2 library called “imwrite”. If you done all these steps successfully, then
# you will see “Successfully saved” in your terminal.
cv2.imwrite("face_detected.png", img)
print('Successfully saved')
