no_of_lines = 4
lines = []
for i in range(no_of_lines):
    lines.append(input())
# print(lines)

# lines = ['5', 'XL XXXXXXXXXL XXS M XXS', '4', 'L M L XXS']

in_shop = lines[0]
size_shop = lines[1].split(' ')
num_req = lines[2]
size_req = lines[3].split(' ')

check_list = []

for size in size_req:
    if size in size_shop:
        check_list.append(True)
    if size[-1] == 'L':
        for cur_size in size_shop:
            if cur_size[-1] == "L" and len(cur_size)>=len(size):
                check_list.append(True)
                break
    if size[-1] == "M":
        for cur_size in size_shop:
            if cur_size[-1] == "L":
                check_list.append(True)
                break
    if size[-1] == "S":
        for cur_size in size_shop:
            if cur_size[-1] == "L" or cur_size == "M" or (cur_size[-1] == "S" and len(cur_size)<=len(size)):
                check_list.append(True)
                break
    else:
        print(size)
        check_list.append(False)

if all(check_list == True):
    print('Yes')