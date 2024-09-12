c_words = {} #para las palabras compuestas
words = [] #para poder iterar las palabras del diccionario

while True:
    word = input()

    if word == "#":
        aux = set(words)
        for w in words:
            syl = "" #silabas de la palabra
            for i in range(len(w)-1):
                syl += w[i]
                if syl in aux:
                    syl2 = w[len(syl):]
                    if syl2 in aux:
                        c_words[w] = (syl, syl2)

        break

    words.append(word)
