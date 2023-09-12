curl -X PUT "elasticsearch:9200/_ingest/pipeline/test1_csv_pipeline" -H "Content-Type: application/json" -d '{
    "processors": [
    {
      "csv": {
        "field": "csv_line",
        "target_fields": ["id", "prices.amountMax", "prices.amountMin", "prices.availability",
                           "prices.condition", "prices.currency","prices.isSale", 
                           "prices.merchant", "asins", "brand", 
                           "name", "primaryCategories", "upc"],
        "separator": "|",
        "empty_value": "NaN"   
      }
    },
    {
      "convert": {
        "field" : "prices.amountMin",
        "type": "float"
      }
    },
    {
      "convert": {
        "field" : "prices.amountMax",
        "type": "float"
      }
    }
  ]
}'

curl -X PUT "elasticsearch:9200/test1_ingest" \
-H "Content-Type: application/json" \
-d '{
    "settings": {
        "index.default_pipeline": "test1_csv_pipeline",
        "analysis": {
          "analyzer": {
            "rebuilt_whitespace": {
              "tokenizer": "standard",
              "filter": [
                "lowercase"       
          ]
        }
      }
    }
  }
}'

i=1
sp="/-\|"
echo -n ' '

while read f1
do
   printf "\b${sp:i++%${#sp}:1}"
   f1=$( echo "$f1" | tr -d "\r")
   curl -s -X POST "elasticsearch:9200/test1_ingest/_doc" -H "Content-Type: application/json" -d "{ \"csv_line\": \"$f1\" }" > /tmp/output.html
done < DataElectProdData1.csv
