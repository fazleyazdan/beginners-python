import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='eu-central-1')

def scan_table(table_name):
    try:
        response = dynamodb.scan(TableName=table_name)
        items = response.get('Items', [])
        return items
    except Exception as e:
        print(f"Error scanning table: {e}")
        return []

def delete_item_from_table(table_name, key):
    try:
        dynamodb.delete_item(TableName=table_name, Key=key)
        print(f"Deleted item: {key}")
    except Exception as e:
        print(f"Error deleting item: {e}")

def delete_all_items_from_table(table_name):
    items = scan_table(table_name)
    for item in items:
        key = {k: v for k, v in item.items() if k in primary_keys}
        delete_item_from_table(table_name, key)

# Example usage
table_name = 'package-acc'
# Define the primary key(s) of your table here
primary_keys = ['id','name']  # Replace with your actual primary key names
delete_all_items_from_table(table_name)
