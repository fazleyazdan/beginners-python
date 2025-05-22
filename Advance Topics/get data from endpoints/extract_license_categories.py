import boto3

# Initialize DynamoDB client (assumes you've logged in using AWS SSO and credentials are available)
dynamodb = boto3.resource('dynamodb')
table_name = 'license-prd'  # replace with your table name
table = dynamodb.Table(table_name)

# Scan the table to get all items
response = table.scan()
items = response.get('Items', [])

# Keep scanning if there are more pages
while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    items.extend(response.get('Items', []))

# Extract unique category values
categories = {item['category'] for item in items if 'category' in item}

# Store in a variable and print
unique_categories = list(categories)
print("Unique category values:", unique_categories)
