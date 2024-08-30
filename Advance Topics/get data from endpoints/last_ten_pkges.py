import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.client('dynamodb', region_name='eu-central-1')

def get_last_ten_packages_with_keyword(table_name, language, keyword):
    paginator = dynamodb.get_paginator('scan')
    recent_packages = []

    try:
        for page in paginator.paginate(
            TableName=table_name,
            FilterExpression="#lang = :lang AND contains(#name, :keyword)",
            ExpressionAttributeNames={
                "#lang": "language",
                "#name": "name",  # Placeholder for reserved keyword
                "#created_at": "created_at"
            },
            ExpressionAttributeValues={
                ":lang": {"S": language},
                ":keyword": {"S": keyword}
            },
            ProjectionExpression="#name, #created_at"
        ):
            for item in page.get('Items', []):
                package_name = item.get('name', {}).get('S')
                created_at = item.get('created_at', {}).get('S')

                if created_at and package_name:
                    recent_packages.append((package_name, created_at))

                    # Sort by created_at in descending order and keep only the last 10 items
                    recent_packages = sorted(recent_packages, key=lambda x: x[1], reverse=True)[:15]

    except ClientError as e:
        raise Exception(f"Error scanning table with paginator: {e}")

    # Return the package names of the last 10 items
    return [package[0] for package in recent_packages]

# Example usage
if __name__ == "__main__":
    table_name = 'package-prd'
    language = 'javascript'  # Replace with the language you want to query
    keyword = 'cra-template'  # The keyword to search for in the package name
    last_ten_packages = get_last_ten_packages_with_keyword(table_name, language, keyword)
    print(f"Last 10 packages with language '{language}' containing '{keyword}': {last_ten_packages}")
