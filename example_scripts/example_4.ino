/*
SOURCE: Written by willblev
TARGET OS: Any (Windows, Mac, Linux)
NOTES:  Sends cursor to the bottom right corner to "hide" there.
*/

#include "DigiMouse.h"

unsigned int mouse_move_amount = 100;

void setup() {
  DigiMouse.begin(); //start or reenumerate USB
}

void loop() {
  DigiMouse.update(); 
          DigiMouse.moveY(mouse_move_amount);
          DigiMouse.moveX(mouse_move_amount);
}
