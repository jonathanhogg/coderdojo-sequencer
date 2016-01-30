
#include <MPR121.h>


const int MPR121_ADDR = 0x5C;
const int MPR121_INT = 4;
const int NUM_PADS = 12;

void setup()
{ 
  Serial.begin(115200);
  
  pinMode(LED_BUILTIN, OUTPUT);

  MPR121.begin(MPR121_ADDR);
  MPR121.setInterruptPin(MPR121_INT);
  MPR121.setTouchThreshold(40);
  MPR121.setReleaseThreshold(20);
  MPR121.updateAll();
}

void loop()
{
  if (MPR121.touchStatusChanged())
  {
    MPR121.updateTouchData();
    
    for (int i = 0; i < NUM_PADS; i++)
    {
      if (MPR121.isNewTouch(i))
      {
        // Light the LED
        digitalWrite(LED_BUILTIN, HIGH);
        // Print a message on the serial connection like "pad #"
        Serial.print("pad ");
        Serial.println(i);
      }
      else if (MPR121.isNewRelease(i))
      {
        // Turn off the LED
        digitalWrite(LED_BUILTIN, LOW);
      }
    }
  }
}


