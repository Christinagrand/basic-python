
# Print the numbers described in the exercise
#liste = []

#for i in range(1,11):
    #liste.append(i)
    #print(liste)


sequence = ""

for number in range(1, 11):
    if number == 1:
        sequence += str(number)
    else:
        sequence += " " + str(number)  
    print(sequence)