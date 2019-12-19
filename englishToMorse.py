def translate(message):

	translation = { "A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..", "E" : ".", 
			 "F" : "..-.", "G" : "--.", "H" : "....", "I" : "..", "J" : ".---",
			 "K" : "-.-", "L" : ".-..", "M" : "--", "N" : "-.", "O" : "---", 
			 "P" : ".--.", "Q" 
			 : "--.-", "R" : ".-.", "S" : "...", "T" : "-",
			 "U" : "..-", "V" : "..-", "W" : ".--", "X" : "-..-", "Y" : "-.--",
			 "Z" : "--..", "0" : "-----", "1" : ".----", "2" : "..---", "3" : "...--",
			 "4" : "....-", "5" : ".....", "6" : "-....", "7" : "--...", "8" : "---..",
			 "9" : "----.", " " : " "}
	if message in translation: 
		return translation[message] + " "


 	
def englishToMorse(message):

	message = message.upper()
	breakdown = list(message)
	answer = ""


	for length in breakdown:
		answer += translate(length)

	return answer






