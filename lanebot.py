import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open Webcam.")
    exit()

window_name = "LaneBot - Original vs. Canny Edges"
cv2.namedWindow(window_name)

cv2.createTrackbar("Lower Threshold", window_name, 45, 300, nothing)
cv2.createTrackbar("Upper Threshold", window_name, 200, 300, nothing)
# nothing(x) is a placeholder function that does nothing. It is required by createTrackbar() but we don't need to perform any action when the trackbar value changes.

print("Webcam opened successfully. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    # cap.read() returns a tuple (ret, frame) where ret is True if the frame was read correctly, and frame is the image itself.

    if not ret:
        print("Error: Could not read frame.")
        break

    t1 = cv2.getTrackbarPos("Lower Threshold", window_name)
    t2 = cv2.getTrackbarPos("Upper Threshold", window_name)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.cvtColor() converts the frame from BGR color space to grayscale.
    # we need to store the result in a variable (gray) to use it later.

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # 5, 5 is the kernel size for the Gaussian blur. A larger kernel size results in more blurring.

    edges = cv2.Canny(blurred, t1, t2)
    # cv2.Canny() detects edges in the blurred image. The two threshold values (45 and 100) determine how strong an edge must be to be detected.

    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    #edges.bgr converts the edges image back to BGR color space for display purposes.

    combined = np.hstack((frame, edges_bgr))
    # np.hstack() horizontally stacks the original frame and the edges image side by side for comparison.

    cv2.imshow("LaneBot - Original vs. Canny Edges", combined)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # 0xFF is a bitwise AND operation that ensures compatibility across different platforms. ord('q') returns the ASCII value of 'q'.
        break

cap.release()
cv2.destroyAllWindows()