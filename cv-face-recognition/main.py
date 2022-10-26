import cv2

def recognition():
    #  Захватываем наш видеопоток под номером 0
    capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    #  Используем обученную сеть для определения передней части лица (frontalface) 
    face_cascade = cv2.CascadeClassifier('Cascade/haarcascade_frontalface_default.xml')

    #  Запускаем бесконечный цикл, каждая итерация обновляет картинку с веб камеры
    while True:
        #  Непосредственно читаем камеру, если ret True программа увидела камеру 
        ret, img = capture.read()

        # detectMultiScale - Обнаруживает объект по нашему каскаду в объекте «img»,
        # возвращает список обнаружений, прямоугольник – координата вершины (x, y) и ширина и высота прямоугольника (w, h)
        faces = face_cascade.detectMultiScale(
            img,                # Наше изображение
            scaleFactor=1.2,    # Масштабный коэффицент, лучше использовать 1.05-1.2, больше- быстрее но меньше вероятность определения
            minNeighbors=5,     # От 3-5.8, больше число больше уверенность что это то что нам нужно
            minSize=(20, 20))   # Минимально возможный размер нашего объекта

        # Перебираем наши распознанные объекты  
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)  # Рисуем прямоугольник на нашем img, затем область где рисуем, цвет и ширина линии

        cv2.imshow('Cam Rekognition', img)  # Отображаем наш img в окне
        if cv2.waitKey(1) == ord('q'):      # Ожидаем нажатия 'q', если дождались, выходим из цикла("Ц" не сработает)
            break

    capture.release()       #  Отпускаем захват нашей WEB-камеры)
    cv2.destroyAllWindows() #  Закрываем окна


if __name__ == '__main__':
    recognition()
