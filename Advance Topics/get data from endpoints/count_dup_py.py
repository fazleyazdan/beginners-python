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
            ExpressionAttributeValues={":val": {"S": "julia"}}
        ):
            for item in page.get('Items', []):
                name = item.get('name', {}).get('S')
                if name:
                    name_counts[name] += 1

    except ClientError as e:
        raise Exception(f"Error scanning table: {e}")

    # 🔥 Only count records that are duplicates
    duplicate_records = sum(count for count in name_counts.values() if count > 1)

    return duplicate_records


# Example usage
if __name__ == "__main__":
    table_name = 'package-prd'
    
    duplicates = count_duplicate_npm_packages(table_name)
    
    print(f"Total duplicate julia package records: {duplicates}")