def create_index(client, index,mapping) -> None:
    if not client.indices.exists(index=index):
        client.indices.create(index=index,body=mapping)
    return





if __name__ == "__main__":
 
    from elasticsearch import Elasticsearch
    es = Elasticsearch("http://localhost:9200")
    mapping = {
        "mappings": {
            "properties": {
            "numbers": { "type": "integer" },
            "contract_name": { "type": "keyword" },
            "banking": { "type": "text" },
            "bike_stands": { "type": "integer" },
            "available_bike_stands": { "type": "integer" },
            "available_bikes": { "type": "integer" },
            "address": { "type": "text" },
            "status": { "type": "text" },
            "position": {
                "type": "geo_point"
            },
            "last_update": { "type": "date",  "format": "yyyy-MM-dd HH:mm:ss||epoch_millis"}
                     
            }
        }
        
        }

    es = Elasticsearch("http://localhost:9200")
    create_index(client=es, index="bikestation",mapping=mapping)
