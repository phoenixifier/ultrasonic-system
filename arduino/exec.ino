// defines pins numbers
const int trigPin = 9;
const int echoPin = 10;
const int buzzer = 8;
const int green = 6;
const int yellow = 5;
const int red = 4;
 
// defines variables
long duration;
int distance;
int safetyDistance;
int sound;

int deviceState = 1;
 
void setup() {
pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
pinMode(buzzer, OUTPUT);
pinMode(green, OUTPUT);
pinMode(yellow, OUTPUT);
pinMode(red, OUTPUT);
Serial.begin(9600); // Starts the serial communication
}
 
void loop() {

if(Serial.available() > 0) {
 int command = Serial.read();
 Serial.println(command);
 if(command == 49) {
   deviceState = 1;
 } else if(command == 50) {
   deviceState = 2;
 }
}


if(deviceState == 2) {
// Clears the trigPin
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
 
// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
 
// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);
 
// Calculating the distance
distance= duration*0.034/2;

safetyDistance = distance;
  if (distance <= 10) {
    sound = 1000;
    tone(buzzer, sound);
  } 
  else if (distance <= 25) {
    sound = 500;
    tone(buzzer, sound);
  }
  else if (distance <= 50) {
    sound = 100;
    tone(buzzer, sound);
  }
  else {
    noTone(buzzer);
  }
if (distance <=50)
{
  digitalWrite(green, HIGH);
}
else
{
  digitalWrite(green, LOW);
}
if (distance <=25)
{
  digitalWrite(yellow, HIGH);
}
else
{
  digitalWrite(yellow, LOW);
}
if (distance <=10)
{
  digitalWrite(red, HIGH);
}
else
{
  digitalWrite(red, LOW);
}
 
// Prints the distance on the Serial Monitor
 //Serial.print("Distance: ");
 //Serial.println(distance);
 }
}
