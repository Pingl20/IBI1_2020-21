import os
import re
translation_dict = {"TTT": "F",
                    "TTC": "F",
                    "TTA": "L",
                    "TTG": "L",
                    "CTT": "L",
                    "CTC": "L",
                    "CTA": "L",
                    "CTG": "L",
                    "ATT": "I",
                    "ATC": "I",
                    "ATA": "I",
                    "ATG": "M",
                    "GTT": "V",
                    "GTC": "V",
                    "GTA": "V",
                    "GTG": "V",
                    "TCT": "S",
                    "TCC": "S",
                    "TCA": "S",
                    "TCG": "S",
                    "CCT": "P",
                    "CCC": "P",
                    "CCA": "P",
                    "CCG": "P",
                    "ACT": "T",
                    "ACC": "T",
                    "ACA": "T",
                    "ACG": "T",
                    "GCT": "A",
                    "GCC": "A",
                    "GCA": "A",
                    "GCG": "A",
                    "TAT": "Y",
                    "TAC": "Y",
                    "TAA": "STOP",
                    "TAG": "STOP",
                    "CAT": "H",
                    "CAC": "H",
                    "CAA": "Q",
                    "CAG": "Q",
                    "AAT": "N",
                    "AAC": "N",
                    "AAA": "K",
                    "AAG": "K",
                    "GAT": "D",
                    "GAC": "D",
                    "GAA": "E",
                    "GAG": "E",
                    "TGT": "C",
                    "TGC": "C",
                    "TGA": "STOP",
                    "TGG": "W",
                    "CGT": "R",
                    "CGC": "R",
                    "CGA": "R",
                    "CGG": "R",
                    "AGT": "S",
                    "AGC": "S",
                    "AGA": "R",
                    "AGG": "R",
                    "GGT": "G",
                    "GGC": "G",
                    "GGA": "G",
                    "GGG": "G"}

os.chdir("D:\\Github\\IBI1_2020-21\\Practical8")

open_file = open("unknown_function.fa", 'r')
lines = open_file.readlines()
result = []
for line in lines:
    if line.startswith(">"):
        result.append(line)
    else:
        protein = ""
        for i in range(0, len(line), 3):
            if translation_dict[line[i:i+3]] != "STOP":
                protein += translation_dict[line[i:i+3]]
            else:
                break
        protein += "\n"
        result.append(protein)
print(result)
for i in range(len(result)):
    if result[i].startswith(">"):
        result[i] = re.findall(r'>.+? ', result[i])[0]
        result[i] += str(len(result[i+1]))
        result[i] += "\n"

protein_new_file = open("protein.fa", "w")
for line in result:
    protein_new_file.write(line)
protein_new_file.close()