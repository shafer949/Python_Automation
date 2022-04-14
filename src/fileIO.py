
#Set file names
fileName = '../inputFile.txt'
output1 = "PassFile.txt"
output2 = "FailFile.txt"

#Open the file
f = open(fileName,'r') 

#Create (write) a new file for passes
passFile = open(output1,'w')

#Create (write) a new file for failures
failFile = open(output2, 'w')

#Loop over each line in the file
for line in f:
    #Split each line by whitespace
    line_split = line.split()
    if line_split[2] == "P":
        #Print only those who passed (P)
        passFile.write(line)
    else:
        #Print only those who failed (F)
        failFile.write(line)

#Close each file after the creation/writing process is complete
passFile.close()
failFile.close()

#cd into the src directory then
#Run py fileIO.py in the terminal (Windows)
#Notice two files are created: PassFile.txt and FailFile.txt within the src directory