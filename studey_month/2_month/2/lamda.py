import json


def lambda_handler(event, context):
    # Получаем HTTP метод (GET, POST, etc.)
    http_method = event.get('httpMethod', 'GET')

    # Обрабатываем разные методы HTTP
    if http_method == 'GET':
        response = {
            'statusCode': 200,
            'body': json.dumps({'message': 'Hello from AWS Lambda!'})
        }
    elif http_method == 'POST':
        # Получаем данные из тела запроса
        body = json.loads(event.get('body', '{}'))
        response = {
            'statusCode': 200,
            'body': json.dumps({'message': 'Data received', 'data': body})
        }
    else:
        response = {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method Not Allowed'})
        }

    return response


import json
import boto3
from botocore.exceptions import ClientError

# Инициализируем клиент DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('YourTableName')


def lambda_handler(event, context):
    try:
        # Получаем данные из тела запроса
        body = json.loads(event.get('body', '{}'))
        item = {
            'id': body.get('id'),
            'name': body.get('name'),
            'description': body.get('description')
        }

        # Сохраняем данные в таблице
        table.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item added successfully'})
        }

    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }


import json
import boto3

# Инициализируем клиент SQS
sqs = boto3.client('sqs')
queue_url = 'https://sqs.region.amazonaws.com/account-id/queue-name'


def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))
    message = body.get('message', 'Default Message')

    # Отправляем сообщение в SQS
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps({'message': message})
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'messageId': response['MessageId']})
    }
