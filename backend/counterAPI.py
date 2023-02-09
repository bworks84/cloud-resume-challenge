import boto3
import os
import json
from boto3.dynamodb.conditions import Key

# get environment variable for database
ddbName = os.environ["dbName"]

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(ddbName)


# then increment the count value

def lambda_handler(event, context):
    response = table.get_item(
        Key={
            'id': 'site',
        })
    count = response["Item"]["visits"]
    print("Get Response = ", response)
    print("Count = ", count)

    # increment count value
    new_count = count + 1
    response = table.update_item(
        Key={'id': 'site'},
        UpdateExpression='set visits = :c',
        ExpressionAttributeValue={':c': new_count},
        ReturnValues='ALL_NEW'
    )

    # Headers for API calls
    # 'body' will be used in js script for front end
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type, X-Amz-Date, Author',
            'Access-Control-Allow-Credentials': 'true',
            'Control-Type': 'application/json'
        },
        'body': int(count),
    }
