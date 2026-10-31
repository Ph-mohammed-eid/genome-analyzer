# --------------------------------------------------
# --- Welcome To Simple Genome Analyzer Program ---
# --------------------------------------------------

def genome_sequence(s):
# Verifying inputs
    if len(s) == 0:
        print("Error: You did not enter any sequence!")
        return None
    else:
        valid_bases = ["A", "T", "C", "G"]
        is_valid = True
        for base in s:
            if base not in valid_bases:
                is_valid = False
                print("Error: The sequence contains numbers or codes that are not allowed!")
                break
        if is_valid:
            return s
        return None

# Taking DNA from the user & uppercases it
dna = None
while dna == None:
    dna = genome_sequence(input('Please enter the DNA sequence: ').upper())


# Calculating length
print("length =",len(dna))

# GC count
gc_count = 0
for base in dna:
        if base == "G" or base == "C":
             gc_count = gc_count + 1
print("GC count =",gc_count)

# GC Percentage
gc_percentage = (gc_count/len(dna)) * 100
print(f"GC Percentage = {round(gc_percentage, 3)}%")

# RNA sequence
rna = dna.replace("T", "U")
print("RNA =",rna)