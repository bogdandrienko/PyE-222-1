import cv2

path = './static/avatars/'
filename = 'Regina.jpg'
quality = 50

# чтение изображения из файла в матрицу пикселей
image = cv2.imread(path + filename)

# чтение из матрицы её параметров: высота, ширина, количество каналов(rgb / rgba) !BGR=RGB
height, width, channels = image.shape

# конвертация матрицы в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# подгружаем файл .xml, которые содержит "описание" алгоритма обнаружения лиц людей
faceCascade = cv2.CascadeClassifier("./static/cascadeHaare.xml")

# "обнаруживаем" в матрице характерные черты лиц(их может быть много)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

# превращает серое "изображение" в чб
thresh, blackAndWhiteImage = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

face1 = {"x": 0, "y": 0, "h": 0, "w": 0}
for i in faces:
    face1["x"] = i[0]
    face1["y"] = i[1]
    face1["h"] = i[2]
    face1["w"] = i[3]
    print(i, type(i))  # [187 267 162 162] <class 'numpy.ndarray'>

# "рисует" вокруг найденных лиц квадраты
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
# cv2.imshow("Faces found", image)

# "выводим" оптимальные параметр "дополнительного" размера отступа от лиц (для больших фото нужно много)
multiply = int(125 * (height / 1000))  # 1000 = 100 | 2000 = 200 | 250 = 25

#
#                                y0              y1              x0             x1
cropped = image[

               0 + face1["y"] - int(multiply * 1.5):0 + face1["y"] + face1["h"] + int(multiply * 0.8),
               0 + face1["x"] - multiply:0 + face1["x"] + face1["w"] + multiply
           ]

# выводим "матрицу" в отдельное окно для показа на экране
cv2.imshow('Original image', image)
cv2.imshow('gray', gray)
cv2.imshow('blackAndWhiteImage', blackAndWhiteImage)
cv2.imshow('cropped image', cropped)

# сохраняем матрицу пикселей в файл и применяем настройки сжатия
cv2.imwrite(path + "face_" + filename, cropped, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

# добавляем "задержку", чтобы фото сразу не закрылось
cv2.waitKey(0)

# "убивает" все процессы cv2 при завершении программы
cv2.destroyAllWindows()

cv2.s