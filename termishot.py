from PIL import ImageGrab 
import time
print("Do you want to take a Screenshot from your Terminal?")
print("Just Type START to take a Screenshot!")
inpt1 = input("Type START or EXIT: ")
if inpt1 == "START" or "start" or "Start":
	print(5)
	time.sleep(1)
	print(4)
	time.sleep(1)
	print(3)
	time.sleep(1)
	print(2)
	time.sleep(1)
	print(1)
	time.sleep(1)
	img = ImageGrab.grab()
	print("(Note: Files with the same name will be deleted!)")
	name = input("Name: ")
	img.save(name + ".png")
	print("Screenshot Done!")
elif inpt1 == "EXIT" or "exit" or "Exit":
	print("Goodbye.")
else:
	("This command doesn't exist!")





