
from unicodedata import name
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials


import secrets




api = FastAPI(
    title='My_BDD_API'
)

security = HTTPBasic()

users_db = {
  "alice": "wonderland",
  "bob": "builder",
  "clementine": "mandarine"
}




def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    for keys,value in users_db.items():
        if secrets.compare_digest(credentials.username, keys) == True and secrets.compare_digest(credentials.password,value) == True:
           correct_username = True
           correct_password = True
        else:
           pass  
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
    
           
@api.get("/users/me")
def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}

    

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Document, Text, connections, analyzer
client = Elasticsearch()
import subprocess

# création d'une route pour insérer un élément
@api.post("/v1/insert/line")
def insert():
    
    subprocess.run(['/bin/bash','./test.sh']) 


    return {}


# création d'une route pour requêter la base par marque
@api.get("/v1/query/brand")
def query():
    
    s = Search(using=client, index="test1_ingest") \
        .query("match", brand= "Boytone") 
        
    response = s.execute()
    
    return response.to_dict()

# création d'une route pour requêter la base par id
@api.get("/v1/query/id")
def query():
    
    s = Search(using=client, index="test1_ingest") \
        .query("match", id="AVphzgbJLJeJML43fA0o") 
        
    response = s.execute()
    
    return response.to_dict()

# création d'une route pour requêter la base par catégorie dans une fourchette de prix
@api.get("/v1/query/primaryCategories/pricesMax")
def query():
    
    s = Search(using=client, index="test1_ingest") \
        .query("match", primaryCategories= "Electronics") \
        .filter("range", **{ "prices.amountMax": { "gte": 20, "lte": 500 }})
    response = s.execute()
    
    l =[]
    for hit in response:
        l.append(hit.meta.score)

    return response.to_dict()
    
  # création d'une route pour requêter la base par marque dans une fourchette de prix
@api.get("/v1/query/brand/pricesMax")
def query():
    
    s = Search(using=client, index="test1_ingest") \
        .query("match", brand= "Sanus") \
        .filter("range", **{ "prices.amountMax": { "gte": 10, "lte": 300 }})
    response = s.execute()
      
    return response.to_dict()     

