import boto3

dynamodb= boto3.client('dynamodb', region_name='us-east-1')

try:
    resposta = dynamodb.update_item(
        TableName= 'cliente',
        Key={
            'cpf':{'S':'0987654321'}
        },
        UpdateExpression='Set clienteativo = :val',
        ExpressionAttributeValues={
            ':val': {'S': 'true'}
        },
        ReturnValues="UPDATED_NEW"
    )
    print(resposta)
except Exception as e:
    print(e)