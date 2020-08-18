from wand.image import Image as wi
import os
from glob import glob
def pdf_jpg(folder,input_dir):
    for filename in os.listdir(folder):
        # print(filename)
        # working_file_name = filename.split('.')[-2]
        # working_file_name = working_file_name + str(".pdf")

        f_name = filename
        filename = str(folder)+str(filename)
        # print(filename)
        pdf =wi(filename=filename,resolution=300)
        i=1 #how much page want to convert 
        pdfImage = pdf.convert("jpeg")
        for img in pdfImage.sequence:
            page = wi(image=img)
            page.save(filename=str(f_name)+".jpg")
            if i==1:
                break

input_dir = "D:/Eigenlytics/pdf_jpg/siddhant/*/"
all_folder = glob(input_dir)
for folder in all_folder:
    pdf_jpg(folder,input_dir)
