#Q1 ALGO0001. Looking for Size

no_of_lines = 4
lines = []
for i in range(no_of_lines):
    lines.append(input())

# lines = ['5', 'XL XXXXXXXXXL XXS M XXS', '4', 'L M L XXS']

in_shop = lines[0]
size_shop = lines[1].split(' ')
num_req = lines[2]
size_req = lines[3].split(' ')


def change_size_to_num(lst):
    S = -1
    M = 0
    L = 1
    num_list = []
    for size in lst:
        if len(size) == 1:
            if size == "S":
                num_list.append(S)
            if size == 'M':
                num_list.append(M)
            if size == 'L':
                num_list.append(L)
        else:
            if size[-1] == 'L':
                num_list.append(L + len(size))
            if size[-1] == "S":
                num_list.append(S - len(size))
    return num_list

size_shop_num = change_size_to_num(size_shop)
size_req_num = change_size_to_num(size_req)

# XL XXXXXXXXXL XXS M XXS
# [3, 11, -4, 0, -4]
# L M L XXS
# [1, 0, 1, -4]
check_list = []
for size in size_req_num:
    # change to a size closest to the current size
    # For example, M change into M instead of XXXXXXXXXL
    if size in size_shop_num:
        check_list.append(True)
         # need to remove the size if it is given to another customer for exchange
        size_shop_num.remove(size)
    else:
        for size_shop in size_shop_num:
            if size <= size_shop:
                check_list.append(True)
                 # need to remove the size if it is given to another customer for exchange
                size_shop_num.remove(size_shop)
                break
if all(check_list) == True:
    print("Yes")
else:
    print("No")