import os
import re
os.chdir("D:\\Github\\IBI1_2020-21\\Practical8")
file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
lines = file.readlines()
result_line = []
for i in range(len(lines)):
    if lines[i].startswith('>') and "unknown function" in lines[i]:
        result_line.append(re.findall(r'(>.+?)(?:_| )', lines[i])[0])
        bases = ""
        for j in range(len(lines[i:-1])):
            if not lines[i+j+1].startswith(">"):
                bases += lines[i+j+1][:-1]
            else:
                break
        bases += "\n"
        result_line.append(bases)
for i in range(len(result_line)):
    if result_line[i].startswith(">"):
        result_line[i] += " "
        result_line[i] += str(len(result_line[i+1])-1)
        result_line[i] += "\n"

new_file = open("unknown_function.fa", "w")
for line in result_line:
    new_file.write(line)
new_file.close()









