import boto3

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')

def count_packages_by_language_gsi_resource(table_name, index_name, language):
    table = dynamodb.Table(table_name)
    count = 0
    last_evaluated_key = None

    while True:
        kwargs = {
            'IndexName': index_name,
            'KeyConditionExpression': "#lang = :lang",
            'ExpressionAttributeNames': {"#lang": "language"},
            'ExpressionAttributeValues': {":lang": language},
            'Select': "COUNT",
        }
        if last_evaluated_key:
            kwargs['ExclusiveStartKey'] = last_evaluated_key
        
        response = table.query(**kwargs)
        count += response.get('Count', 0)
        last_evaluated_key = response.get('LastEvaluatedKey')

        if not last_evaluated_key:
            break
    
    return count

# Example usage
if __name__ == "__main__":
    table_name = 'package-prd'
    index_name = 'id'  # Replace with your GSI name for 'language'
    language = 'python'  # Replace with the language you want to query
    count = count_packages_by_language_gsi_resource(table_name, index_name, language)
    print(f"Total number of packages with language '{language}': {count}")
