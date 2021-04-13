def reverse_complement_calculator(seq):
    # capitalize the sequence
    upper_seq = seq.upper()
    complement_seq = []
    # comlement the sequence
    for base in upper_seq:
        if base == "A":
            complement_seq.append("T")
        elif base == "T":
            complement_seq.append("A")
        elif base == "C":
            complement_seq.append("G")
        else:
            complement_seq.append("C")
    # reverse the complement sequence
    reverse_complement = reversed(complement_seq)
    result = "".join(reverse_complement)

    return result
# example
reverse_complement_calculator("AtcTGaTCA")




