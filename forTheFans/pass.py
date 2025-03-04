import itertools
import py7zr

def get_permutations(lst):
    return list(itertools.permutations(lst))

# Example usage
my_list = ["09", "9", "14", "20", "00", "289", "24", "25"]
permutations = get_permutations(my_list)
passwords = set()
for perm in permutations:
    test = ""
    index = 0
    while len(test) < 7:
        test += perm[index]
        index += 1
    if len(test) == 7:
        print(test)

