numbers = [1,2,3,6,4,6]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

#duplicates are removed