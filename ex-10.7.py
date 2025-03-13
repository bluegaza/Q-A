letterCounts = {}
for letter in "Mississippi":
    letterCounts[letter] = letterCounts.get (letter, 0) + 1
    
letterCounts
{’M’: 1, ’s’: 4, ’p’: 2, ’i’: 4}
letterItems = letterCounts.items()
letterItems.sort()
print letterItems
[(’M’, 1), (’i’, 4), (’p’, 2), (’s’, 4)]