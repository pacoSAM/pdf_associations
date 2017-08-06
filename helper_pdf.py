import os
import Image


def convert_image_to_pdf(image, extension):
    """converts your image in your extension"""
    file = os.path.splitext(image)[0] + "." + str(extension)
    outfile = increment_filename_ifexit(file, extension)
    conver = ("convert %s %s") % (image, outfile)
    if os.system(conver) == 0:
        return outfile
    else:
        print("cannot convert", image)


def check_format(file_list):
    """Returns True if files is pdf or image"""
    checker = True
    for file in file_list:
        if os.path.splitext(file)[1] != ".pdf":
            try:
                Image.open(file)
            except IOError:
                checker = False
                break
    return checker


def increment_filename_ifexit(filename, extension):
    """increments filename: return new name if there is the same filename in your repository"""
    i = 1
    while True:
        if os.path.exists(filename) == True:
            outfile = os.path.splitext(
                filename)[0] + "[%s]." % i + str(extension)
            if os.path.exists(outfile) == False:
                break
            i += 1
        else:
            outfile = filename
            break
    return outfile


def combine_in_one_pdf(list_pdf, output_file_name):
    """create new file that contain all pdfs"""

    outfile = os.path.splitext(output_file_name)[0] + ".pdf"
    outfile = increment_filename_ifexit(outfile, "pdf")
    conver = ("convert " + " ".join(list_pdf) +" "+ outfile)
    if os.system(conver) == 0:
        return outfile
    else:
        return False


def get_all_file_type(extension, path):
    """ Returns a list of filenames for all files with the extension selected in a directory. """
    form = "." + str(extension)
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(form)]
