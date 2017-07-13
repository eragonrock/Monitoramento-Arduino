#include <DallasTemperature.h> //Biblioteca para o sensor de temperatura DS18B20
#include <OneWire.h>           //Biblioteca para o sensor de temperatura DS18B20
//#include <SoftwareSerial.h> 
#define DS18B20 7                     //Define o pino do sensor de temperatura DS18B20

OneWire ourWire(DS18B20);            //Configura uma instncia OneWire para se comunicar com o sensor de temperatura DS18B20
DallasTemperature sensors(&ourWire); //Envia a leitura da temperatura para o DallasTemperature
int portaLDR = A5;                   //Porta analógica utilizada pelo LDR ( sensor de luminisidade )  


void setup()
{
  Serial.begin(9600);                //Inicializaçao da comunicaçao serial, no caso com o servidor
  sensors.begin();                   // INICIA O SENSOR DS18B20
}
 
void loop(){
  char dados;
  if (Serial.available() > 0){      //Se houve algum sinal sendo passado pela serial
    dados = Serial.read();          //tais dados sao alocados na variavel - dados -
    ler(dados);
  }
}
 
void ler(char dados){
    if (dados=='1'){      
      int lum = analogRead(portaLDR);  //Lê o valor fornecido pelo LDR 
      Serial.println(lum);             //envia leitura para a porta serial e consequentemente para o servidor
    }else{
      
      sensors.requestTemperatures();                     //REQUISITA A TEMPERATURA DO SENSOR
      float temp = (sensors.getTempCByIndex(0)*500)/1023;// Valor da temperatura convertido em graus Celsos 
      Serial.println(temp*2);                            // Envia leitura para a porta serial e consequentemente para o servidor
     
    }
}
