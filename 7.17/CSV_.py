# f = open('workfile', 'w')
# # do somthing...
# print(f.closed)
# f.close()
# print(f.closed)

# f = open('not_existed_file')

# """
# <hello>

# hello world
# hello python
# """

# f = open('hello', 'w+')
# f.write("hello")
# f.write("world")
# print(f.read())
# f.close()

# f = open('newfile', 'w+')
# f.write('Create by me')
# f.tell()
# f.seek(1)
# print(f.read())
# f.close()

# date = input('輸入日期')
# event = input('輸入事件:')
# description = input('輸入心得:')
# with open('hello.txt','r+') as f:
#     f.write(str(date))
#     f.write(str(event))
#     f.write(str(description))
#     f.seek(0)
#     print(f.read())

# import csv
# with open('menu.csv', 'w', encoding='utf-8-sig') as csvfile:
#     filewriter = csv.writer(csvfile, delimiter=',')
#     filewriter.writerow(['品名', '價格','銷售量'])
#     filewriter.writerow(['餛飩麵', '50','666'])
#     filewriter.writerow(['蛋花湯', '25','123'])
#     filewriter.writerow(['可樂', '20','989'])

# with open('menu.csv', 'r', encoding='utf-8-sig') as f:
#     reader = csv.reader(f)

#     # read file row by row
#     for row in reader:
#         print(row)
#$$$
import csv
with open('/Users/deli/Desktop/X-village-class-practice/7.17/AQI.csv', 'r+', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    min=100
    clearplace=''
    for row in reader:
        if row[2] =='AQI':
            continue
        if int(row[2])<min:
            min = int(row[2])
            clearplace = row[0]
    print(clearplace)
        

        


