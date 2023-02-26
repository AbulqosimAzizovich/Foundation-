

"""1) Stack e'lon qiling va uning musbat
va manfiy elementlar sonini toping."""

# class Stack:
#     def __init__(self):
#         self.lst = []
#         self.musbat = 0
#         self.manfiy = 0

#     def Append(self, obj):
#         self.lst.insert(0, obj)

#     def Delete(self):
#         if self.lst != []:
#             self.lst.pop(0)
#         else:
#             print("Bo'sh")

#     def First(self):
#         if self.lst != []:
#             return self.lst[0]
#         else:
#             print("Bo'sh")

#     def Musbat_manfiy(self):
#         for i in range(len(self.lst)):
#             print(self)
#             if self.First() >= 0:
#                 self.musbat += 1
#             elif self.First() < 0:
#                 self.manfiy += 1
#             self.Delete()
#         return self.musbat, self.manfiy


# stc = Stack()
# stc.Append(15)
# stc.Append(-25)
# stc.Append(17)
# stc.Append(5)
# stc.Append(15.6)
# stc.Append(-5)
# stc.Append(73)
# print("Musbat va manfiy", stc.Musbat_manfiy())


"""2) Stack e'lon qiling va uning o'rtadagi
elementini o'chiring.(Agar elementlar soni
toq bo'lsa o'rtadagi element o'chirilsin,
agar elementlar soni juft bo'lsa o'rtadagi
2ta element o'chirilsin)"""


# class Stack:
#     def __init__(self):
#         self.lst = []

#     def Append(self, obj):
#         self.lst.insert(0, obj)

#     def Delete(self):
#         if self.lst != []:
#             if len(self.lst) % 2 == 0:
#                 k = len(self.lst) // 2
#                 self.lst.pop(k-1)
#                 self.lst.pop(k-1)
#             else:
#                 k = len(self.lst) // 2
#                 self.lst.pop(k)
#         else:
#             print("Bo'sh")

#     def Show(self):
#         for i in self.lst:
#             print(i)


# sd = Stack()
# sd.Append(1)
# sd.Append(2)
# sd.Append(3)
# sd.Append(4)
# sd.Append(5)
# sd.Append(6)
# sd.Append(7)
# # sd.Append(8)
# # sd.Append(9)
# # sd.Append(10)

# sd.Show()
# print("*" * 25)
# sd.Delete()
# sd.Show()


"""3) Stack e'lon qiling va uning elementlarini
teskari tartibda joylashtiring"""


# class Stack:
#     def __init__(self):
#         self.lst = []

#     def Append(self, obj):
#         self.lst.append(obj)

#     def Append_reverse(self, obj):
#         self.lst.insert(0, obj)

#     def Reverse(self):
#         pass

#     def Show(self):
#         for i in self.lst:
#             print(i)


# sd = Stack()
# # sd.Append(1)
# # sd.Append(2)
# # sd.Append(3)
# # sd.Append(4)
# # sd.Append(5)
# sd.Show()
# print("*"*40)
# sd.Append_reverse(1)
# sd.Append_reverse(2)
# sd.Append_reverse(3)
# sd.Append_reverse(4)
# sd.Append_reverse(5)
# sd.Show()


"""4) Queue e'lon qiling va navbatdagi oxirigi
elementiga teng bo'lgan elementlarni barchasini o'chiring"""


# class Queue:
#     def __init__(self):
#         self.lst = []

#     def Append_front(self, obj):
#         self.lst.insert(0, obj)

#     def Append_back(self, obj):
#         self.lst.append(obj)

#     def Delete(self):
#         k = self.lst[-1]
#         for i in self.lst:
#             if k == i:
#                 self.lst.remove(i)

#     def Show(self):
#         print(self.lst)


# q1 = Queue()
# q1.Append_front(20)
# q1.Append_front(10)
# q1.Append_front(50)
# q1.Append_back(40)
# q1.Append_back(50)
# q1.Delete()
# q1.Show()


"""5) Queue e'lon qiling va uning o'rtasiga '+++'
elementini qo'shib qo'ying. (Agar elementlar soni
juft bo'lsa o'rtadagi 2ta element o'rtasiga
joylashtiring, agar toq bo'lsa o'rtadagi
elementning o'rniga joylashtiring)"""


# class Queue:
#     def __init__(self):
#         self.lst = []

#     def Append(self, obj):
#         self.lst.append(obj)

#     def Plus(self):
#         k = len(self.lst) // 2
#         if self.lst != []:
#             k = len(self.lst) // 2
#             if len(self.lst) % 2 == 0:
#                 self.lst.insert(k, "+++")

#             else:
#                 self.lst[k] = "+"
#         else:
#             print("Bo'sh")

#     def Show(self):
#         print(self.lst)


# q1 = Queue()
# q1.Append(10)
# q1.Append(20)
# q1.Append(30)
# q1.Append(40)
# q1.Append(50)
# q1.Append(60)
# q1.Plus()
# q1.Show()
