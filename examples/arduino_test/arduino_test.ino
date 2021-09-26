#include<Servo.h>

char serialData;
int pin=13;
int servopin_x = 10;
int servopin_y = 9;

Servo myservox;
Servo myservoy;

int pos = 0;


void setup()
{
  pinMode(pin,OUTPUT);
  Serial.begin(9600);
  myservox.attach(servopin_x);
  myservoy.attach(servopin_y);
}

void loop()
{
  if(Serial.available() > 0)
  {
    serialData = Serial.read();
    //Serial.print(serialData);

    if(serialData == '0')
    {
      digitalWrite(pin,HIGH);
      myservox.write(40);
    }
    
    else if(serialData == '1')
    {
        myservox.write(45);
    }
    else if(serialData == '2')
    {
        myservox.write(50);
    }
    else if(serialData == '3')
    {
        myservox.write(60);
    }
    else if(serialData == '4')
    {
        myservox.write(70);
    }
    else if(serialData == '5')
    {
        myservox.write(80);
    }
    else if(serialData == '6')
    {
        myservox.write(90);
    }
    else if(serialData == '7')
    {
        myservox.write(95);
    }   
    else if(serialData == '8')
    {
        myservox.write(100);
    }
    else if(serialData == '9')
    {
        myservox.write(105);
    }  




    else if(serialData == 'a')
    {
      digitalWrite(pin,HIGH);
      myservoy.write(9);
    }
    
    else if(serialData == 'b')
    {
        myservoy.write(18);
    }
    else if(serialData == 'c')
    {
        myservoy.write(27);
    }
    else if(serialData == 'd')
    {
        myservoy.write(36);
    }
    else if(serialData == 'e')
    {
        myservoy.write(45);
    }
    else if(serialData == 'f')
    {
        myservoy.write(54);
    }
    else if(serialData == 'g')
    {
        myservoy.write(63);
    }
    else if(serialData == 'h')
    {
        myservoy.write(72);
    }   
    else if(serialData == 'i')
    {
        myservoy.write(81);
    }
    else if(serialData == 'j')
    {
        myservoy.write(90);
    }
      
  }
}
