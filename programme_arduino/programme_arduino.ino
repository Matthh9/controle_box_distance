#include <IRremote.h>
#include <string.h>

#define PortResetElectrique A0

String lecture ;
int port ;
IRsend emission_ir; // crée une instance

// miroir série
void setup() {
  Serial.begin(9600); // initialise le port série  
  Serial.setTimeout(100); // permet de mettre le timeout de lecture du port serie à 100 ms, permet d'appuyer plus rapidement sur des touches sur l'ihm du programme python
  
  pinMode(2, OUTPUT);      // sets the digital pin as output
  pinMode(4, OUTPUT);      // sets the digital pin as output
  pinMode(5, OUTPUT);      // sets the digital pin as output
  pinMode(6, OUTPUT);      // sets the digital pin as output
  pinMode(7, OUTPUT);      // sets the digital pin as output
  pinMode(8, OUTPUT);      // sets the digital pin as output
  pinMode(9, OUTPUT);      // sets the digital pin as output
  pinMode(10, OUTPUT);      // sets the digital pin as output
  pinMode(11, OUTPUT);      // sets the digital pin as output
  pinMode(12, OUTPUT);      // sets the digital pin as output
  pinMode(PortResetElectrique, OUTPUT);      // pour les resets electrique
  pinMode(15, OUTPUT);      // sets the digital pin as output
  pinMode(16, OUTPUT);      // sets the digital pin as output
  pinMode(17, OUTPUT);      // sets the digital pin as output
  pinMode(18, OUTPUT);      // sets the digital pin as output
  pinMode(19, OUTPUT);      // sets the digital pin as output
  
  digitalWrite(2, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);
  digitalWrite(12, LOW);
  digitalWrite(PortResetElectrique, LOW);
  digitalWrite(15, LOW);
  digitalWrite(16, LOW);
  digitalWrite(17, LOW);
  digitalWrite(18, LOW);
  digitalWrite(19, LOW);
  
} // fin setup

void loop() {
  
  while (Serial.available()) { // tant que caractère en réception
    lecture = Serial.readString() ; 
    Serial.print("message recu : ");
    Serial.println(lecture);

    //Si on recoit un message reset_electrique
    if(lecture.indexOf("reset_electrique")!=-1){
      Serial.println("reset");
      digitalWrite(PortResetElectrique, HIGH);
      delay(5000);
      digitalWrite(PortResetElectrique, LOW);

      delay(100);
      digitalWrite(port, LOW); // on coupe le précédent port, permet la libération du relay pour reboot
      delay(100);
      digitalWrite(port, HIGH); // on autorise le port de controle
    } 

    //Si on recois un message avec port -> changement de machine controlee
    else if(lecture.indexOf("port")!=-1){
      Serial.println("changement de techno");
      Serial.println("activation port correspondant sur la carte");
      
      digitalWrite(port, LOW); // on coupe le précédent port
      lecture.remove(0, 4); // on transforme la chaine de caractère en supprimant la partie "port"
      Serial.println(port);
      port=lecture.toInt(); //et tranforme le reste en entier
      digitalWrite(port, HIGH);
      
    } 

    //si on recoit un message avec salve -> lecture d'un message de type salve;n;code : enovoie de n fois le code avec un certain temps de pause
    else if(lecture.indexOf("salve")!=-1){
      Serial.println("salve");
      lecture.remove(0,lecture.indexOf(";")+1);
      int repetition = lecture.substring(0,lecture.indexOf(";")).toInt();
      lecture.remove(0,lecture.indexOf(";")+1);
      long code = convertStrToHex(lecture.substring(0,lecture.indexOf(";")));
      Serial.println(code);
      
      //lecture.concat(";");
      for (int i=0; i<repetition;i++){
        emission_ir.sendNEC(code, 32);
        delay(10);
      }
    }
    
    //si on recoit un message avec ; -> envoie simultané de plusieurs code
    else if(lecture.indexOf(";")!=-1){
      Serial.println("envoie multiple");
      //lecture.concat(";");
      while(lecture.indexOf(";")!=-1){
        emission_ir.sendNEC(convertStrToHex(lecture.substring(0,lecture.indexOf(";"))), 32);
        lecture.remove(0,lecture.indexOf(";")+1);
        delay(250);
      }
    }

    //si fin
    else if(lecture.indexOf("Fin")!=-1){
      digitalWrite(port, LOW);
    }

    //reception d'une commande, on envoie le code infrarouge    
    else {
      Serial.println("Envoi commande");
      Serial.println(convertStrToHex(lecture));
      emission_ir.sendNEC(convertStrToHex(lecture), 32);
    }

  } // fin While
} // fin loop



long convertStrToHex(String texte){
  long extract;

  extract = convertCharToHex(texte[0]);
    for(char i = 1; i < texte.length(); i++){
      //On décale d'un octet la valeur puis on ajoute l'octet suivant que l'on convertit (Char to HEX)
      extract = extract<<4 | convertCharToHex(texte[i]);
  }
  
  return extract;
}

char convertCharToHex(char ch){
  char returnType;
  switch(ch){
    case '0':
    returnType = 0;
    break;
    case  '1' :
    returnType = 1;
    break;
    case  '2':
    returnType = 2;
    break;
    case  '3':
    returnType = 3;
    break;
    case  '4' :
    returnType = 4;
    break;
    case  '5':
    returnType = 5;
    break;
    case  '6':
    returnType = 6;
    break;
    case  '7':
    returnType = 7;
    break;
    case  '8':
    returnType = 8;
    break;
    case  '9':
    returnType = 9;
    break;
    case  'A':
    returnType = 10;
    break;
    case  'B':
    returnType = 11;
    break;
    case  'C':
    returnType = 12;
    break;
    case  'D':
    returnType = 13;
    break;
    case  'E':
    returnType = 14;
    break;
    case  'F' :
    returnType = 15;
    break;
    default:
    returnType = 0;
    break;
  }
  return returnType;
}
