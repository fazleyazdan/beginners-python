import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='eu-central-1')

def check_table_and_get_items(table_name, limit=2):
    try:
        response = dynamodb.scan(
            TableName=table_name,
            Limit=limit
        )
        items = response.get('Items', [])
        if items:
            print(f"Table '{table_name}' contains data.")
            return items
        else:
            print(f"Table '{table_name}' is empty.")
            return None
    except Exception as e:
        print(f"Error scanning table: {e}")
        return None

# Example usage
table_name = 'package-dev'
items = check_table_and_get_items(table_name)

if items:
    for item in items:
        print(item)
