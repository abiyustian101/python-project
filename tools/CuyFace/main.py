import cv2

face_ref = cv2.CascadeClassifier("face_ref.xml")
camera = cv2.VideoCapture(0)

def face_recognition(frame):
    optimal_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected = face_ref.detectMultiScale(optimal_frame, scaleFactor=1.2,minSize=(500,500), minNeighbors=5)
    return detected

def drawer_box(frames):
    for x,y,w,h in face_recognition(frames):
        cv2.rectangle(frames, (x, y), (x + w, y + h), (255, 0, 0), 5)

def close():
    camera.release()
    cv2.destroyAllWindows()
    exit()

def main():
    while True:
        _, buka_kamera = camera.read()
        drawer_box(buka_kamera)
        cv2.imshow("CuyFace AI", buka_kamera)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            close()

if __name__ == "__main__":
    main()

