import os
import Image


def convert_image_to_pdf(image, extension):
    """convert your image in your extension"""
    file = os.path.splitext(image)[0] + "." + str(extension)
    outfile = verif_name(file, extension)
    conver = ("convert " + "%s" + " %s") % (image, outfile)
    if os.system(conver) == 0:
        return outfile
    else:
        print("cannot convert", image)


def check_format(file_list):
    """Return True if files is pdf or image"""
    checker = True
    for file in file_list:
        if os.path.splitext(file)[1] != ".pdf":
            try:
                Image.open(file)
            except IOError:
                check = False
                break
    return checker


def verif_name(filename, extension):
    """increment filename: return new name if they is the same filename in your repository"""
    i = 1
    while True:
        if os.path.exists(filename) == True:
            outfile = os.path.splitext(
                filename)[0] + "(%s)." % i + str(extension)
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
    conver = ("convert " + " ".join(list_pdf) + outfile)
    if os.system(conver) == 0:
        return outfile
    else:
        return False


def get_all_file_type(extension, path):
    """ Returns a list of filenames for all jpg images in a directory. """
    form = "." + str(extension)
    return [os.path.join(f) for f in os.listdir(path) if f.endswith(form)]
