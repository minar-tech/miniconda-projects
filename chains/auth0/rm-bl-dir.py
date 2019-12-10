#!/home/mnyman/miniconda3/envs/chains/bin/python

import os

def create_list():

    # ---------- create list of files ----------
    path = './1_raw'
    file_list = [f for f in os.listdir(path) if f.endswith('.html')]

    # ---------- remove empty lines ----------
    for file in file_list:

        f_input = "1_raw/%s" % file
        f_output = "2_rmws/%s" % file

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

        print("Removed empty lines in" + file) 


if __name__ == "__main__":
    create_list()
