import time
import os
import shutil
from termcolor import colored


# ********************************************************************************
image_extensions = ['.jpg', '.JPG', '.png', '.jpeg', '.gif', '.eps', '.bmp', '.tif', '.tiff']
video_extensions = ['.mp4', '.ogg', '.wmv', '.3gp']

zip_folder = "D:\\Myfolders\\zip_folders"
images = "D:\\MyFolders\\Images"
pdfs = "D:/MyFolders/PDFs"
htmls = "D:/MyFolders/HTMLs"
documents = "C:/Users/Administrator/Documents/Docs"
miscellaneous = "D:/MyFolders/Miscellaneous"
videos = "D:/MyFolders/Videos"
text_files = "D:/MyFolders/TextFiles"
apps = "C:/Users/Administrator/Downloads/Executables"

# ******************************************************************************************


def automated_file_transfer(origin):
	os.chdir(origin)
	for f in os.listdir():
		file_name, extension = os.path.splitext(f)
		try:
			if extension in image_extensions:
				shutil.move(f, images)
			elif extension == '.pdf':
				shutil.move(f, pdfs)
			elif extension == '.zip':
				shutil.move(f, zip_folder)
			elif extension == '.html':
				shutil.move(f, htmls)
			elif extension == '.docx':
				shutil.move(f, documents)
			elif extension == '.txt':
				shutil.move(f, documents)
			elif extension in video_extensions:
				shutil.move(f, videos)
			elif extension == '.exe':
				shutil.move(f, apps)
		except shutil.Error:
			print(colored("(---->ERROR)~ An error occured, could not move the file.", 'yellow'))
			

path = "C:\\Users\\Administrator\\Downloads"


if __name__ == '__main__':
	automated_file_transfer(path)

