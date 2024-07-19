import csv
with open("wlit1.csv","w") as file:
    writer=csv.writer(file)
 
import json
new_data={"name=fjf","age=22"}

with open("wlit1.json", 'r')as file:
    json.dump(new_data,file)