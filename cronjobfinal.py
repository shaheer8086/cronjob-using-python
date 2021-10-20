import shutil
import datetime
import stat
import os
import time
import glob


now = datetime.datetime.now()
#the backup file rename with timestamp
timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))
#the path of files you want to backup
original = r'/home/pi/Downloads/buz.py'
#the backup file converted to zip file
target = r'/home/pi/Downloads/cronbackup/buz.py'+timestamp+'.zip'
shutil.copyfile(original, target)
#the destination path of backup to be stored
path, dirs, files = next(os.walk("/home/pi/Downloads/cronbackup"))
list_of_files = glob.glob('/home/pi/Downloads/cronbackup/*')

file_count = len(files)
print (file_count)
#destination files count auto remove the 9th file if exist
max_files = 8
if (file_count > max_files):
    min_file = min(list_of_files, key=os.path.getctime)
    os.remove(min_file)
    print ("old data deleted")
else:
    print("no files more than 8")
