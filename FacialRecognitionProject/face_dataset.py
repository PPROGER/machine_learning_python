import cv2
import os

def Face_datasets(cam,width,height,face_id,puty_s,count_foto):
    cam = cv2.VideoCapture(int(cam))
    cam.set(3, int(width)) # set video width
    cam.set(4, int(height)) # set video height

    face_detector = cv2.CascadeClassifier('/home/pproger/Desktop/machine_learning_python/FacialRecognitionProject/Cascades/haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
#face_id = input('\n enter user id end press  ==>  ')

    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
    count = 0

    while(True):
        ret, img = cam.read()
        img = cv2.flip(img, 1) # flip video image vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite(puty_s+"User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30: # Take 30 face sample and stop video
            break

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()