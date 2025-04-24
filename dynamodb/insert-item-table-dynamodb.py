import boto3

dynamodb= boto3.client('dynamodb', region_name='us-east-1')

items = [
    {
        'cpf': {'S': '1234567890'},
        'nome': {'S': 'Gabriel Lopes'},
        'clienteativo': {'S': 'true'}
    },
    {
        'cpf': {'S': '0987654321'},
        'nome': {'S': 'Labriel Gopes'},
        'clienteativo': {'S': 'false'}
    },
    {
        'cpf': {'S': '0010110110'},
        'nome': {'S': 'Abriel Opes'},
        'clienteativo': {'S': 'true'}
    }    
]

for item in items:
    try:
        dynamodb.put_item(
            TableName='cliente',
            Item=item
        )
        print(f"Item {item['cpf']['S']} inserted successfully.")
    except Exception as e:
        print(f"Error inserting item {item['cpf']['S']}: {e}")