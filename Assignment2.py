def recursive(index, words):
    if index == len(corrupt):
        print(words)  # print all possible combinations

    temp = ""
    for i in range(index, len(corrupt)):
        temp += corrupt[i]
        try:
            dictionary[temp]
            # print(temp, end=" ")
            recursive(i+1, words+temp+" ")
        except:
            continue


lines = []
with open('a2Input.txt') as f:        # rename text file -------------------------------
    lines = f.readlines()

dictionary = {}
count = 0
for line in lines:
    if count == 0:
        length = int(line)
        count += 1
        continue
    if count == 1:
        count += 1
        corrupt = line.strip()
        continue
    dictionary[line.strip()] = 1
    count += 1

recursive(0, "")
