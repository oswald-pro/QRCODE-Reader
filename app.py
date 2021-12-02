import cv2

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

courses = ["Math", "English", "Computer Science", "Lab"]



def QRCode_Reader():
    # read the QRCODE image
    img = cv2.imread("studentcode.jpg")

    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()

    # detect and decode
    data, bbox, straight_qrcode = detector.detectAndDecode(img)

    # if there is a QR code
    if bbox is not None:
        print(f"QRCode data:\n{data}")
        Attendance()


def Image_capture():

    while True:
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()

        cv2.imshow('Attendance system', frame)

        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite(filename='studentcode.jpg', img=frame)
            camera.release()
            print("Image in process")
            # read the QRCODE image
            QRCode_Reader()



def Attendance():
    print("""
    ----------------------------------------
          welcome to attendance system
          
      A-Maths                     B-English
      C-Computer Science          D-Lab
    ----------------------------------------
    """)
    key = input("Select your course: ")

    if key == "A":
        print("Place your ID Card for Maths attendance")
        Image_capture()


    elif key == "B":
        print("Place your ID Card for English attendance")
        QRCode_Reader()
    elif key == "C":
        print("Place your ID Card for Computer Science attendance")
        QRCode_Reader()
    elif key == "D":
        print("Place your ID Card for Lab attendance")
        QRCode_Reader()


if __name__ == '__main__':
    Attendance()
