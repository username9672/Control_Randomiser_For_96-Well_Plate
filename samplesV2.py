
import random

#initialise variables
index = 0
positiveRand = 0
rand1 = 0
rand2 = 0
rand3 = 0
rand4 = 0
listLen = 0
strVar = ""
intVar = 0
removeWhite = ""

#initialise arrays
neg = [""] * 4
letter = ["A", "B", "C", "D", "E", "F", "G", "H"] *12
number = [""] *96


for index in range(0, 8):
    number[index] = "1"
for index in range(8, 16):
    number[index] = "2"
for index in range(16, 24):
    number[index] = "3"
for index in range(24, 32):
    number[index] = "4"
for index in range(32, 40):
    number[index] = "5"
for index in range(40, 48):
    number[index] = "6"
for index in range(48, 56):
    number[index] = "7"
for index in range(56, 64):
    number[index] = "8"
for index in range(64, 72):
    number[index] = "9"
for index in range(72, 80):
    number[index] = "10"
for index in range(80, 88):
    number[index] = "11"
for index in range(88, 96):
    number[index] = "12"
    
    
#open input file and read it
#name of file in place of fileName.txt
text_file = open("filename.txt", "r")
lines = text_file.readlines()


#create or write to output file
#if filename is an existing file it will overwrite existing data
outputFile = open("outputFile.txt", "w")

#make file appendable
outputFile = open("outputFile.txt", "a")


#remove whitespace after the numbers
for index in range (len(lines)):
  removeWhite = lines[index]
  lines[index] = removeWhite.strip()

 
#strip "\n"
for index in range(listLen):
  lines[index]=lines[index][:-2]


#make int
for index in range(len(lines)):
  intVar = lines[index]
  lines[index] = int(intVar)
  
  
#sort ascending
lines.sort()


#make str
for index in range(len(lines)):
  strVar = lines[index]
  lines[index] = str(strVar)
  
  
#find length of list
listLen = len(lines)


#get what user wants negative control to be called
for index in range(4):
    neg[index] = str(input("Please enter what you want negative control " + str(index + 1) + " to be called: "))


#get what user wants positive control to be called
pos = str(input("Please enter what you want the positive control to be called: "))


if listLen >= 0 and listLen <=22:

    #make random position for positive control
    positiveRand = random.randint(0, (listLen + 2))
    
    #make random position in the first quadrant for negative control 1
    rand1 = random.randint(0, (listLen + 2))

    #add positive control to list at random position
    lines.insert(positiveRand, pos)

    #add negative control 1 at random position
    lines.insert(rand1, neg[0])
    
    #print and add results to output file for every element of list "lines"
    for index in range(listLen + 2):
        
        #put results into outputfile
        outputFile.write(letter[index] + number[index] + "\t" + lines[index] + "\n")

        #print results
        print (letter[index] + number[index] + "\t" + lines[index] + "\n")


elif listLen >= 23 and listLen <=45:
    
    #make random position for positive control
    positiveRand = random.randint(0, (listLen + 3))

    #make random position in the first quadrant for negative control 1
    rand1 = random.randint(0, 24)

    #make random position in the second quadrant for negative control 2
    rand2 = random.randint(25, (listLen + 3))

    #add positive control to list at random position
    lines.insert(positiveRand, pos)

    #add negative control 1 at random position
    lines.insert(rand1, neg[0])

    #add negative control 2 at random position
    lines.insert(rand2, neg[1])

    #print and add results to output file for every element of list "lines"
    for index in range(listLen + 3):

        #put results into outputfile
        outputFile.write(letter[index] + number[index] + "\t" + lines[index] + "\n")

        #print results
        print (letter[index] + number[index] + "\t" + lines[index] + "\n")


elif listLen >= 46 and listLen <=68:

    #make random position for positive control
    positiveRand = random.randint(0, (listLen + 4))

    #make random position in the first quadrant for negative control 1
    rand1 = random.randint(0, 24)

    #make random position in the second quadrant for negative control 2
    rand2 = random.randint(25, 48)

    #make random position in the third quadrant for negative control 3
    rand3 = random.randint(49, (listLen + 4))

    #add positive control to list at random position
    lines.insert(positiveRand, pos)

    #add negative control 1 at random position
    lines.insert(rand1, neg[0])

    #add negative control 2 at random position
    lines.insert(rand2, neg[1])

    #add negative control 3 at random position
    lines.insert(rand3, neg[2])

    #print and add results to output file for every element of list "lines"
    for index in range(listLen + 4):

        #put results into outputfile
        outputFile.write(letter[index] + number[index] + "\t" + lines[index] + "\n")

        #print results
        print(letter[index] + number[index] + "\t" + lines[index] + "\n")

elif listLen >= 69 and  listLen <= 91:

    #make random position for positive control
    positiveRand = random.randint(0, (listLen + 5))

    #make random position in the first quadrant for negative control 1
    rand1 = random.randint(0, 24)

    #make random position in the second quadrant for negative control 2
    rand2 = random.randint(25, 48)

    #make random position in the third quadrant for negative control 3
    rand3 = random.randint(49, 72)

    #make random position in the fourth quadrant for negative control 4
    rand4 = random.randint(73, 96)

    #add positive control to list at random position
    lines.insert(positiveRand, pos)

    #add negative control 1 at random position
    lines.insert(rand1, neg[0])

    #add negative control 2 at random position
    lines.insert(rand2, neg[1])

    #add negative control 3 at random position
    lines.insert(rand3, neg[2])

    #add negative control 4 at random position
    lines.insert(rand4, neg[3])

    #print and add results to output file for every element of list "lines"
    for index in range(listLen + 5):

        #put results into outputfile
        outputFile.write(letter[index] + number[index] + "\t" + lines[index] + "\n")

        #print results
        print(letter[index] + number[index] + "\t" + lines[index] + "\n")

#error for if file contains too many sample numbers
elif listLen > 91:
    print("Error, input file invalid")

#close the output file 
outputFile.close()






