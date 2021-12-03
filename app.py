import cv2
import sqlite3

connection = sqlite3.connect('attendance.db')
c = connection.cursor()


# ------------------------------ DB Functions ----------------------------------------
def create_attendancetable():
    c.execute('CREATE TABLE IF NOT EXISTS attendancetable (studentID TEXT)')
    connection.commit()


def mark_student(studentID):
    c.execute('INSERT INTO attendancetable (studentID ) VALUES (?)', (studentID))
    connection.commit()


def view_all_users():
    c.execute('SELECT * FROM attendancetable')
    result = c.fetchall()
    return result


# -------------------------------------------------------------------------------------

def QRCode_Reader():
    # read the QRCODE image
    img = cv2.imread("QRCodeImage/studentcode.jpg")

    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()

    # detect and decode
    data, myqrcode, straight_qrcode = detector.detectAndDecode(img)

    # if there is a QR code
    if myqrcode is not None:
        print("Attendance marked for the student ID: {}".format(data))

        mark_student(str(data))
        Attendance()


def Image_capture():
    while True:
        # Activate Camera/webcam
        camera = cv2.VideoCapture(0)

        ret, frame = camera.read()
        cv2.imshow('Attendance system', frame)
        key = cv2.waitKey(1)
        if key == ord('s'):
            cv2.imwrite(filename='QRCodeImage/studentcode.jpg', img=frame)
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
      
      E-View Attendance list
      
    ----------------------------------------
    """)
    key = input("Select your course: ")

    if key == "A":
        print("Place your ID Card for Maths attendance")
        Image_capture()

    elif key == "B":
        print("Place your ID Card for English attendance")
        Image_capture()
    elif key == "C":
        print("Place your ID Card for Computer Science attendance")
        Image_capture()
    elif key == "D":
        print("Place your ID Card for Lab attendance")
        Image_capture()

    elif key == "E":
        print("Attendance list")
        student_result = view_all_users()
        print(student_result)


if __name__ == '__main__':
    Attendance()
