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


#! Function for deleting all items from the table
def delete_all_items_from_table(table_name, primary_keys):
    items = scan_table(table_name)
    while items:
        keys = [{k: v for k, v in item.items() if k in primary_keys} for item in items]
        delete_item_from_table(table_name, keys)
        items = scan_table(table_name)


#! Function to check whether the table is empty or contains some data
def check_table_and_empty_if_needed(table_name, primary_keys):
    items = scan_table(table_name)
    if not items:
        return f"table already empty"
    else:
        delete_all_items_from_table(table_name, primary_keys)
        if len(items) > 0:
            return f"items not deleted, deleting again"
        else:
           return f"items deleted on second attempt"


#! Test case to check the table is empty or not
def test_table_empty_or_emptied():
    table_name = 'package-acc'
    primary_keys = ['id', 'name'] 
    print(check_table_and_empty_if_needed(table_name, primary_keys))

test_table_empty_or_emptied()