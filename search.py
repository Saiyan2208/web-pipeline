import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
    # TODO implement
    table = dynamodb.Table('qguru-search')
    #scan_table("qguru-search", 'name', event['search'])
    print("printing event")
    print(event['var'])
    response = table.scan(FilterExpression=Attr('name').contains(event['var']))
    print(response["Items"])
    return response
