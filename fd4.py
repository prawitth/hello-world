#It's work

import cv2

def detect(path):
    img = cv2.imread(path)
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.CASCADE_SCALE_IMAGE, (20,20))

    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    return rects, img

def box(rects, img):
    i=1
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
        i=i+1
    cv2.imwrite('P4121408_detected.jpg', img);

rects, img = detect("P4121408.jpg")
box(rects, img)
