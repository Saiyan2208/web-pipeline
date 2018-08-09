import boto3

def lambda_handler(event, context):
   # TODO implement
   res = boto3.client('dynamodb')
   response = res.scan(TableName="qgurudynamodb")
   return response
