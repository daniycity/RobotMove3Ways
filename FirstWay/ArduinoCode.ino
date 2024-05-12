#include <Servo.h>

int pinLB=12;		//define pin 12
int pinLF=3;		//define pin 3
int pinRB=13;		//define pin 13
int pinRF=11;		//define pin 11
String val;	//temp variables
Servo myservo;		//set myservo

void setup(){
	Serial.begin(9600);			//define motor output pin
	pinMode(pinLB,OUTPUT);		//pin 12
	pinMode(pinLF,OUTPUT);		//pin 3 (PWM)
	pinMode(pinRB,OUTPUT);		//pin 13
	pinMode(pinRF,OUTPUT);		//pin 11 (PWM)
	myservo.attach(9);		//define servo motor output pin to D9 (PWM)
}

void forward(){
	digitalWrite(pinLB,LOW);
	digitalWrite(pinRB,LOW);
	analogWrite(pinLF,255);
	analogWrite(pinRF,255);
}

void fermo(){
	digitalWrite(pinLB,HIGH);
	digitalWrite(pinRB,HIGH);
	analogWrite(pinLF,0);
	analogWrite(pinRF,0);
}

void right(){
	digitalWrite(pinLB,HIGH);		//wheel on the left moves forward
	digitalWrite(pinRB,LOW);		//wheel on the right moves backward
	analogWrite(pinLF,255);
	analogWrite(pinRF,255);
}

void left(){
	digitalWrite(pinLB,LOW);		//wheel on the left moves backward
	digitalWrite(pinRB,HIGH);		//wheel on the right moves forward
	analogWrite(pinLF,255);
	analogWrite(pinRF,255);
}

void back(){
	digitalWrite(pinLB,HIGH);
	digitalWrite(pinRB,HIGH);
	analogWrite(pinLF,255);
	analogWrite(pinRF,255);
}

void loop(){
	//I read the variable from the bluetooth serializable port
	val=Serial.readString();
	if(val=="forward")forward();
	if(val=="back")back();
	if(val=="left")left();
	if(val=="right")right();
	if(val=="stop")stop();
}
