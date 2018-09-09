import cv2

cap = cv2.VideoCapture(0)

while(True):
    # จับภาพแบบ frame ต่อ frame
    ret, frame = cap.read()

    # กำหนดค่าสีจาก frame เป็น cv2.COLOR_BGR2GRAY สีแบบเทา
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # แสดงผลของ frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # แสดงภาพจากกล้อง
cap.release()
cv2.destroyAllWindows()