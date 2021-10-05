#define STEP_MT1 4      // pin STEP de A4988 a pin 4
#define DIR_MT1 5     // pin DIR de A4988 a pin 5
#define STEP_MT2 8
#define DIR_MT2 9


int entryByte;

void setup() 
{
  // initialize serial communication:
  Serial.begin(9600);

  
  pinMode(STEP_MT1, OUTPUT);  // pin 4 como salida
  pinMode(DIR_MT1, OUTPUT);   // pin 5 como salida
  pinMode(STEP_MT2, OUTPUT);  // pin 8 como salida
  pinMode(DIR_MT2, OUTPUT);   // pin 9 como salida
}

void loop() {
  if(Serial.available() >0){
    entryByte = Serial.read();

    //MOTOR 1 SUPERIOR-------------------------------------------
    //MOVER SENTIDO HORARIO
    if(entryByte == '4'){
      digitalWrite(DIR_MT1, HIGH);    // giro en un sentido
      digitalWrite(STEP_MT1, HIGH);       // nivel alto
      delay(10);  
      digitalWrite(STEP_MT1, LOW);       // nivel BAJO
      delay(10);        
    }
    //MOVER ANTIHORARIO
    if(entryByte == '5'){
      digitalWrite(DIR_MT1, LOW);    // giro en SENTIDO OPUESTO
      digitalWrite(STEP_MT1, HIGH);       // nivel alto
      delay(10);  
      digitalWrite(STEP_MT1, LOW);       // nivel alto
      delay(10);
     }
     //------------------------------------------------
     //MOTOR 2 INFERIOR------------------------------------------- 
    if(entryByte == '8'){
      digitalWrite(DIR_MT2, HIGH);    // giro en un sentido
      digitalWrite(STEP_MT2, HIGH);       // nivel alto
      delay(10);  
      digitalWrite(STEP_MT2, LOW);       // nivel alto
      delay(10);        
    }
    //MOVER ANTIHORARIO
    if(entryByte == '9'){
      digitalWrite(DIR_MT2, LOW);    // giro en SENTIDO OPUESTO
      digitalWrite(STEP_MT2, HIGH);       // nivel alto
      delay(10);  
      digitalWrite(STEP_MT2, LOW);       // nivel alto
      delay(10);
     
    }
    
  }

}
