# tinyDuck
A simple Python script which converts Ducky scripts into Arduino sketches for the Digispark. 

The USB rubber ducky (http://usbrubberducky.com) is "*...a Human Interface Device programmable with a simple scripting language allowing penetration testers to quickly and easily craft and deploy security auditing payloads that mimic human keyboard input*". It has an 60 MHz 32-bit  processor as well as the option to store your code on a microSD card, making this little number fast, powerful, sexy, and deadly. It is available on the Hak5 shop (http://hakshop.com)  and will set you back around $45 USD. They do fantastic work, so if you enjoy playing with tinyDuck, please consider buying a real Rubber Ducky!

The Digispark (http://digistump.com/products/1) is a multi-purpose development board based on the ATtiny85 microcontroller. It can emulate a USB keyboard with the  Arduino library DigiKeyboard (https://github.com/digistump/DigisparkArduinoIntegration). It runs considerably slower at 8MHz (but can be pushed up to 20 MHz), and only has ~6k flash memory for your code. It costs ~$8 USD; however, clones can found for <$2 on Ebay or any Chinese electronics distributor sites.

## Usage
To convert a Ducky script into an Arduino sketch to be used on the Digispark, simply run the following:
```
python tinyDuck.py  <Ducky_script_filename>
```
By default, tinyDuck.py will create a sketch (.ino) with the same base name as the original Ducky file and in the same directory. Alternatively, you can specify the path/filename of the desired output with the '--out' parameter.

**This code has only been tested and verified to work with simple Ducky scripts- if you find any bugs, please report them!**

*Rubber Ducky Scripts:*
https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Payloads

*Convert Ducky scripts to Arduino sketches:*
https://github.com/mame82/duck2spark
https://pypi.python.org/pypi/digiduck
https://github.com/geckom/DigiDucky
https://hhoca.com/2016/10/02/poor-mans-rubber-ducky/

*DigiSpark Ducky tutorials:*
http://0xdeadcode.se/archives/581    
https://hhoca.com/2016/10/02/poor-mans-rubber-ducky/
http://www.redteamr.com/2016/08/digiducky/
https://illlogicnet.wordpress.com/2016/09/20/digiexploit/

