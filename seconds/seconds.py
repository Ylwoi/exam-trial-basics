def seconds(num_list):
    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]

    every_second = []
    for number in range(len(num_list)):
        if number % 2 != 0:
            every_second.append(num_list[number])
    return every_second


print(seconds([1, 2, 3, 4, 5])) # should print [2, 4]
