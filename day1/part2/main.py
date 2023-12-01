# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    Lines[count] = line.strip()
    count += 1

file1 = open('main.txt', 'w')

#Calculates the answer
numbers = {'one' : 'on1e', 'two' : 'tw2o', 'three' : 'thr3e','four': 'fo4ur', 'five':'fi5ve','six': 'si6x','seven': 'sev7en','eight' : 
'ei8ght','nine':'ni9ne'}
found_numbers = []
sum=0


for line in Lines:
    #Replaces words
    for key,value in numbers.items():
        line = line.replace(key, value)

    ptr1=0
    ptr2=len(line)-1
    num1=0
    num2=0
    num1_found = False
    num2_found = False

    while num1_found == False or num2_found == False:
        if line[ptr1].isdigit() and num1_found == False:
            num1=int(line[ptr1])
            num1_found = True
        if line[ptr2].isdigit() and num2_found == False: 
            num2=int(line[ptr2])
            num2_found = True
        ptr1 += 1
        ptr2 -= 1

    sum += int(str(num1) + str(num2))
    file1.writelines(str(sum)  + "\n")

print(sum)
file1.close()