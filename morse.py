import os;
import time;
import sys
string="";
if len(sys.argv)==1:
	string = input("").lower();
else:
	iterstring = iter(sys.argv)
	next(iterstring);
	for j in iterstring:
		string = string + j + " "
Morse = {
"a":".-",
"b":"-...",
"c":"-.-.",
"d":"-..",
"e":".",
"f":"..-.",
"g":"--.",
"h":"....",
"i":"..",
"j":".---",
"k":"-.-",
"l":".-..",
"m":"--",
"n":"-.",
"o":"---",
"p":".--.",
"q":"--.-",
"r":".-.",
"s":"...",
"t":"-",
"u":"..-",
"v":"...-",
"w":".--",
"y":"-.--",
"z":"--..",
" ":"   ",
"1":".----",
"2":"..---",
"3":"...--",
"4":"....-",
"5":".....",
"6":"-....",
"7":"--...",
"8":"---..",
"9":"----.",
"0":"-----"
}
Coded="";
for s in string:
	try:
		Coded = Coded + str(Morse[s])+" ";
	except:
		continue;
for i in range(5):
	os.system("xdotool key Caps_Lock")
	time.sleep(0.5)
	os.system("xdotool key Caps_Lock")
	time.sleep(0.5)
for i in Coded:
	if i == ".":
		os.system("xdotool key Caps_Lock")
		time.sleep(0.5)
		os.system("xdotool key Caps_Lock")
	if i == "-":
		os.system("xdotool key Caps_Lock")
		time.sleep(1.5)
		os.system("xdotool key Caps_Lock")
	time.sleep(0.5)
