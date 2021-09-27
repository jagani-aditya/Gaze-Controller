import face_recognition
import cv2
from multiprocessing import Process, Manager, cpu_count
import time
import numpy
import dlib
from imutils import face_utils
import serial

p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

arduinoData = serial.Serial("/dev/ttyACM0",9600)
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Stats to be included are : 
# 1. Speaking Status
# 2. Name of Subjects in frame
# 3. Number of subjects in frame
# 4. Frames per second
# 5. X and Y values of servo's
# 6. Location of subject in frame 

# This is a little bit complicated (but fast) example of running face recognition on live video from your webcam.
# This example is using multiprocess.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get next worker's id
def next_id(current_id):
    if current_id == worker_num:
        return 1
    else:
        return current_id + 1


# Get previous worker's id
def prev_id(current_id):
    if current_id == 1:
        return worker_num
    else:
        return current_id - 1

def lip_area_calculation(frame):
    temp_x = []
    temp_y = []
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print('******************************************')
    rects = detector(gray,0) 
#    dets = detector(frame,1)
#    print("Faces detected = ",format(len(dets)))
     
    faces = face_cascade.detectMultiScale(gray, 1.3, 8)

    temp_x = []
    temp_y = []

    if len(faces) == 0:
        print("No_Faces:",len(faces))
    else:
        for i in range(0,len(faces)):
               #print("Face ",i,"sum_X + w/2 = ",faces[i][0]+int((faces[i][2])/2))
               #print("Face ",i,"sum_Y + h/2 = ",faces[i][1]+int((faces[i][3])/2))
               temp_x.append(faces[i][0]+int((faces[i][2])/2))
               temp_y.append(faces[i][1]+int((faces[i][3])/2))        
	s_y = min(temp_y)
        index = temp_y.index(max(temp_y))
        s_x = temp_x[index]
        servo_eyes(s_x,s_y)
	print("No_Faces:",len(faces))



    for (i,rect) in enumerate(rects):
	shape = predictor(gray,rect)
	shape = face_utils.shape_to_np(shape)
	a = shape[49]
	b = shape[59]
	c = shape[55]
	d = shape[53]
	length_1 = d[0] - a[0]
	length_2 = c[0] - b[0]
	width_1 = b[1] - a[1]
	width_2 = c[1] - d[1]
	area_out = length_1*width_1*length_2*width_2 	
	# make rectangle of inner boundary lips
	e = shape[61]
	f = shape[67]
	g = shape[65]
	h = shape[63]
	length_3 = h[0] - e[0]
	length_4 = g[0] - f[0]
	width_3 = f[1] - e[1]
	width_4 = g[1] - h[1]
	area_in = length_3*width_4*length_3*width_4
	percentage = (area_in*1000/area_out)
	stat_speaking = "Speaking"
	stat_silent = "Silent"
	if percentage > 5:
		print(stat_speaking)
	else:
		print(stat_silent)

#  EXT_LEFT                 MID                  EXT_RIGHT
#      120                  70                      20  
def servo_x_calculation(servo_x):
    if servo_x <= 40:
        arduinoData.write(b'A')
        print("0")
    elif servo_x > 40 and servo_x <= 45:
        arduinoData.write(b'B')
        print("1")
    elif servo_x > 45 and servo_x <= 50:
        arduinoData.write(b'C')
        print("2")
    elif servo_x > 50 and servo_x <= 55:
        arduinoData.write(b'D')
        print("3")
    elif servo_x > 55 and servo_x <= 60:
        arduinoData.write(b'E')
        print("4")
    elif servo_x > 60 and servo_x <= 70:
        arduinoData.write(b'F')
        print("5")
    elif servo_x > 70 and servo_x <= 80:
        arduinoData.write(b'G')
        print("6")
    elif servo_x > 80 and servo_x <= 90:
        arduinoData.write(b'H')
        print("7")
    elif servo_x > 90 and servo_x <= 100:
        arduinoData.write(b'I')
        print("8")
    elif servo_x > 100:
        arduinoData.write(b'J')
        print("9")


#  TOP                  MID                  BOTTOM
#  50                   110                     180  
def servo_y_calculation(servo_y):
    if servo_y <= 50:
        arduinoData.write(b'a')
        print("a")
    elif servo_y > 50 and servo_y <= 60:
        arduinoData.write(b'b')
        print("b")
    elif servo_y > 60 and servo_y <= 70:
        arduinoData.write(b'c')
        print("c")
    elif servo_y > 70 and servo_y <= 80:
        arduinoData.write(b'd')
        print("d")
    elif servo_y > 80 and servo_y <= 90:
        arduinoData.write(b'e')
        print("e")
    elif servo_y > 90 and servo_y <= 100:
        arduinoData.write(b'f')
        print("f")
    elif servo_y > 100 and servo_y <= 110:
        arduinoData.write(b'g')
        print("g")
    elif servo_y > 110 and servo_y <= 120:
        arduinoData.write(b'h')
        print("h")
    elif servo_y > 120 and servo_y <= 130:
        arduinoData.write(b'i')
        print("i")
    elif servo_y > 130 and servo_y <= 140:
        arduinoData.write(b'j')
        print("j")
    elif servo_y > 140 and servo_y <= 150:
        arduinoData.write(b'k')
        print("k")
    elif servo_y > 150 and servo_y <= 160:
        arduinoData.write(b'l')
        print("l")
    elif servo_y > 160 and servo_y <= 170:
        arduinoData.write(b'm')
        print("m")
    elif servo_y > 170 and servo_y <= 180:
        arduinoData.write(b'n')
        print("n")    

def servo_eyes(x,y):
    cent_x = x
    cent_y = y
    servo_x = (cent_x*180)/580
    servo_x_calculation(servo_x)

    servo_y = (cent_y*180)/420
    servo_y_calculation(servo_y)
    print('Screen X=',cent_x,'  Screen Y=',cent_y)
    print('Servo X=',servo_x,'  Servo Y=',servo_y)
             

# A subprocess use to capture frames.
def capture(read_frame_list):
    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)
    # video_capture.set(3, 640)  # Width of the frames in the video stream.
    # video_capture.set(4, 480)  # Height of the frames in the video stream.
    # video_capture.set(5, 30) # Frame rate.
    #print("Width: %d, Height: %d, FPS: %d" % (video_capture.get(3), video_capture.get(4), video_capture.get(5)))
    while not Global.is_exit:
        # If it's time to read a frame
        if Global.buff_num != next_id(Global.read_num):
            # Grab a single frame of video
            ret, frame = video_capture.read()
            read_frame_list[Global.buff_num] = frame
            Global.buff_num = next_id(Global.buff_num)
            lip_area_calculation(frame)
        else:
            time.sleep(0.01)

    # Release webcam
    video_capture.release()


# Many subprocess use to process frames.
def process(worker_id, read_frame_list, write_frame_list):
    known_face_encodings = Global.known_face_encodings
    known_face_names = Global.known_face_names
    while not Global.is_exit:

        # Wait to read
        while Global.read_num != worker_id or Global.read_num != prev_id(Global.buff_num):
            time.sleep(0.01)

        # Delay to make the video look smoother
        time.sleep(Global.frame_delay)

        # Read a single frame from frame list
        frame_process = read_frame_list[worker_id]

        # Expect next worker to read frame
        Global.read_num = next_id(Global.read_num)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_frame = frame_process[:, :, ::-1]

        # Find all the faces and face encodings in the frame of video, cost most time
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
	
        # Loop through each face in this frame of video
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance = 0.45)

            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
		print('SUBJECT NAME = ',name)
		
# EDIT**********EDIT*********EDIT
            # Draw a box around the face
            cv2.rectangle(frame_process, (left, top), (right, bottom), (0, 0, 255), 2)
#	    print(left,top,right,bottom)

            # Draw a label with a name below the face
            cv2.rectangle(frame_process, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame_process, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            
        # Wait to write
        while Global.write_num != worker_id:
            time.sleep(0.01)

        # Send frame to global
        write_frame_list[worker_id] = frame_process

        # Expect next worker to write frame
        Global.write_num = next_id(Global.write_num)


if __name__ == '__main__':

    # Global variables
    Global = Manager().Namespace()
    Global.buff_num = 1
    Global.read_num = 1
    Global.write_num = 1
    Global.frame_delay = 0
    Global.is_exit = False
    read_frame_list = Manager().dict()
    write_frame_list = Manager().dict()

    # Number of workers (subprocess use to process frames)
    worker_num = cpu_count()

    # Subprocess list
    p = []

    # Create a subprocess to capture frames
    p.append(Process(target=capture, args=(read_frame_list,)))
    p[0].start()
    
    # Load a sample picture and learn how to recognize it.
    obama_image = face_recognition.load_image_file("obama.jpg")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

    # Load a second sample picture and learn how to recognize it.
    biden_image = face_recognition.load_image_file("aditya.jpg")
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

    amit_image = face_recognition.load_image_file("amit.jpg")
    amit_face_encoding = face_recognition.face_encodings(amit_image)[0]

    # Create arrays of known face encodings and their names
    Global.known_face_encodings = [
        obama_face_encoding,
        biden_face_encoding,
	amit_face_encoding
    ]
    Global.known_face_names = [
        "Barack Obama",
        "Aditya",
	"Amit"
    ]

    # Create workers
    for worker_id in range(1, worker_num + 1):
        p.append(Process(target=process, args=(worker_id, read_frame_list, write_frame_list)))
        p[worker_id].start()

    # Start to show video
    last_num = 1
    fps_list = []
    tmp_time = time.time()
    while not Global.is_exit:
        while Global.write_num != last_num:
            last_num = int(Global.write_num)

            # Calculate fps
            delay = time.time() - tmp_time
            tmp_time = time.time()
            fps_list.append(delay)
            if len(fps_list) > 5 * worker_num:
                fps_list.pop(0)
            fps = len(fps_list) / numpy.sum(fps_list)
            print("FPS = %.2f" % fps)

            # Calculate frame delay, in order to make the video look smoother.
            # When fps is higher, should use a smaller ratio, or fps will be limited in a lower value.
            # Larger ratio can make the video look smoother, but fps will hard to become higher.
            # Smaller ratio can make fps higher, but the video looks not too smoother.
            # The ratios below are tested many times.
            if fps < 6:
                Global.frame_delay = (1 / fps) * 0.1
            elif fps < 20:
                Global.frame_delay = (1 / fps) * 0.5
            elif fps < 30:
                Global.frame_delay = (1 / fps) * 0.25
            else:
                Global.frame_delay = 0

            # Display the resulting image
            cv2.imshow('Video', write_frame_list[prev_id(Global.write_num)])

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            Global.is_exit = True
            break

        time.sleep(0.01)

    # Quit
    cv2.destroyAllWindows()
