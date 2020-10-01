import argparse,os
parser = argparse.ArgumentParser(
add_help=True,
description='A script which converts Rubber Ducky scripts into Arduino sketches to be run on the Digispark USB dev board (based on the ATtiny85).',
epilog="Specify the path+filename of the Ducky script you wish to convert. By default, tinyDuck.py will create an output file with the same base name follwed by the .ino extension for Arduino sketches. Optionally you can specify the name of the output file with the '-out' parameter.")
parser.add_argument('infile', help="Filename of the Ducky script to convert",type=str)
parser.add_argument('--outfile', help="[optional] Filename of the output Arduino sketch", type=str)
args = parser.parse_args()
print("       ..---..") 
print("     .'  _    `.       ==========")
print(" __..'  (o)    :       -TINYDUCK-")
print("`..__          ;       ==========")
print("     `.       /")
print("       ;      `..---...___")
print("     .'                   `~-. .-')")
print("    .          _              ' _.'")
print("   :         =(.)__             :")
print("   \          (___/            '")
print("    +                         J")
print("    `._                   _.'")
print("        `~--....___...---~'")

if not args.outfile:
	baseName=os.path.splitext(args.infile)
	output=baseName[0]+'.ino'
elif args.out.endswith('.ino'):
		output=args.outfile
else:
		output=args.outfile+'.ino'

hexDictionary={
'_':'0x2D','-':'0x2D',',':'0x36',';':'0x33',':':'0x33','!':'0x1E','?':'0x38',"'":'0x34','"':'0x34','(':'0x26',')':'0x27','[':'0x2F',']':'0x30','{':'0x2F','}':'0x30','@':'0x1F',
'*':'0x25','/':'0x38','\\':'0x31','&':'0x24','#':'0x20','#':'0x32','%':'0x22','^':'0x23','+':'0x2E','<':'0x36','=':'0x2E','>':'0x37','|':'0x31','~':'0x32','$':'0x21','0':'0x37','A':'0x4',
'ALT':'MOD_ALT_LEFT','ALT':'MOD_ALT_RIGHT','B':'0x5','BREAK':'0x48','C':'0x6','CAPS':'0x39','CAPSLOCK':'0x39','CONTROL':'MOD_CONTROL_LEFT','CONTROL':'MOD_CONTROL_RIGHT',
'CTRL':'MOD_CONTROL_RIGHT','D':'0x7','DEL':'0x2A','DELETE':'0x2A','DOWN':'0x51','DOWNARROW':'0x51','E':'0x8','END':'0x4D','ENTER':'0x28','ESC':'0x29','ESCAPE':'0x29','F':'0x9',
'F1':'0x3A','F10':'0x43','F11':'0x44','F12':'0x45','F2':'0x3B','F3':'0x3C','F4':'0x3D','F5':'0x3E','F6':'0x3F','F7':'0x40','F8':'0x41','F9':'0x42','FUCNTION3':'0x3C','FUNCTION1':'0x3A',
'FUNCTION10':'0x43','FUNCTION11':'0x44','FUNCTION12':'0x45','FUNCTION2':'0x3B','FUNCTION4':'0x3D','FUNCTION5':'0x3E','FUNCTION6':'0x3F','FUNCTION7':'0x40','FUNCTION8':'0x41',
'FUNCTION9':'0x42','G':'0x0A','GUI':'MOD_GUI_LEFT','GUI':'MOD_GUI_RIGHT','H':'0x0B','HOME':'0x4A','I':'0x0C','INS':'0x49','INSERT':'0x49','J':'0x0D','K':'0x0E','L':'0x0F',
'LEFT':'0x50','LEFTARROW':'0x50','M':'0x10','N':'0x11','NUMLOCK':'0x53','O':'0x12','P':'0x13','PAGEDN':'0x4E','PAGEDOWN':'0x4E','PAGEUP':'0x4B','PAUSE':'0x48','PRINTSCREEN':'0x46',
'PRNTSCRN':'0x46','Q':'0x14','R':'0x15','RIGHT':'0x4F','RIGHTARROW':'0x4F','S':'0x16','SCRLLOCK':'0x47','SCROLLLOCK':'0x47','SHIFT':'MOD_SHIFT_LEFT','SHIFT':'MOD_SHIFT_RIGHT',
'SPACE':'0x2C','T':'0x17','TAB':'0x2B','U':'0x18','UP':'0x52','UPARROW':'0x52','V':'0x19','W':'0x1A','WIN':'MOD_GUI_LEFT','WINDOWS':'MOD_GUI_RIGHT','X':'0x1B','Y':'0x1C','Z':'0x1D'}

def convertLine(line):
	'''Takes a line from the Ducky script file and parses it, then converts it to the equivalent line which will work for the DigiSpark'''
	if line.startswith('STRING'):      # if line is a string, use DigiKeyboard.println
		typeString=line.lstrip('STRING ').rstrip("\n")
		output=("DigiKeyboard.println(\"%s\");\n" %(typeString))
	elif line.startswith('REM'):       # if line is a comment, use //
		output=(line.replace('REM', '//')+"\n")
	elif line.startswith('DELAY'):     # if line is a delay, use DigiKeyboard.delay()
		millis=int(line.split()[1])
		output=("DigiKeyboard.delay(%d);\n" %(millis))
	elif line.startswith('DEFAULT_DELAY') or line.startswith('DEFAULTDELAY'):
		defaultDelay=int(line.split[1])				
	else:                              # if line is keystroke, convert it to equivalent HID hex or DigiKeyboard defined string
		keyStrokes=line.split()
		if len(keyStrokes)>1:          # if there are multiple keystrokes (key + modifier) put them in correct format
			try:
				keyMod=hexDictionary[keyStrokes[0]]
			except KeyError:
				print("The key '%s' was not found in the dictionary of known keys." %(keyMod))
			try:
				key=hexDictionary[keyStrokes[1].upper()]
			except KeyError:
				print("The key '%s' was not found in the dictionary of known keys." %(key))
			output=("DigiKeyboard.sendKeyStroke(%s,%s);\n"%(key,keyMod))		
		else:
			try:
				output=("DigiKeyboard.sendKeyStroke(%s);\n"%(hexDictionary[line.rstrip().upper()]))
			except KeyError:
				print("The key '%s' was not found in the dictionary of known keys." %(line.rstrip().upper()))
	return output
			 				 
with open(args.infile,'r') as duckyScript:
	with open(output,'w') as tinyScript:
		lastLine=''
		tinyScript.write("#include <DigiKeyboard.h>\n")  # adds first lines to the file (including library, starting void setup)
		tinyScript.write("// Sketch was converted from USB Rubber Ducky script with tinyDuck by robil")
		tinyScript.write("void setup() {\n")
		tinyScript.write("DigiKeyboard.sendKeyStroke(0);\n")		
		for line in duckyScript:
			if not line.startswith('REPLAY'): 
				lastLine=convertLine(line)
				tinyScript.write(lastLine)
			else:                                   # if line is REPLAY, write the last command x number of times.
				numberToRepeat=int(line.split()[1])
				for x in range(1,numberToRepeat):	
					tinyScript.write("DigiKeyboard.delay(50);\n")
					tinyScript.write(lastLine)

		tinyScript.write("}\n")   # closes void setup
		tinyScript.write("void loop() {}")
		print("Converted the Ducky script '%s' into the Aruino sketch '%s'"%(args.infile,output))

		
