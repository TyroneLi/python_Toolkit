import os
'''
在folder_path中加载xml文件的路径，
得到Pascal数据集格式的TXT文件
'''

def listdir(folder_path, write_file_path):
	f = open(write_file_path, 'w')
	for file in os.listdir(folder_path):
		#file_path = os.path.join(path, file)
		file_path = file
		if os.path.isdir(file_path):
			listdir(file_path, list_name)
		elif os.path.splitext(file_path)[1] == '.xml':
			# list_name.append(file_path)
			print(file_path[0:-4])
			f.write(file_path[0:-4] + '\n')
	f.close()


if __name__ == "__main__":

	folder_path = "./Annotations"
	file = "20.txt"
	listdir(folder_path, file)

	