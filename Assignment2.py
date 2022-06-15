class Corrector:
    def divider(self, t, inputWords):
        wordSet = set(inputWords)
        memo = {}

        def recursive(sub):
            if sub in memo:
                return memo[sub]

            result = []
            for i in range(len(sub)):
                prefix = sub[:i+1]
                if prefix in wordSet:
                    if prefix == sub:
                        result.append(prefix)
                    else:
                        restOfWords = recursive(sub[i+1:])
                        for phrase in restOfWords:
                            result.append(prefix + ' ' + phrase)

            memo[sub] = result
            return result

        return recursive(t)

with open("Dictionary.txt") as f:
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

for i in (Corrector.divider(self="", t=corrupt, inputWords=dictionary)):
            print(i)
