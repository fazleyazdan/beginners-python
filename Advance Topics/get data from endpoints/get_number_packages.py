import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.client('dynamodb', region_name='eu-central-1')

def count_packages_by_language_paginator(table_name, language):
    paginator = dynamodb.get_paginator('scan')
    count = 0

    try:
        for page in paginator.paginate(
            TableName=table_name,
            FilterExpression="#lang = :lang",
            ExpressionAttributeNames={"#lang": "language"},
            ExpressionAttributeValues={":lang": {"S": language}},
            Select="COUNT"
        ):
            count += page.get('Count', 0)
    except ClientError as e:
        raise Exception(f"Error scanning table with paginator: {e}")

    return count

# Example usage
if __name__ == "__main__":
    table_name = 'package-prd'
    language = 'julia'  # Replace with the language you want to query
    count = count_packages_by_language_paginator(table_name, language)
    print(f"Total number of packages with language '{language}': {count}")


# ! working : the speed is dependant on the size of the database as well as the internet connection
