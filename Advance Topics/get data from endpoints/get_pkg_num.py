from amazondax import AmazonDaxClient

dax = AmazonDaxClient(region_name='eu-central-1')

def count_packages_by_language_dax(table_name, index_name, language):
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
        
        response = dax.query(**kwargs)
        count += response.get('Count', 0)
        last_evaluated_key = response.get('LastEvaluatedKey')

        if not last_evaluated_key:
            break
    
    return count

if __name__ == "__main__":
    table_name = 'package-dev'
    index_name = 'id'
    language = 'c++'
    count = count_packages_by_language_dax(table_name, index_name, language)
    print(f"Total number of packages with language '{language}': {count}")
