import unittest
import os
from os import listdir, getcwd
from PyPDF2 import PdfFileReader, utils
from path_test import PATH_FOR_INCREMENT_NAME, CONVERT_PATH
from helper_pdf import *


def get_file_expected(filename):
    """returns the new filename if name already exist """
    decompose_file = os.path.splitext(filename)
    outfile = decompose_file[0]
    extension = decompose_file[1]
    maxim = len(outfile) - 1

    name_except = outfile + "(1)" + extension

    if outfile[maxim] == ")":
        i = 1
        while True:
            try:
                int(outfile[maxim - i])
                i += 1
            except Exception:
                break
        if outfile[maxim - i] == "(":
            n = int(outfile[maxim - i + 1:maxim])
            name_except = outfile[:n - 1] + "(%s)%s" % (n + 1, extension)

    return name_except, extension


def takefileList_inTestRepository(list_extension, path):
    """Returns a list contain all files in path  which have same extensions indicate in list_extension """
    list_file = []
    for extension in list_extension:
        list_file.extend(get_all_file_type(extension, path))

    return list_file


def verif_error_pdf(pdf):
    """check if pdf is readble"""
    try:
        PdfFileReader(pdf)
    except utils.PdfReadError:
        msg = str(pdf) + " is not PDF"
        raise utils.PdfReadError(msg)


class HelperTest(unittest.TestCase):
    """Test for principal function in helper_pdf.py"""

    def setUp(self):
        self.file_to_test = ''
        self.images_to_test = []
        self.files_to_combine = []

    def test_increment_filename_ifexit(self):
        """ test: to know if filename 'll be incremented if there are file which same name"""
        path_test = PATH_FOR_INCREMENT_NAME
        for file in listdir(path_test):
            elmt = get_file_expected(file)
            name_except = elmt[0]
            extension = elmt[1]
            rep = increment_filename_ifexit(name_except, extension)
            self.assertEqual(name_except, rep)

    def test_convert_image_to_pdf(self):
        """test: if file returned by function is a (pdf) else Error"""
        im_xtension = ["jpg", "png"]
        path = CONVERT_PATH
        self.images_to_test = takefileList_inTestRepository(im_xtension, path)

        for image in self.images_to_test:
            pdf = convert_image_to_pdf(image, "pdf")
            if pdf == None:
                self.assertIsNone(pdf)
            else:
                PdfFileReader(pdf)

    def test_combine_in_one_pdf(self):
        """test: if the output file exist , is a pdf and contain all elements combinate"""
        outfile = 'pacosam.pdf'
        file_xtension = ["jpg", "png", "pdf"]
        path = CONVERT_PATH
        self.files_to_combine = takefileList_inTestRepository(
            file_xtension, path)
        outfile = combine_in_one_pdf(self.files_to_combine, outfile)
        if outfile == False:
            self.assertIsTrue(outfile)
        if os.path.isfile(outfile) == True:
            self.assertRaises(utils.PdfReadError, verif_error_pdf(outfile))


if __name__ == "__main__":
    unittest.main()
