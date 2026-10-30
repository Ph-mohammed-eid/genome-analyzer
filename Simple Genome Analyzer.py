# --------------------------------------------------
# --- Welcome To Simple Genome Analyzer Program ---
# --------------------------------------------------

# Taking DNA from the user & uppercases it
dna = input('Please enter the DNA sequence: ').upper()
if len(dna) == 0:
        print("Error: You did not enter any sequence!")
else:

# Verifying inputs
    valid_bases = ["A", "T", "C", "G"]
    is_valid = True
    for base in dna:
        if base not in valid_bases:
            is_valid = False
            print("Error: The sequence contains numbers or codes that are not allowed!")
            break

# Calculating length
    if is_valid:
        print("length =",len(dna))

# GC count
        gc_count = 0
        for base in dna:
            if base == "G" or base == "C":
                gc_count = gc_count + 1
        print("GC count =",gc_count)

# GC Percentage
    
        gc_percentage = (gc_count/len(dna)) * 100
        print("GC Percentage =",gc_percentage,"%")

# RNA sequence
        rna = dna.replace("T", "U")
        print("RNA =",rna)






