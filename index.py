def create_index(client, index,mapping) -> None:
    if not client.indices.exists(index=index):
        client.indices.create(index=index,body=mapping)
    return





if __name__ == "__main__":

    
    from elasticsearch import Elasticsearch
    es = Elasticsearch("http://localhost:9200")
    if es.indices.exists(index="station-velos"):
        es.indices.delete(index="station-velos")
    mapping = {
        "mappings": {
            "properties": {
            "numbers": { "type": "integer" },
            "contract_name": { "type": "text" },
            "banking": { "type": "text" },
            "bike_stands": { "type": "integer" },
            "available_bike_stands": { "type": "integer" },
            "available_bikes": { "type": "integer" },
            "address": { "type": "text" },
            "status": { "type": "text" },
            "position": {
                "type": "geo_point"
            },
            "timestamps": { "type": "text" }
            }
        }
        }

    es = Elasticsearch("http://localhost:9200")
    create_index(client=es, index="station-velos",mapping=mapping)
