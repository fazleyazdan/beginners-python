import boto3
from munch import Munch


#! NOTE: The secret can be retrieved without using the region name. because it is already configured in my system
def get_secret():
    secret_name = "github-admin-token"
    # region_name = "eu-central-1" 

    # Create a Secrets Manager client
    client = boto3.client(
        "secretsmanager",
        # region_name=region_name
        )

    # Retrieve the secret
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    Munch(get_secret_value_response)

secret_val = get_secret()
print(secret_val.SecretString)
