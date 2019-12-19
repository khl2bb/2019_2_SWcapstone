#define trigPin 13                   // trigPin을 13으로 설정합니다.
#define echoPin 12   

#include <SoftwareSerial.h>

SoftwareSerial hc06(2,3);

void setup() {
   pinMode(trigPin, OUTPUT);   // trigPin 핀을 출력핀으로 설정합니다.
   pinMode(echoPin, INPUT);    // echoPin 핀을 입력핀으로 설정합니다.
   Serial.begin(9600);
   hc06.begin(9600);
   
}

void loop() {
  
  long duration, distance, check;                   // 각 변수를 선언합니다.
  digitalWrite(trigPin, LOW);                 // trigPin에 LOW를 출력하고
  delayMicroseconds(2);                    // 2 마이크로초가 지나면
  digitalWrite(trigPin, HIGH);                // trigPin에 HIGH를 출력합니다.
  delayMicroseconds(10);                  // trigPin을 10마이크로초 동안 기다렸다가
  digitalWrite(trigPin, LOW);                // trigPin에 LOW를 출력합니다.
  duration = pulseIn(echoPin, HIGH);

  distance = duration * 17 / 1000;
  
   if (distance >= 200 || distance <= 0)       // 거리가 200cm가 넘거나 0보다 작으면
  {
    //Serial.print(distance);
    Serial.println("거리를 측정할 수 없음");   // 에러를 출력합니다.\
  }
  
  }  else{
    Serial.println(distance);                         // distance를 시리얼 모니터에 출력합니다.
    //Serial.println(" cm");  // cm를 출력하고 줄을 넘깁니다.     // distance가 10이면 10 cm로 출력됩니다.
  }
  
  if(hc06.available()){
    Serial.write(hc06.read());
  }

  if(Serial.available()){
   
   if(0 < distance <= 50)
   hc06.write(Serial.read());
   Serial.println
    delay(500);
  
  }

  delay(500); 
 //98:D3:32:30:DF:F7
 //sudo rfcomm bind rfcomm0 98:D3:32:30:DF:F7
 }
