import cv2
import numpy as np
# Initialize the webcam
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# Set the frame width and height
cap.set(3, 640)
cap.set(4, 480)

# Loop until the 'q' key is pressed
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Draw a crosswire on the frame
    cv2.line(frame, (0, 26), (640, 24), (0, 0, 255), 2)
    cv2.line(frame, (0, 196), (640, 198), (0, 0, 255), 2)
    cv2.line(frame, (0, 444), (640, 449), (0, 0, 255), 2)

    cv2.line(frame, (90, 89), (24, 332), (0, 0, 255), 2)
    cv2.line(frame, (557, 88), (610, 335), (0, 0, 255), 2)

    # Display the frame
    cv2.imshow('Crosswire', frame)
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
#cap.release()

# Close all windows
cv2.destroyAllWindows()
