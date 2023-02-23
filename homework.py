"""1 - Usul """

ls = [5, 1, 35, 21, 'salom', 5, 'A', 'Hayr', 12]

raqam = []
char = []
word = []

for i in ls:
    i = str(i)
    if i.isdigit():
        raqam.append(i)
    elif i.isalpha() and len(i) == 1:
        char.append(i)
    else:
        word.append(i)

a = []
raqam1 = []

for i in raqam:
    i = int(i)
    raqam1.append(i)


def SelectionSort(arr: list):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j

        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    print(arr)


SelectionSort(raqam1)


def SelectionSortWord(arr: list):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j

        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    print(arr)


SelectionSortWord(word)


def SelectionSortLetter(arr: list):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j

        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    print(arr)


SelectionSortLetter(char)


a.extend(raqam1)
a.extend(char)
a.extend(word)

print(a)

"""2 - Usul"""


l = [5, 1, 35, 21, 'salom', 5, 'A', 'z', 'Hayr', 12]
ls = []
lch = []
for i in range(len(l)-1, -1, -1):
    s = str(l[i])
    if s.isalpha() and len(s) == 1:
        lch.append(s)
        l.pop(i)
    elif s.isalpha():
        ls.append(s)
        l.pop(i)


def SelectionSort(arr: list):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]


SelectionSort(l)
SelectionSort(ls)
SelectionSort(lch)
l.extend(lch)
l.extend(ls)
print(l)
