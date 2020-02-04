import cv2

def Cam():

    # Включаем первую камеру
    cap = cv2.VideoCapture(0)
  
    # "Прогреваем" камеру, чтобы снимок не был тёмным
    for i in range(30):
        cap.read()

    # Делаем снимок
    ret, frame = cap.read()

  
    # Записываем в файл
    cv2.imwrite('face_id/cam1.png', frame)
  
    # Отключаем камеру
    cap.release()

