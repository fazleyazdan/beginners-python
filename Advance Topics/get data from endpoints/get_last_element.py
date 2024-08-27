import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.client('dynamodb', region_name='eu-central-1')

def get_last_package_name(table_name, language):
    paginator = dynamodb.get_paginator('scan')
    last_package_name = None
    last_created_at = None

    try:
        for page in paginator.paginate(
            TableName=table_name,
            FilterExpression="#lang = :lang",
            ExpressionAttributeNames={
                "#lang": "language",
                "#name": "name"  # Placeholder for reserved keyword
            },
            ExpressionAttributeValues={":lang": {"S": language}},
            ProjectionExpression="#name, created_at"
        ):
            for item in page.get('Items', []):
                package_name = item.get('name', {}).get('S')
                created_at = item.get('created_at', {}).get('S')
                if created_at and (last_created_at is None or created_at > last_created_at):
                    last_created_at = created_at
                    last_package_name = package_name
    except ClientError as e:
        raise Exception(f"Error scanning table with paginator: {e}")

    return last_package_name

# Example usage
if __name__ == "__main__":
    table_name = 'package-prd'
    language = 'javascript'  # Replace with the language you want to query
    last_package_name = get_last_package_name(table_name, language)
    print(f"Name of the last package with language '{language}': {last_package_name}")
