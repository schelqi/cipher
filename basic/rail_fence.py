#  the Rail Fence Cipher


def encrypt(message, height):
    rail_fence = []
    for i in range(height):
        rail_fence.append(str())
    level = 0
    next = 1
    for c in message:
        for i in range(height):
            if i == level:
                rail_fence[i] += c

        if level + 1 == height:
            next = -next

        level += next
        if level == -1:
            level = 1
            next = -next

    return "".join(rail_fence)


def decrypt(message, height):
    msg_len = len(message)
    rail_fence = list("."*msg_len)
    index = 0
    for i in range(0, msg_len, height + 1):
        rail_fence[i] = message[index]
        index += 1
    start = 1
    step = 2
    for i in range(height - 1):
        for j in range(start, msg_len, step):
            rail_fence[j] = message[index]
            index += 1
        start += 1
        step *= 2

    return "".join(rail_fence)


fence = encrypt(input("Enter your message:"), 3)
print(fence)
print("###########################################################")
print(decrypt(fence, 3))
