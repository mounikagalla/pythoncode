import boto3
import os

print ("test1")
s3= boto3.client('s3')
print ("test2")
#file= r'C:/Users/CHAITANYA/Desktop/temp.txt'
file= r'C:\Users\CHAITANYA\Desktop\temp.txt'
#file= r'.\temp.txt'
print (" check file")
if os.path.isfile(file):
    print (" file is present")
    with open (file,'rb') as data:
        print (" test4")
        s3.upload_fileobj(data,'mounikabucket486','sample_folder')
        print (" file uploaded")
else:
    print (" file not present")
print ("test3")