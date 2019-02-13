import boto3
s3 = boto3.client('s3', aws_access_key_id='AKIAIHOAGU4OQH6ZK4MA', aws_secret_access_key='TvpvnBbT6WCWemVQ7uqhcMkTcup7YF/2IpzXR4Cf')
print ("credentials")
s3.download_file('mounikabucket486','sample_folder/temp.txt','/Users/Chaitanya/Desktop/temp1.txt')
print ("file is downloaded")