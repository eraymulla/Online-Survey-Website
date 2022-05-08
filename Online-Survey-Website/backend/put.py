import requests
BASE ="http://127.0.0.1:5000/"


response = requests.put(BASE+ 'admin/'+{'userid':1,'name':'Eray','surname':'Mulla'})

print(response.content)