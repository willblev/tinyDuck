
infile='/home/william/github/tinyDuck/ducky_script_example.txt'
outfile='/home/william/github/tinyDuck/ducky_example_converted_v2.ino'
decDictionary={'CTRL':'MOD_CONTROL_LEFT','SHIFT':'MOD_SHIFT_LEFT','ALT':'MOD_ALT_LEFT','GUI':'MOD_GUI_LEFT','CTRL':'MOD_CONTROL_RIGHT',
'SHIFT':'MOD_SHIFT_RIGHT','ALT':'MOD_ALT_RIGHT','GUI':'MOD_GUI_RIGHT','CONTROL':'MOD_CONTROL_LEFT','WIN':'MOD_GUI_LEFT','CONTROL':'MOD_CONTROL_RIGHT',
'WINDOWS':'MOD_GUI_RIGHT','END':77,'PAGEDN':78,'RIGHT':79,'LEFT':80,'DOWN':81,'UP':82,'NUMLOCK':83,'PAGEDOWN':78,'RIGHTARROW':79,'LEFTARROW':80,
'DOWNARROW':81,'UPARROW':82,'1':30,'2':31,'3':32,'4':33,'5':34,'6':35,'7':36,'8':37,'9':38,'0':39,'ENTER':40,'ESC':41,'DEL':42,'TAB':43,
'SPACE':44,'-':45,'=':46,'[':47,']':48,"\\":49,"#":50,';':51,"'":52,',':54,'0':55,"/":56,'CAPS':57,'F1':58,'F2':59,'F3':60,'F4':61,
'F5':62,'F6':63,'F7':64,'F8':65,'F9':66,'F10':67,'F11':68,'F12':69,'PRNTSCRN':70,'SCRLLOCK':71,'PAUSE':72,'INSERT':73,'HOME':74,'PAGEUP':75,
'A':4,'B':5,'C':6,'D':7,'E':8,'F':9,'G':10,'H':11,'I':12,'J':13,'K':14,'L':15,'M':16,'N':17,'O':18,'P':19,'Q':20,'R':21,'S':22,'T':23,
'U':24,'V':25,'W':26,'X':27,'Y':28,'Z':29,'!':30,'@':31,'#':32,'$':33,'%':34,'^':35,'&':36,'*':37,'(':38,')':39,'ESCAPE':41,'DELETE':42,
'_':45,'+':46,'{':47,'}':48,'|':49,'~':50,':':51,'"':52,'<':54,'>':55,'?':56,'CAPSLOCK':57,'FUNCTION1':58,'FUNCTION2':59,
'FUCNTION3':60,'FUNCTION4':61,'FUNCTION5':62,'FUNCTION6':63,'FUNCTION7':64,'FUNCTION8':65,'FUNCTION9':66,'FUNCTION10':67,'FUNCTION11':68,'FUNCTION12':69,
'PRINTSCREEN':70,'SCROLLLOCK':71,'BREAK':72,'INS':73}
defaultDelay=100

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
	'''Takes a line from the ducky script and parses it, then converts it to DigiSpark'''
	
	if line.startswith('STRING'):
		typeString=line.lstrip('STRING ').rstrip("\n")
		output=("DigiKeyboard.println(\"%s\");\n" %(typeString))
	elif line.startswith('REM'):
		output=(line.replace('REM', '//')+"\n")
	elif line.startswith('DELAY'):
		millis=int(line.split()[1])
		output=("DigiKeyboard.delay(%d);\n" %(millis))
	elif line.startswith('DEFAULT_DELAY') or line.startswith('DEFAULTDELAY'):
		defaultDelay=int(line.split[1])				
	else:
		 keyStrokes=line.split()
		 if len(keyStrokes)>1:
			 keyMod=hexDictionary[keyStrokes[0]]
			 key=hexDictionary[keyStrokes[1].upper()]
			 output=("DigiKeyboard.sendKeyStroke(%s,%s);\n"%(key,keyMod))
		 else:
			 output=("DigiKeyboard.sendKeyStroke(%s);\n"%(hexDictionary[line.rstrip().upper()]))
	return output
			 				 
with open(infile, 'r') as duckyScript:
	with open(outfile, 'w') as tinyScript:
		lastLine=''
		tinyScript.write("#include <DigiKeyboard.h>\n")  # adds first lines to the file (including library, starting void setup
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

