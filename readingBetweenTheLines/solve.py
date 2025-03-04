with open('hidden','rb') as file:
    binary_data = file.read()

print(binary_data)

output = ""
countTotal = 0
for x in binary_data:
    if x == 10:
        output += "."
    else:
        output += "_"
    countTotal += 1

output2 = ""
for x in binary_data:
    if x == 10:
        output2 += "."
    else:
        output2 += "_"

output3 = ""
count = 0
for x in binary_data:
    if x == 10:
        count += 1
    else:
        output3 += str(count)
        count = 0

print(output)
print(output2)
print(output3)
print(countTotal)
