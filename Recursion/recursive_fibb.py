def recursive_fibb(number):
    if number <= 1:
        return 1
    else:
        return recursive_fibb(number - 1) + recursive_fibb(number - 2)


number_of_terms = int(input())
for i in range(number_of_terms):
    print(recursive_fibb(i))
