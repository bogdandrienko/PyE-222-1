import cv2


def work_with_image():
    source_image = cv2.imread('data/test.png')
    cv2.imshow("source_image", source_image)
    height, width, _ = source_image.shape

    multi = 150
    h_multi = multi
    w_multi = int((width / height) * multi)

    # word = [[255,
    #         0,
    #         0,
    #         100]],  # many dimesional
    # word1 = word[2:4, 2:4]
    cropped_image = source_image[
                    0 + h_multi:height - h_multi,  # height
                    0 + w_multi:width - w_multi  # width
                    ]

    cv2.imshow("cropped", cropped_image)
    cv2.imwrite("data/cropped.jpg", cropped_image)

    gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray_image", gray_image)
    cv2.imwrite("data/gray_image.jpg", gray_image)

    # (thresh, im_bw) = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    thresh = 90
    black_and_white_image = cv2.threshold(gray_image, thresh, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow("black_and_white_image", black_and_white_image)
    cv2.imwrite("data/black_and_white_image.jpg", black_and_white_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def work_with_video():
    cap = cv2.VideoCapture('data/example.mp4')
    while cap.isOpened():
        ret, source_image = cap.read()
        if ret:
            height, width, _ = source_image.shape

            multi = 300
            h_multi = multi
            w_multi = int((width / height) * multi)
            cropped_image = source_image[
                            0 + h_multi:height - h_multi,  # height
                            0 + w_multi:width - w_multi  # width
                            ]

            # face_cascade = cv2.CascadeClassifier("image_or_video_scanner/static/cascadeHaare.xml")
            #
            # gray = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)
            # faces = face_cascade.detectMultiScale(
            #     gray,
            #     scaleFactor=1.3,
            #     minNeighbors=5,
            #     minSize=(20, 20),
            #     flags=cv2.CASCADE_SCALE_IMAGE
            # )
            # for (x, y, w, h) in faces:
            #     cv2.rectangle(source_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow('detect', cropped_image)

            gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
            cv2.imshow("gray_image", gray_image)

            thresh = 120
            black_and_white_image = cv2.threshold(gray_image, thresh, 255, cv2.THRESH_BINARY)[1]
            # print(len(black_and_white_image[0]))
            w, b = 0, 0
            for i in black_and_white_image:
                all_count = len(i)
                count_white = len(list(filter(lambda x: x == 255, i)))

                # print(f"{all_count} {count_white}")

                if count_white > (all_count // 2):
                    # print("w")
                    w += 1
                else:
                    # print("b")
                    b += 1

            if w > b:
                print(f"БЕЛЫЙ")
            else:
                print("ЧЁРНЫЙ")

            # white = []
            # for i in black_and_white_image[0]:
            #     if i == 255:
            #         white.append(i)
            # print(len(white))
            #
            # white = list(filter(lambda x: x == 255, black_and_white_image[0]))
            # print(len(white))

            print(type(black_and_white_image[0]))
            cv2.imshow("black_and_white_image", black_and_white_image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # work_with_image()
    work_with_video()
    pass
