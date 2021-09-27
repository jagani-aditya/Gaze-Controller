# Gaze Controller

## Project Desciption 

<p align="center">
  <img src="/Media/InMoov_Video.gif" alt="animated" />
</p>

When there is an interaction between a robot and a person, gaze control is very important for face-to-face communication. However, when a robot interacts with several people, neurorobotics plays an important role to determine the person to look at and those to pay attention to among the others. There are several factors which can influence the decision: who is speaking, who he/she is speaking to, where people are looking, if the user wants to attract attention, etc. This project implements an algorithm to detect, recognize people in frame, and pays attention to people who are speaking to enhance human-robot interaction. 


## Platform
* Python 3
* Ubuntu 16.04 LTS

## Libraries
* face_recognition
* dlib
* numpy
* imutils
* serial

## Implementation

### Command-Line Interface

When you install `face_recognition`, you get two simple command-line 
programs:

* `face_recognition` - Recognize faces in a photograph or folder full for 
   photographs.
* `face_detection` - Find faces in a photograph or folder full for photographs.

#### `face_recognition` command line tool

The `face_recognition` command lets you recognize faces in a photograph or 
folder full  for photographs.

First, you need to provide a folder with one picture of each person you
already know. There should be one image file for each person with the
files named according to who is in the picture:

![known](https://cloud.githubusercontent.com/assets/896692/23582466/8324810e-00df-11e7-82cf-41515eba704d.png)

Next, you need a second folder with the files you want to identify:

![unknown](https://cloud.githubusercontent.com/assets/896692/23582465/81f422f8-00df-11e7-8b0d-75364f641f58.png)

Then in you simply run the command `face_recognition`, passing in
the folder of known people and the folder (or single image) with unknown
people and it tells you who is in each image:

```bash
$ face_recognition ./pictures_of_people_i_know/ ./unknown_pictures/

/unknown_pictures/unknown.jpg,Barack Obama
/face_recognition_test/unknown_pictures/unknown.jpg,unknown_person
```


##### Speeding up Face Recognition

Face recognition can be done in parallel if you have a computer with
multiple CPU cores. For example, if your system has 4 CPU cores, you can
process about 4 times as many images in the same amount of time by using
all your CPU cores in parallel.

If you are using Python 3.4 or newer, pass in a `--cpus <number_of_cpu_cores_to_use>` parameter:

```bash
$ face_recognition --cpus 4 ./pictures_of_people_i_know/ ./unknown_pictures/
```

You can also pass in `--cpus -1` to use all CPU cores in your system.

#### Python Module

You can import the `face_recognition` module and then easily manipulate
faces with just a couple of lines of code. It's super easy!

API Docs: [https://face-recognition.readthedocs.io](https://face-recognition.readthedocs.io/en/latest/face_recognition.html).

##### Automatically find all the faces in an image

```python
import face_recognition

image = face_recognition.load_image_file("my_picture.jpg")
face_locations = face_recognition.face_locations(image)

# face_locations is now an array listing the co-ordinates of each face!
```

See [this example](https://github.com/ageitgey/face_recognition/blob/master/examples/find_faces_in_picture.py)
 to try it out.


##### Automatically locate the facial features of a person in an image

```python
import face_recognition

image = face_recognition.load_image_file("my_picture.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)

# face_landmarks_list is now an array with the locations of each facial feature in each face.
# face_landmarks_list[0]['left_eye'] would be the location and outline of the first person's left eye.
```

See [this example](https://github.com/ageitgey/face_recognition/blob/master/examples/find_facial_features_in_picture.py)
 to try it out.


#### Once you're done with installation

Run the ```face_recognition``` module by first navigating to ```examples``` directory

```$ python run_HRI.py ```
 
This should start the face_recognition module. Now we need to launch the arduino file located in ```arduino_test``` directory inside ```examples``` directory and upload the following code

```arduino_test.ino```

into your Arduino.

#### Arduino Pin Configuration

Two servos need to be attached. 

For Servo 1; attach 

```Digital Pin(Servo_1) --> Pin 10 ```
```Digital Pin(Servo_2) --> Pin 9 ```




 
