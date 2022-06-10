class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)
        memo = {}

        def helper(sub):
            if sub in memo:
                return memo[sub]

            result = []
            for i in range(len(sub)):
                prefix = sub[:i+1]
                if prefix in wordSet:
                    if prefix == sub:
                        result.append(prefix)
                    else:
                        restOfWords = helper(sub[i+1:])
                        for phrase in restOfWords:
                            result.append(prefix + ' ' + phrase)

            memo[sub] = result
            return result

        return helper(s)
    
with open("a2Input") as f:
    lines = f.readlines()
    lines = (line for line in lines if line)

    list = []

    for line in lines:
        list.append(line.strip())

    n = (int(list[0])) #nr of words
    faultyString = list[1] #input string
    
    wordDict1 = []
    
    for i in range(2,n+2):
        wordDict1.append(list[i])
 

    test = Solution
    print(Solution.wordBreak(self="", s=faultyString, wordDict=wordDict1))
    
    
