import os, random
def setup():
	if not os.path.exists('./test_files'):
			os.makedirs('./test_files')

def create_files():
	for i in range(3000):
		name = ''
		for j in range(85):
			name += chr(random.randint(1,5555))
		try:
			open('test_files/' + name, 'w')
		except Exception as e:
			print(e)
	

if __name__ == '__main__':
	setup()
	create_files()
