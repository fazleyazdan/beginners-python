import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.client('dynamodb', region_name='eu-central-1')

def count_packages_with_registry_vcpkg(table_name):
    paginator = dynamodb.get_paginator('scan')
    count = 0

    try:
        for page in paginator.paginate(
            TableName=table_name,
            FilterExpression="#reg = :val",
            ExpressionAttributeNames={"#reg": "registry_name"},
            ExpressionAttributeValues={":val": {"S": "conan"}},
            Select="COUNT"
        ):
            count += page.get('Count', 0)
    except ClientError as e:
        raise Exception(f"Error scanning table with paginator: {e}")

    return count

# Example usage
if __name__ == "__main__":
    table_name = 'package-prd'
    count = count_packages_with_registry_vcpkg(table_name)
    print(f"Total number of packages with registry 'vcpkg': {count}")
