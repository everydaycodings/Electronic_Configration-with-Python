elem = int(input("Enter the atomic number of element: "))

eleconfig = ""
prefix = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p", "7s", "5f", "6d", "7p"]

def maxocc(s):
    global maxoccu
    if s[1] == "s":
        maxoccu = 2
    if s[1] == "p":
        maxoccu = 6
    if s[1] == "d":
        maxoccu = 10
    if s[1] == "f":
        maxoccu = 14

for x in range(len(prefix)):
    maxocc(prefix[x])
    if elem == 0:
        break
    elif elem >= 118:
        break
    elif elem >= maxoccu:
        eleconfig = eleconfig + prefix[x] + str(maxoccu) + " "
        elem = elem - maxoccu
    elif elem < maxoccu:
        eleconfig = eleconfig + prefix[x] + str(elem)
        break
    print(elem)

print(eleconfig)