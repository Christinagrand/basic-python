
# Print the pattern

for i in range(9):
    if i < 5:
        print((i)*"* "+1*"*")
    else:
        j=i-4
        print((i-2*j)*"* "+1*"*")
