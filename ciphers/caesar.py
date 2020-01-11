test = """tm bcsv qolfp
f'dmvd xuhm exl tgak
hlrkiv sydg hxm
qiswzzwf qrf oqdueqe
dpae resd wndo
liva bu vgtokx sjzk
hmb rqch fqwbg
fmmft seront sntsdr pmsecq"""

literals = "abcdefghijklmnopqrstuvwxyz"
key = 0
key_bak = 0
offset = 0

list = [1,5,9,12,15,18,22,-1]
count = 0
key = list[0]

for char in test:
    if char == ' ':
        print(' ', end='')
        offset += 1
        key = list[count]
    elif char == '\n':
        print('')
        #key = key_bak = key_bak + 4
        key = list[count]
        offset = 0
        count += 1
    else:
        if list[count] + offset >= len(literals):
            list[count] -= len(literals) + offset
        newChar = literals.find(char) + list[count] + offset
        if newChar >= len(literals):
            newChar -= len(literals)
        print (literals[newChar], end='')

print ('\n------------------------')
