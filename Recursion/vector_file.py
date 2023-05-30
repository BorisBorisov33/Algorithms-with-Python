def generate_0_1(index, vector):
    if index >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2):
        vector[index] = num
        generate_0_1(index + 1, vector)


n = int(input())
vector = [0] * n
# print(vector)

generate_0_1(0, vector)
