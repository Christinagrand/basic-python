import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.

lower = False
upper = False
num = False
char = False

if 6 <= len(password) <= 16:
    for i in password:
        if i.islower():
            lower = True
        elif i.isupper():
            upper = True
        elif i.isnumeric():
            num = True
        elif i in "$#@":
            char = True

if lower and upper and num and char:
    is_valid = True

print(is_valid)
