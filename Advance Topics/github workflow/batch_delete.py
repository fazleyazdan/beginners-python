import boto3
from munch import Munch
import requests
import time

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb', region_name='eu-central-1')
dynamodb_resource = boto3.resource('dynamodb', region_name='eu-central-1')

