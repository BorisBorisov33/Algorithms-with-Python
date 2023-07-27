def order_elements(my_dictionary, b_array):
    for first, second in my_dictionary.items():
        second = str(second).lstrip()
        print(first,second)

        if (len(str(second))) == 4:
            b_array.append(str(first).strip())

        # print(b_array[-1])
        # if b_array[-1] in second:
        #     print(first)

    return b_array


my_dictionary = {}

input_line = input()

while input_line != "End":

    key, values = input_line.split('->')
    # values = [x for x in values.split()] if values else []
    if key not in my_dictionary:
        my_dictionary[key] = []

    if values not in my_dictionary[key]:
        my_dictionary[key].append(values)

    input_line = input()


a_array = []


print(order_elements(my_dictionary, a_array))

# this to be updated