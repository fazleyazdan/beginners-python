import boto3
from munch import Munch
import requests
import time

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='eu-central-1')
dynamodb_resource = boto3.resource('dynamodb', region_name='eu-central-1')

#! Function for fetching the Token from AWS
def get_secret():
    secret_name = "github-admin-token" 

    # Create a Secrets Manager client
    client = boto3.client("secretsmanager")

    # Retrieve the secret
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    secret_val = Munch(get_secret_value_response)
    return secret_val.SecretString    

token = get_secret()

#! Function for storing items from the table
def scan_table(table_name):
    table = dynamodb_resource.Table(table_name)
    response = table.scan()
    items = response.get('Items', [])
    return items    


#! Function for Deleting an item from the table
def delete_item_from_table(table_name, keys):
        table = dynamodb_resource.Table(table_name)
        with table.batch_writer() as batch:
            for key in keys:
                batch.delete_item(Key=key)


