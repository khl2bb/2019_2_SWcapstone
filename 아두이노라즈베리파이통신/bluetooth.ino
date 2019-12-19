#include <SoftwareSerial.h>


SoftwareSerial softwareSerial(2, 3); // RX, TX



void setup() {


 softwareSerial.begin(9600);

 pinMode(LED_BUILTIN, OUTPUT);

}


void loop() {


 if (softwareSerial.available() > 0 ) {



   char command = softwareSerial.read();

   int ledStatus = digitalRead(LED_BUILTIN);


   switch (command){


     case '1':

     

       if (ledStatus == LOW){

         digitalWrite(LED_BUILTIN, HIGH);

         softwareSerial.println("LED가 켜졌습니다.\n");

       }

       else{

         softwareSerial.println("이미 LED가 켜져있습니다.\n");

       }

       break;


     case '2':

     

       if (ledStatus == HIGH){

         digitalWrite(LED_BUILTIN, LOW);

         softwareSerial.println("LED가 꺼졌습니다.\n");

       }

       else{

         softwareSerial.println("이미 LED가 꺼져있습니다.\n");

       }

       break;


     case 'S':

     case 's':

         

       if (ledStatus == LOW){

         softwareSerial.println("LED 상태: 꺼짐\n");

       }

       else {

         softwareSerial.println("LED 상태: 켜짐\n");

       }

       break;

     

   }      

 }

}
