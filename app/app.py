import boto3
from person import Person
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('mutant')


@app.route('/')
def handler(event):  # put application's code here
    operation = event['operation']

    if operation == 'create':
        item = event['item']
        person = Person(item['name'], item['age'], item['dna'])
        response = create_item({"name": person.name,
                                "age": person.age,
                                "dna": person.dna,
                                "is_mutant": person.is_mutant(),
                                "creation_date": datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
    elif operation == 'read':
        response = read_item()
    else:
        response = {'error': 'Operación no soportada'}

    return response


@app.route('/is-mutant', methods=['POST'])
def create_item(item):
    table.put_item(Item=item)
    print(item)
    return {'is_mutant': item['is_mutant']}


@app.route('/report', methods=['GET'])
def read_item():
    data = table.scan().get('Items', [])
    count_mutant = len(list(filter(lambda x: x["is_mutant"] == True, data)))
    count_human = len(list(filter(lambda x: x["is_mutant"] == False, data)))
    ratio = (count_mutant / (count_mutant + count_human))
    response = {"count_human_dna": count_human, "count_mutant_dna": count_mutant, "ratio_mutan": ratio,"data": data}
    return response


if __name__ == '__main__':
    app.run()
