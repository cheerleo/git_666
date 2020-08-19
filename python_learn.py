# 一、字符串及变量
#
# 1.变量的命名规则
# 变量只能包含 字母、数字、下划线。
# 变量不能包含空格，不能用数字开头。不能用python BIF（内建函数）及关键字命名。
# 变量不能包含任何除了下划线以外的符号。
# 两种命名方法：(1)驼峰命名法：stuScore, classStuName；(2)下划线命名法：stu_score, class1_stu_name。
#
# 2.字符串的处理（“字符”表示单一字符，“字符串”表示一串字符）
# m1 = "my nAMe is leo" #字符串的开始和结束可以用双引号""也可以用单引号''
# m2 = m1.title()
# m3 = m1.upper()
# m4 = m1.lower() #注意：title、upper、lower并不更改原有的m1变量数据，m1本身保持不变
# m5 = "my t_name \"is\" leo " # “ \ ”表示转义字符，使""不再具有字符串开始和结束的功能
# length = len(m4)
#
# 3.字符串的拼接和特殊符号
# t_name = " hello" + " world" # 字符串的拼接
# print("hello" + " world" + t_name)
# print("hello \t world") #\t表示制表符“table”，输出个大空格
# print("hello \n world") #\n表示换行符
#
# joy = "the unfailing childlike appetite " \
#       "of what's next and the joy " \
#       "of the game of living."
# 若定义的字符串太长，可以在每一句的末尾增加 “ \ ”符号换行。该符号也是转义字符。
#
# 二、数字类型
#
# 1.整数运算
# res1 = 7+8    # “ = ”表示赋值运算符
# res2 = 7-8
# res3 = 7*8    # “ * ”表示乘以
# res4 = 8/3
# res5 = 8//3   # “ // ”表示整除
# res6 = 8%3    # “ % ”表示求余数或者“取模运算”
# res7 = 4**2   # “ ** ”表示次方运算
# res8 = 3+6*4  # 运算优先级与数学相同,复杂式子通常用括号来控制优先级
#
# 2.浮点数运算
# res9 = 7.2+8     # 浮点数加整数的运算结果是浮点数
# res10 = 7.1-8.0  # 结果是-0.9000000000000004，有精度问题。
# 加减乘除都有可能出现精度问题，实际项目开发会用到更精确的算法。
#
# 3.数字和字符串的运算
# 数字和字符串不能直接拼在一起运算
# 需要将数字转换成字符串，用"18"或者str(18)
# msg1 = "my age is " + "18"
# msg2 = "my age is " + str(18)
#
# 或者将字符串转换成数字，用int("18")或者float("2.3")
# age1 = int("18") + 5     # 注意不能是int("18dd"),必须是纯数字才能转换
# age2 = float("2.3") + 5  # 注意不能是float("2.3dd"),必须是纯数字才能转换
#
# print(int(3.7656))  # int(3.7656)表示取整数位，这是int()的第二个功能
# msg3 = "nice!"*5    # 表示将"nice!"输出五遍，注意不能乘以浮点数5.0或5.3
#
# 4.变量的赋值
# v = 10       # 也可以是 v = "xxx"
# v = v + 1    # “ = ” 等号指的是把右边的值赋给左边的变量，等号优先级最低
# v += 1       # “ += ” 表示的是 v = v + xxx (xxx可以是字符串或者数字，依据 v 的初始性质而定）
# v = v - 1    # 简写成 v -= 1
# v = v * 3    # 简写成 v *= 3
# v = v / 3    # 简写成 v /= 3
# v = v % 3    # 简写成 v %= 3
# v = v // 3   # 简写成 v //= 3
#
# 三、print()打印以及input()输入的命令使用
#
# 1.print()打印
# (1)基本功能
# print("leo")                    # print括号里面可放入字符串、数字、列表、字典等等
# print([666, 23, 111])
#
# (2)打印组合信息
# print("Sum is: ", a + b)
# print括号里面可放入提示词，再用 “ , ” 或 “ + ”与要输出的结果连接
# 但用“ + ”，必须保证两边的数据类型相同，同是字符串或者同是数字
#
# (3)打印的特殊属性
# for i in range(0, 11):
#     print(i, end="-")           # print()内含end="\n"的默认变量，默认打印完换一行。可以修改" "双引号内部的值，输出不同效果。
#
#
# 2.input()输入
# res = input()  # 无论输入的是什么，input都会将其转换成字符串
# print("hello " + res + "!!!")
#
# res1 = input("please enter 1st number: ")  # input括号里面可以输入字符串显示给用户
# res2 = input("please enter 2nd number: ")
# a = int(res1)  # 原本input提取的只是字符串，用int()将字符串抓换成整数
# b = int(res2)  # 如果用户输入的不是数字，则报错。可通过特殊方法提前判断
#
# 四、列表 List (与字典不同，列表是有序的）
#
# 1.列表的定义
# 列表名称 = [数据1, 数据2, 数据3]，列表的"数据1"是 “0号” 索引位
# 列表是默认可以换行输入，不需要在每行末尾添加“ \ ”符号
# train_names = ["neo", "michael", "leo", "jacky", "bruce"]
# scores = [54, 93, 87, 88]
# text = ["leo", "jacky", 99, 798]
# names1 = ["neo", "michael", "leo",
#          "jacky", "bruce", "lee",
#          "james", "lucy", "lily"]
#
# 2.列表的定位和切片（slice）--- （重要定位命令：train_names[]）
# print(train_names[3])   # 定位并显示names里的 “3号”元素
# print(train_names[-1])  # 定位并显示names里的最后一个元素（“3号”元素）
# print(train_names[1].title())
# # title、upper、lower（三类字符串方法）可用于列表内容大小写变换，但并不影响原有列表数据
# # title、upper、lower 不能用于列表里的数字数据，因为他们是针对字符串str的
# # 注意索引位可以是正数也可以是负数，负数代表倒序
#
# print(train_names[0:3])  # 截取子列表，输出['michael', 'leo', 'jacky']，注意不包含 “3号”元素
# print(train_names[0:4])  # 不包含 “4号”元素
# print(train_names[1:1])  # 得到 “空值”
# print(train_names[1:2])  # 截取 “1号”元素
#
# print(train_names[:3])  # 从第一个元素开始截取到 “2号”元素
# print(train_names[1:])  # 从 “1号”元素开始截取到最后一个元素
# print(train_names[:])   # 不填索引位，相当于选取全部元素（复制原列表），与print(train_names)等效
#
# # 注意，切片操作实际上是[索引位1，索引位2)，是右侧开区间
# # 切片是Python序列的重要操作之一，适用于列表、元组、字符串、range对象等类型。
# # 切片的具体详情： https://blog.csdn.net/sinat_28576553/article/details/84404653
#
# 3.列表的增加、插入、删除及弹出 （只有知道某元素值的索引位，才能直接修改它，或者用remove与insert配合，间接修改）
# train_names[2] = "superman"   # 定位并修改 “2号”元素。train_names[索引位] = XX，表示直接修改某个索引位的元素值。
# train_names.append("roy")     # append默认在列表的末尾新增元素
# train_names.insert(3, "neo")  # insert用于在某个索引位插入新的元素
# train_names.remove("neo")     # 指定元素——remove用于删除指定的元素，如果列表里有多个"neo"，则只删除索引位最靠前的那个
# del(train_names[3])           # 指定位置——del用于删除列表某个索引位的元素，del后也可不带括号del train_names[3]
# train_names.pop()             # pop用于将某个索引位的元素取出删除，简称“弹出”（默认先弹出最后一个元素），类似开枪时子弹射出。
# print(train_names.pop(1))     # pop通常配合print使用，元素弹出之前，先显示。
#
# 4.列表的排序
# 方法1： sort 永久排序 —— 会修改原列表
# msg = ["neo", "1michael", "1Michael", "Leo", "jacky", "bruce"]
# msg.sort()   # 对str元素排序时，大原则是按照首字母顺序排，首字母相同比较第二个字母。对数字元素排序直接比较大小。
# print(msg)   # 特殊：若有str元素首字母大写，则排在前。若str元素以数字开头，则该元素排在首字母大写元素前。
# # names1列表的排序结果是['1Michael', '1michael', 'Leo', 'bruce', 'jacky', 'neo']
# # sort不可用于排序中文，中文首字拼音排序需要自己写排序算法。
# msg.sort(reverse=True)  # reverse=True指的是倒序排列
#
# 方法2： sorted 排序 —— 不修改原列表
# newList = sorted(msg)  # 注意：sorted用法为sorted(msg)，而sort用法是msg.sort()
# print(sorted(msg))     # sorted排序之后的结果需要存在新的列表里，或者直接print
# newList1 = sorted(msg, reverse=True)   # sorted倒序用法，注意与sort的区别
#
# 5.多维列表
# mixList = ["love", 873, 6.66, "travel", 96, "food"]               # 列表可以是str元素和数字元素的混合
# mixList1 = [[98, "love"], [76, 23, "travel"], 576]                # 列表里的元素可以是列表，称为多维列表
# mixList2 = [[98, [77, "food"], "love"], [76, 23, "travel"], 576]  # 列表里的元素可以是列表，称为多维列表
# print(mixList2[0][1][0])  # 在多维列表里，定位其列表元素中的元素
#
# 6.列表其他操作
# aList = ["Lihua", "Rain", "Jack", "Xiuxiu", "Peiqi", "Black"]
# bList = [1, 2, 3, 4, 5, 2, 1]
#
# print(aList.index("Peiqi"))  # index用来查看某元素的索引值（位置）
# print(len(aList))            # len用来查看列表里有多少个元素
#
# aList.extend(bList)          # extend用来在原列表 aList 末尾加上新列表 bList
# cList = bList + aList        # 列表可直接相加合并，注意 bList + aList 与 aList + bList 得到的新列表不相同
# aList = aList + bList        # 也可以写成 aList += bList
#
# msg.reverse()                # reverse是对列表的镜像翻转
# print(msg)                   # reverse会修改原列表，属于永久翻转
#
# print(max(bList))            # 求列表中元素的最大值
# print(min(bList))            # 求列表中元素的最小值
# print(sum(bList))            # 求列表中元素的总和。注意不能写sum(1, 2, 3) ，要写作sum([1, 2, 3])才能运算。因为sum()的参数必须是list。
#
# 7.列表的遍历及批量修改元素
# 方法1（直接遍历元素值）—— 无法修改原列表的元素值，只能访问和显示（显示的结果可修改）：
# aList = ["Lihua", "Rain", "Jack", "Xiuxiu", "Peiqi", "Black"]
# for n in aList:               # 这是一个for循环，其中n充当aList（集合体）的临时变量，临时变量可以自由定义。
#     n = n + " is great!"      # 注意for语句结尾的冒号 “：”，以及本句的tab缩进。缩进的语句就是我们想实现的循环体。
#     print(n)                  # 同一个for循环里，循环体可以有好几个，这里的print(n)也是循环体。
# print(aList)                  # 没有缩进的语句，不再是循环体，单独输出。另外，可以看到原列表元素值并未被修改。
#
# 方法2（通过遍历索引位的方式遍历元素值）—— 可批量修改原列表的每个元素值：
# aList = ["Lihua", "Rain", "Jack", "Xiuxiu", "Peiqi", "Black"]
# for t in range(0, len(aList)):  # 首先遍历索引位：len(aList)为6，而range()为右侧开区间，所以range范围是0至5，与索引位匹配。
#     aList[t] += " is great!"    # 相比法1，法2可以利用“ alist[] = xx ”的特性来遍历修改元素的值，这是法2最大的优点。
#     print(aList[t])
# print(aList)                    # 法2的print(aList)结果显示原列表的每个元素值均已被修改，而法1不变。
#
# 8.列表的生成
# 方法1：
# dList = []                  # 首先定义一个空列表dList
# tempo = range(1, 11)        # 用range()先生成一串数字（1到10）存在tempo，注意range()同样是右侧开区间。
# for i in tempo:             # 再用for循环遍历tempo中的一串数字
#     dList.append(i)         # 把每个遍历到的数字放在dList列表的末尾，形成完整的dList列表
# print(dList)
#
# 方法2（直接用list(range())生成）：
# dList = list(range(2, 20))      # range()生成的数字并不是列表，无法直接print，使用list()可将其直接转换成列表
# dList1 = list(range(2, 20, 3))  # range(2, 20, 3)中的 3 表示步进step(递增)的量，只能是整数int
#
# 【例题1】 生成一个列表，元素为1到10的平方数：
# 法1（先预设一个空列表）：
# nList = []
# tem = range(1, 11)          # 这一步也可以是tem = list(range(1, 11))，先生成一个新列表tem
# for i in tem:
#     square = i ** 2
#     nList.append(square)
# print(nList)
#
# 法2（法1的简化）：
# nList = []
# for i in range(1, 11):     # range()生成的一串数字是可以直接遍历的，不需要先存储在某个变量里
#     nList.append(i ** 2)
# print(nList)
#
# 法3（先生成含1到10的列表，再修改）：
# dList = list(range(1, 11))  # 先用list(range())生成一个列表dList
# print(dList)
# for i in dList:             # 在列表dList里遍历，i = 1，2，3....10。注意：i遍历的是元素的值而不是索引位
#     dList[i - 1] = i ** 2   # dList[]表示修改某个索引位的元素值，1的索引位是1-1，2的索引位是2-1，得每个元素的索引位皆为i-1
# print(dList)
#
# 法4（极简形式，list comprehension 【列表推导式】方法）：
# 列表推导式(list comprehension)和生成器表达式(generator expression)类似
# 详见：https://blog.csdn.net/qq_36523839/article/details/79807866
# 【注意】生成器generator并不是一次性把所有元素都生成放在内存里，而是有需要的需要再逐一生成并提取出来；
# 【注意】列表推导式list comprehension一次性把所有元素都生成放在内存里，如果元素很多的话，非常占空间。

# dList = [t**2 for t in range(1, 11)]  # 使用list comprehension，相当于法2的再简化
# print(dList)                          # 输出[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# pList = (t*1 for t in range(1, 11))   # 使用generator expression，注意是圆括号形式。
# print(pList)                          # 输出 <generator object <genexpr> at 0x000002C651FE6D48>

# 另外，其实推导式分为列表推导式（list），字典推导式(dict)，集合推导式(set)三种
# （1）字典推导式：
# names_dict = {1: "Lihua", 2: "Rain", 3: "Jack", 4: "Xiuxiu", 5: "Peiqi", 6: "Black"}
# print(names_dict)
# new_dict = {v: k for k, v in names_dict.items()}  # 使用字典推导式，调换字典中key和value的位置
# print(new_dict)

# （2）集合推导式：
# a_set = {i ** 2 for i in [3, 3, 5, 6, 7, 7, 9]}   # 使用集合推导式，功能类似列表推导式，但是利用上了集合的元素去重功能
# print(a_set)

# 【例题2】 将整数123456转化为列表，元素为1到6的平方数（list comprehension 方法）
# num = 123456
# list_of_digits = [(int(i))**2 for i in str(num)]   # 使用 list comprehension 方法，将整数转换为数字列表。
# print(list_of_digits)
#
# 9.列表的复制
# train_names = ["Lihua", "Rain", "Jack", "Xiuxiu", "Peiqi", "Black"]
#
# 方法1（新列表独立存放元素）：
# newList = train_names[:]    # 方法1相当于为newList在内存里开辟新的房间，存放与names完全相同的列表元素
# newList[4] = "佩琪"   # 对于用方法1复制的新列表newList，修改其元素值并不会影响到原列表names
#
# 方法2（新列表不独立，与原列表共用元素）：
# newList = train_names       # 方法2相当创建了新标签newList，指向原列表names里的所有元素，newList与names共用相同元素
# newList[4] = "佩琪"   # 对于用方法2创建的新标签newList，修改其元素值就是修改原列表names的元素值
#
# 特殊情况：
# newList = train_names * 2     # 基于方法2创建newList，复制两次（或用方法1 newList = train_names[:] * 2）
# newList[4] = "佩琪"     # 复制多次的情况下，采用方法1、方法2，修改新列表均并不会影响到原列表names的元素值
#
# 10.列表的扩展
# aList = ["Lihua", "Rain", "Jack", "Xiuxiu", "Peiqi", "Black"]
# bList = [1, 2, 3, 4, 5, 2, 1]
# aList.extend(bList)          # extend用来在原列表 aList 末尾加上新列表 bList
# cList = bList + aList        # 列表可直接相加合并，注意 bList + aList 与 aList + bList 得到的新列表不相同
# aList = aList + bList        # 也可以写成 aList += bList
#
# 11.【元组（Tuple） ———— 是特殊的列表，不可修改】
# 元组用（）表示，是不可修改的列表（元组仅可查询），其他性质与列表相同。
# dList = ["Lihua", "Rain", "Jack", "Xiuxiu"]
# dTup = ("Lihua", "Rain", "Jack", "Xiuxiu")
# dTup1 = ("Lihua",)           # 如果定义元组时，只有一个元素，必须加上逗号“,”，否则会被认为是给变量赋值
# dTup2 = (18,)                # 若是("Lihua")和(18)，会被认为括号是多余的，识别为字符串"Lihua"和数字18
#
# for i in dTup:               # 元组可遍历
#     i = i + " is great!"     # 但不能用索引位遍历法配合dList[]修改元素值
#     print(i)                 # 可显示修改后的结果
#
# 12.【集合(set) ———— 无序不重复序列，用于数据去重、
# python中，用set来表示一个无序不重复元素的序列。set的主要作用就是用来给数据去重，比如直接把会重复的元素添加进空集合，或者将list转化成set来去重
# 可以使用大括号 { } 或者 set() 函数创建集合，但是注意创建空集合必须用set()而不是{}，因为{}表示空字典。
# 【注意】集合set不记录元素位置或者插入点。因此，sets不支持索引和切片, 或其它类序列（sequence-like）的操作。

# （1）用{}创建set集合
# aSet = {"Leo", "Mike", "Leo", 123, 878, 123}    # 元素可为各种类型，可以赋值重复数据，但是存储时会去重
# print(len(aSet))                                # 存放了6个数据，长度显示是4
# print(aSet)                                     # print输出是元素去重之后的，且每次元素显示的顺序均不同
# for i in aSet:
#     print(i)                   # 集合遍历，每一次的元素输出顺序都是不同的，因为set不记录元素位置或者插入点

# （2）空set集合用set()函数表示，而不是{}
# set_1 = set()
# print(len(set_1))
# print(set_1)                   # 空集合显示为set()

# （3）用set()函数创建set集合 ———— 只能传入一个参数，可以是list,tuple,str等
# set_2 = set(("hello", "Jerry", 133, 98, 133, "Jerry"))
# set_3 = set("ppyytthhoonn")    # 传入的字符串也是会去重的
# print(len(set_2))
# print(len(set_3))
# print(set_2)
# print(set_3)

# （4）为列表去重
# a_lst = ["Leo", "Mike", "Leo", 123, 878, 123]
# a_set = set(a_lst)
# print(a_set)                   # 输出{123, 'Leo', 878, 'Mike'}，已自动去重

# 五、条件判断
#
# 1.比较运算符和布尔类型
# a = 5
# b = 5
# res1 = a > b             # 若为真，则返回True，反之则返回False。“a > b”称为布尔表达式，返回的值True和False称为布尔值。
# res2 = a >= b            # “ >= ” 用于判断a是否大于或者等于b
# res3 = a < b
# res4 = a <= b            # “ <= ” 用于判断a是否小于或者等于b
# res5 = a == b            # “ == ” 用于判断两个值是否相等（不同于赋值运算符“ = ”）
# res6 = a != b            # “ != ” 用于判断两个值是否不相等
# res7 = "leo" == "ddd"    # 比较运算符也可以用来比较字符串
# 注意: True = not False ， not True = False
#
# 2.其他判断符号（and、or、in、not in）
# a = 5
# b = 5
# aList = [168, "Rain", "Jack", "Xiuxiu", "Peiqi", "Black"]
# res1 = a >= 4 and b < 9
# res2 = a >= 4 or b >= 9    # 多个条件一起判断时，用and或者or来连接不同条件
# res3 = 168 in aList
# res4 = "Roy" not in aList  # in和not in用来判断某数字或字符串是否在某集合里（列表、元组等）
#
# 3.条件判断句式
#
# 句式1：(if..else..) ———— 若只有if条件判断为True有输出，则可以不需要else。
# age = int(input("请输入年龄： "))
# if age >= 18:                 # if右边写判断语句，如果为True(或者not False)，则执行下一行的print。注意加冒号“：”
#     print("请购买全价票")      # 执行的命令前需要tab缩进
# else:                         # 不满足if后面的判断语句的，执行else下的命令。注意加冒号“：”
#     print("可购买半价票")      # 执行的命令前需要tab缩进
#
# 句式2：(if..elif..else..) ———— if和else的条件只能有一个，而elif的条件可以有零到无穷多个。
# age = int(input("请输入年龄："))
# if age <= 4:                  # 第一步：判断if后面的条件；
#     print("可免费进入")
# elif age <= 12:               # 不满足if的条件，则进入第二步，判断elif(表示else if)后面的条件；
#     print("可购买半价票")
# elif age <= 60:               # elif的条件可以有很多个，逐一判断；
#     print("请购买全价票")
# else:                         # 所有elif的条件均不满足，则进入第三步，直接输出else下的命令。
#     print("可免费进入")
#
# 【例题 1】 交换x和y变量存储的值
# x = "aaa"
# y = 89
# temp = y       # 利用临时容器temp，作为交换的媒介，完成x和y的交换
# y = x
# x = temp       # 可以三行代码简化为一行，使用 x, y = y, x。无需临时容器temp。
#
# 【例题 2】 用户输入三个整数，把三个整数从小到大排列
# 本题可以用sort方法实现，也可用if语句实现
#
# 方法1：（sort方法）
# aList = []
# aList.append(int(input("请输入第一个整数：")))
# aList.append(int(input("请输入第二个整数：")))
# aList.append(int(input("请输入第三个整数：")))
# aList.sort()
# print(aList)
#
# 方法2：（通过if语句实现）
# a = int(input("请输入第1个整数："))
# b = int(input("请输入第2个整数："))
# c = int(input("请输入第3个整数："))
# if a > b:                # 我们预期[a, b, c]，a < b < c，则从左到右开始判断
#     a, b = b, a          # step1判断：若a变量存储的值比b变量存储的值大，则交换a和b存的值；
# if b > c:
#     b, c = c, b          # step2判断：若b存的值比c存的值大，则交换b和c的值，确保c存的值最大；
# if a > b:
#     a, b = b, a          # step3判断：再从左边开始，如果a变量存储的值比b大，则交换a和b的值，确保a存的值最小。
# print([a, b, c])
#
# 【例题 3】 根据用户输入的三条边的边长，判断能否组成三角形
# l1 = float(input("请输入第一条边长："))
# l2 = float(input("请输入第二条边长："))
# l3 = float(input("请输入第三条边长："))
# if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
#     print("这三条边可以组成三角形")
# else:
#     print("无法组成三角形")
#
# 【例题 4】 猜数字游戏，随机生成1-20的整数，让用户猜，直到猜对为止。
# import random
# tar = random.randint(1, 20)              # 注意：random.randint()是左右闭区间，range()是左闭右开区间
# print("猜猜我心里想的数字是多少（1-20）")
# for i in range(0, 20):                   # 循环语句的作用是让猜测的动作重复执行，range(0, 20)表示可以猜20次，i没有实际意义
#     guess = int(input("请输入："))        # 注意这里的输入要放在for循环内部，保证用户可以重复输入，程序重复判断
#     if guess > tar:
#         print("太大了，继续呀")
#     elif guess < tar:
#         print("小了，继续呀")
#     else:
#         print("恭喜你，猜对了！！！")
#         break                            # 这里的break用于终止循环体，随后执行循环外的代码。break终止一般放在else后面。
# print("游戏结束")
#
# 六、字典
#
# 1.概念
# stu1 = {"t_name": "leo", "age": 18, "gender": "男"}
# stu2 = {"t_name": "leo",
#         "age": 18,
#         "gender": "男"}      # 与列表一样，字典也是允许分割多行进行定义的。
#
# 字典是若干 {"key": "value"}（键值对）的集合，键值对之间以逗号隔开；
# 列表适合存储同一种类的数据，比如“全体学生的name或者age”，但是字典适用于保存“某个学生的各种信息”；
# key相当于列表里的“索引位”，列表里的索引位是自动生成的，从0号位开始的数字，而字典里的key是自己定义的，可以是字符串、数字或布尔类型；
# value可以是任意类型的数据，比如字符串类型、数字类型、列表等等；
# 列表 —— 数据在内存里的存储位置是连续的，列表创建好之后索引位是有序的；
# 字典 —— 键值对在内存里的储存依照特定规则，没有先后顺序，相对无序。
#
#  2.字典的定位/修改、增加、删除 （重要定位命令：stu1[]）
# print(stu1["t_name"])        # stu1["t_name"]用于定位字典里的数据,用法与列表里的 aList[索引位]相同；
# stu1["t_name"] = "jack"      # 用于修改某个key对应的value；
# stu1["rank"] = 3           # 用于在字典里插入一对新的{"key": "value"}，相当于列表操作里的aList.append(xxx)；
# del(stu1["age"])           # 依据key的定位，删除某个键值对。相当于列表操作里的del(aList[1])，也是依照索引号定位。
# 因为字典的存储是无序的，所以无需数据插入功能。
#
#  3.字典和列表的嵌套使用
# 例1 学生名录（列表里嵌套字典）
# stu1 = {"t_name": "leo", "age": 18, "gender": "male"}
# stu2 = {"t_name": "michael", "age": 19, "gender": "male"}
# stu3 = {"t_name": "lucy", "age": 20, "gender": "female"}
# stu4 = {"t_name": "rose", "age": 15, "gender": "female"}
# students = [stu1, stu2, stu3, stu4]
# print(students[2]["t_name"], students[2]["gender"])         # 可以通过students[][]的形式访问嵌套列表里的具体信息
# 例2 某个学生详细信息
# stuX = {"t_name": "leo", "age": 18, "gender": "male", "hobby": ["篮球", "足球", "游泳"]}
#
#  4.判断字典是否相等
# stu1 = {"t_name": "leo", "age": 18, "gender": "male"}
# stu2 = {"gender": "male", "t_name": "leo", "age": 18}
# print(stu1 == stu2)                     # 结果是True，因为字典里存储的数据是无序的，没有先后之分
#
# aList1 = ["leo", "neo", "roy"]
# aList2 = ["neo", "roy", "leo"]
# print(aList1 == aList2)                 # 结果是False，因为列表里存储的数据是有序的，调换顺序即视为不相等
#
#  5.字典的遍历 （先取出键、值、对，再遍历）
#
# 思路是先用.keys() / .values() / .items()取出键、值、对，形成集合，对其遍历，或者转化成列表再遍历
# stu1 = {"t_name": "leo", "age": "18", "gender": "男"}
#
# # 方法1（一般不用）：
# for i in stu1:                        # stu1后面不带key/values/items，则默认输出key
#     print(i)
#
# # 方法2：
# for t in stu1.keys():                 # stu1.keys()提取字典里所有的key，形成key集合（并不是列表形式）。再遍历key集合，输出。
#     print(t)                          # 若使用stu1.values()，则提取字典里所有的value，形成value集合
#
# # 方法3 —— 遍历键：
# keys1 = list(stu1.keys())             # stu1.keys()提取keys形成集合，再转化为列表keys1
# for x in keys1:                       # 再对列表keys1进行列表的各种遍历操作
#     print(x)
#
# # 方法3 —— 遍历键值对：
# kvs = list(stu1.items())              # stu1.items()提取键值对形成集合，再转化为列表kvs
# print(kvs)                            # kvs = [('t_name', 'leo'), ('age', '18'), ('gender', '男')]
# for q in kvs:                         # 注意列表kvs里的每一个元素q都是元组（key: value）
#     print(q[0], q[1])                 # q[]用来在元组里定位
#
# # 方法4 —— 键、值、对均可遍历（定义两个临时变量）：
# for k, v in list(stu1.items()):       # 可以同时定义两个临时变量k和v，k代表key，v代表value。注：可以不需要先list()转化成列表。
#     print(k)                          # 仅输出keys
#     print(v)                          # 仅输出values
#     print(k, v)                       # 输出keys - values
#
#  6.判断键和值是否属于某个字典
# stu1 = {"t_name": "leo", "age": "18", "gender": "男"}
# res1 = "address" in stu1                # 默认判断xxx是否是stu1字典的key
# res2 = "t_name" in stu1.keys()            # 判断xxx是否是stu1字典的key
# res3 = "hobby" not in stu1.keys()
# res4 = 19 in stu1.values()              # 判断xxx是否是stu1字典的value
#
#  7.设置键的默认值 —— 作用是防止查找不存在的key时导致报错，可以手动先设置默认值
# stu1 = {"t_name": "leo", "age": 18, "gender": "男"}
#
# # 弱修改（设置key的默认value） —— 相较强修改的优势：若要查找的key存在，弱修改并不影响原value。
# stu1.setdefault("t_name", "jack")           # .setdefault()方法是为key设置默认值，如果key存在于字典里，则不修改value。
# print(stu1["t_name"])                       # 如果key不存在，则创建该key及对应value。
#
# # 强修改
# stu1["t_name"] = "jack"                     # stu1[]是直接修改key的对应value。
# print(stu1["t_name"])                       # 如果key不存在，则创建该key及对应value。
#
# 【本节例题】
# aDict = {}
# aDict["t_name"] = input("please type in your t_name:")
# aDict["age"] = input("please type in your age:")
# aDict["gender"] = input("please type in your gender:")
# aDict["hobby"] = input("please type in your hobby:")
# print("Your info:", aDict)
#
# 七、while循环（while包含 “判断 + 循环” 的功能）以及循环的嵌套
#
# 1.基本概念
#
# （1）while的基本句式
# while True:                         # while后面跟的是判断的条件语句，默认无限循环
#     print("xxx")                    # 缩进里的是循环体
#
# （2）while与if条件判断的区别
# while包含 “判断 + 循环” 的功能，每一次的循环结束之后，都要判断while带的条件语句是否为True，只有当判断为False时才停止循环。
# if则只判断一次，自身不带循环功能。需要结合for..range..才能实现循环，可以直接限定循环次数。
#
# 【例 1】 依次输出数字 0 —— 10
#
# #方法1 while循环法：
# i = 1                               # 本行不属于while的条件判断或者循环体，对于 i 变量赋值为 1 是一次性的；
# while i < 11:                       # 本行属于while的条件判断语句，当i<11时进入while的循环体。也可写作i<=10，但要耗费电脑更多的计算资源；
#     print(i)
#     i += 1                          # 本句是 i = i + 1 的简写。每一次循环都要为 i 变量重新赋值，依次加 1。
#
# #方法2 for..range..循环法：
# for i in range(0, 11):
#     if True:                        # 本句 “if True：”可以省略
#         print(i)
#
# （3）while与for..range..循环的区别
#
# while语句自带条件判断，不可直接限定循环次数，只要条件为True，就会无限循环。条件为False时终止循环。
# for..range.. 语句本身不带条件判断，需与if结合才能实现判断。可限定循环次数比如range（0,15），提前终止循环需人工添加break。
#
# 【例 2】 猜数字游戏，随机生成1-20的整数，让用户猜，直到猜对为止。
#
# #方法1 while循环法：
# import random
# num = random.randint(1, 20)
# guess = int(input("guess a number:"))                  # 注意：while方法下第一次让用户输入数字是在while判断语句之前
# while guess != num:                                    # while在这里的作用包括 “判断 + 循环”
#     if guess < num:
#         guess = int(input("too small, try again:"))
#     elif guess > num:
#         guess = int(input("too big, try again:"))
# print("right!!!!")
#
# #方法2 for..range..循环法：
# import random
# tar = random.randint(1, 20)
# print("猜猜我心里想的数字是多少（1-20）")
# for i in range(0, 15):                                # for..range..在这里的作用仅仅是让计算机循环执行后面的语句
#     guess = int(input("请输入："))                     # 注意：for..range..方法下第一次让用户输入数字是在for..range..之后
#     if guess > tar:
#         print("太大了，继续呀")
#     elif guess < tar:
#         print("小了，继续呀")
#     else:
#         print("恭喜你，猜对了！！！")
#         break
# print("游戏结束")
#
# 【例 3】 求1-100的累计和。
#
# #方法1 while循环法：
# total = 0                      # 先设置个“容器”total，来存放累加求和的值；
# i = 1                          # 初始化变量 i = 1；
# while i < 101:
#     total += i                 # 再用while循环，将1到100的数字放入“容器”里累加；
#     i += 1                     # 注意：切记每次循环的结尾为变量 i 重新赋值，每次赋值加 1；
# print(total)                   # 当i >= 101时，结束循环，输出total的结果。
#
# #方法2 for..range..循环法：
# total = 0                      # 同while法一样，先设置个“容器”total，来存放累加求和的值；
# for i in range(1, 101):
#     total += i                 # 再用for..range..循环，将1到100的数字放入“容器”里累加。
# print(total)
#
# #方法3 非循环法：
# print(sum(range(1, 101)))      # 利用range(1, 101)生成数列（默认是list)之后，直接用sum()相加。注意：sum()的参数必须是list。
#
# 2. while循环终止的三种方法（利用while实现有限循环功能）
#
# 方法1： 直接根据while的判断语句，判断为False的时候，即终止循环。一般要注意先初始化临时变量i = 1或0，有时候循环结束时要写 i += 1。
# 方法2： 在while语句之前插入flag（标志位），令while的判断语句为flag，根据循环体中的if xxx: flag = False，来终止循环。
# 方法3： 令while的判断语句为True，根据循环体中的if xxx: break，来终止循环。
#
# 【例】 让用户一直输入数字，直到输入 0 ，终止循环并输出累计和。
# 方法1：
# total = 0
# i = 1                           # 一般都要先设i = 1，仅仅为了初始化，使while循环顺利开始。
# while i != 0:
#     i = int(input("Type in a number: "))
#     total += i
# print(total)                    # 当i == 0时，结束循环，输出total的结果。
#
# 方法2：
# total = 0
# i = 1
# flag = True                     # 在while之前插入flag标志位，并初始化为True，使while循环顺利开始。
# while flag:
#     i = int(input("Type in a number: "))
#     total += i
#     if i == 0:
#         flag = False            # 若i == 0，则flag = False，while识别到False，结束循环。
# print(total)
#
# 方法3：
# total = 0
# while True:
#     i = int(input("Type in a number: "))
#     total += i
#     if i == 0:
#         break                  # 若i == 0，则直接break结束循环。
# print(total)
#
# 3.循环功能模板总结（while及for..range..)
#
# （1）while 无限循环
# while True:
#     xxx语句 (循环体)
#
# （2）while 有限循环
# 利用上节提到的while循环终止的三种方法。
# 其中最经典的方法：
# i = 1                         # 准备遍历 i 之前先初始化 = 1；
# while i < 某整数：            # 这里为循环的次数设置的封顶（小于某整数）；
#     xxx语句 (循环体)
#     i += 1                   # 循环体的结尾记得加上这句，让i累进，使while循环正常进行。
#
# （3）for..range.. 有限循环
# for i in range(0, 某整数):
#     xxx语句 (循环体)
#
# 4.while循环的运用 —— 遍历列表和字典
#
# （1）遍历列表的元素
# aList = ["Lihua", "Rain", "Jack", "Xiuxiu", "Peiqi", "Black"]
# # 方法1：（直接遍历列表的元素）
# for t in aList:
#     print(t)
# # 方法2：（利用索引位来遍历列表的元素 —— 基于for..range..循环）
# for i in range(0, len(aList)):
#     print(aList[i])
# # 方法3：（利用索引位来遍历列表的元素 —— 基于while循环）
# i = 0                        # 以i = 0进行初始化
# while i < len(aList):        # 表示while i = 0, 1, 2..., [len(aList)-1]，相当于 for i in range(0, len(aList))
#     print(aList[i])
#     i += 1
#
# （2）遍历字典的键值对
# stu1 = {"t_name": "leo", "age": 18, "gender": "男"}
# # 方法1：（同时提取键值对，转化成含键值对元组的list，再用双临时变量遍历列表的（key, value）元素）
# for k, v in list(stu1.items()):
#     print(k, v)
#
# # 方法2：（先将字典的keys提取出来形成list，再用索引位遍历list里的key，最后根据key得到相应的value）
# keyList = list(stu1.keys())
# i = 0                        # 以i = 0进行初始化
# while i < len(keyList):
#     k = keyList[i]           # 用索引位遍历list，得到所有的key
#     v = stu1[k]              # 再用key找到对应的value（字典里的key相当于列表里的索引位）
#     print(k, v)
#     i += 1
#
# （3）遍历且转移列表的元素
# aList = ["Lihua", "Rain", "Jack", "Xiuxiu", "Peiqi", "Black"]
# newList = []
# while aList:                     # aList为非空列表时，判断为True；aList为空时，判断为False。这里也可用while len(aList) != 0
#     newList.append(aList.pop())  # 用pop()来依次弹出aList中的元素，并用append()依次添加到newList当中。
# newList.reverse()                # reverse()，用来对列表进行镜像翻转，使得newList的元素次序与aList相同。
# print(newList)
#
# （4）遍历且删除列表中的元素
# bList = ["Lihua", "Rain", "Jack", "Lihua", "Peiqi", "Lihua"]
# while "Lihua" in bList:
#     bList.remove("Lihua")
# print(bList)
#
# （5）循环添加字典数据
# d = {}
# while True:
#     k = input("请输入键值对的键：")
#     v = input("请输入键值对的值：")
#     d[k] = v                                      # 此行为新添加的key赋予相应的value
#     if input("是否继续添加（yes/no）：") == "no":
#         break
# print(d)
#
# 5.循环的嵌套
#
# 【例题1】 输出六行，每行是连在一起的二十个“ * ”星号。
# for t in range(1, 7):
#     for i in range(1, 21):
#         print("*", end="")
#     print()
#
# 【例题2】 输出九九乘法表
# for b in range(1, 10):                        # 先设置乘法的格式为 a * b，每一行b由1到9依次递增
#     for a in range(1, b + 1):                 # 每一行a均从1开始取值遍历，但是a始终不大于b，取值范围为[1, b]
#         print(a, "*", b, "=", a*b, end="  ")  # end=" "使得每次输出结束不换行
#     print()                                   # for循环之外的print()使得每一行的输出结束之后换行
#
# 【例题3】让用户输入一个整数，判断是不是质数。（注意：0和1不是质数）
# (1) 法1：需要用户输入，之后判断
# while True:
#     num = int(input("请输入一个整数："))
#     tCount = []                             # 先设置一个空列表存储能使得 num 被整除的 i
#     for i in range(1, num + 1):             # 遍历[1, num]区间内的数字
#         if num % i == 0:                    # 如果出现数字i使得num被整除，则将i存入tCount列表里
#             tCount.append(i)
#     if len(tCount) == 2:                    # 接下来判断tCount列表里一共有多少个元素，如果只有1和num本身，则num为质数
#         print(num, "是质数。")
#     else:                                   # 如果tCount列表的元素少于两个，说明是0或者1的情况；如果大于两个，说明不是质数
#         print(num, "不是质数。")
#
# (2) 法2：直接取出取值范围内的质数
# for num in range(0, 21):
#     tCount = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             tCount.append(i)
#     print(num, "的约数为:", tCount, "因此,", end="")
#     if len(tCount) == 2:
#         print(num, "是质数")
#     else:
#         print(num, "不是质数")
#
# (3) 法3： 定义一个标记再做判断（缺点是无法排除0和1）
# while True:
#     num = int(input("请输入一个大于1的整数: "))
#     isPrime = True                        # 先定义一个标记，默认为True
#     for i in range(2, num):
#         if num % i == 0:                  # 判断num是否能被[2, num-1]区间内的数字整除
#             isPrime = False               # 只要有一个i使得num可以被整除，说明num不是质数，将标记修改为False，再break
#             break
#     if isPrime:                           # 这里的if isPrime相当于if isPrime == True
#         print(num, "是质数。")
#     else:
#         print(num, "不是质数。")
#
# 【例题4】让用户输入一个三位数，打印输出个位、十位、百位分别是什么
# 法1：求余数及取整的方法
# num = int(input("请输入一个三位数："))
# print("个位是：", num % 10)
# print("十位是：", (num // 10) % 10)         # 这里的整除 “//” 也可以用int()取整来代替，“//” 是向下取整。
# print("百位是：", num // 100)               # int()其实是向零取整，在结果为负数时与“//”不同。int(-0.6/2)=0，-0.6//2=-1.0
#
# 法2：字符串切片（slice）方法
# num = input("请输入一个三位数：")
# print("个位是：", num[2])
# print("十位是：", num[1])
# print("百位是：", num[0])
#
# 【例题5】打印出所有的水仙花数，水仙花数是指某个三位数，其个位、十位、百位数字的立方和等于这个数本身。
# 法1：求余数及取整的方法
# for num in range(100, 1000):
#     if (num % 10)**3 + ((num // 10) % 10)**3 + (num // 100)**3 == num:
#         print(num, "是水仙花数")
#
# 法2：字符串切片（slice）方法（转换成字符串切片，再转换为数字类型计算）
# for num in range(100, 1000):
#     n = str(num)
#     if (int(n[0]))**3 + (int(n[1]))**3 + (int(n[2]))**3 == num:
#         print(num, "是水仙花数")
#
# 【例题6】求任意数的阶乘
# num = int(input("请输入一个要求阶乘的数字："))
# factorial = 1
# if num < 0:
#     print("抱歉，负数没有阶乘。")
# elif num == 0:
#     print("零的阶乘为1。")
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print(num, "的阶乘为：", factorial)
#
# 【例题7】求阶乘的和 1！+2！+3！+... 20！
# total = 0                                   # 先设置total存放阶乘的和，初始化为0
# for num in range(1, 21):                    # 遍历[1,20]，表示分别要求1、2、3、4...20的阶乘
#     factorial = 1                           # 从这里开始的三行代码，表示求某个数的阶乘
#     for i in range(1, num+1):
#         factorial *= i
#     total += factorial                      # 每求完一个数的阶乘，就存放在total里面
# print(total)
#
# 八、函数 —— 注意 ：def func(a, b) 可以看成是一种特殊的input()
#
# 1.基本概念
# def func():                              # def后面是自己定义的函数名加上()，注意加上冒号":"
#     print("function test")               # 缩进里面表示的是函数体
#
# 2.函数的参数（形参、实参）、返回值和None ——— 以自定义的add(a, b)函数为例
# （1）定义函数：
# def add(a, b):                           # 定义的a和b是【parameter形参】，指函数定义时的参数
#     res = a + b
#     print(res)
#     return res                           # 若无return，add(a, b)就是空值None，无法对add(a, b)进行其他操作
#
# （2）函数调用（执行）：
# add(8, 9)                                # 输入的8和9是【argument实参】，指函数使用时实际输入的参数
# print(add(8, 9))
#
# （3）print和return存在的四种输出情况：
# 函数体中只有print(res)，add(8, 9)将直接输出17，而print(add(8, 9))先输出17，再输出空值None
# 函数体中只有return res，add(8, 9)将无任何输出，而print(add(8, 9))的输出为17
# 函数体中print(res)与return res皆有，add(8, 9)将直接输出17，而print(add(8, 9))先输出17，再输出17
# 函数体中print(res)与return res皆无，add(8, 9)将无任何输出，而print(add(8, 9))的输出为空值None
#
# （4）总结
# 如果没有设定return，函数add(a, b)本身是空值None，无法对add(a, b)进行直接操作，调用函数时print(add(a, b))一定会出现None。
#
# （5）也可以return布尔值（True或者False）
# def is_negative_1(i):
#     if i < 0:
#         return True
#     else:
#         return False
#
# def is_negative_2(i):
#     return i < 0
#
# 函数is_negative_1和is_negative_2是【等价】的，一般用is_negative_2的写法

# 【例题】构建求阶乘的函数fact()
# def fact(num):                     # 若是用input()来接收，这里就是num = int(input("请输入一个要求阶乘的数字："))
#     factorial = 1
#     if int(num) < 0:
#         return "抱歉，负数没有阶乘。"
#     elif int(num) == 0:
#         return "零的阶乘为1。"
#     else:
#         for i in range(1, int(num) + 1):
#             factorial = factorial * i
#         return "%d的阶乘为：%d" % (num, factorial)
#         # 这里是格式化形式，可用于print函数、return等，%d代表整数，%s代表字符串。
#         # 这里的return如果不用格式化形式，而是num, "的阶乘为：", factorial，输出结果会有隔断和括号。
#
# 3.位置参数【实参】、关键字参数【实参】、默认参数【形参】
# (1) 位置参数（positional argument）【实参】
# def add(a, b):
#     res = a + b
#     return res
#
# print(add(2, 3))           # 当函数调用时严格按照a, b的顺序来输入，这里的a和b就是位置参数。
#
# (2) 关键字参数（keyword argument）【实参】
# def add(a, b, c):
#     res = a + b + c
#     return res
#
# print(add(2, c=2, b=3))
# 当函数调用时直接给参数赋值输入，此处c=2和b=3就是关键字参数，顺序可以打乱。注意：关键字参数必须在位置参数之后。
#
# (3) 默认参数（default parameter）【形参】—— 定义默认参数要牢记一点：默认参数必须指向不变对象！
# def add(a, b=8, c=10):     # 这里b和c就是默认参数（以关键字参数形式定义）。注意：定义时，关键字参数必须放在位置参数之后。
#     res = a + b + c
#     return res
#
# print(add(2))              # 函数调用时候只需填位置参数的值即可，默认b=8，c=10
# print(add(2, 3))           # 若要修改默认值，只需在相应位置填入更新的值即可。此处只修改了b的值，c依然是默认值
# print(add(2, c=11, b=3))   # 以关键字参数形式，修改默认参数值，顺序可打乱。注意：调用时，关键字参数也必须放在位置参数之后。
# print(add(2, c=11))        # 可依照实际需要，只修改其中某个参数的默认值
#
# 4.可变参数（*参数名 和 **参数名）
# Python参数传递语法是 *参数名 和 **参数名 (通常写作*args和**kwargs)，用在函数定义的时候，允许定义的函数接受任意数目的参数。
#
# (1) * 参数名 ——　将【任意数据形式】的实参打包成【元组】供函数使用
# def func(*args):
#     print(args)                               # 输入的实参将被打包成元组，这里的【args是个元组】
#     for i in args:                            # 遍历args元组
#         print(i)
#
# func(1)                                       # 若*args只有一个输入的实参，则args元组只有一个元素，输出时会强制加上逗号“,”，与带括号的数字区分。
# func(1, 3, [34, "abc"], {"t_name": "leo"})      # 输入的实参可以是任意个数（可不输入）、任意数据形式。
#
# (2) ** 参数名　——　将【关键字参数形式】的实参打包成【字典】供函数使用
# def func(**kwargs):
#     print(kwargs)                             # 输入的实参将被打包成字典，这里的【kwargs是个字典】
#     for i in kwargs.items():                  # 遍历kwargs字典
#         print(i)
#
# func(t_name="leo", age=18)                      # 输入的实参可以是任意个数（可不输入），但必须是关键字参数形式。
#
# (3)位置参数、*参数、**参数的混用
# def func(a, *nums, **stu1):                   # 在函数定义时，合法顺序为位置参数，*参数，**参数。
#     print(a, nums, stu1)
#
# func(99, 88, 65, t_name="Leo", age=18)          # 在函数调用时也必须是合法顺序。
#
# 5.局部变量和全局变量 —— 注意：不是函数的参数
#
# (1) 基本概念、变量同名情况
# 全局变量global variable（公用）: 定义在函数之外的变量，在全局均有效 —— 可以在函数内部调用！
# 局部变量local variable（私有）: 定义在某函数体内部的变量，该变量仅在该函数内部（局部作用域）有效，在函数外部该变量不存在。
#
# t_name = "Jacky"          # 函数之外，定义全局变量name，可以在函数内部调用！
#
# def func1():
#     t_name = "Leo"        # 同名情况：func1内部自己定义了局部变量name，为func1私有，不影响全局name，也不会被其他函数调用。
#     print(t_name)
#
# def func2():
#     print(t_name)         # func2内部未定义局部变量name，但可调用全局变量name = "Jacky"。
#
# func1()                 # 输出 Leo
# func2()                 # 输出 Jacky
# print(t_name)             # 输出 Jacky
#
# (2) 在函数内部修改全局变量
# t_name = "Jacky"
#
# def func3():
#     global t_name         # 通过global t_name，在函数内部修改全局变量name。global出现之后，之后函数体里的name均为全局变量name。
#     t_name = "Mike"       # 因为有global语句，本行代码不再是添加局部变量name，而是修改全局变量name。
#     print(t_name)         # 因为有global语句，本行代码不再是调用局部变量name，而是调用全局变量name。
#
# func3()                 # 输出 Mike
# print(t_name)             # 输出 Mike
#
# (3) 全局变量并不会影响函数定义时的参数
# b = 7
# c = 5
#
# def add(a, b, c):       # 虽然函数的参数 b, c 与全局变量的 b, c 同名，但是并不会被影响，不会被赋予默认值。
#     return a + b + c
#
# print(add(1))           # 这里将报错 add() missing 2 required positional arguments: 'b' and 'c'
#
# 6.递归(recursion) —— 注意：与迭代(iteration)不同
#
# 循环(loop)是最基础的概念，所有重复的行为都是循环，包括递归(recursion)与迭代(iteration)
#
# （1）递归的基本概念
# 递归的定义：程序调用自身的编程思想称为递归，是函数自己调用自己。
# 递归的作用：它通常把一个大型的复杂的问题，转化为一个与原问题相似的规模较小的问题来解决，可以极大的减少代码量。
#
# （2）构成递归需具备的条件
# 首先是：子问题须与原始问题为同样的事，且更为简单；
# 其次是：不能无限制地调用本身，须有个明确的递归结束条件（递归出口），化简为非递归状况处理。
#
# （3）递归的执行：分解 + 回溯
# 第一步（分解）:把复杂的问题的求解推到比原问题简单一些的问题的求解。
# 第二步（回溯）:当获得最简单的情况（递归出口）后，逐步返回，依次得到复杂的解。
# 总结：逐层深入分解问题，找到最简单的情况之后，再从最简单的值开始逐层返回、累进计算。
#
# （4）迭代(iteration)
# 迭代的定义：是利用已知的变量值，根据指定规则不断演进得到变量新值的编程思想（如：total = total + i）。
# 迭代的例子：
# while 配合 i = i + 1          for..range.. 配合 total = total + i
# i = 0                         total = 0
# while i < 10:                 for i in range(1, 11):
#     i = i + 1                     total = total + i
#
# （5）总结
# 能用迭代(iteration)的就不用递归(recursion)，递归调用函数，浪费空间，并且递归太深容易造成堆栈的溢出.
#
# 【例题】计算 1 + 2 + 3 + 4 + ... + n
#
# 法1：迭代法（for..range..）
# num = int(input("请输入一个整数："))
# total = 0
# for i in range(1, num+1):
#     total = total + i
# print(total)
#
# 法2：sum(range())法
# num = int(input("请输入一个整数："))
# print(sum(range(1, num+1)))
#
# 法3：递归法（先分解，找到递归出口之后，再回溯）
#
# 由 F(n)   = 1 + 2 + 3 + 4 + ... + (n-1) + n
#    F(n-1) = 1 + 2 + 3 + 4 + ... + (n-1)
# 可得 F(n) = F(n-1) + n
#
# 例: F(5) = F(4) + 5                                                      F(5) = 10 + 5 = 15
#            F(4) = F(3) + 4                                       F(4) = 6 + 4 = 10
#                   F(3) = F(2) + 3                        F(3) = 3 + 3 = 6
#                          F(2) = F(1) + 2         F(2) = 1 + 2 = 3
#                                 F(1) = 1 (递归出口)
#
# def func(num):
#     if num == 1:                # num == 1，return 1 是递归出口func(1) = 1，必须放在递归分解公式之前，防止函数无限调用自身。
#         return 1                # 在分解到递归出口func(1) = 1时，就不再分解，开始回溯计算。
#     return func(num-1) + num    # return 使得递归分解公式成型：func(num) = func(num-1) + num
# #
# print(func(100))
#
# 【函数练习 1】定义city_nation()函数，实现输出"London,UK"的效果
# def city_nation(city, nation):
#     return "\"" + city + "," + nation + "\""  # 注意：return与print用法不同，组合输出不能用 “,”，要用“+”，但两边类型须相同
#     return "\"%s, %s\"" % (city, nation)      # 注意：return与print均可用格式化输出的形式，用在return里更方便
#
# print(city_nation("Fuzhou", "China"))
# print(city_nation("Bristol", "UK"))
#
# 【函数练习 2】定义make_album()函数，输出字典（含歌手、专辑、歌曲数）。歌曲数作为可选参数添加。
#  法1 ：利用*args可变参数 —— 注意：输出时是元组，只有一个元素时，会有逗号的问题！
# def make_album(singer, album, *num):                 # 利用*num实现可选参数
#     dic = {"歌手": singer, "专辑": album}
#     if num:
#         dic["歌曲数"] = num
#     return dic
#
# print(make_album("Adele", "Someone Like You", 11))   # 注意：当元组中只有一个元素，会自动加上逗号，与带括号的数字区分
# print(make_album("周杰伦", "七里香"))
#
#  法2 ：利用默认参数，也可以实现可选
# def make_album(singer, album, num=0):                # 利用num=0实现可选参数
#     dic = {"歌手": singer, "专辑": album}
#     if num != 0:
#         dic["歌曲数"] = num
#     return dic
#
# print(make_album("Adele", "Someone Like You", 11))   # 用实参11来修改num的默认值，使得num=11，此时输出不再有元组的逗号问题
# print(make_album("周杰伦", "七里香"))
#
# 【函数练习 3】定义函数，判断输入的对象（字符串、列表、元组）的某个字符或者某个元素是否为空内容（无内容"",空格" ",制表符"    ",换行符等）
# 本题假设列表、元组里的元素均为字符串。
# def each_factor(temp):
#     for i in temp:              # 这里用循环对temp的每个字符或者元素进行处理。
#         if i.strip() == "":     # strip()默认去除【字符串】【头尾】所有的空格或换行符，并生成新的字符串。若某个字符或者元素为空内容，strip()必定生成无内容""
#             print("存在null")
#             break
#
# each_factor("wo nd rf ul")
# each_factor(["3d", "", "Leo"])
#
# 【函数练习 4】定义函数，判断输入字典的value是否长度大于2，如果大于2，截取前两个，更新原输入字典。
# 本题假设字典的value均为字符串或者列表
# def check_value_len(d):
#     for k, v in d.items():              # 注意：同时遍历字典的key和value时，in后面必须是dict.items()
#         if len(v) > 2:
#             d[k] = v[:2]
#     return d
#
# stu1 = {"t_name": "Leo", "hobby": "basketball", "address": "Deans Court", "birthday": "19910301"}
# print(check_value_len(stu1))
#
# 【函数练习 5】写函数，利用递归获取斐波那契数列（Fibonacci sequence）中的第十个数，并将该值返回给调用者。
# 斐波那契数列定义式：F[n] = F[n-1] + F[n-2] (n>=3, F[1]=1, F[2]=1)，从第三项开始，每一项都等于前两项之和。
# 斐波那契数列：1 1 2 3 5 8 13 21 34 55 ...
# def func(num):
#     if num == 1 or num == 2:              # 注意：这里不能是if num == 1 or 2，表示or或者and判断时，两边都要写完整的表达式
#         return 1
#     return func(num - 1) + func(num - 2)
#
# print(func(10))
#
# 九、模块
#
# 1. 创建并导入模块
# 模块可以是自定义的一个.py格式文件，里面包含自己的代码。调用自定义模块时，需要和发起调用的文件处于同一路径。
# 创建模块名（.py文件名）时必须要小写
# import functest                                    # 导入了同一路径底下的functest.py文件
# print(functest.func(2, 77, 88, t_name="ke", age=9))  # 调用functest.py文件里定义的函数func(a, *nums, **stu1)
# print(functest.add(77, 23, 3))                     # 调用add(a, b, c)
#
# 2. 导入模块里的某一个函数（省去调用前缀，且可加快程序运行速度）
# from functest import add                           # 仅导入了functest模块的add函数
# from functest import add, func                     # 导入了functest模块中的add函数及func函数
# print(add(5, 7, 1))                                # 直接导入函数之后，调用可以省去functest.
# print(func(2, 77, 88, t_name="ke", age=9))           # 直接导入函数之后，调用可以省去functest.
#
# 3. 为导入的模块或函数起别名（防止与之前导入的某模块或函数重名而出现运行错误）
# import functest as fc                              # 为functest模块起了别名fc
# print(fc.add(3, 4, 2))
#
# from functest import add as a, func as f           # 为functest模块的add函数起了别名a，为func函数起了别名f
# print(a(3, 2, 1))
# print(f(2, 77, 88, t_name="ke", age=9))
#
# 4. 导入模块里的所有函数（该方法很少用，因为无法确认该模块里的函数名是否与之前的重名）
# from functest import *                             # “ * ” 表示functest模块里的所有函数
# print(add(2, 3, 4))
# print(func(1, 22, 33, t_name="ke", age=9))
#
# 十、类 （class）
#
# 类是创建对象（实例）的模板，各个具体的对象拥有的数据都互相独立，互不影响；
# 类里面可以包含变量和函数，类中定义（封装）的函数称为类的“方法”；
# 使用类可以创建各种各样的对象，因此使用类来编程也叫“面向对象编程”；
# 类及面向对象的详解：https://www.runoob.com/python/python-object.html。
#
# 1.创建类、设置属性默认值、访问类的属性、调用类的方法
#
# 【Step 1】： __init__初始化，定义类包含的属性，为属性绑定对应的形参
#
# 具体步骤：
# （1）用【class 类名（必须首字母大写）:】定义一个类；
# （2）使用__init__(self, 形参1, 形参2...)方法，注意第一个形参必须是self (也可以是其他名称，但按照惯例是self)；
# 这里的形参是为了在创建对象的时候传入实参，从而给具体对象的属性赋值用的。通常，我们认为类应当具有几个什么属性，__init__()里就设定几个形参；
# （3）先定义我们创建的类需要什么属性，记为【self.属性名】；
# （4）再为属性绑定形参，使用【self.属性名 = 形参（属性值）】来绑定，注意：属性名和形参可以是不一样的名字，但一般取名相同。
# 【注意1：属性可以绑定形参、默认值、甚至其他类生成的对象】
# 【注意2：不论是类属性绑定的形参，还是类方法定义的形参，在创建对象和调用方法时，传入的实参可以是其他类生成的对象】
#
# class Dog:
#     def __init__(self, t_name, age):
#         self.t_name = t_name                   # 为属性绑定形参（属性值），左边的name是属性名，右边的name是形参。这里也可以是self.mingzi = t_name
#         self.age = age                     # self.age是属性名，age是属性值。这里也可以是self.nianling = age
#
# 【注意：self.name的name和形参name并不一样，只是我们一般给属性和形参取一样的名字！！】
#  __init__()方法是一种特殊的方法，被称为 “类的构造函数” 或 “初始化方法”，创建类时必须首先使用。
#  self 代表类的实例（对象），self 在定义类的属性及各种方法时是必须有的，虽然在调用时不必传入相应的参数。
#
# 【Step 2】：根据需求定义函数，类中定义的函数称为类的“方法”
#  类的方法与普通的函数只有一个特别的区别 —— 类的方法里必须首先定义一个self参数，才能定义其他需要的形参。
#
#     def sit(self):                         # 为dog类定义一个sit方法
#         print(self.t_name + "坐下来了！")
#
#     def roll(self):                        # 为dog类定义一个roll方法
#         print(self.t_name + "在打滚！")
#
#     def get_name(self):                    # 取得某属性值的方法，一般以get_属性名()来命名。
#         print(self.t_name)                   # 也可以直接用【对象名.属性名】取得属性值，get_属性名()方法不一定需要。
#
# 【Step 3】：根据Step 1 & 2定义的类的模板，创建object（对象），也叫作instance（实例）。
#
#  要点：
# （1）创建对象语句：对象名 = 类名(self, 实参1, 实参2...)
# （2）在创建对象时须传入实参（类定义的时候设置了多少个形参，创建对象时就必须传入多少个对应的实参），注意：self是自动与对象名匹配的，不需要手动传入。
# （3）创建时，程序会自动执行__init__()函数内部定义的语句【这个过程是给对象的属性赋值】：
#  self = 对象名
#  self.属性1 = 实参1
#  self.属性2 = 实参2
#  ...
# 执行完__init__()函数体之后，将类里封装的所有方法与对象绑定，使这些方法能以【对象名.方法名()】的形式被对象调用。
#
# 创建对象的例子：
#
# dog1 = Dog("皮特", 2)        # 创建属于Dog类的对象dog1，程序自动将self定义为dog1，并给dog1的name及age属性赋值：dog1.t_name = "皮特"，dog1.age = 2
# flash = Dog("Flash", 3)      # 创建属于Dog类的对象flash，同时把flash的name属性赋值"Flash"，age属性赋值3
# flash.weight = 20            # 也可以直接为对象添加一个未在类初始化时定义的属性。
#
# 2. 为类的属性定义默认值（两种方法）
#
# 法1：不在__init__()里添加color形参，仅在为属性绑定形参时写上self.fur_color = "白色" ， 表示直接为fur_color属性绑定了固定值"白色" （起到设置默认值的作用）
# 法1 —— 在创建对象的同时不可修改默认值
#
# class Pet:
#     def __init__(self, t_name, age):
#         self.t_name = t_name
#         self.age = age
#         self.fur_color = "白色"             # 定义Pet的fur_color属性，并为其绑定固定值"白色"
#
# dog1 = Pet("乔治", 3)                       # 使用法1，在创建对象时不可直接更改fur_color属性值，因为__init__()未设置fur_color属性对应的形参，Pet() 里无法传入相应的实参
# dog1.fur_color = "黑色"                     # 只能先创建默认"白色"的dog1，再用dog1.fur_color = "黑色"，将dog1更改为"黑色"
# print(dog1.t_name, dog1.age, dog1.fur_color)
#
# 法2：在__init__()里添加color形参="白色"，并且将fur_color属性与color形参绑定
# 法2 —— 在创建对象的同时可直接修改默认值
#
# class Pet:
#     def __init__(self, t_name, age, color="白色"):
#         self.t_name = t_name
#         self.age = age
#         self.fur_color = color              # 定义Pet的fur_color属性，并将其与color形参绑定
#
# dog1 = Pet("乔治", 3, "黑色")               # 使用法2时，在创建对象时可直接更改默认值，传入color形参"黑色" ，覆盖默认color形参"白色" 。
# print(dog1.t_name, dog1.age, dog1.fur_color)
#
# 3. 访问已创建对象的属性、调用设置的方法 ———— 使用【对象名.属性名】来调用，但是一般设置【get_属性名()】方法来调用
#
# print(dog1.t_name)                            # 用【对象名.属性名】访问对象的属性name
# dog1.get_name()                             # 由于定义了访问属性的get_name()方法，因此也可以用它来访问对象的属性name
# dog1.sit()                                  # 用 “dog1.方法名()” 来调用已定义的方法
# flash.roll()
#
# 4. 修改属性的值 —— 可用【对象名.属性名 = xxx】修改属性值，但是一般设置【set_属性名()】方法来修改，方便属性修改的统一管理
#
# class Car:
#     def __init__(self, manuf, typ, year):
#         self.manuf = manuf
#         self.typ = typ
#         self.year = year
#         self.car_mile = 100                  # 为Car类设置car_mile属性，直接为其绑定默认值100。
#
#     def desc(self):
#         print(self.manuf, self.typ, self.year)
#
#     def get_car_mile(self):                  # 一般把提取属性值的参数命名为【get_属性名()】，也可以不用设置方法，直接用【对象名.属性名】提取属性值。
#         print("已行驶%s英里。" % self.car_mile)
#
#     def set_car_mile(self, mileage):         # 一般把修改属性值的参数命名为【set_属性名()】，注意：需要给属性绑定的形参要放在set_属性名()的括号里。
#         if self.car_mile < mileage:          # 这里对car_mile属性的修改做了要求，只有在传入的实参大于已有的属性值时，才允许修改。
#             self.car_mile = mileage          # 【设置set_car_mile(self, mileage)方法，方便属性统一管理】，修改car_mile属性值统一用本方法。
#
#     def add_car_mile(self, mileage):         # 【设置add_car_mile(self, mileage)方法，方便属性统一管理】，增加car_mile属性值统一用本方法。
#         if mileage >= 0:
#             self.car_mile += mileage
#
# car1 = Car("Porsche", "918", 2008)
#
# # 情况1：不受限的修改
# car1.manuf = "Benz"                          # 直接用 “对象名.属性名 = xxx” 来修改属性值
#
# # 情况2：受限制的修改 —— 一般都要设置修改条件，防止属性管理混乱
# car1.set_car_mile(50)                        # 由于set_mileage()方法限定了修改条件if self.mileage < mileage，所以无法下调mileage（设置了默认值100）
# car1.set_car_mile(150)                       # 符合修改条件if self.mileage < mileage，可成功修改
# car1.add_car_mile(30)
# print(car1.car_mile)
#
# 5. 继承 ———— 【子类（derived class）】将继承【父类（base class）】已定义的属性和方法 —— 【super().方法名(填：除了self的参数)】用于继承
#
# 面向对象编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。
# 通过继承创建的新类称为子类或派生类（derived class），被继承的类（base class）称为基类、父类或超类。
# 继承也允许把一个子类的对象作为一个父类对象对待。
#
# 子类继承的步骤：
# 第一步：使用 class 子类名 (父类名): 创建一个继承于父类的子类，子类将自动继承父类封装的方法，子类的对象可直接调用；
# 第二步：使用 def __init__(self, 父类的形参.., 独有的形参, ..): 定义子类的形参（照抄父类的形参，再添加子类独有的形参）；
# 第三步：使用 super().__init__(父类的形参...) 继承父类已定义的属性，完成父类属性与形参绑定、完成父类属性默认值的绑定；
# 第四步：子类独有的属性要记得定义和绑定形参。
# 其他：在子类里可以创建独有的方法，也可以将父类的方法重写
# 注：super的用法【super().方法名(填父类方法定义时，除了self以外的所有形参)】表示将父类某方法所定义的全部语句继承（照搬）到子类。
#
# class Pet:                                     # Pet是父类
#     def __init__(self, t_name, age):
#         self.t_name = t_name
#         self.age = age
#         self.fur_color = "white"               # Pet的fur_color属性，其默认值"white"也会继承给子类，应当用这种方法定义默认值，否则子类继承会有未知问题。
#
#     def sit(self):
#         print("%s岁的%s坐下来了！" % (self.age, self.t_name))
#
#     def roll(self):
#         print(self.t_name + "在打滚！")
#
# class Cat(Pet):                                # class Cat(Pet)表示新的子类Cat将继承父类Pet的属性和已定义的方法。
#     def __init__(self, t_name, age, weight):     # 依然要先使用def __init__(self,...)定义，把父类的形参先照抄一遍，子类属性“weight”定义的形参要记得添加。
#         super().__init__(t_name, age)            # super(). __init__(父类的形参...) 继承父类已定义的属性，继承父类name、age属性与形参绑定、继承父类fur_color属性默认值的绑定。
#         self.weight = weight                   # 子类特有的属性“weight”要记得定义，并为其绑定形参。
#
#     def eat(self):                             # 为子类【添加新方法】——子类私有
#         print(self.t_name + "在吃饭！")
#
#     def roll(self):                            # 在子类里将父类方法【重写】——子类私有
#         print("%s公斤的%s在翻滚！" % (self.weight, self.t_name))
#
# george = Cat("Geo", 23, 88)
# george.roll()
# print(george.fur_color, george.t_name)
#
# 6. 类的组合使用，一个主类调用另一个相关的类 （并不是继承关系）———— 为了代码的整洁和便于管理。
#
# 利用【主类的self.属性名 = 其他类生成的对象】关联绑定！！
#
# （1）在同一个.py文件里调用
#
# class Gun:                                             # 新建一个Gun类，用于设置主类Role中attack()方法的相关属性和方法定义
#     def __init__(self, gun_damage, gun_bullet_count):
#         self.gun_damage = gun_damage                   # 将原来定义在主类Role中的damage和bullet_count属性转移到Gun类中定义为gun_damage和gun_bullet_count，也可以与主类同名
#         self.gun_bullet_count = gun_bullet_count
#
#     def attack(self):                                  # 将原来Role类attack()的方法定义转移到Gun类的attack()方法下
#         self.gun_bullet_count -= 1
#         print("You made a shot! Causes damage of", self.gun_damage)
#         print("Bullet left: ", self.gun_bullet_count)
#
# class Role:                                            # Role作为主类
#     def __init__(self, t_name, level, health, rtype, damage, bullet_count):
#         self.t_name = t_name
#         self.level = level
#         self.health = health
#         self.rtype = rtype
#         self.weapon = Gun(damage, bullet_count)        # 【本语句是联系主类Role与Gun类的关键！！使主类的对象能调用Gun类封装的方法。】
#
# 本语句既设置了一个Role类属性weapon，又创建了Gun类对象（名为self.weapon）。因此可以用【self.weapon.Gun类方法】来调用Gun类封装的方法。
# 比如，当创建Role类的对象player1时，传入实参：damage=200，bullet_count=80，从而由Gun(200, 80)创建名为player1.weapon的Gun类对象。
# 随后，200传递给Gun类的属性gun_damage，80传递给gun_bullet_count，同时自动定义self = player1.weapon。
# 最后，自动为属性赋值，player1.weapon.gun_damage = 200，player1.weapon.gun_bullet_count = 80，player1.weapon对象创建完毕。
#
# 注意1 ：如果本语句不把Gun类对象命名为self.weapon，而是命名为weapon，weapon变量将无法被其他函数取用，为__init__方法的局部变量（私有）。
# 注意2 ：可以在任意函数里创建某个已设定的类的对象。
#
#    def condition(self):
#        print("Name:", self.t_name, "Level:", self.level, "Health:", self.health, "Class:", self.rtype)
#
#    def attack(self):
#        self.weapon.attack()                           # 【本语句其实就是Gun类的self.weapon对象调用Gun类的attack()方法。】
#
# 巧妙的地方：由于我们将self.weapon设置为了Gun类一个对象的名字，由此实现了在Role类的某个对象在调用attack方法时，将自动调用Gun类的attack，实现主类方法定义的整洁。
#
# player1 = Role("Leo", 20, 100, "Vanguard", 260, 266)
# print(player1)               # print的结果是 Role object at 0x0000021237308408，说明player1是Role类的对象
# print(player1.weapon)        # print的结果是 Gun object at 0x000002415BB48748，说明player1.weapon是Gun类的对象
# player1.condition()
# player1.attack()
#
# （2）调用其他.py文件中的类 ———— 与调用其他模块（.py形式文件）相同，须把文件存放在同一个文件夹下
#
# import weapon                                # （1）仅使用import weapon调用，需要在属性设置时用【文件名.类名】调用。
#                                              # （2）若用from weapon import Gun或者Sword，定义属性时无需【文件名.类名】调用。
# class Role:                                  # Role作为主类
#     def __init__(self, t_name, level, health, rtype, damage, bullet_count):
#         self.t_name = t_name
#         self.level = level
#         self.health = health
#         self.rtype = rtype
#         self.gun = weapon.Gun(damage, bullet_count)   # 此处用【文件名 . 类名】来调用Gun类，如果最开始是from weapon import Gun的话，这里就无需【文件名 . 类名】调用。
#         self.sword = weapon.Sword(damage)             # 调用了weapon文件里的另一个类 —— Sword类
#
#     def condition(self):
#         print("Name:", self.t_name, "Level:", self.level, "Health:", self.health, "Class:", self.rtype)
#
#     def gun_attack(self):
#         self.gun.attack()
#
#     def sword_attack(self):
#         self.sword.attack()
#
# player1 = Role("Leo", 20, 100, "Vanguard", "260", 266)
# player1.condition()
# player1.gun_attack()
# player1.sword_attack()
#
# 7. 类变量、对象变量
#
# (1) 类变量、对象变量的定义
#
# 类变量（Class Variable）是共享的（Shared）——可以被基于该类创建的所有对象访问，是该类的所有对象共享的。存在于class的模板内部，但不在class的方法内。
# 对象变量（Object variable），写作【self.变量名】。由类的每一个对象所私有，在不同对象之间不会被共享。但可以被同一个对象的不同方法所调用。
#
# (2) 全局/局部变量、类/对象变量的总结
#
# a、全局变量：在模块内、在所有函数外面、在class外面，这就是全局变量。
# b、局部变量：在函数内、在class的方法（构造、类方法、静态方法、实例方法）内（变量未加self修饰），这就是局部变量
# c、类变量：在class内的，但不在class的方法内的，这就是类变量，又称静态变量
# d、对象变量：在class的方法内的，用self修饰的变量，这就是对象变量，又称实例变量
#
# (3) 类/对象变量的总结
#
# class Robot:
#     population = 0                             # population是一个类变量，用来计数机器人的数量
#     def __init__(self, t_name):
#         self.t_name = t_name                       # 这里的self.name是对象变量
#         print("初始化:{}".format(self.t_name))   # 这里用format 格式化函数，代替原来的 “ % ”写法，相当于"初始化:%s" % self.t_name
#         Robot.population += 1                  # 调用方法【类名.类变量名】
#
# bot1 = Robot("rp-300")                         # 当有对象被创建时，将调用并修改类变量population
# print("当前bot数量:", Robot.population)
# bot2 = Robot("rp-500")
# print("当前bot数量:", Robot.population)
#
# 【类的例题】构造Person类，派生出Student类和Teacher类，并继承父类。（注意继承时，super().方法名()的使用）
# （1）在Student类里设置study()方法，将Teacher类的一个对象作为study()的一个参数。
# （2）设置__str__()方法，改变print(某对象)的输出结果
#
# class Person:
#     def __init__(self, t_name, age, gender):
#         self.t_name = t_name
#         self.age = age
#         self.gender = gender
#
#     def person_info(self):
#         print(self.t_name, self.age, self.gender)
#
# class Student(Person):
#     def __init__(self, t_name, age, gender, college, cls):
#         super().__init__(t_name, age, gender)
#         self.college = college
#         self.cls = cls
#
#     def person_info(self):                  # super的用法：【super().方法名(填：除了self的参数)】表示将父类某方法所包含的内容照继承（照搬）到子类。
#         super().person_info()               # 这里是把原来person_info(self)包含的print(self.t_name, self.age, self.gender)照搬到子类。
#         print(self.college, self.cls)
#
#     def study(self, my_teacher):            # 注意：my_teacher是study()方法的形参，可以把Teacher类的一个对象作为实参传入！
#         print(my_teacher.teach_obj())       # 这里限制了my_teacher的实参必须是Teacher类的一个对象，才能顺利引用Teacher类封装的teach_obj()方法。
#         print(my_teacher.t_name + "，我学会了！")
#
# class Teacher(Person):
#     def __init__(self, t_name, age, gender, college, profess):
#         super().__init__(t_name, age, gender)
#         self.college = college
#         self.profess = profess
#
#     def __str__(self):
#         return "t_name:%s, age:%d, college:%s" % (self.t_name, self.age, self.college)
#
#     # __str__()方法和__init__()方法一样，都是python中的特殊函数，一般来说直接print(对象名)会返回类型和该对象的内存地址，
#     # 而地址信息通常对我们没有什么用，通过__str__()方法可以指定print(对象名)输出任何我们想要的信息。
#
#     def person_info(self):
#         super().person_info()
#         print(self.college, self.profess)
#
#     def teach_obj(self):
#         return self.t_name + "今天教了面向对象程序设计。"
#
# stu1 = Student("Leo", 18, "male", "CS", "class 9")
# stu1.person_info()
# te1 = Teacher("Roy老师", 30, "male", "CS", "Python")
# te1.person_info()
# stu1.study(te1)             # te1对应study(self, my_teacher)方法里的形参my_teacher
# print(te1)                  # 由于设置了__str__()方法，所以这里不再输出tea1对象的内存地址信息
#
# 十一、文件处理和程序异常检查
#
# 1. 利用os模块直接控制win系统的文件和目录
#
# （1）查看和更改当前工作目录（目录就是文件夹） —— 【getcwd()、chdir() 方法】
#
# import os
# print(os.getcwd())                                        # os模块下的getcwd()方法将返回当前的工作目录：cwd表示current working directory。
# os.chdir("C:\\Users\\ASUS\\Desktop")                      # os模块下的chdir()方法将更改工作目录，chdir表示change directory，路径需要用""括起来
# os.chdir("C:/Users/ASUS/Desktop")                         # 注意书写路径的时候一定要用两个 “ \\ ” 防止和转移字符混淆，或者直接用一个反斜杠 “ / ”。
# print(os.getcwd())
#
# （2）创建新的目录 —— 【makedirs()方法】
#
# os.makedirs("tt11\\Zhuo")                                 # 用相对路径tt11\\Zhuo在当前路径底下创建一个新的目录
# os.makedirs("C:\\Users\\ASUS\\Desktop\\LeoTest\\Zhuo")    # 用绝对路径创建
#
# （3）打开目录下的某个文件 —— 【with open("路径", 默认为"r") as xxx】—— open()是python内置的，无需导入OS模块使用
#
# open()方法为python内置，基本用法 f = open('路径', 参数)，文件使用完毕后必须用f.close()关闭，因为文件对象会占用操作系统的资源。
# 但是由于文件读写时都有可能产生出错，后面的f.close()就不会调用。为了保证无论是否出错都能正确地关闭文件，Python引入了with语句来自动帮我们调用close()方法。
# 所以应当尽量用with open("路径", 默认为"r") as xxx来打开文件，而不是f = open('路径', 参数)
# 使用with open() as 读写文件详细: https://blog.csdn.net/xrinosvip/article/details/82019844
#
# 情况1：全文读取全文显示 —— 【read()方法】
# with open("C:\\Users\\ASUS\\Desktop\\test1.txt") as file: # 使用with open("文件的绝对路径或相对路径")打开相应的文件，文件名前不加路径表示打开当前目录下的文件
#     content = file.read()                                 # 使用read()方法读取相应的文件，如果源文件每行输入之后都换行，则每行读取到的内容都是“xxxx \n”自带换行符。
#     print(content)                                        # 全文读取，一次性print时，不会有换行符的问题
#
# 情况2：依次读取每行，并显示 —— 【直接用for遍历】
# with open("test1.txt") as file:         # 使用with open()打开相应的文件。
#     for line in file:                   # 直接使用for来遍历每一行。注意除了最后一行，每行读取到的内容都是“xxxx \n”自带换行符，且print本身会自动换行，所以输出会多一行空白行。
# #         print(line, end="")           # 法1：使用end=""来消除print的自动换行功能，恢复正常显示。
#           print(line.strip())           # 法2：使用strip()来移除字符串【头尾】指定的字符序列（默认为【空格】或者【换行符 “ \n ”】）。
#
# 情况3：依次读取每行，保存到列表里 —— 【readlines()方法】
# with open("test1.txt") as file:
#     new_lst = file.readlines()          # 使用readlines()方法读取每一行，并且保存在列表里，每个元素都自带换行符“ \n ”，除了最后一个元素。
# for i in new_lst:
#     print(i)
#
# （4）创建文件、将内容写入某个文件（覆写和增加） —— 【with open("路径", "w"或"a") as xxx】
#
# with open("test1.txt", "w") as file:     # 创建和覆写："w"。如果test1文件已经存在，本命令是覆盖原有的test1内容。如果不存在test1，本命令是在当前目录创建test1.txt并写入"Love Python!"
#     file.write("Love Python!")           # 使用write()方法写入需要的内容。
#
# with open("test1.txt", "a") as file:     # 增加："a"（a表示append）。并不会覆写源文件的内容，而是在后面直接增加内容。
#     file.write("\n你好，世界！")         # 使用write()方法写入需要的内容。
#
# 2. 异常（exception）处理 ———— 作用是在发生异常时，自定义报错且程序不终止
#
# 异常处理详细：https://www.runoob.com/python/python-exceptions.html
# 异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。一般情况下，在Python无法正常处理程序时就会发生一个异常。
# 异常是Python对象，表示一个错误。当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行。
#
# 为了在发生异常时，自定义报错且程序不终止，通常使用try...except...来捕获。
# 注意：except 后面一定要写精确的error名，要精准预判错误，才能让try..except..起作用。
#
# 异常捕捉处理的通用格式：
# try:
#      <A语句>          # 缩进：需要捕捉异常（可能发生异常）的语句放在这里
# except <xxxError>：   # <xxxError>必须是精确的error名
#      <B语句>          # 缩进：如果发生xxxError，执行本语句
# else:
#      <C语句>          # 缩进：如果没有异常发生，执行else下的语句，通常不需要用else及<C语句>
# <D语句>               # 即使<A语句>出现异常，try..except..之外的<D语句>正常执行
#
# （1）情况1：不做异常捕捉，一旦代码出错，程序立即终止，后续代码不会执行（报错行之前的代码正常执行）。
# a = 10
# b = 0
# print("a/b之前：", 3**2)                   # 不影响a/b之前的代码执行
# print(a/b)
# print("a/b之后：", 9//3)
#
# （2）情况2：做了try..except..捕获。无异常的情况下，try..except..不影响各代码照常执行。
# try:
#     a = 10
#     b = 3
#     print("try..except..内:", 3**2)
#     print(a/b)
#     print("try..except..内:", 2*8)
# except ZeroDivisionError:                 # 提前预判error，except后面一定要写精确的error名，才能让try..except..起作用。
#     print("代码出现异常了。")
# print("继续执行外部正常代码:", 9 + 10)
#
# （3）情况3：做了try..except..捕获。(a/b)出现异常报错时，程序并未停止，不影响try..except..外部代码的执行（且报错行之前的代码正常执行）。
# try:
#     a = 10
#     b = 0
#     print("try..except..内:", 3**2)       # a/b出现异常，try..except..内部，不影响a/b之前的代码执行
#     print(a/b)
#     print("try..except..内:", 2*8)        # a/b出现异常，try..except..内部，a/b之后的代码不执行
# except ZeroDivisionError:
#     print("代码出现异常了。")              # 出现ZeroDivisionError异常时，不显示系统异常提示，而是执行print("代码出现异常了。")
#
# print("继续执行外部正常代码:", 9 + 10)     # a/b出现异常，不影响try..except..外部的代码执行。
#
#
# 十二、python高级函数（lambda、map、reduce、filter减少代码量，增加效率）：

# 1、匿名函数 lambda —— 【简化函数定义形式】

# 写法：函数名 = lambda 参数1, 参数2, 参数3：函数体
# 【注意】函数体里的return可以在lambda形式里省略！！

# 【例1】
# (1) 常规函数形式
# def func1(a):
#     return a ** 2
# print(func1(4))

# (2) lambda形式
# func1 = lambda a: a ** 2             # 函数体省略了return
# print(g(2))

# 【例2】 lambda形式也可设置默认值
# (1) 常规函数形式
# def func2(a, b=5):
#     print(a + b)
# func2(10, 3)
# func2(10)

# (2) lambda形式
# func2 = lambda a, b=5: print(a + b)  # 函数体未省略print
# func2(10, 3)
# func2(10)

# 【例3】 lambda形式可以压缩if..else语句
# 写法：函数名 = lambda 参数1, 参数2, 参数3：if内的执行语句（空格）if条件判断语句（空格）else（空格）else内的语句
# 把常规if..else语句必要的 “：” 省略了，换成空格，且if条件判断语句与if内的执行语句倒装。

# (1) 常规函数形式
# def func3(num):
#     if num % 2 == 0:
#         return "%d is even." % num
#     else:
#         return "%d is odd." % num
# print(func3(9))

# (2) lambda形式
# func3 = lambda num: "%d is even." % num if num % 2 == 0 else "%d is odd." % num
# print(func3(9))

# 2、map函数 —— 【以打包成数列的形式，批量将参数导入函数中进行计算】 —— 通常需要加list()形成列表，再输出

# 写法：map(函数名, iterable1, iterable2,...)，可迭代对象iterable包括列表、元组、range(数字)、字符串等等。
# # 要点：(1)map函数的可迭代对象iterable可以有多个 (2)当处理多个可迭代对象时，要求调用的函数有对应个数的参数
# 作用：将列表、元组、字符串等可迭代对象里的元素，依次代入函数中计算，返回的结果通常需要用list()形成列表，再输出

# 【例 1】 map处理单个可迭代对象
# (1) 常规用法
# a_list = [1, 2, 3, 4]
# def power(x):
#     return x ** 2
# list_1 = list(map(power, a_list))               # 调用定义好的列表或元组
# print(list_1)
# list_2 = list(map(power, (2, 4, 11)))           # 直接填入列表或元组
# print(list_2)
# list_3 = list(map(power, range(10)))            # 填入range()生成的数列也是可以的。【注意】无需给range()加上list。
# print(list_3)

# (2)与lambda函数形式结合的用法
# a_list = [1, 2, 3, 4]
# new_list = list(map(lambda x: x ** 2, a_list))
# # 注意：通常用lambda定义函数都需要令 “函数名 = lambda xx: xxx”，所以这里可以直接用lambda x: x ** 2表示函数名
# print(new_list)

# 【例 2】 map处理多个可迭代对象，需要调用的函数必须也有相应个数的参数
# 【注意】传入的可迭代对象元素数量（length长度）不一致，map函数会自动对齐，取长度最短的那一个作为标准，多余的元素不处理。这是为了保证函数中传入足够的参数。
# (1) 常规用法
# a_list = [1, 2, 3, 4]
# b_list = [2, 4, 7, 11, 88]
# def testfunc(a, b):
#     return a * b
# print(list(map(testfunc, a_list, b_list)))

# aa = "welcome"
# bb = "python world"
# def testfunc(a, b):
#     return a + b
# print(list(map(testfunc, aa, bb)))
# # 输出['wp', 'ey', 'lt', 'ch', 'oo', 'mn', 'e ']

# (2)与lambda函数形式结合的用法
# a_list = [1, 2, 3, 4]
# b_list = [2, 4, 7, 11, 88]
# c_list = [9, 12]
# print(list(map(lambda a, b, c: a * b + c, a_list, b_list, c_list)))         # 省略def定义函数的部分，用lambda简写的形式

# 3、reduce函数 (需要import functools) —— 【用于求累积结果（累积和、累积乘积、字符串相加等】 —— 结果是一个数或者字符串，无需加list()输出

# 写法：functools.reduce(函数名, iterable, 可选：初始参数)
# 要点：(1)reduce函数的可迭代对象iterable(列表、元组、字符串等)只能有一个; (2)调用的函数必须只有两个参数
# 作用：可迭代对象的元素依次取出，代入函数，函数的【每次计算的结果作为第一个参数、可迭代对象的下一个元素作为第二个参数】代入再计算（迭代）

# 【例 1】算1, 2, 3, 4, ....n 的阶乘
# (1) 不用reduce的做法
# num = int(input("please type in a number:"))
# fac = 1
# for i in range(1, num + 1):
#     fac = fac * i
# print(fac)

# (2) 用reduce的做法 ——— 不指定初始值 ——— 计算的起点（代入函数的第一个实参）是可迭代对象里的第一个元素
# import functools
# def factorial(a, b):
#     print("X = %d, Y = %d" % (a, b))
#     return a * b
# print(functools.reduce(factorial, [1, 2, 3, 4]))       # 结果是1 * 2 * 3 * 4 = 24

# 每次迭代的分解：
# X = 1, Y = 2
# X = 2, Y = 3
# X = 6, Y = 4
# 24

# (3) 用reduce的做法 ——— 指定初始值 ——— 计算的起点（代入函数的第一个实参）是指定的初始值
# import functools
# def factorial(a, b):
#     print(f"X = a, Y = b")                # 这里使用的是 f 格式化输出法
#     return a * b
# print(functools.reduce(factorial, [2, 3, 4, 5], 8))    # 结果是8 * 2 * 3 * 4 * 5 = 960

# 每次迭代的分解：
# X = 8, Y = 2
# X = 16, Y = 3
# X = 48, Y = 4
# X = 192, Y = 5
# 960

# (4) 用reduce的做法 ——— lambda形式
# 只用一行代码实现：计算任意输入数字的阶乘：
# import functools
# print(functools.reduce(lambda a, b: a * b, range(1, int(input("Please type in a number:")) + 1)))
# lambda形式也可以设定初始值：
# import functools
# print(functools.reduce(lambda a, b: a * b, range(1, 5), 8))

# 【例 2】字符串的处理
# import functools
# str_a = "wonderful world"
# print(functools.reduce(lambda a, b: a + b, str_a, "What a "))
# # 输出字符串What a wonderful world，实现在字符串前增加初始值"What a "

# import functools
# str_a = ["am", "a", "zing", " ", "pyt", "h", "on"]
# print(functools.reduce(lambda a, b: a + b, str_a))
# # 输出字符串amazing python，相当于将字符串相加

# 4、filter函数  —— 【简化传统的遍历法，筛选子数列】 —— 通常需要加list()形成列表，再输出

# 写法：filter(函数名, iterable)
# 要点：filter函数的可迭代对象iterable只能有一个
# 作用：依据所调用的函数，筛选出可迭代对象iterable的一个子数列
# 【注意】所调用函数的返回值必须是布尔值：True或者False！！

# 【例 1】筛选出range(20)数列中可以被0整除的子数列
# (1)传统遍历法
# a_list = []
# for i in range(20):
#     if i % 2 == 0:
#         a_list.append(i)
# print(a_list)

# (2) filter法
# def func1(x):
#     return x % 2 == 0                   # 相当于if x % 2 == 0: return True, else: return False。类比num = 3, print(num % 2 == 0)的结果将是False。
# print(list(filter(func1, range(20))))   # 利用func1函数筛选出0-19数列中，能被0整除的子数列：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# print(list(map(func1, range(20))))      # 【注意】与map函数的区分！！同样调用func1函数，将输出[True, False, True, False,...]

# (3) filter与lambda形式结合
# print(list(filter(lambda i: i % 2 == 0, range(20))))   # lambda i: i % 2 == 0相当于func1(x)

# 【例 2】筛选出range(-20, 21)数列中大于零的子数列
# 几种等价的情况 —— 以下三种函数的filter情况都是等价的(各自的lambda形式也等价)
# (1) 法 1
# def is_positive_1(i):
#     if i > 0:
#         return True
#     else:
#         return False
#
# print(list(filter(is_positive_1, range(-20, 21))))
# 或者直接用lambda形式: print(list(filter(lambda i: True if i > 0 else False, range(-20, 21))))

# (2) 法 2
# def is_positive_2(i):
#     if i > 0:
#         return 1
#     else:
#         return 0
#
# print(list(filter(is_positive_2, range(-20, 21))))
# 或者直接用lambda形式: print(list(filter(lambda i: 1 if i > 0 else 0, range(-20, 21))))
#
# (3) 法 3
# def is_positive_3(i):
#     return i > 0
#
# print(list(filter(is_positive_3, range(-20, 21))))
# 或者直接用lambda形式: print(list(filter(lambda i: i > 0, range(-20, 21))))
#
#


# # # # # # # # # # # # # # # # # # # # # # # #其他内容 # # # # # # # # # # # # # # # # # # # # # # # #
#
# 【思考 1】以下三个函数的结果是一样的（用于理解__init__()方法和对象创建时的参数传递）
# def func(a, screen):      # 类比__init__()方法
#     num1 = a              # 类比类里的属性定义，为属性num1绑定形参a
#     num2 = screen
#     return num1 + num2
#
# window = 9
# print(func(1, window))    # 类比创建对象时自动调用__init__()方法，传入window的值作为实参
#
# def func(a, screen):
#     num1 = a
#     num2 = screen
#     return num1 + num2
#
# screen = 9
# print(func(1, screen))
#
# def func(a, screen):
#     num1 = a
#     num2 = screen
#     return num1 + num2
#
# print(func(1, 9))


# 【附 1】定时器：（间隔x秒，循环启动）-- 递归调用

# import threading
# def fun_timer():
#     print('Hello Timer!')
#     global timer
#     timer = threading.Timer(0.5, fun_timer)     # 第二次 开始到之后都是间隔0.5秒
#     timer.start()
#
# timer = threading.Timer(2, fun_timer)           # 第一次启动间隔3秒
# timer.start()

# 【附 2】格式化输出的几种方法：

# 1. f格式化输出法（在需要print的字符串前加上 f）
# t_name = input("请输入名字：")
# age = input("请输入年龄：")
# print(f"{t_name}'s age is {age}!")

# 2. 用 str.format
# t_name = input("请输入名字：")
# age = input("请输入年龄：")
# print("{}'s age is {}!".format(t_name, age))
# 或者
# print("{t_name}'s age is {age}!".format(t_name="Leo", age=18))
# 再或者
# print("{}'s age is {}!".format("Leo", 18))

# 3. 用 %
# print("%s's age is %d!" % ("Leo", 18))

# 【附 3】 使用len()定义字符串切片的起始位置

# str_a = "www.this is a wonderful world.com/and we love the Earth//357549405"
# print(str_a[len("www.this is a wonderful world.com/and we love the Earth//"):])
# 通过len(xxx)来确定切片起始索引位，注意起始切片位是xxx之后的那一个字符，因为字符串第一个索引位是0
#
# str_b = "Earth//357549405"
# print(len(str_b))
# print(str_b[0])  # 注意字符串第一个索引位（index）是 0

# 【附 4】 类变量、实例变量、实例方法、类方法、静态方法
#
# class Dog:
#     # 1、类变量
#     # 类变量是属于整个类的变量，由所有具体的对象共享。
#     # 定义方法时：
#     # (1) 通过【类名】、【对象指代名self.__class__.】或者【对象指代名self】调用；
#     # (2) 注意：必须通过【类名】或者【对象指代名self.__class__.】调用 = xxx 才能更新类变量值！！
#     # 在类之外调用时：通过【类名】、【对象具体名.__class__.】或者【对象具体名self】调用。
#     dog_count = {'黄色': 30, '黑色': 20}
#
#     def __init__(self, t_name, color, weight):
#     # 2、实例变量
#     # 实例变量由【对象指代名self】定义，每个具体的对象都有自己不同的实例变量值。
#     # 定义方法时：
#     # (1) 通过【对象指代名self】调用；
#     # (2) 通过【对象指代名self】调用 = xxx 可更新实例变量值
#     # 在类之外调用时：通过【对象具体名】调用。
#         self.t_name = t_name
#         self.color = color
#         self.weight = weight
#     # 此处省略了更新dog_count的代码
#
#     # 3、实例方法
#     # 定义时，必须把self作为第一个参数，通常只用于访问【实例变量】，也可以使用self.dog_count或者Dog.dog_count调用【类变量】。
#     # 调用时，必须通过【对象名】调用。
#     def bark_update(self):
#         print(f'{self.t_name} 叫了起来')
#         # 定义方法时通过【对象指代名self】调用实例变量
#         print(self.dog_count)
#         print(Dog.dog_count)
#         print(self.__class__.dog_count)
#         # 第一次print，使用self.或者Dog.均可调用【类变量】，结果相同。
#
#         self.t_name = "新名字：超级狗狗"
#         # 把所有对象的name统一定义为新的值"新名字：超级狗狗"
#         self.dog_count = {'yellow': 15}
#         # 注意：(1) 相当于定义了一个与类变量同名的实例变量dog_count，并非修改【类变量】。
#         # (2) 从此将无法用【对象self或对象具体名】调用类变量dog_count！！！
#         Dog.dog_count = {'黄色': 0, '黑色': 23}
#         # 将对【类变量】dog_count做出修改
#
#         print(f'{self.t_name} 叫了起来')
#         # 所有对象的name值已重新设置
#         print(self.dog_count)
#         print(Dog.dog_count)
#         print(self.__class__.dog_count)
#         # 第二次print，使用self.将无法调用类变量dog_count，而是调用了同名的实例变量dog_count。
#
#     # 4、类方法 （使用@classmethod进行声明）
#     # 定义时，必须把cls作为第一个参数，通常只用于访问【类变量】。
#     # 调用时，可以通过【类名】或者【对象名】调用。注意：使用【对象名】调用时，程序将自动找到对应的【类名】传入！！
#     @classmethod
#     def dog_num(cls):
#         num = 0
#         for v in cls.dog_count.values():
#             num = num + v
#         return num
#
#     # 5、静态方法（使用@staticmethod进行声明）
#     # 定义时，不强制传入self或者cls，通常不用于访问【实例变量】或【类变量】。
#     # 调用时，可以通过【类名】或者【对象名】调用。
#     # 本质上，不属于类的定义范畴，只是个普通的函数，可以移到类外边定义。放在类里边是因为该方法做的事情与Dog类紧密相关。
#     @staticmethod
#     def total_weights(dogs):          # 只需传入我们需要的参数或对象名，没有任何强制要求，与普通函数定义相同。
#         total = 0
#         for i in dogs:
#             total = total + i.weight  # 使用对象名访问每只狗的属性
#         return total
#
# print(f"共有 {Dog.dog_num()} 条狗")
# d1 = Dog("大黄", "黄色", 10)
# d1.bark_update()
# print(f"共有 {d1.dog_num()} 条狗")  # 使用【对象名】调用类方法时，程序将自动找到对应的【类名】传入。
#
# d2 = Dog("旺财", "黑色", 8)
# d2.bark_update()
#
# print(f"狗共重 {Dog.total_weights([d1, d2])} 公斤")
# print(f"狗共重 {d1.total_weights([d1, d2])} 公斤")  # 使用【对象名】调用静态方法时，程序将自动找到对应的【类名】传入。
# print(d1.__class__.dog_count)

# 【附 5】 二进制文件和编码规范

# 计算机里存储的所有文件本质上都是二进制文件（由0和1组成），只不过我们根据文件类型和用途，人为定义了这些0和1的翻译方式，即“编码规范”。
# 我们打开文件时，计算机调用相应的编码规范，将0和1转换为文本文件格式（如txt、html、xml），图片格式（如jpeg、png）以及音频视频格式等，为人类所读。
# 所以，如果人为使用文本编码规范对图片文件进行翻译（比如将图片后缀png改为txt），就会生成所谓的乱码。
# 文字编码规范有ASCII、Unicode、中文的GB2312等等。

# 1、复制文件
# 采用的二进制方式读取（rb）和写入（wb），就不存在文件编码的问题
# with open("./文件处理测试/test.docx", "rb") as f:
#     with open("./文件处理测试/test_copy.docx", "wb") as p:
#         for line in f.readlines():
#             p.write(line)
# print('done.')
#
# # 2、复制图片
# # 采用的二进制方式读取（rb）和写入（wb），就不存在文件编码的问题
# with open("./文件处理测试/Screenshot.png", "rb") as f:
#     with open("./文件处理测试/Screenshot_copy.png", "wb") as w:
#         for line in f.readlines():
#             w.write(line)
# print('done.')

# mag_list = ["12", "333", "kkk", "88898"]
# with open(f"xxx.txt", "w", newline="", encoding="utf-8-sig") as f:
#     for m in mag_list:
#         print(m)
#         f.write(m + "\n")

# 【附 6】解包与压包zip ———— 针对可迭代对象使用
# 详见：python有趣的解包压包用法https://zhuanlan.zhihu.com/p/33896402

# 一、解包

# python中的解包可以这样理解：以list为例，一个list是一个整体，想把list中每个元素当成独立的个体剥离出来，这个过程就是解包。
# 解包对列表、元组、字典等可迭代对象均可使用。

# 1、多变量解包

# （1）对列表适用
# testList = [12, 23, "yes"]
# a, b, c = testList
# print(a)
# print(b)
# print(c)
# print(*testList)  # 注意：星号 “ * ”也可以直接解包列表，输出12 23 yes
# print(testList)   # 注意区别

# （2）对字典适用
# x, y = {"t_name": "Leo", "age": 16}
# print(x, y)
# x, y = {"t_name": "Leo", "age": 16}.items()
# print(x, y)

# （3）对列表推导式适用
# a, b, c = [i*2 for i in range(2, 5)]
# print(a, b, c)

# （4）对生成器（generator）适用
# 生成器和列表推导式是非常类似的，它和列表推导式的用法基本一致。
# 生成器的工作方式是每次处理一个对象，而不是一口气处理和构造整个数据结构，这样做的潜在优点是可以节省大量的内存。
# a, b, c = (i*2 for i in range(2, 5))
# print(a, b, c)

# （5）<特别：星号“ * ”的使用>
# 如果可迭代对象包含的元素和前面待赋值变量数量不一致，则会报错 “too many values to unpack”。
# 我们可以通过“ * ”来表示多个元素，防止报错。
# first, *mid, last = [i*2 for i in range(10)]    # 使用 *mid来 指代除了第一个与最后一个元素之外的其他所有元素，组成列表 *mid
# print(first, mid, last)                         # 输出 0 [2, 4, 6, 8, 10, 12, 14, 16] 18

# 2、星号“ * ”解包 ———— 用“ * ”将列表、元组、字符串、字典等可迭代对象包含的元素拆出来

# （1）解包列表、字典等实际保存的序列
# 例：函数被调用的时候，使用星号 * 解包一个可迭代对象作为函数的参数
# def func(a, b, c):
#     return a, b, c
#
# print(func(*[1, 2, 3]))
# print(func(*(1, 2, 3)))
# print(func(*"abc"))
# print(func(*{"a": 1, "b": 2, "c": 3}))            # 字典使用单星号“ * ”解包时，默认拆出keys
# print(func(*{"a": 1, "b": 2, "c": 3}.values()))   # 可以指定拆出来是keys、values或者items
# print(func(*{"a": 1, "b": 2, "c": 3}.items()))
# print(func(**{"a": 1, "b": 2, "c": 3}))           # 【特别】：字典可以使用两个星号“ ** ”解包，其“键值对”将作为关键字参数传递给函数。
#                                                   # 【注意】：字典“ ** ”解包时，需要键的名字和函数定义时参数的名字相同！！

# （2）解包range()等虚拟序列
# print(*range(10))     #  若直接print输出 range(0, 10)
# print(*enumerate(d))  #  若直接print输出 <enumerate object at 0x00000235743A8098>

# 3、在for循环中解包（多变量解包、星号“ * ”解包、product()函数和enumerate()函数使用）

# （1）遍历时将多个变量同时作为临时变量
# for t_name, age, hobby in aList:
#     print(f"t_name:{t_name}, age:{age}, hobby:{hobby}")

# （2）星号“ * ”解包aList，product合成所有27种组合，再for遍历并解包
# import itertools
# for t_name, age, hobby in itertools.product(*aList):   # 星号“ * ”也可用于解包，配合itertools.product()函数使用
#     print(f"t_name:{t_name}, age:{age}, hobby:{hobby}")
# # *aList解包出列表里的三个元素("Leo", "Mike", "Lily")，(17, 18, 27)，("hiking", "soccer", "swimming")
# # itertools.product()函数使得解包出来的三个元组中的元素重新组合，生成所有27种不同的元素组合。

# （3）星号“ * ”解包aList，product合成所有27种组合，再for遍历并解包（同时解出索引号）
# import itertools
# for ids, (t_name, age, hobby) in enumerate(itertools.product(*aList)):
#     print(f"序号:{ids+1}, t_name:{t_name}, age:{age}, hobby:{hobby}")
# # 配合enumerate()，可在遍历的同时输出元素的索引号

# 4、特殊：单元素解包（当然也可以通过索引切片[0]提取）
# 例：
# z1, = [3]          # 解包出list的唯一元素
# z2, = ("hello",)   # 解包出tuple的唯一元素
# print(z1)          # 输出 3
# print(z2)          # 输出 hello

# 二、压包 zip

# 将若干组可迭代对象合成在一起，这些对象可以是不同的类型。

# （1）列表和元组压包
# a = ['Leo', 'Jacky', 'Alex']
# b = (1, 2, 3)
# c = zip(a, b)        # 直接打印zip的结果将出现<zip object at 0x00000164ECC05088>
# print(c)
# for i in c:
#     print(i)

# （2）字典和元组压包
# 注意字典可以用.items() .values() .keys()方法
# a = {'Leo': 11, 'Jacky': 23, 'Alex': 56}
# b = (1, 2, 3)
# c = zip(a.keys(), b)
# for i in c:
#     print(i)

# （3）列表和生成器压包
# 注意：将两组可迭代对象合成在一起，两个对象元素数量可以不匹配，不匹配的部分将被删除
# a = ['Leo', 'Jacky', 'Alex']
# b = (x for x in range(1, 11, 3))
# c = zip(a, b)
# for i in c:
#     print(i)

# （4）混合多重压包
# a = ['Leo', 'Jacky', 'Alex']
# b = "832"
# c = ('super', 'lucky', 'good')
# d = "LJA"
# e = {'流川枫': 11, '樱木': 18, 'Mike': 23}.items()
# print(list(zip(a, b, c, d, e)))

# （5）zip可以对tensor使用
# import torch
# a = torch.randn(2, 3)
# b = torch.randint(8, (2, 3))
# print(a)
# print(b)
#
# zipped = zip(a, b)
# for i in zipped:
#     print(i)

# 【附 7】可迭代对象iterable和迭代器iterator

# 可迭代对象iterable和迭代器iterator，详见 https://zhuanlan.zhihu.com/p/32508947

# 1、迭代工具
# Python中有一类工具叫做迭代工具，他们能从左至右扫描对象。这包括了for循环、列表解析、in成员关系测试、map、reduce函数等。

# 2、可迭代对象 （iterable）
# 而可迭代对象，顾名思义就是可以用在上述迭代工具环境中，通过一次次迭代不断提取元素的对象。
# 可迭代对象 （iterable）分为两大类：
# （1）一种是实际保存的序列，即列表list、元组tuple、字典dict、集合set、字符串str等，这些称为 “容器” （container）
# （2）另一种是按需提取元素的虚拟序列，如range函数返回值、zip函数返回值、enumerate函数返回值、generator生成器返回值等等，
# 这些虚拟序列不会一次性产生包含所有元素的完整序列，我们需要再for循环中按需一次提取一个元素
# 另外，直接print虚拟序列是无法显示元素的，需要用list()、tuple()等函数转化成实际保存的序列。
# 【注意】generator生成器比较特殊，既是iterable也是iterator。其次，generator生成器相较列表推导式，最大的优点是非常节省内存！！！！

# 3、迭代器（iterator）
# 可迭代对象（iterable）支持内置iter函数，通过对可迭代对象调用iter函数，会返回一个迭代器（iterator），迭代器支持内置next函数，
# 通过不断对其调用next函数，会依次前进到序列中的下一个元素并将其返回，最后到达一系列结果的末尾时，会引发StopIteration异常。

# 4、迭代协议 -- for循环等迭代工具的实现原理
# 我们来完整的看看迭代过程是怎么实现的：当任何可迭代对象传入到for循环或其他迭代工具中进行遍历时，
# 迭代工具都是先通过iter函数获得与可迭代对象对应的迭代器，然后再对迭代器调用next函数，不断的依次获取元素，
# 直到StopIteration异常，代表迭代器中已无下一个元素，for循环自动处理该异常，跳出循环。这就是完整的迭代过程，也称之为“迭代协议”。

# （1）示例（可迭代对象转换为迭代器）：
# from collections.abc import Iterable, Iterator  # 导入Iterable, Iterator，为了用isinstance()做判断

# lst = [2, 3, 4]
# a_iter = iter(lst)                       # 对可迭代对象lst使用iter函数，生成a_iter迭代器
# print(a_iter)                            # 输出 <list_iterator object at 0x000002373F346E08>
# print(isinstance(a_iter, Iterable))      # 使用isinstance()判断a_iter是否是Iterable，结果为True，说明迭代器本身也是可迭代对象
# print(isinstance(a_iter, Iterator))      # 输出True
# print(a_iter is iter(a_iter))            # 输出True，说明对迭代器调用iter方法，则会返回迭代器自身。

# 【特别】对于generator生成器，既是iterable也是iterator，所以可以直接使用next(generator)来逐一输出元素。
# generator = (i*i for i in range(10))
# g_iter = iter(generator)
# print(isinstance(generator, Iterator))   # True
# print(isinstance(generator, Iterable))   # True
# print(isinstance(g_iter, Iterator))      # True
# print(isinstance(g_iter, Iterable))      # True

# （2）示例【手动迭代实现for循环】---- 迭代器的生成必须在循环之外
# 【特别注意】，需要先生成一个iterator：tIter，再把next(tIter)放进循环里，才能遍历tList所有元素。
# 【特别注意】，如果将next(iter(tList))直接放进循环里，会无限输出第一个元素。原因是iter(tList)循环执行，每次next调用的都是新生成的iterator。

# tList = ["Leo", 76, "Mike", 18]
# tIter = iter(tList)
# try:                          # 利用try...except...包裹while True语句，捕捉StopIteration异常。
#     while True:               # 若不用try...except...包裹，当迭代器中已无下一个元素，会报错StopIteration
#         print(next(tIter))
# except StopIteration:         # 处理StopIteration异常，使得程序不报错，且循环停止
#     pass                      # pass 是空语句，是为了保持程序结构的完整性。不做任何事情，一般用做占位语句。

# 【附 8】虚拟序列生成函数 zip()、product()、enumerate()的区分
# 三种都会在原来列表、元组的元素基础上，生成新的由元组组成的可迭代对象
# from itertools import product
# a = [23, 433, 5545, 545]
# b = ["wef", 55, "www"]

# （1）直接print会输出<zip、itertools.product或enumerate object at 内存地址>
# test_1 = zip(a, b)
# test_2 = product(a, b)
# test_3 = enumerate(a)

# （2）需要配合 list()或者tuple()使用
# print(list(test_1))
# print(list(test_2))
# print(list(test_3))

# （3）或者用于for循环遍历
# for i in test_2:
#     print(i)

# 【附 9】list和array的索引方法有区别
# import numpy as np
# # a是普通的list
# a = [[12, 4],
#      [34, 1],
#      [65, 11],
#      [77, 22],
#      [99, 74]]
# # b是numpy里的array
# b = np.array([[12, 4],
#               [34, 1],
#               [65, 11],
#               [77, 22],
#               [99, 74]])
#
# # list a 的普通遍历
# for i in range(len(a)):
#     print(f"第{i + 1}个点的X坐标值为{a[i][0]}")

# # array b 的遍历，注意索引的方法：数组名[行索引位，列索引位]
# for i in range(len(b)):
#     print(f"第{i + 1}个点的X坐标为{b[i, 0]}")
#
# # enumerate()函数遍历array b
# # 用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
#
# print(list(enumerate(b)))
# # 输出 [(0, array([12,  4])), (1, array([34,  1])), (2, array([65, 11])), (3, array([77, 22])), (4, array([99, 74]))]
#
# for num, (x, y) in enumerate(b):
#     print(num)
#     print(x)


# 【附 10】时间操作、time模块的相关信息
#
# 一、time()、perf_counter()和process_time()的区别

# 1.【time.time()方法】 -- 算时间差值时【包含sleep()程序休眠】的时间
# 返回自纪元以来的秒数作为浮点数。比如：在Windows和大多数Unix系统上，纪元是1970年1月1日00:00:00（UTC），
# time()精度上相对没有那么高，而且受系统的影响，适合大程序程序的计时。
# 2.【 time.perf_counter()方法】 -- 算时间差值时【包含sleep()】的时间
# 返回性能计数器的值（以小数秒为单位）作为浮点数，即具有最高可用分辨率的时钟，适用小程序测量短持续时间。
# 3.【time.process_time()方法】 -- 算时间差值时【不包含sleep()】的时间
# 返回当前进程的系统和用户CPU时间总和的值（以小数秒为单位）作为浮点数，适用小程序测量短持续时间。

# import time
# # （1）起始时间
# t0 = time.time()
# c0 = time.perf_counter()
# p0 = time.process_time()
# print(f"time()_start time：{t0}")
# print(f"perf_counter()_start time：{c0}")
# print(f"process_time()_start time：{p0}")
# # （2）需要测试运行时间的代码
# r = 1
# for i in range(1, 100000):
#     r *= i
# time.sleep(2)   # 休眠 2 秒
# print(r)
# # （3）结束时间
# t1 = time.time()
# c1 = time.perf_counter()
# p1 = time.process_time()
# print(f"time()_end time：{t1}")
# print(f"perf_counter()_end time：{c1}")
# print(f"process_time()_end time：{p1}")
# # （4）程序运行花费的时间
# spend1 = t1 - t0
# spend2 = c1 - c0
# spend3 = p1 - p0
# print(f"time()方法用时：{spend1}")
# print(f"perf_counter()方法用时：{spend2}")
# print(f"process_time()方法用时：{spend3}")
# print("测试完毕")

# 二、秒数变为“时分秒”输出
# divmod()把【整除】和【取余】的运算结果结合起来，返回一个元组(a // b, a % b)。
# 例子：print(divmod(17, 3))  # 输出(5, 2)
# seconds = 432244.443
# m, s = divmod(int(seconds), 60)
# h, m = divmod(m, 60)
# print(f'{h:02d}hrs,{m:02d}mins,{s:02d}secs')   # d表示输出为整数，02表示不足两位时需要补零

# 使用 .xf 控制保留几位小数的格式化输出
# print(f"seconds = {26.325834:.1f}")
# print(f"seconds = {26.325834:.2f}")
# print(f"seconds = {26.325834:.3f}")
# print(f"seconds = {26.325834:.4f}")

# 三、格式化输出现在的时间
# from datetime import datetime
# now = datetime.now()
# print(f"The time is: {now:%F, %X}")

# 四、倒计时
# import time
# print("倒计时启动")
# for i in range(5)[::-1]:
#     print(i + 1)
#     time.sleep(0.8)

# 【附 11】namedtuple的用法

# 普通元组创建：元组名 = (元素值1, 元素值2, ...)。
# namedtuple创建：元组名 = 元组类名(元素名1=元素值1, 元素名2=元素值2, ...)，可以不加“ 元素名x= ”，创建前要先设置模板。
# 与普通元组最大的区别：创建前要先设置模板，但可以用【元组实例名.元素名】的方法访问元组的元素值。
# 详见https://www.jianshu.com/p/60e6484a7088

# 1、定义
# namedtuple是一个工厂函数，定义在python标准库的collections模块中，使用此函数可以创建一个可读性更强的【元组】；
# namedtuple函数所创建（返回）的是一个元组的子类（python中基本数据类型都是类，且可以在buildins模块中找到）；
# namedtuple函数所创建元组，中文名称为“具名元组”；

# 2、对比（相比普通元组和传统类的创建）
# （1）相比普通元组
# 在使用普通元组的时候，我们只能通过index来访问元组中的某个数据；
# 使用具名元组，我们既可以使用index来访问，也可以使用具名元组中每个元素的名称来访问；
# 值得注意的是，具名元组和普通元组所需要的内存空间相同，所以 不必使用性能来权衡是否使用具名元组；
# （2）相比传统类的创建
# 另外，namedtuple的使用类似于创建一个类，只适合简单的类，不需要写大量的定义class类代码。
# 相比传统的类创建，用namedtuple生成的类少了很多内置的变量，比如__name__等，很省空间。

# 3、创建和使用步骤
# （1）导入模块并设置namedtuple类模板
# from collections import namedtuple
# Player = namedtuple("Player", ["t_name", "age", "height"])

# 原始定义：namedtuple(typename, field_names, *, rename=False, defaults=None, module=None):
# 第一个参数typename为【类名】，一般情况下都要使得【类名】与等号左边的【变量名】一致，为了代码可读性。
# 第二个参数field_names参数类型为列表、元组或字符串序列，用于【为创建的元组的每个元素命名】，该过程类似于class类创建时设置【属性名】，
# 可以传入像["t_name", "age", "height"]这样的序列，也可以传入"t_name age height"或"t_name, age, height"这种被逗号或空格分割的单字符串。

# （2）实例化，创建具名元组
# p1 = Player("流川枫", 29, 175)
# print(p1)
# 生成一个具名元组namedtuple，传入元素值。类似于class类的实例化，并传入属性值。
# 也可以用传入关键字参数的方法生成：p1 = Player(t_name="流川枫", age=29, height=175)
# print(p1)
# 直接print输出 Player(t_name='流川枫', age=29, height=175)，不同于普通类的实例，因为namedtuple原始定义中修改了__repr__，
# 也不同于普通元组的显示，在()前加上了类名，在元素前加上了 “ 元素名称= ”。

# print(p1[0])                      # 【注意】可以像普通元组一样索引！！
# print(p1.age, p1.t_name)            # 【注意】也可以像普通类的实例一样获取属性值

# player_info = ["樱木", 21, 189]
# p2 = Player(*player_info)         # *player_info的作用就是将列表或元组解包，再将拆开的元素作为类的属性值传入
# print(p2)

# （3）namedtuple可遍历
# print(len(p2))                    # 从长度可知namedtuple确实包含3个元素
# for i in p2:                      # 可普通for遍历
#     print(i)
# for i in range(len(p2)):          # 可由索引号遍历
#     print(p2[i])

# （4）namedtuple可转化为OrderedDict
# from collections import namedtuple
# Player = namedtuple("Player", ["t_name", "age", "height"])
# p1 = Player("流川枫", 29, 175)
# order_d = p1._asdict()
# print(order_d)                    # 输出：OrderedDict([('t_name', '流川枫'), ('age', 29), ('height', 175)])
# print(order_d.keys())

# 【附 12】OrderedDict与普通字典的比较

# 普通字典：Python3.6 版本以后，遍历字典得到的键、值是按照键、值对创建顺序排列的（读取有序），但是字典内部存储仍然是无序的（存储无序）。
# OrderedDict：是字典的一个子类，相比普通字典，OrderedDict的键值对存储是有序的，读取也是有序的（读取存储皆有序）。

# 1、相似点：均可使用构造函数创建字典
# （1）普通字典创建
# stu1 = dict((("t_name", "leo"), ("age", 18), ("gender", "male")))         # 传入一个元组或列表
# stu2 = dict(t_name="Leo", age=18, gender="male")                          # 或者传入关键字参数
# print(stu1)
# print(stu2)
# （2）OrderedDict创建
# from collections import OrderedDict
# od1 = OrderedDict((("t_name", "leo"), ("age", 18), ("gender", "male")))   # 传入一个元组或列表
# od2 = OrderedDict(t_name="Leo", age=18, gender="male")                    # 或者传入关键字参数
# print(od1)
# print(od2)

# 2、不同点
# （1）普通字典
# stu1 = {"t_name": "leo", "age": 18, "gender": "male"}
# stu2 = {"gender": "male", "t_name": "leo", "age": 18}
# for i in stu1:
#     print(i)                                    # 按照键值对创建的顺序输出keys（读取有序）
# print("普通字典比较:", stu1 == stu2)            # 结果是True，因为字典里键值对的存储是无序的，没有先后之分（存储无序）

# （2）列表（存储读取皆有序）
# aList1 = ["leo", "neo", "roy"]
# aList2 = ["neo", "roy", "leo"]
# print("列表比较:", aList1 == aList2)           # 结果是False，因为列表里存储的数据是有序的，调换顺序即视为不相等（存储有序）

# （3）OrderedDict（存储读取皆有序）

# from collections import OrderedDict
# od1 = OrderedDict(t_name="leo", age=18, gender="male")
# od2 = OrderedDict(gender="male", t_name="leo", age=18)
# for o in od2:
#     print(o)                                  # 按照键值对创建的顺序输出keys（读取有序）
# print("OrderedDict比较:", od1 == od2)         # 结果是False，因为OrderedDict存储的键值对是有序的，调换顺序即视为不相等（存储有序）


# # 【附 13】高阶函数
#
# def func():
#     print("hello")
# def ye(t_name):
#     t_name()
#
# func()
# ye(func)


# 【附 14】Image模块、plt模块读取绘制图片以及Tensor和PIL、ndarray格式的相互转换

# 【重要】：PIL.Image或numpy.ndarray转化为Tensor，常常用在训练模型阶段的数据读取，而Tensor转化为PIL.Image或numpy.ndarray则用在验证模型阶段的数据输出。
# 【注意】：Tensor的shape是(C x H x W)，而cv2，plt，PILshape都是(H x W x C)

# import torch
# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt
# import torchvision.transforms as transforms
#
# # （1）定义PIL图片转tensor格式的方法transform，以及tensor转PIL图片的方法rev_transform
# # transforms.ToTensor()的作用：
# # 将PIL格式或者 numpy.ndarray (H x W x C)，像素取值范围为[0, 255]的图片，转换成 torch.FloatTensor (C x H x W)数据，像素取值范围为[0.0, 1.0]。
#
# transform = transforms.Compose([                    # Compose可以将括号里的所有图片转换一起执行
#     transforms.Resize((28, 28)),                    # 转换图片尺寸
#     transforms.Grayscale(num_output_channels=1),    # 将图片转换为灰度图，Grayscale的存在导致没法用tensor转nd—array的方法输出转换结果，会报错！！！！！！！！！！！！！
#     transforms.ToTensor()                           # 像素值归一化，并图片转换为tensor数据
# ])
#
# rev_transform = transforms.ToPILImage()       # 注意：rev_transform的输入必须是(C x H x W)，不能是(N x C x H x W)，因为PIL格式没有batch_size(N)维度。
#
# # （2）Image模块读取PIL图像
# # 【注意】：PIL图像可以直接使用plt显示！！！！
#
# # cv2模块读入图片以numpy矩阵的形式存放，默认为[0, 255]。cv2默认以【BGR】的顺序读入图像。
# # plt模块读入图片同样以numpy形式存放，但是其读入的通道顺序为【RGB】，cv2不同。
# # Image模块读入图像时，有自己的图像文件格式PIL。PIL图片也可以和numpy.ndarray格式相互转换。
#
# img_pil = Image.open("./test_pics/lena.jpg")  # 使用Image模块读取图片，格式为PIL。可以使用convert("RGB")转化为三通道图、convert("L") 转换成灰度图。
# print(type(img_pil), np.min(img_pil), np.max(img_pil))  # 打印PIL格式图片的type、使用np.min和np.max打印图片的像素值最大和最小值。
# img_numpy = np.array(img_pil)                           # 使用np.array()可将PIL格式转化为numpy.ndarray格式。
# print("img_numpy:", img_numpy.dtype, img_numpy.size, img_numpy.shape)   # 显示图片shape为(855, 400, 4)，分别表示(height, width, channel)
#
# # （3）将PIL图像转换成tensor
# img_tensor = transform(img_pil)                         # 转换格式得到Tensor，shape为(C x H x W)
# img_tensor = torch.unsqueeze(img_tensor, dim=0)         # 插入batch_size维度(N)，shape变为(N x C x H x W)，这样才能传入神经网络模型进行计算
# print(img_tensor.shape)                                 # 显示shape为torch.Size([1, 1, 28, 28])
#
# # （4）将tensor转换成PIL图像
# # 原始图像经过了transforms.Resize、transforms.Grayscale变换，但是rev_transform只是transforms.ToTensor的逆变换，
# # 所以还原的PIL与原图不同，除非将Resize和Grayscale操作都进行逆变换。
#
# img_tensor = torch.squeeze(img_tensor, dim=0)       # 丢弃batch_size维度(N)，变回(C x H x W)，否则rev_transform操作报错
# img_new_pil = rev_transform(img_tensor)             # 逆转换得到PIL格式图片，可以直接用plt展示出来
#
# # （5）将原始PIL图像和经变换还原的PIL图像，使用plt一起展示
# plt.rcParams["font.sans-serif"] = ["SimHei"]        # 解决绘图中文标签显示错误的问题，定义字体为黑体
# plt.rcParams["axes.unicode_minus"] = False          # 用来正确显示负号
# plt.figure("图片样例")                               # 图像窗口名称
# plt.axis("on")              # 关掉坐标轴为 off
# plt.subplot(1, 2, 1)        # subplot可以绘制画布，subplot(行数，列数，每行第几个图)
# plt.title("原始PIL")         # 显示单张图像对应的标题
# plt.imshow(                 # plt.imshow()函数负责对图像进行处理，但是不能显示图像。使用plt.show()才能显示出来。
#     img_pil,                # 若img_pil是灰度图像，则这里必须要加上cmap="gray"才能正常显示灰度，否则是伪彩色。
#     cmap="gray"             # 如果img_pil不是灰度图像，即使这里加上cmap="gray"，也会正常显示彩色图像
# )
#
# plt.subplot(1, 2, 2)
# plt.title("经变换还原的PIL")
# plt.imshow(
#     img_new_pil,
#     cmap="gray"
# )
# plt.show()

# 【附 15】plt模块使用subplot分块绘图

# import numpy as np
# import matplotlib.pyplot as plt

# 1、等分绘图
# plt.figure()
# plt.subplot(221, facecolor='r')  #指定分为2行2列，绘制在第一个位置，facecolor指定背景颜色red
# plt.subplot(222, facecolor='b')  #指定分为2行2列，绘制在第二个位置，facecolor指定背景颜色blue
# plt.subplot(223, facecolor='g')
# plt.subplot(224, facecolor='y')
# plt.show()

# 2、不等分绘图，区域有大有小
# plt.figure()
# plt.subplot(221)  #指定分为2行2列，绘制在第一个位置
# plt.subplot(222)  #指定分为2行2列，绘制在第二个位置
# plt.subplot(212)  #整合2行2列的第三和第四个位置，2表示如果分为2行1列的话，当前绘制位置是第二个
# plt.show()

# 【附 16】展示transform图像预处理的效果

# import torch
# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt
# import torchvision.transforms as transforms
#
# transform = transforms.Compose([
#     transforms.RandomResizedCrop(224),  # 将原图随机裁剪成224 * 224的尺寸
#     transforms.RandomHorizontalFlip(),  # 将原图在水平方向上随机翻转
#     transforms.ToTensor(),
#     transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))  # 像素值标准化
# ])

# 1、读取数据集图片并transform
# 【模拟torchvision.datasets.ImageFolder加载数据集时发生的事情】
# img_pil = Image.open("./test_pics/lena_1.jpg")
# img_tensor = transform(img_pil)

# 2、展示transform后的图片
# 法（1）、将tensor变为numpy的nd-array格式，用于plt输出。
# 无需另外定义 tensor >> nd-array 的方法，但需要调整shape
# img_tensor = (img_tensor * 0.5) + 0.5         # 用于逆标准化，若需要保留标准化的结果，此行要删除
# np_img = img_tensor.numpy()                   # tensor和nd-array之间可以直接互相转化
# plt.imshow(np.transpose(np_img, (1, 2, 0)))   # 【调整shape】原来的shape为(C x H x W)，0代表C、1代表H、2代表W，经过transpose(1, 2, 0)变换为(H x W x C)，之后才能用于plt显示
# plt.show()

# 法（2）、将tensor变为PIL格式，用于plt输出。
# 需要定义 tensor >> PIL 的方法，但无需调整shape
# rev_transform = transforms.ToPILImage()      # 注意：要先定义tensor转化为PIL格式的方法rev_transform
# img_tensor = (img_tensor * 0.5) + 0.5
# img_new_pil = rev_transform(img_tensor)
# plt.imshow(img_new_pil)
# plt.show()

# 【附 17】自动生成nd-array，直接plt出来
# import numpy as np
# import matplotlib.pyplot as plt
# a = np.arange(100).reshape(10, 10)
# print(a)
#
# plt.figure()
# plt.imshow(a, cmap="gray")
# plt.show()

# 【附 18】 generator生成器的yield用法
# # 使用yield说明使用函数构造了一个generator，yield其实是程序里的“协程”概念。
# # yield与传统函数定义的return相比，不同的地方在于yield后面跟的结果会被自动储存，放进generator，以供遍历使用。而return调用的时候会一次性输出。
# def gene_nums(nums):
#     for n in nums:
#         if n % 3 == 0:
#             yield 3 * 1000
#         elif n % 5 == 0:
#             yield 5 * 1000
#         else:
#             yield n * 1
#
# nums = list(range(10))
# # 【注意】gene_nums函数生成的是一个generator。print显示<generator object gene_nums at xxx>
# print(gene_nums(nums))
# for i in gene_nums(nums):
#     print(i)

# 【附 19】 opencv
# import cv2
# print(cv2.__version__)
# img = cv2.imread("./test_pics/lena_1.jpg")
# cv2.imshow("Lena", img)
# cv2.waitKey()

# 【附 20】 命令行参数解析工具
# 【作用】：当python脚本通过命令行运行时，可让用户输入一些参数值，这些参数可以被脚本程序读取使用。
# 【意义】：【类似input的用户交互】，法2的argparse在写一些公用脚本的时候经常用到，它可以很方便地让别人明白，你的程序需要哪些参数，它们各自的意义是什么。

# 法1 使用sys.argv（简易版的argparse）
# sys.argv其实就是一个列表，保存的元素为用户通过外部cmd命令行（或anaconda prompt）调用python脚本时输入的参数。
# 命令行输入样例：python python_learn.py 第一个参数 第二个参数 ...

# 第一步：写好脚本，保存为python_learn.py
# import sys
# print("第一个参数：", sys.argv[1])  # 在命令行界面显示输入的第一个参数
# print("第二个参数：", sys.argv[2])  # 在命令行界面显示输入的第二个参数
# print(sys.argv[0])
# print(sys.argv)
# 第二步：在anaconda prompt中使用
# 输入：
# (base) E:\0.learn to code\python_learn>python python_learn.py 你好 李雷
# 输出：
# 你好
# 李雷
# python_learn.py
# ['python_learn.py', '你好', '李雷']

# 法2 使用argparse
## argparse是python自带的命令行参数解析包，可以用来方便地读取命令行参数。

# 第一步：写好脚本，保存为python_learn.py
# （1）生成一个argparse解析器对象，并写上description描述信息。
# 通过在命令行输入python python_learn.py -h，可显示【description】和【可选参数列表optional arguments】
# import argparse
# parser = argparse.ArgumentParser(description="argparse测试样例")
# （2）通过add_argument方法，为解析器设置需要的参数名称，分别命名为name和age，通过在命令行输入【-t_name 参数值】和【-age 参数值】来赋值
# parser.add_argument('-t_name', default='Leo')  # 若不输入参数值，name默认值为"Leo"
# parser.add_argument('-age', default=20)      # 若不输入参数值，age默认值为20
# （3）通过parse_args方法，获取用户输入的参数
# args = parser.parse_args()
# （4）对获取的参数值进行的其他操作
# print(args)                                  # 打印所有参数名及参数值
# print(f"Hello {args.t_name} {args.age}")       # 通过【args.参数名】可获取参数值

# 第二步：在anaconda prompt中使用
# 输入 (以下三种输入皆可)：
# (base) E:\0.learn to code\python_learn>python python_learn.py -t_name Jacky -age 25
# (base) E:\0.learn to code\python_learn>python python_learn.py -na Jacky -ag 25    【注意】 -t_name 和 -age 可以省略若干字母
# (base) E:\0.learn to code\python_learn>python python_learn.py -n Jacky -a 25
# 输出：
# Namespace(age='25', t_name='Jacky')
# Hello Jacky 25

# 【附 21】 将大列表分割成小列表，返回一个生成器generator待遍历
# a_lst = [i for i in range(1, 13)]
# print(a_lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
# def split_list(a_lst, splited_len):
#     for i in range(0, len(a_lst), splited_len):
#         yield a_lst[i:i + splited_len]           # 把每次遍历产生的结果通过yield整合在一起，成为一个生成器generator
#
# for lst in split_list(a_lst, 4):               # 遍历split_list函数生成的generator
#     print(lst)

# 【附 22】 使用字符串str串联seq序列
# 【注意】这个seq序列中的元素必须全部为字符串str
# 例1：
# str = "-"
# seq = ["a", "8", "c"]
# print(str.join(seq))
# 例2：
# lst = ["l", "e", "o"]
# print("".join(lst))

# lst = ["l", "e", "o"]
# print(lst.index("o"))
# print(lst.__len__())


# 【附 23】 带有可变参数的函数
# def func1(*num):  # 使用*num可变参数，用于接收不定数量的实参
#     return num    # 如果接收了多个实参，这里将返回一个元组，可对元组进行遍历等操作
#
# def func2(*num):
#     return sum(num)
#
# print(func1(2, 4, 6, 9))
# print(func2(2, 4, 6, 9))

# 【附 24】装饰器decorator

# 一、概述

# 1、本质
# 装饰器本质上是一个 【Python函数或类】。
# 它可以让被装饰的【函数/类】（简称“原函数”）在不需要做任何代码修改的前提下增加额外功能，装饰器的返回值也是一个【函数/类】。

# 2、作用
# 它经常用于有切面需求的场景，比如：【插入日志、性能测试、事务处理、缓存、权限校验等场景】，装饰器是解决这类问题的绝佳设计。
# 有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码到装饰器中并继续重用。
# 概括的讲，装饰器的作用就是为已经存在的函数/类添加额外的功能。

# 3、定义装饰器及其使用的核心结构【重要】
# （1）函数型装饰器
# def 装饰器函数名称(func):         # func将传入原函数名作为实参
#     <语句>
#     def wrapper(形参):           # 为了使得装饰器对各类不同原函数通用，这里的形参通常写不定参数(*args, **kwargs)
#         <包裹语句 1>
#         func(形参)
#         <包裹语句 2>
#     return wrapper

# （2）类装饰器
# Class 装饰器类名:
#     def __init__(self, func):   # func将传入原函数名作为实参
#         self.func = func
#     def __call__(self, 形参):
#         <包裹语句 1>
#         self.func(形参)
#         <包裹语句 2>

# （3）装饰并调用原函数
# @装饰器函数名/类名    ---> 【核心重点】相当于执行：原函数名 = 装饰器函数名/类名(func=原函数名)，逻辑是先传入原函数名，在后续代码中再定义原函数的具体内容
# def 原函数名(形参):
#     <主代码语句>
# 原函数名(实参)       ---> 【注意】这里调用的已经不是原来的函数<主代码语句>了，实际是在调用wrapper(实参)！！

# 二、原函数不带参数的运用案例

# 例如有这样的需求：打印0-10000这几个数字，想要看打印的效率怎么样。
# 原函数如下：
# def prn_nums():
#     for i in range(10001):
#         print(i)
# prn_nums()

# 1、法 1 直接改造原有函数
# 我们完全可以调用一个python的time库，截取运行前后的时间，得到运行效率。
# import time
#
# def prn_nums():
#     t1 = time.time()
#     for i in range(10001):
#         print(i)
#     t2 = time.time()
#     print(f"运行时间：{t2 - t1}")
#
# prn_nums()
#
# 【法 1小结】
# 可以发现此时运行程序的时间是0.04s。
# 但是，如果有成千个相同的需求，难道我们每次都要改造原有的函数？
# 事实上在工作中很多原函数代码是不允许修改的，且每次修改原函数效率也很低，所以我们引入【装饰器】！！

# 2、法 2 使用简单装饰器
# （1）构建装饰器函数
# import time
#
# def display_time(func):  # display_time就是一个装饰器函数，最外层只用于【传入原函数名】以及【返回内部函数名】，在这里传入原函数名
#     def wrapper():       # 装饰器必须要设置一个内部包裹的函数，通常命名为wrapper，根据需求，用各种插入日志、性能测试等代码包裹原函数
#         t1 = time.time()
#         func()           # 把【原函数名prn_nums】当做参数传递进来时，执行func()就相当于执行prn_nums()
#         t2 = time.time()
#         print(f"运行时间：{t2 - t1}")
#     return wrapper       # 装饰器函数最外层返回【内部函数名wrapper】，注意：这里wrapper并没有被调用，只是返回函数名而已！！！！
#
# （2）原函数
# def prn_nums():
#     for i in range(10001):
#         print(i)
#
# （3）函数调用
# prn_nums = display_time(prn_nums)  # 【重要】这一步相当关键，因为display_time(func)返回wrapper，所以这里相当于wrapper赋值给了prn_nums
# prn_nums()                         # 由于上面的赋值操作，执行prn_nums()相当于执行 wrapper()

# 【法 2小结】
# display_time就是一个装饰器，它是一个普通的函数，把真正的主函数 func 包裹在其中，看起来像 prn_nums 被 display_time装饰了一样。
# 执行时，prn_nums = display_time(prn_nums)赋值操作非常重要，使得之后的操作中，直接调用 prn_nums() 即可得到想要的结果！
# 在这个例子中，函数进入和退出时 ，被称为一个横切面，这种编程方式被称为面向切面的编程。

# 2、法 3 使用【语法糖 “@符号”】进一步简化
# （1）构建装饰器函数
# import time
#
# def display_time(func):
#     def wrapper():
#         t1 = time.time()
#         func()
#         t2 = time.time()
#         print(f"运行时间：{t2 - t1}")
#     return wrapper
#
# （2）原函数
# @display_time     # 在此处执行prn_nums = display_time(prn_nums)，【注意】这里先将函数名prn_nums传入了装饰器，prn_nums函数的具体内容后面再定义
# def prn_nums():
#     for i in range(10001):
#         print(i)
#
# （3）函数调用
# prn_nums()        # 【注意】这里调用的已经不是原来的prn_nums函数了，而是执行wrapper()
#
# 【法 3小结】
# （1）装饰器语法糖的作用1：
# 原函数【调用方式不变】：省去法2的 prn_nums = display_time(prn_nums) 赋值操作，直接调用 prn_nums() 即可得到想要的结果。
# 原函数【源代码未修改】：原函数prn_nums无需任何修改，在定义之前加上装饰器语法糖即可。
# （2）装饰器语法糖的作用2：
# 如果我们有其他的类似函数，可以继续调用已定义好的装饰器来修饰原函数，而不用重复修改原函数或者增加新的封装。提高了程序的可重复利用性，增加程序可读性。
# （3）python函数的独特性：
# 装饰器在 Python 使用如此方便都要归因于 Python 的函数能像普通的对象一样能作为参数传递给其他函数，可以被赋值给其他变量，可以作为返回值，可以被定义在另外一个函数内。
#
# 三、原函数带参数的运用案例
#
# 1、原函数含单一参数
# import time
#
# def decorator(func):
#     def wrapper(num):
#         t1 = time.time()
#         func(num)
#         print(f"运行时间：{time.time() - t1}")
#     return wrapper
#
# @decorator         # 此处执行prn_nums = decorator(prn_nums)，【注意】这一步prn_nums并没有带自己的参数num传入decorator函数，因为prn_nums函数具体内容在后面才定义
# def prn_nums(num):
#     for i in range(0, num):
#         print(i)
#
# prn_nums(100001)   # 相当于执行wrapper(100001)

# 2、原函数含多参数
# import time
#
# def decorator(func):
#     def wrapper(*args):   # 这里的形参可以直接用*args代替start, end, step
#         t1 = time.time()
#         func(*args)       # 这里的形参可以直接用*args代替start, end, step
#         print(f"原函数'{func.__name__}'的运行时间：{time.time() - t1}")  # func对象调用魔法方法__name__，输出func的函数名
#     return wrapper
#
# @decorator
# def nums_test(start, end, step):
#     for n in range(start, end, step):
#         print(n)
#
# nums_test(10, 100001, 1000)

# 3、原函数含多参数，且包含关键字参数
# import time
#
# def decorator(func):
#     def wrapper(*args, **kwargs):    # **kwargs保证了原函数在使用时可以传入关键字参数
#         t1 = time.time()
#         func(*args, **kwargs)        # **kwargs保证了原函数在使用时可以传入关键字参数
#         print(f"原函数'{func.__name__}'的运行时间：{time.time() - t1}")  # func对象调用魔法方法__name__，输出func的函数名
#     return wrapper
#
# @decorator
# def nums_test(start, end, step):
#     for n in range(start, end, step):
#         print(n)
#
# nums_test(10, step=55, end=100001)  # 以关键字形式传入end和step

# 四、@decorator(参数)形式传入参数 --- 使用外层函数包裹装饰器

# 在原有装饰器基础上之上，在最外层嵌套一个函数。最外层函数中定义一个参数，可在最外层代码引用该参数。
# 装饰器的语法允许我们在调用时，提供其它参数，比如 @decorator(参数)。这样，就为装饰器的编写和使用提供了更大的灵活性

# import time
#
# def display_time(str):
#     print(str)
#     def decorator(func):
#         def wrapper(num):
#             t1 = time.time()
#             func(num)
#             t2 = time.time()
#             print(t2 - t1)
#         return wrapper
#     return decorator    # 【注意】 最外层必须返回decorator，否则生成的decorator装饰器函数无法保存在内存中，后续就无法调用
#
# @display_time("Test is running!!")  # 这里执行的内容在下面具体解释
# def prn_nums(num):
#     for i in range(num):
#         print(i)
#
# prn_nums(100000)

# 【特别注意】
# Python解释器在执行 @display_time("running") 代码时包含两大步骤：
# 1、第一步：执行最外层display_time函数
# （1）str = "running"传入display_time函数，执行最外层的print(str)；
# （2）执行 def decorator(func)，构建一个decorator装饰器函数，返回wrapper；
# （3）返回decorator装饰器函数，保存到内存，供后续调用；
# 2、第二步：装饰器的常规使用
# 原函数名prn_nums传入decorator装饰器函数，再赋值给原函数名：prn_nums = decorator(prn_nums)

# 【小结】
# 最外层的display_time函数实际上是对原有装饰器decorator的一个函数封装，并返回一个装饰器decorator。我们可以将它理解为一个含有参数的闭包。
# 当我们调用的时候，Python 能够发现这一层的封装，并把参数传递到装饰器的环境中。

# 五、类装饰器
# 装饰器不仅可以是函数，还可以是类，相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。
# 使用类装饰器主要依靠类的魔法方法__call__。

# import time
#
# class Deco:                     # 【注意1】相当于函数型装饰器的外层 def decorator(func):
#     def __init__(self, func):
#         self._func = func
#
#     def __call__(self, *args):  # 【注意2】相当于函数型装饰器的 def wrapper(*args):
#         t1 = time.time()
#         self._func(*args)
#         print(f"运行时间：{time.time() - t1}")
#
# @Deco                           # 【注意3】这里执行prn_nums = Deco(prn_nums)，传入函数名prn_nums创建Deco类的实例prn_nums
# def prn_nums(num):
#     for i in range(num):
#         print(i)
#
# prn_nums(100001)                # 由于定义了魔法方法__call__，实例prn_nums可以像普通函数一样调用，等同于类方法的常规调用方式：prn_nums.__call__(100001)

# 【附 25】拆分文件名和文件扩展名
# import os
# pic_name, pic_extension = os.path.splitext("nihao.jpg")
# print(pic_name)
# print(pic_extension)

# 【附 26】生成强加密的随机数
# secrets是python3.6加入到标准库的,使用secrets模块，可以生成适用于处理机密信息（如密码，帐户身份验证，安全令牌）的加密强随机数。
# secrets.token_hex(n)返回十六进制随机文本字符串。nbytes表示有多少个字节（bytes）。
# import secrets
# random_name = secrets.token_hex(nbytes=8)
# print(random_name)

# 【附 27】将信息加密生成token，以及token的解密
# 通常用于将可信的信息传入不可信的环境中，比如在用户需要重置密码时使用
# 假设flask的初始设置中：app.config["SECRET_KEY"] = '7429814508655a515c27275990a1613f'

# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# # （1）设置加密器
# s = Serializer('7429814508655a515c27275990a1613f', expires_in=20)
# # （2）准备需要加密的信息
# sample_data = {"user_id": 18}
# # （3）将准备的信息加密放进token中
# token = s.dumps(sample_data).decode("utf-8")
# print(token)
# # （4）解析token并提取信息
# def verify_token(token):
#     s = Serializer('7429814508655a515c27275990a1613f')
#     # 利用try...except捕捉异常，except后边通常应该加上具体的“异常名称”，这里没写
#     try:
#         user_id = s.loads(token)["user_id"]
#     except:
#         return None  # 如果因为token过期、token错误等各种情况，解析不出user_id，则返回None
#     return user_id

# 命令行运行例子：
# >>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# >>> s = Serializer("KEYsdff34f2", expires_in=10)     ------------- > 我们定义了token的有效期是10秒钟
# >>> token = s.dumps({"user_id":20}).decode("utf-8")
# >>> s.loads(token)
# {'user_id': 20}
# >>> s.loads(token)
# {'user_id': 20}
# >>> s.loads(token)
# {'user_id': 20}
# >>> s.loads(token)  ------------- > 由于我们定义了token的有效期是10秒钟，因此10秒之后再解析会报错Signature expired
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "C:\Users\ASUS\Anaconda3\lib\site-packages\itsdangerous\jws.py", line 205, in loads
#     date_signed=self.get_issue_date(header),
# itsdangerous.exc.SignatureExpired: Signature expired
# >>> token  ------------- > 10秒之后仍然可以打印出token的值，但是已经无法解析了，该token失效
# 'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU5NjkwMjQwNiwiZXhwIjoxNTk2OTAyNDE2fQ.eyJ1c2VyX2lkIjoyMH0.2hzBGh4kpH0Juz0gO35MTKemxnKdLWoPIo6SizMegSHi-K-f3SJQGsrlMFAgIZpEb08HuG_x4_E8F93Ran3w2w'

# 【附 28】os模块读取环境变量
# 环境变量
# 【作用】将一些敏感的数值添加到环境变量中，是为了保密，使其不直接在代码中展示出来
# 【添加】系统属性 --> 高级 --> 环境变量 --> ASUS的用户变量处手动新建
# 【提取】使用os.environ.get()获取提前添加环境变量值
# 【注意】新添加的环境变量需要重启之后，才能获取到值！！！！！

import os
# 1、遍历并获取所有系统变量+用户变量
# env_dist = os.environ
# for key in env_dist:
#     print(f"{key}:{env_dist[key]}")

# 2、获取已添加的环境变量值
# 【注意】新添加的环境变量需要重启之后，才能获取到值！！！！！
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

print(SECRET_KEY)
print(SQLALCHEMY_DATABASE_URI)
print(MAIL_USERNAME)
print(MAIL_PASSWORD)

class Stu:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"名字：{self.name}, 年龄：{self.age}"

    def __call__(self, score):
        print(f"Score of {self.name} is {score}")

    def run(self):
        print(self.name, "is running!")

stu1 = Stu("Leo", 18)
print(stu1)
stu1.run()
stu1(11)


