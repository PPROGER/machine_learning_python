import cv2

def Cam_registration():

    # Включаем первую камеру
    cap = cv2.VideoCapture(0)
  
    # "Прогреваем" камеру, чтобы снимок не был тёмным
    for i in range(5):
        cap.read()

    # Делаем снимок
    ret, frame = cap.read()

  
    # Записываем в файл
    cv2.imwrite('face_id/cam.png', frame)
  
    # Отключаем камеру
    cap.release()

