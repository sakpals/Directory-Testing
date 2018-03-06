import nested_dir
import random_files
import os
import shutil
import random

def setup():
	random_files.setup()
	random_files.create_files()
	n_dir = nested_dir.NestedDir()
	n_dir.nested_unicode_100_to_900_dirs(depth=50, name_len=15)
	n_dir.nested_unicode_1000_to_9500_dirs(depth=50, name_len=25)
	n_dir.nested_unicode_10000_to_50000_dirs(depth=50, name_len=20)

def inject_files_into_folders(dir_loc, file_loc, num=None,interval=0):
	"""
	Puts specified number of files at specified number of intervals in nested directory structure.
	"""
	files = os.listdir(file_loc)
	count = 0
	for dir_name, dirs, files in os.walk(dir_loc):
		rand_num = random.randint(0,5)
		if count == interval:
			if num:
				for i in range(num):
					shutil.copy2(file_loc+random.choice(os.listdir(file_loc)), dir_name)
			else:
				for i in range(rand_num):
					shutil.copy2(file_loc+random.choice(os.listdir(file_loc)), dir_name)
			count = 0
		else:
			count += 1
	print('done')

if __name__ == '__main__':
    setup()
    inject_files_into_folders(dir_loc='./test_nested_dirs/unicode_100_to_900', file_loc='./test_files/',num=2,interval=0)
    inject_files_into_folders(dir_loc='./test_nested_dirs/unicode_1000_to_9500', file_loc='./test_files/',interval=2)
    inject_files_into_folders(dir_loc='./test_nested_dirs/unicode_10000_to_50000', file_loc='./test_files/',num=6, interval=2)
