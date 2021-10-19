import shutil
import datetime
import stat
import os
import time
import glob


now = datetime.datetime.now()
timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))
original = r'/home/pi/Downloads/buz.py'
target = r'/home/pi/Downloads/cronbackup/buz.py'+timestamp+'.zip'
shutil.copyfile(original, target)

path, dirs, files = next(os.walk("/home/pi/Downloads/cronbackup"))
list_of_files = glob.glob('/home/pi/Downloads/cronbackup/*')

file_count = len(files)
print (file_count)

max_files = 8
if (file_count > max_files):
    min_file = min(list_of_files, key=os.path.getctime)
    os.remove(min_file)
    print ("old data deleted")
else:
    print("no files more than 8")