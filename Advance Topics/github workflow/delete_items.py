import boto3
from munch import Munch

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='eu-central-1')

def get_secret():
    secret_name = "github-admin-token" 
    client = boto3.client("secretsmanager")
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    secret_val = Munch(get_secret_value_response)
    return secret_val.SecretString    

token = get_secret()

def scan_table(table_name):
    response = dynamodb.scan(TableName=table_name, Limit=10)
    items = response.get('Items', [])
    return items

def delete_item_from_table(table_name, key):
    print(f"Deleting item with key: {key}")  # Debugging
    dynamodb.delete_item(TableName=table_name, Key=key)

def delete_all_items_from_table(table_name, primary_keys):
    items = scan_table(table_name)
    for item in items:
        key = {k: v for k, v in item.items() if k in primary_keys}
        print(f"Key to delete: {key}")  # Debugging
        delete_item_from_table(table_name, key)
    return len(items)

def check_table_and_empty_if_needed(table_name, primary_keys):
    items = scan_table(table_name)
    if not items:
        print("Table is already empty.")  # Debugging
        return True
    else:
        emptied = delete_all_items_from_table(table_name, primary_keys)
        print(f"Emptied: {emptied}")  # Debugging
        if emptied > 0:
            return False
        else:
            return True

def test_table_empty_or_emptied():
    table_name = 'package-acc'
    primary_keys = ['id', 'name'] 
    is_empty = check_table_and_empty_if_needed(table_name, primary_keys)
    print(f"Is table empty or emptied: {is_empty}")  # Debugging
    assert is_empty

test_table_empty_or_emptied()
