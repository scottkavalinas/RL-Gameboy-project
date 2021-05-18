import random
import os
import time
from pynput.keyboard import Key, Controller   #For getting user inputs
from fileLocations import GameFile
keyboard = Controller()



def openFunc(FileLocation):       #function for opening the rom and emulator
	os.startfile(FileLocation)


gold= GameFile   #Make sure that your rom's default application is set as the emulator you want to use
gold = GameFile.getRom()

openFunc(gold)

time.sleep(5)
buttonTime = 0.0001   #Set how long a button press will take
releaseTime = 0.0001

#define functions to press A, B, up, down, left, right and space
def press_A(buttonTime):
	Button_A_Press = keyboard.press('z')
	time.sleep(buttonTime)
	Button_A_Release = keyboard.release('z')
	time.sleep(releaseTime)
	print(" Button 'A' has been pressed")

def press_B(buttonTime):
	Button_B_Press = keyboard.press('x')
	time.sleep(buttonTime)
	Button_B_Release = keyboard.release('x')
	time.sleep(releaseTime)
	print(" Button 'B' has been pressed")

def press_UP(buttonTime):
	Button_UP_Press = keyboard.press('w')
	time.sleep(buttonTime)
	Button_UP_Release = keyboard.release('w')
	time.sleep(releaseTime)
	print(" Button 'UP' has been pressed")

def press_DOWN(buttonTime):
	Button_DOWN_Press = keyboard.press('s')
	time.sleep(buttonTime)
	Button_DOWN_Release = keyboard.release('s')
	time.sleep(releaseTime)
	print(" Button 'DOWN' has been pressed")

def press_LEFT(buttonTime):
	Button_LEFT_Press = keyboard.press('a')
	time.sleep(buttonTime)
	Button_LEFT_Release = keyboard.release('a')
	time.sleep(releaseTime)
	print(" Button 'LEFT' has been pressed")

def press_RIGHT(buttonTime):
	Button_RIGHT_Press = keyboard.press('d')
	time.sleep(buttonTime)
	Button_RIGHT_Release = keyboard.release('d')
	time.sleep(releaseTime)
	print(" Button 'RIGHT' has been pressed")

def hold_SPACE(buttonTime):
	Button_SPACE_Press = keyboard.press(Key.space)
	time.sleep(buttonTime)

def release_SPACE(buttonTime):
	Button_B_Press = keyboard.release(Key.space)
	time.sleep(releaseTime)	



def menu_SKIP(): #repeatedly presses A to skip the start menu in pokemnon gold
	for i in range(45):
		press_A(buttonTime)


count = 0
iterations = 100    #set the number of random movements to make

hold_SPACE(buttonTime) #In the visualboy advanced emulator, space runs the game at a faster speed
menu_SKIP() #skip the menu
release_SPACE(buttonTime)


# Generate random movements
hold_SPACE(buttonTime)
for i in range(iterations):
	number = random.randint(0,3)
	buttonTime = 0.001 * random.randint(1,10)
	if number == 0:
		press_UP(buttonTime)
	if number == 1:
		press_DOWN(buttonTime)
	if number == 2:
		press_RIGHT(buttonTime)
	if number == 3:
		press_LEFT(buttonTime)
	
	press_A(0.0001)
	press_A(0.0001)
	press_A(0.0001)
	press_B(0.0001)
	press_B(0.0001)
	count += 1
	print(count)


