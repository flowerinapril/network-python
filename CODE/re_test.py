# import re
#
# print(re.search('www', 'www.runoob.com.www').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配


import re


# # 将匹配的数字乘于 2
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)
#
#
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))

#
# result1 = re.findall(r'\d+', 'runoob 123 google 456')
#
# pattern = re.compile(r'\d+')  # 查找数字
# result2 = pattern.findall('runoob 123 google 456')
# result3 = pattern.findall('run88oob123google456', 0, 10)
#
# print(result1)
# print(result2)
# print(result3)

#
# import re
#
# it = re.finditer(r"\d+", "12a32bc43jf3")
# for match in it:
#     print(match.group())



