import boto3
s3=boto3.client('s3')

fileName='0.jpg'
bucket='amanmausam'
s3.upload_file(fileName,bucket,fileName)    
   