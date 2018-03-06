import os
import random
class NestedDir():
	def __init__(self):
		self.root_path = './test_nested_dirs/'

	def setup(self):
		if not os.path.exists(self.root_path):
			os.makedirs(self.root_path)

	def nested_alphabet_dirs(self):
		"""
		Creates nested directory structure of the alphabet. 
		"""
		path = "alphabet/a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z"
		if not os.path.exists(self.root_path+path):
			os.makedirs(self.root_path+path)	
			print("Done")

	def nested_increasing_length_name_dirs(self, depth):
		"""
		Creates nested directory of folders (random unicode names). The length of the name of each folder
		corresponds to the depth of the directory.
		"""
		dir_name = 'increasing_length/'
		folder_names = []
		name = ''
		path = ''
		starting_decimals = [98, 161, 191, 240, 281, 307, 350, 390, 422, 470, 522]
		for start in starting_decimals:
			# dir depth
			for i in range(1,depth+1):
				# name length (same as dir_depth)
				for j in range(start, start+i):
					name += chr(random.randint(1,100))
				folder_names.append(name)
				name = ''
			path = '/'.join(folder_names)
			if not os.path.exists(self.root_path+dir_name+path):
				os.makedirs(self.root_path+dir_name+path)	
				print("Done ", "starting_unicode: ", start,", depth: ", depth)
			path = ''
			folder_names = []

	def nested_unicode_100_to_900_dirs(self, depth, name_len):
		"""
		Creates nested directory of folders (random unicode characters within range 100-900) according to 			specified depth and name length of folders.
		"""
		dir_name = 'unicode_100_to_900/' 
		folder_names = []
		name = ''
		path = ''
		#dir depth
		for i in range(1,depth+1):
			# name length 
			for j in range(1,name_len+1):
				name += chr(random.randint(100,900))
			folder_names.append(name)
			name = ''
		path = '/'.join(folder_names)
		if not os.path.exists(self.root_path+dir_name+path):
			os.makedirs(self.root_path+dir_name+path)	
			print("Done ", "starting_unicode: 100",", depth: ", depth, ", len: ", name_len)
		path = ''
		folder_names = []

	def nested_unicode_1000_to_9500_dirs(self, depth, name_len):
		"""
		Creates nested directory of folders (random unicode characters within range 1000-9500) according to 			specified depth and name length of folders.
		"""
		dir_name = 'unicode_1000_to_9500/'
		folder_names = []
		name = ''
		path = ''

		#dir depth
		for i in range(1,depth+1):
			# name length
			for j in range(1,name_len+1):
				name += chr(random.randint(1000,9500))
			folder_names.append(name)
			name = ''
		path = '/'.join(folder_names)
		if not os.path.exists(self.root_path+dir_name+path):
			os.makedirs(self.root_path+dir_name+path)	
			print("Done ", "starting_unicode: 1000",", depth: ", depth, ", len: ", name_len)
		path = ''
		folder_names = []

	def nested_unicode_10000_to_50000_dirs(self, depth, name_len):
		"""
		Creates nested directory of folders (random unicode characters within range 10000-50000) according to 			specified depth and name length of folders.
		"""
		dir_name = 'unicode_10000_to_90000/'
		folder_names = []
		name = ''
		path = ''
		#dir depth
		for i in range(1,depth+1):
			# name length
			for j in range(1,name_len+1):
				name += chr(random.randint(10000,50000))
			folder_names.append(name)
			name = ''
		path = '/'.join(folder_names)
		if not os.path.exists(self.root_path+dir_name+path):
			os.makedirs(self.root_path+dir_name+path)	
			print("Done ", "starting_unicode: 10000",", depth: ", depth, ", len: ", name_len)
		path = ''
		folder_names = []

	def run(self):
		for i in range(1):
			self.nested_alphabet_dirs()

			self.nested_increasing_length_name_dirs(depth=3)
			self.nested_increasing_length_name_dirs(depth=3)
			self.nested_increasing_length_name_dirs(depth=3)
	
			self.nested_unicode_100_to_900_dirs(depth=5, name_len=40)
			self.nested_unicode_100_to_900_dirs(depth=1, name_len=10)
			self.nested_unicode_100_to_900_dirs(depth=5, name_len=80)
		
			self.nested_unicode_1000_to_9500_dirs(depth=5, name_len=25)
			self.nested_unicode_1000_to_9500_dirs(depth=1, name_len=5)
			self.nested_unicode_1000_to_9500_dirs(depth=5, name_len=30)

			self.nested_unicode_10000_to_50000_dirs(depth=5, name_len=20)
			self.nested_unicode_10000_to_50000_dirs(depth=1, name_len=5)
			self.nested_unicode_10000_to_50000_dirs(depth=5, name_len=35)
		
		
if __name__ == '__main__':
	nested = NestedDir()
	nested.setup()
	nested.run()
	    
