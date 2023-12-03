#This is morse code program
#Converting words into morse code
#Creating sound with morse code for a word


#creating letter with morse code bucket
import winsound
import time
morseCodeBucket = {
  
    'A' : ".-",
    'B' : "-...",
    'C' : "-.-.",
    'D' : "-..",
    'E' : ".",
    'F' : "..-.",
    'G' : "--.",
    'H' : "....",
    'I' : "..",
    'J' : ".---",
    'K' : "-.-",
    'L' : ".-..",
    'M' : "--",
    'N' : "-.",
    'O' : "---",
    'P' : ".--.",
    'Q' : "--.-",
    'R' : ".-.",
    'S' : "...",
    'T' : "-",
    'U' : "..-",
    'V' : "...-",
    'W' : ".--",
    'X' : "-..-",
    'Y' : "-.--",
    'Z' : "--..",
    ' ' : "   "
    }


#setting up the Beep sound
freq_dot = 500
freq_dash = 500
dot_time = 200
dash_time = 500

#setting up functions to play Dot sound and Dash sound 
def playDot():
    winsound.Beep(freq_dot,dot_time)

def playDash():
    winsound.Beep(freq_dash,dash_time)


#setting up function to print morse code
def printMorse(word):
    print("Morse Code for ",word, " is \n")
    for letter in word:
        print(morseCodeBucket[letter],end=" ")
    

if __name__ == '__main__':

    yourWord = input("Enter a word to change into morse code : ")
    yourWord = yourWord.strip()
    newWord = yourWord.upper()

    printMorse(newWord)
    
    for every_letter in newWord:
        for every in morseCodeBucket[every_letter]:
            if(every == '.'):
                playDot()
              
            elif(every == '-'):
                playDash()
        
        time.sleep(0.5)
                
                


    
