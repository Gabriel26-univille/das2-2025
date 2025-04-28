import boto3

dynamodb= boto3.client('dynamodb', region_name='us-east-1')

try:
    resposta = dynamodb.get_item(
        TableName= 'cliente',
        Key={
            'cpf':{'S':'0987654321'}
        }
    )
    if "Item" in resposta:
        print("Item encontrado:")
        print(resposta['Item'])
    else:
        print("Item não encontrado")
except Exception as e:
    print(e)