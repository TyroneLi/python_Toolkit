import os

def renameFile(folderPath, specificFormat):
	for file_path in os.listdir(folderPath):
		os.path.splitext(file_path)[1] == specificFormat
		print(file_path)
		os.rename(folderPath+file_path, folderPath+"20181026_BV_"+file_path[0:-4]+specificFormat)

if __name__ == '__main__':
	folderPath = "/home/king/project/dataset/20181026-train_鹏鹏/JPEGImages/"
	specificFormat = ".jpg"
	renameFile(folderPath, specificFormat)