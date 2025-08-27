import boto3
import json
from botocore.exceptions import ClientError

dynamodb = boto3.client('dynamodb', region_name='eu-central-1')

def count_packages_with_source_osv_in_string(table_name):
    paginator = dynamodb.get_paginator('scan')
    count = 0

    try:
        for page in paginator.paginate(
            TableName=table_name,
            ProjectionExpression="database_specific"
        ):
            for item in page.get('Items', []):
                db_field = item.get('database_specific', {}).get('S')  # If it's stored as a string
                if db_field:
                    try:
                        db_data = json.loads(db_field)
                        if db_data.get('source') == 'osv':
                            count += 1
                    except json.JSONDecodeError:
                        continue  # Ignore malformed JSON
    except ClientError as e:
        raise Exception(f"Error scanning table: {e}")

    return count

# Example usage
if __name__ == "__main__":
    table_name = 'vulnerability-prd'
    count = count_packages_with_source_osv_in_string(table_name)
    print(f"Total packages with database_specific.source = 'osv': {count}")
