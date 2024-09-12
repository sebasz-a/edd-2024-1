dictionary = {}

N = int(input())
for i in range(N):
    word = tuple(input().split())
    dictionary[word[0]] = word[1]

while True:
    query = input()
    if query == "#":
        break
    if query in dictionary:
        print(dictionary[query])
    else:
        print("Entrada no encontrada")
