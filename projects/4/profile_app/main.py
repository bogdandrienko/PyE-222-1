import os
import cv2
from flask import Flask, render_template, request, redirect, url_for

# как изображение на жёстком диске, прочитать и сохранить, и уменьшить качество и размер
# как сделать изображение серым
# как найти на изображении лицо и обрезать изображение

# как отправить файл из браузера в flask
# как принять файл в flask и сохранить на диск


app = Flask(__name__, template_folder='templates', static_url_path='/static', static_folder='static')


@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    img = ""
    if request.method == "POST":
        name = request.form.get('name', None)
        quality = int(request.form.get('quality', 50))
        avatar = request.files.get('avatar', None)
        if avatar and name.strip():
            filepath = '.\\static\\avatars'  # "./static/avatars"
            filename = f'{name}.jpg'
            img = filename
            avatar.save(os.path.join(filepath, filename))

            # todo opencv
            matrix_rbg = cv2.imread(os.path.join(filepath, filename))
            height, width, _ = matrix_rbg.shape
            gray = cv2.cvtColor(matrix_rbg, cv2.COLOR_BGR2GRAY)
            faceCascade = cv2.CascadeClassifier("./static/cascadeHaare.xml")
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            face1 = {"x": 0, "y": 0, "h": 0, "w": 0}
            for i in faces:
                face1["x"] = i[0]
                face1["y"] = i[1]
                face1["h"] = i[2]
                face1["w"] = i[3]
            multiply = int(50 * (height / 1000))
            cropped = gray[
                      0 + face1["y"] - int(multiply * 1.5):0 + face1["y"] + face1["h"] + int(multiply * 0.8),
                      0 + face1["x"] - multiply:0 + face1["x"] + face1["w"] + multiply
                      ]
            cv2.imwrite(os.path.join(filepath, "new_" + filename), cropped, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
        else:
            raise Exception("Вы не передали имя или фото!")
    return render_template("PostImagePage.html", img="new_" + img)
