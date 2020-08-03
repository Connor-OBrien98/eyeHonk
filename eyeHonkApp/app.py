import cv2
import numpy as np
import dlib
# from mouse import move_mouse
from sms import food, water, bathroom, honk
from math import hypot

cap = cv2.VideoCapture(0)
# move_mouse()
# honk()


# dlib functionality
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# midpoint formula for getting the blinking ratio
def midpoint(p1, p2):
    return int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2)


font = cv2.FONT_HERSHEY_PLAIN


def get_blinking_ratio(eye_points, facial_landmarks):
    #getting top bottom left and right parts of the eye
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
    ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)

    #finding the distance between the points
    hor_line_length = hypot((left_point[0] - right_point[0]), left_point[1] - right_point[1])
    ver_line_length = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    ratio = hor_line_length / ver_line_length
    return ratio


def get_gaze_ratio(eye_points, facial_landmarks):
    # Using shape predictor for points passed in
    left_eye_region = np.array([(facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y),
                                (facial_landmarks.part(eye_points[1]).x, facial_landmarks.part(eye_points[1]).y),
                                (facial_landmarks.part(eye_points[2]).x, facial_landmarks.part(eye_points[2]).y),
                                (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y),
                                (facial_landmarks.part(eye_points[4]).x, facial_landmarks.part(eye_points[4]).y),
                                (facial_landmarks.part(eye_points[5]).x, facial_landmarks.part(eye_points[5]).y)],
                               np.int32)
    # show whole eye lines
    # cv2.polylines(frame, [left_eye_region], True, (0, 0, 255), 2)

    #Masking the eye for calculation
    height, width, _ = frame.shape
    mask = np.zeros((height, width), np.uint8)
    cv2.polylines(mask, [left_eye_region], True, 255, 2)
    cv2.fillPoly(mask, [left_eye_region], 255)
    eye = cv2.bitwise_and(gray, gray, mask=mask)

    #Getting the minimum and max for x and y points in eye
    min_x = np.min(left_eye_region[:, 0])
    max_x = np.max(left_eye_region[:, 0])
    min_y = np.min(left_eye_region[:, 1])
    max_y = np.max(left_eye_region[:, 1])

    #creating eye threshhold shape
    gray_eye = eye[min_y: max_y, min_x: max_x]
    _, threshold_eye = cv2.threshold(gray_eye, 50, 255, cv2.THRESH_BINARY)
    height, width = threshold_eye.shape

    #mapping out the right and leftside of the focuses eye, to calculate the amount
    #of white dots in the eye to detect the gaze direction
    left_side_threshold = threshold_eye[0: height, 0: int(width / 2)]
    left_side_white = cv2.countNonZero(left_side_threshold)

    right_side_threshold = threshold_eye[0: height, int(width / 2): width]
    right_side_white = cv2.countNonZero(right_side_threshold)

    cv2.imshow("eye", eye)
    cv2.imshow("threshold eye", threshold_eye)

    #setting gaze ratio
    if left_side_white == 0:
        gaze_ratio = 0.5
    elif right_side_white == 0:
        gaze_ratio = 2.1
    else:
        gaze_ratio = left_side_white / right_side_white

    #returning gaze ratio
    return gaze_ratio

while True:
    #Setting up webcam to capture frames
    _, frame = cap.read()
    new_frame = np.zeros((500, 500, 3), np.uint8)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        # cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

        landmarks = predictor(gray, face)

        # Detect blinking
        left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

        is_blinking = blinking_ratio > 5.6

        if is_blinking:
            cv2.putText(frame, "BLINKING", (150, 150), font, 7, (255, 0, 0), 3)
            # gaze_ratio = 2.0

        # Gaze detection
        gaze_ratio_left_eye = get_gaze_ratio([36, 37, 38, 39, 40, 41], landmarks)
        gaze_ratio_right_eye = get_gaze_ratio([42, 43, 44, 45, 46, 47], landmarks)
        gaze_ratio = (gaze_ratio_left_eye + gaze_ratio_right_eye) / 2

        print(gaze_ratio)

        if gaze_ratio <= 0.7:
            cv2.putText(frame, "RIGHT", (50, 100), font, 2, (0, 0, 255), 3)
            new_frame[:] = (0, 0, 255)
            if is_blinking:
                gaze_ratio = 0.6
                # cv2.putText(frame, "RIGHT", (50, 100), font, 2, (0, 0, 255), 3)
                print('RIGHT')
                # food()
                # cap.release()
                # cv2.destroyAllWindows()
                # cv2.putText(frame, "SELECT RIGHT", (150, 150), font, 7, (255, 255, 0), 3)
        elif 0.6 < gaze_ratio < 1.9:
            cv2.putText(frame, "CENTER", (50, 100), font, 2, (0, 0, 255), 3)
            print("center")
        else:
            new_frame[:] = (255, 0, 0)
            cv2.putText(frame, "LEFT", (50, 100), font, 2, (0, 0, 255), 3)
            if is_blinking:
                gaze_ratio = 2.5
                print('LEFT')

                # cv2.putText(frame, "SELECT LEFT", (150, 150), font, 7, (255, 0, 255), 3)

    cv2.imshow("Frame", frame)
    cv2.imshow("New Frame", new_frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()