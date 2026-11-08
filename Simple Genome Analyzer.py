# --------------------------------------------------
# --- Welcome To Simple Genome Analyzer Program ---
# --------------------------------------------------

# Opening the file
while True:
    file_name = input("Please Enter The File Name Name: ")
    try: 
        file = open(file_name,"r")
        # Saving DNA in a list
        dna = list()
        for line in file:
            line = line.strip()
            if not line or line.startswith(">"):
                continue
            for base in line:
                dna.extend(base.upper())
        if not dna:
            print(f"Error: \"{file_name}\" is Empty!")
            continue
        file.close()
        break

    except FileNotFoundError:
        print(f"Error: \"{file_name}\" Has Not Found!")
        continue

# Calculating length
dna_length = len(dna)
print("length =",dna_length)

# Bases count
bases = dict()
for base in dna:
        bases[base] = bases.get(base,0) + 1
for k,v in bases.items():
    print(f"{k}: {v}")
    

# Calculating the total without N value
canonical_total = sum(bases.get(b, 0) for b in "ATGC")
print("Main Total=",canonical_total)

valid_bases = set("ATGCNRYMKSWBDHV")
contents_dict = {} #storing the results for the report

# Taking the base to calculat contant
while True:
    base = input("Enter base\bases to see its content\nOr Enter \"skip\" to pass: ").upper().strip()
    if base == "SKIP": 
        break

    elif len(base) < 1:
        print("Unverified input!")
        continue

    else:
        input_list = list(base.split())
        lst = list()
        is_valid = True

        for b in input_list:
            if all(x in valid_bases for x in b):
                lst.append(b)
            else:
                print(b, "Invalid input!")
                is_valid = False
        if not is_valid:
            continue

# counting the given base contant
    lst = list(dict.fromkeys(lst))
    try:
        for selected_bases in lst:
            total = canonical_total
            base_count = 0
            for base in selected_bases: 
                if base == "N":
                    total = dna_length
                base_count = base_count + bases.get(base,0)
            base_content = (base_count / total) * 100
            print(selected_bases,f"content = {round(base_content, 3)}%")
            contents_dict[selected_bases] = round(base_content, 3) #storing the results for the report
            continue
        continue
    except ZeroDivisionError: 
        print("Error: No Valid Bases Available For Calculation.")
        break

print("Done!")

# Report file
report = open("Genome_Analyzer_Report.txt","w")
report.write("Simple Genome Analyzer\n")
report.write("=======================\n")
report.write(f"File Name: {file_name}\n")
report.write(f"Sequence Length: {dna_length}\n\n")
report.write("-------------------------------------------\n")

# Bases counts
report.write("Nucleotide Distribution\n\n")
# report.write("\n")
for k,v in bases.items():
    report.write(f"{k}: {v}\n") 
report.write("-------------------------------------------\n")

# Bases Content
report.write("Base Content Results\n\n")
# report.write("\n")
for base, content in contents_dict.items():
    report.write(f"{base}: {content}%\n")
report.write("-------------------------------------------\n")

report.close()