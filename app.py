import cv2
import mediapipe as mp
from mediapipe.python.solutions import drawing_utils
import pyautogui

index_y = 0
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
screen_width, screen_height = pyautogui.size()
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    f_height, f_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * f_width)
                y = int(landmark.y * f_height)
                print(x, y)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = screen_width / f_width * x
                    index_y = screen_height / f_height * y
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    t_x = screen_width / f_width * x
                    t_y = screen_height / f_height * y
                    if abs(index_y - t_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
