/*
SOURCE: Example sketch created by willblev
TARGET OS: All (Windows, Mac, Linux, etc.)
NOTES: Turns on and off CAPS LOCK key at random intervals. Duration and frequency can be adjusted with on_wait and off_wait parameters.
*/
#include <DigiKeyboard.h>
// Prank to turn on and off CAPS LOCK briefly every 25-100 seconds
int on_wait = 100;  // Interval for how long to toggle CAPS LOCK will be ON. If set to 100, CAPS will be on for 0.3 to 0.7 seconds
int off_wait = 3000;  // Delay interval between toggles. If set to 4000, CAPS will be turned on/off every 15 to 60 seconds

void setup() {
  DigiKeyboard.update();
}

void loop() {
  DigiKeyboard.sendKeyStroke(57); //turn ON
  DigiKeyboard.delay(random(3,7)*on_wait);
  DigiKeyboard.sendKeyStroke(57); //turn OFF
  DigiKeyboard.delay(random(5,20)*off_wait);
}
