import cv2
import serial

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(0)

arduinoData = serial.Serial('/dev/ttyACM1',9600)

def servo_x_calculation(servo_x):
    if servo_x <= 90:
        arduinoData.write(b'0')
        print("0")
    elif servo_x > 90 and servo_x <= 100:
        arduinoData.write(b'1')
        print("1")
    elif servo_x > 100 and servo_x <= 105:
        arduinoData.write(b'2')
        print("2")
    elif servo_x > 105 and servo_x <= 110:
        arduinoData.write(b'3')
        print("3")
    elif servo_x > 110 and servo_x <= 115:
        arduinoData.write(b'4')
        print("4")
    elif servo_x > 115 and servo_x <= 120:
        arduinoData.write(b'5')
        print("5")
    elif servo_x > 120 and servo_x <= 125:
        arduinoData.write(b'6')
        print("6")
    elif servo_x > 125 and servo_x <= 130:
        arduinoData.write(b'7')
        print("7")
    elif servo_x > 130 and servo_x <= 135:
        arduinoData.write(b'8')
        print("8")
    elif servo_x > 135:
        arduinoData.write(b'9')
        print("9")


def servo_y_calculation(servo_y):
    if servo_y <= 20:
        arduinoData.write(b'j')
        print("J")
    elif servo_y > 20 and servo_y <= 40:
        arduinoData.write(b'i')
        print("I")
    elif servo_y > 40 and servo_y <= 60:
        arduinoData.write(b'h')
        print("H")
    elif servo_y > 60 and servo_y <= 80:
        arduinoData.write(b'g')
        print("G")
    elif servo_y > 80 and servo_y <= 100:
        arduinoData.write(b'f')
        print("F")
    elif servo_y > 100 and servo_y <= 120:
        arduinoData.write(b'e')
        print("E")
    elif servo_y > 120 and servo_y <= 140:
        arduinoData.write(b'd')
        print("D")
    elif servo_y > 140 and servo_y <= 160:
        arduinoData.write(b'c')
        print("C")
    elif servo_y > 160 and servo_y <= 180:
        arduinoData.write(b'b')
        print("B")
    elif servo_y > 180:
        arduinoData.write(b'a')
        print("A")


def servo_eyes(x,y):
    cent_x = x
    cent_y = y
#    print("Angle values = ",cent_x,cent_y)

    servo_x = (cent_x*180)/580
    print("SERVO X =",servo_x)
    servo_x_calculation(servo_x)

    servo_y = (cent_y*180)/420
    print("SERVO Y =",servo_y)
    servo_y_calculation(servo_y)



while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 8)

    temp_x = []
    temp_y = []

    #print(type(faces))
    if len(faces) == 0:
        print("No Faces in FRAME")
    else:
        print("Faces = ",faces)
        for i in range(0,len(faces)):
               #print("Face ",i,"sum_X + w/2 = ",faces[i][0]+int((faces[i][2])/2))
               #print("Face ",i,"sum_Y + h/2 = ",faces[i][1]+int((faces[i][3])/2))
               temp_x.append(faces[i][0]+int((faces[i][2])/2))
               temp_y.append(faces[i][1]+int((faces[i][3])/2))


        s_y = max(temp_y)
        index = temp_y.index(max(temp_y))
        s_x = temp_x[index]
#        print("SCREEN = ",s_x,s_y)
        servo_eyes(s_x,s_y)


    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]


    cv2.imshow('Face Detect InMoov',img)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
