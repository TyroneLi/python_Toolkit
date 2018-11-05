import os
import shutil

def removeFIles(srcAnnotationPath, srcFolderPath, dstFolderPath, specificFormat):
	count = 0
	for file_path in os.listdir(srcAnnotationPath):
		# print("file\n", file_path)
		os.path.splitext(file_path)[1] == specificFormat
		file_path = file_path[0:-4]
		file_path = file_path + ".jpg"
		fileName = file_path
		file_path = srcFolderPath + file_path
		count += 1
		shutil.move(file_path, dstFolderPath + fileName)
	print("coutn:\n", count)


if __name__ == '__main__':
	srcAnnotationPath = "/home/king/project/dataset/2018-10-24-train/Annotations"
	srcFolderPath = "/home/king/project/dataset/2018-10-24-train/JPEGImages/"
	dstFolderPath = "/home/king/project/dataset/2018-10-24-train/JPEGImagess/"
	specificFormat = ".jpg"
	removeFIles(srcAnnotationPath, srcFolderPath, dstFolderPath, specificFormat)
