'''from datetime import datetime
date_time_str = '18/09/19 01:55:19'

date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')


print ("The type of the date is now"),  type(date_time_obj)
print ("The date is", date_time_obj)'''
from os import listdir
import os
list_of_files = listdir(r"C:\Users\Sandeep\PycharmProjects\series1\data\pickle files")
pat =r"C:\Users\Sandeep\PycharmProjects\series1\data\pickle files"
list_of_col = ["M01AB", "M01AE", "N02BA", "N02BE", "N05B", "N05C", "R03", "R06"]
m = {}
for i in range(8):
    m[list_of_col[i]]=list_of_files[i]
print(m)
print(os.path.join(pat, "r.txt"))



