# s = """
# I'm learning Python
# You are learning Python
# We are learning Python
# """
# print(s)

# s = '這裡有賣香蕉、蘋果、鳳梨、芭樂'
# s[4:].split('、')
# for i in s:
#     print(i)

# 99multi.py
RANGE1 = [1, 3]
RANGE2 = [1, 9]

def calc(a,b):
    return [
        {'sign': '*', 'result':a*b},
    ]

for i in range(RANGE1[0], RANGE1[1] + 1):
    for j in range(RANGE2[0], RANGE2[1] + 1):
        for k in calc(i, j):
            print('{:>7}'.format(str(i) + k['sign'] + str(j) + '=' + str(k['result'])),"|",end = " ")
    print()