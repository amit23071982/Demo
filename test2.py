import boto3

s3 = boto3.resource('s3')
s3_object = s3.Bucket('your-bucket-name').objects('file_name).get()
print(s3_object)
print(s3_object['Body'].read().decode)

