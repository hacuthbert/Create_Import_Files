import re
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
#f = open("demofile2.txt", "r")
#print(f.read())

regex = re.compile("^Mary")
with open("demofile2.txt") as f:
    for line in f:
        result = regex.search(line)

print(f'this line starts with Mary.   {line}')

# re.compile('[a-z]+')
#general secret re.compile('[a-zA-Z0-9+]{40}')
#aws secret re.compile('(?:ASIA|AKIA|AROA|AIDA)([A-Z0-7]{16})')