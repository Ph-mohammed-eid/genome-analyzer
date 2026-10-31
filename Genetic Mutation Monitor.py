# # Genetic Mutation Monitor

# def genome_sequence(s):
# # Verifying inputs
#     if len(s) == 0:
#         print("Error: You did not enter any sequence!")
#         return None
#     else:
#         valid_bases = ["A", "T", "C", "G"]
#         is_valid = True
#         for base in s:
#             if base not in valid_bases:
#                 is_valid = False
#                 print("Error: The sequence contains numbers or codes that are not allowed!")
#                 break
#         if is_valid:
#             return s
#         return None

# # Taking inputs
# dna = genome_sequence(input('Please enter the DNA sequence: ').upper())
# mutation = genome_sequence(input('Please enter the mutation sequence: ').upper())

# # Finding mutation
# if mutation in dna:
#     print("The mutation was found.")
# else:
#     print("The mutation was not found.")


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

# Taking inputs
dna = None
while dna == None:
    dna = genome_sequence(input('Please enter the DNA sequence: ').upper())

mutation = None
while mutation == None:
    mutation = input('Please enter the mutation sequence: ').upper()


# Finding mutation
if mutation in dna:
    print("The mutation was found.")
else:
    print("The mutation was not found.")