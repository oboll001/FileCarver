import re
import sys
#
#
#Finds all the files in a specified type
#
#
#
#
#This method is the jpeg flag
def findJPEG(data):
    jpeg_header = b'\xff\xd8\xff'
    jpeg_footer = b'\xff\xd9'
    jpeg_head_list = [match.start() for match in re.finditer(re.escape(jpeg_header), data)]
    jpeg_foot_list = [match.start() for match in re.finditer(re.escape(jpeg_footer), data)]
    i = 0
    while (i < len(jpeg_head_list)):
        subdata = data[jpeg_head_list[i]:jpeg_foot_list[i]]
        carveFileName = "Image"+str(i)+".jpg"
        carve_obj = open(carveFileName, 'wb')
        carve_obj.write(subdata)
        carve_obj.close()
        i = i+1
        print("Found a jpeg and carving it to "+carveFileName)
#This method is the pdf flag
def findPDF(data):
    pdf_header = b'\x25\x50\x44\x46'
    pdf_footer = b'\x45\x4f\x46\x0a'
    pdf_head_list = [match.start() for match in re.finditer(re.escape(pdf_header), data)]
    pdf_foot_list = [match.start() for match in re.finditer(re.escape(pdf_footer), data)]
    i = 0
    while (i< len(pdf_head_list)):
        subdata = data[pdf_head_list[i]:pdf_foot_list[i]]
        carveFileName = "Carve"+str(i)+".pdf"
        carve_obj = open(carveFileName, 'wb')
        carve_obj.write(subdata)
        carve_obj.close()
        i = i+1
        print("Found a pdf and carving it to "+carveFileName)



#Finds all flags
index = len(sys.argv)
x = 0
fileName = "File not Found"
fileFound = False
pdfFlag = False
jpgFlag = False
while(x < index -1):
    if(sys.argv[x] == '-h'):
        print("To input a file, run the file with flags"
              "\nuse the flag '-f' followed with the input data file and"
              "\nuse '-t' followed by 'pdf' or 'jpg' to get all pdf or jpg files.")
    elif(sys.argv[x] == '-f'):
        fileName = sys.argv[x + 1]
        fileFound = True
    elif(sys.argv[x] == '-t'):
        if(sys.argv[x+1] == "jpg"):
            jpgFlag = True
        elif(sys.argv[x+1]=="pdf"):
            pdfFlag = True
    x=x+1
#Use the appropriate flag responses if available
if(fileFound == True):
    file_obj = open(fileName, 'rb')
    data = file_obj.read()
    file_obj.close()
    if(jpgFlag == True):
        findJPEG(data)
    if(pdfFlag ==True):
        findPDF(data)
    if(pdfFlag == False and jpgFlag == False):
        print("The file was found, but no valid type has been specified"
              "\nUse '-t' followed by 'jpg' to find all jpeg files"
              "\nUse '-t' followed by 'pdf' to find all pdf files")
else:
    print("\n No File Found. To input a file, run thr file with flags"
          "\n use the flag '-f' followed with the input data file and"
          "\n use '-t' followed by 'pdf' or 'jpg' to get all pdf or jpg files.")


