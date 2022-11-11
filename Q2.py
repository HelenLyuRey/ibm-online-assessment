# Q2 DEBUG0001. Dataset Validity

with open('data.txt') as topo_file:
    allValid = True
    errorCodes = []
    next(topo_file)
    for line in topo_file:
        new_line = line.rstrip('\n')
        line_list = new_line.split(' ')
        if (line_list[1] == 'false'):
            allValid = False
            errorCodes.append(line_list[2])

if (allValid == True):
    print("Yes")
else:
    print("No")
    print(' '.join(errorCodes))

# Second way, different from pseudo-code
# import pandas as pd

# df = pd.read_csv("data.txt", sep=" ",skiprows=1,header=None)
# df2 = df.set_axis(['index','status', 'err_msg'], axis=1, inplace=False)

# status = all(df2['status']==True)

# if (status == True):
#     print("Yes")
# else:
#     print("No")
#     msg_list = [x for x in list(df2['err_msg']) if str(x) != 'nan']
#     print(' '.join(msg_list))
