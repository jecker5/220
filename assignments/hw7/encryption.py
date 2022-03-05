def encode(message, key):
    acc = ""
    for i in message:
        c = ord(i)
        i = chr(key+c)
        acc += i
    l = len(acc)
    acc = acc[:l-1]
    return acc
