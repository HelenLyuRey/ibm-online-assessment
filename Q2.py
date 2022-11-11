import pandas as pd

df = pd.read_csv("data.txt", sep=" ",skiprows=1,header=None)
df2 = df.set_axis(['index','status', 'err_msg'], axis=1, inplace=False)

status = all(df2['status']==True)

if (status == True):
    print("Yes")
else:
    print("No")
    msg_list = [x for x in list(df2['err_msg']) if str(x) != 'nan']
    print(' '.join(msg_list))