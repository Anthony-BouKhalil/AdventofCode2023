# Using readlines()
file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    Lines[count] = line.strip()
    count += 1

#Calculates the answer
sum=0
for line in Lines:
    ptr1=0
    ptr2=len(line)-1
    num1=0
    num2=0
    num1_found = False
    num2_found = False

    while ptr1 <= ptr2:
        if line[ptr1].isdigit() and num1_found == False:
            num1=int(line[ptr1])
            num1_found = True
        if line[ptr2].isdigit() and num2_found == False: 
            num2=int(line[ptr2])
            num2_found = True
        ptr1 += 1
        ptr2 -= 1

    sum += num1 + num2

print(sum)