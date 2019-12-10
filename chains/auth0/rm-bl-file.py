#!/home/mnyman/anaconda3/bin/python3.7

import sys

def rmBlanks(param):

    f_input = "1dload/%s" % param
    f_output = "2strip/%s" % param

    f_process = open(f_input, "r")
    lines = f_process.readlines()
    f_process.close()

    keep = []
    for line in lines:
        if not line.isspace():
            keep.append(line)

    f_process = open(f_output, "w")
    f_process.write("".join(keep))
    f_process.close()

    print("Done!")

if __name__ == "__main__":
    rmBlanks(sys.argv[1])
