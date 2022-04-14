import subprocess

#Introduction
#Print "Hello World" five times
for i in range(0,5):
    subprocess.check_call(['py','example.py'])

#cd into the src directory then
#Run py script.py in the terminal (Windows)