import cv2
import face_recognition

from model import User


def load_faces_in_db():
    users = User.query.all()
    face_images = []

    for user in users:
        if user.face:
            face_images.append((face_recognition.face_encodings(user.face)[0], user.username))

    return face_images


def check_person_exists_in_database():
    cap = cv2.VideoCapture(0)

    knownFace_Images = load_faces_in_db()

    x = 0
    detected_person_name = None

    while True:
        try:
            _, frame = cap.read()
            cv2.imwrite("abc.jpg", frame)
            unknownFace_Image = face_recognition.load_image_file("abc.jpg")
            unknownFace = face_recognition.face_encodings(unknownFace_Image)[0]

            for knownFace, username in knownFace_Images:
                try:
                    print("-----------------------")
                    answer = face_recognition.compare_faces([knownFace], unknownFace)
                except TypeError:
                    continue
                x += 1
                if answer[0]:
                    print("true")
                    detected_person_name = username
                    break

            if detected_person_name is not None:
                break
            elif x < 5:
                print("false")
                break

            print(answer)
            print(5)

            print('unknownFace', type(answer), answer)
        except:
            pass

    print("Detected person name:", detected_person_name)

    return detected_person_name is not None
