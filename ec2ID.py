import json

# try:
with open('terraform.tfstate') as data_file:
    decoded = json.load(data_file)

# print "JSON parsing: ", decoded['modules'][0]['resources']['aws_instance.example123']['primary']['id']
# print "JSON parsing: ", decoded['modules'][0]['resources']['aws_instance.example123']['type']

names = decoded['modules'][0]['resources']

sent_str = ""

for index in names:
    if names[index]['type'] == 'aws_instance':
        id='"'+names[index]['primary']['id']+'"'
        sent_str += str(id) + ","

sent_str = sent_str[:-1]

payload='variable "instance_ids" {\n    default = ['+sent_str+']\n}'

f = open('variables.tf','w')
f.write(payload)
f.close()

# except (ValueError, KeyError, TypeError):
#     print "JSON format error"
