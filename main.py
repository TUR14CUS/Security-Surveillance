import glob
import cv2
import time
from emailing import send_email
import os
from threading import Thread

video = cv2.VideoCapture(0) # 0 is the default camera on your computer
time.sleep(1)  # This will make the video run slower

first_frame = None
status_list = []
count = 1

def clean_folder():
    images = glob.glob('images/*.jpg')
    for image in images:
        os.remove(image)

while True:
    status = 0
    check, frame = video.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau
        continue

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    cv2.imshow('Delta Frame', delta_frame)

    _, thresh_frame = cv2.threshold(delta_frame, 70, 255, cv2.THRESH_BINARY)
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow('Dilated Frame', dil_frame)

    contours, _ = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.jpg", frame)
            count += 1
            all_images = glob.glob('images/*.jpg')
            index = int(len(all_images) / 2)
            image_with_object = all_images[index]

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 1:
        email_thread = Thread(target=send_email, args=(image_with_object,))
        email_thread.daemon = True
        email_thread.start()

    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1)

    if key == ord('q'): # Press 'q' to quit
        break

video.release()
clean_folder()
