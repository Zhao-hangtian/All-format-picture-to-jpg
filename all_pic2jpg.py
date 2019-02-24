import os
from PIL import Image

# TOOLS FUNCTION
# CHECK AND CREATING FOLDER jpg AND png
def mkdir(path):
	if not os.path.exists(path):
		print("There is not folder [" + path + "], creating...")
		os.mkdir(path)
		print("created new folder [" + path + "] successfully!")

# CHECK IS FILE A IMAGE
def isValidImage(file_path_name):
	valid = True
	try:
		Image.open(file_path_name).verify()
	except Exception as e:
		valid = False
	return valid



# MAIN
if __name__ == '__main__':
	print(os.getcwd())
	mkdir("pic")
	mkdir("jpg")
	# CONVERT ( USE RELATIVE DIRECTION STRUCTURE )
	os.chdir(os.getcwd()+"\\pic")
	for file_path_name in os.listdir(os.getcwd()):
		# print(file_path_name)
		if isValidImage(file_path_name):
			img = Image.open(file_path_name)
			suffix = file_path_name.split(".")[-1]
			new_file_path_name = "..\\jpg\\" + file_path_name.replace(suffix, "jpg")
			os.chdir(os.getcwd())
			img.save(new_file_path_name)

