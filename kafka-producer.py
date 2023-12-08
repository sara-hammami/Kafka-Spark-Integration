import requests 
from kafka import KafkaProducer
import json
import time
from datetime import datetime

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))

api_key = "98a904e7d3a679ff31758e009a9216e364c37925"
base_url = 'https://api.jcdecaux.com/vls/v1/'
endpoint = 'stations'
country_code = 'FR'

while True:  # Infinite loop for continuous streaming, you may adjust this as needed
    try:
        url = f'{base_url}{endpoint}?country_code={country_code}&apiKey={api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            for line in data:
                utcfromtimestamp = datetime.utcfromtimestamp(int(line['last_update'])/1000).strftime('%Y-%m-%d %H:%M:%S')

                d = {
                    'numbers': line['number'],
                    'contract_name': line['contract_name'],
                    'banking': line['banking'],
                    'bike_stands': line['bike_stands'],
                    'available_bike_stands': line['available_bike_stands'],
                    'available_bikes': line['available_bikes'],
                    'address': line['address'],
                    'status': line['status'],
                    'position':line['position'],
                    'last_update': utcfromtimestamp
                }

                producer.send('bike-station', value=d)
                print(d)
                time.sleep(2)
                
            
        else:
            print(f'Error: {response.status_code}')
            print(response.text)

    except Exception as e:
        print(f'An error occurred: {str(e)}')

  
    time.sleep(60)  
