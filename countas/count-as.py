def count_as(filename):
    # Create a function that takes a filename as string parameter,
    # counts the occurances of the letter "a", and returns it as a number.
    # If the file does not exist, the function should return 0 and not break.

    try:
        my_file = open(filename, mode='r')
        text = my_file.read()
        count = 0
        for char in text:
            if char == 'a' or char == 'A':
                count += 1
        return count
    except FileNotFoundError:
        return 0

print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0
