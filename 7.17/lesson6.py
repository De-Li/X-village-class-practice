# print(abs(complex(3,4)))
# my_tuple = ("A", "B", "c")
# print(max(my_tuple))

# import timeit

# my_code_0 = "my_array_0 = [x for x in range(1000)]"
# my_code_1 = "my_array_1 = list(range(1000))"

# print (timeit.timeit(stmt = my_code_0, number=100000), "\n")
# print (timeit.timeit(stmt = my_code_1, number=100000), "\n")

# import timeit

# # 要計時的模組載入
# my_setup = "import random"

# my_code = "my_value = random.randint(0, 10)"

# print (timeit.timeit(setup= my_setup, stmt= my_code, number= 100000))

# import timeit

# my_code_0 = "my_array_0 = [x for x in range(1000)]"
# my_code_1 = "my_array_1 = list(range(1000))"

# print (timeit.repeat(stmt = my_code_0, repeat= 5, number = 100000), "\n")
# print (timeit.repeat(stmt = my_code_1, repeat= 5, number = 100000), "\n")

# from itertools import combinations

# for i in combinations("12345678", 2):
#     print(i)

# from itertools import combinations_with_replacement

# for i in combinations_with_replacement("1234", 2):
#     print(i)

# from itertools import permutations

# for i in permutations("1234", 2):
#     print(i)

# import random

# # 午餐列表
# lunch = ["好煮義", "大肥鴨", "三商巧福", "鄉村", "一心二葉", "不要吃"]

# # 隨機選擇午餐
# selectLunch = random.randint(0, len(lunch)-1)
# print(lunch[selectLunch])