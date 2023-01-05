import cv2
import sys

# Create haar cascade 
cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

# Set video source to default webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect objects based on supplied haar cascade to be stored as rectangles in faces
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle-like shape (only corners) around the faces
    i = 0   # Will represent number of faces detected
    for (x, y, w, h) in faces:
        line_length = 10    # length of line from corners of rectangle

        cv2.line(frame, (x, y), (x , y + line_length), (0, 255, 0), 2)  # Top left
        cv2.line(frame, (x, y), (x + line_length , y), (0, 255, 0), 2)

        cv2.line(frame, (x+w, y), (x+w , y + line_length), (0, 255, 0), 2)  # Bottom left
        cv2.line(frame, (x+w, y), (x+w - line_length , y), (0, 255, 0), 2)

        cv2.line(frame, (x, y+h), (x + line_length, y+h), (0, 255, 0), 2)  # Top right
        cv2.line(frame, (x, y+h), (x, y+h - line_length), (0, 255, 0), 2)

        cv2.line(frame, (x+w, y+h), (x+w , y+h - line_length), (0, 255, 0), 2)  # Bottom right
        cv2.line(frame, (x+w, y+h), (x+w - line_length , y+h), (0, 255, 0), 2)

        i = i + 1   # Increment number of detected faces

    # Display number of faces in top left of frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Faces detected: ' + str(i),(10,50), font, 1,(255,255,255),2,cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break while loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()