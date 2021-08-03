word = 'makan'
s = ""

for i in range(len(word)-1,-1,-1):
    s += word[i]

if (s == word):
    print(True)
else:
    print(False)