import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        encoding_list = []
        for i in x: 
           encoding_list.append(hex(ord(i)))
        encoding = ''.join(encoding_list)
        print(encoding)

    case "decode":
        y = x.split('0x')
        decoding_list = []
        y.pop(0) #remove first element
        for i in y:
            decoding_list.append(chr(int(i, base = 16)))
        decoding = ''.join(decoding_list)
        print(decoding)
