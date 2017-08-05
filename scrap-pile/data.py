
import json 

  #Returns value
resp = '{"category":"Unknown","action":"Click","label":"Movie","value":"0","productionName":"The Dark Tower","productionId":"105934"}'

data=json.load(resp)

data['productionName'] 
 