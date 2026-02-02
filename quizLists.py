names = []
while True:
    name = input("Enter a name (or leave blank to finish):")
    if not name:
        break
    names.append(name)

#Remove Duplicates using set, convert back to list
unique_names = list(set(names))

#Sort the unique_names alphabetically
unique_names.sort()

#Print the final sorted words
print(f"Sorted Unique names: {unique_names}")

#Count and print total number of names
print(f"Total number of names entered: {len(unique_names)}")
