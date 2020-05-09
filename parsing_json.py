import requests
r = requests.get('http://www.bom.gov.au/fwo/IDQ60901/IDQ60901.94576.json')
json_data = r.json()
# print(json_data)
observation = json_data['observations']
# notice = json_data['observations']['notice']
data = json_data['observations']['data']
print(data['name'])
# latest_data = data[0]
# print(latest_data['name'])
#
# print('suhu terakhir di',latest_data['name'],'adalah',latest_data['air_temp'])

# # full display
# hitung = 0
# for x in data:
#     hitung +=1
#     print(hitung, 'Suhu terakhir di', x['name'],'adalah' , x['air_temp'])