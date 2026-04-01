import boto3
from collections import defaultdict
from botocore.exceptions import ClientError

dynamodb = boto3.client('dynamodb', region_name='eu-central-1')

def count_duplicate_npm_packages(table_name):
    paginator = dynamodb.get_paginator('scan')
    
    name_counts = defaultdict(int)

    try:
        for page in paginator.paginate(
            TableName=table_name,
            FilterExpression="#reg = :val",
            ExpressionAttributeNames={"#reg": "registry_name"},
            ExpressionAttributeValues={":val": {"S": "npm"}}
        ):
            items = page.get('Items', [])
            
            for item in items:
                name = item.get('name', {}).get('S')
                if name:
                    name_counts[name] += 1

    except ClientError as e:
        raise Exception(f"Error scanning table: {e}")

    # Count duplicates
    duplicate_count = sum(1 for name, count in name_counts.items() if count > 1)

    # Optional: total duplicate records (not just unique names)
    duplicate_records = sum(count for count in name_counts.values() if count > 1)

    return duplicate_count, duplicate_records


# Example usage
if __name__ == "__main__":
    table_name = 'package-prd'
    
    unique_duplicates, total_duplicate_records = count_duplicate_npm_packages(table_name)
    
    print(f"Unique duplicate package names: {unique_duplicates}")
    print(f"Total duplicate records: {total_duplicate_records}")