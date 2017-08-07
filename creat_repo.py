from os  import mkdir
from os import path as managePath

# repo = "PDF_COMBINE"

def chek_existdir(path_repo):
	"""Chek if your path exist in current directory, if not it's going to creat it"""
	if managePath.isdir(path_repo) == False:
		mkdir("PDF_COMBINE")

