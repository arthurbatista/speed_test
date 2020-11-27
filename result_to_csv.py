import pandas as pd
import json

_file = open('result.out', 'r') 
lines = _file.readlines() 

tests = []  
for line in lines:

    flatten_json = {}

    _json = json.loads(line)
    for k,v in _json.items():
        if type(v) != dict:
            flatten_json[k] = v
        else:
            for k2,v2 in v.items():
                flatten_json[k + '_' + k2] = v2
                
    tests.append(flatten_json)

df = pd.DataFrame(tests)
# df.to_csv('result.csv', index=False)
columns = df.columns
# print(columns)

# print(df[['ping_latency', 'isp', 'interface_internalIp', 'interface_name']])

def calculate_download(row):
    download_bytes = row['download_bytes'] * 8
    download_elapsed = row['download_elapsed'] / 1000
    return download_bytes / download_elapsed / 1000000

def calculate_upload(row):
    download_bytes = row['upload_bytes'] * 8
    download_elapsed = row['upload_elapsed'] / 1000
    return download_bytes / download_elapsed / 1000000

df['download'] = df.apply(calculate_download, axis=1)
df['upload'] = df.apply(calculate_upload, axis=1)

for location in pd.unique(df['server_location']):

    print(f'*********** {location} ***********')
    print('\n')

    _df = df[df.server_location == location]

    claro = _df[_df['isp'] == 'Claro NET'][['ping_latency', 'download', 'upload']]
    tim = _df[_df['isp'] == 'TIM Brasil'][['ping_latency', 'download', 'upload']]

    print('TIM')
    print(tim.describe())
    print('\n')
    print('Claro')
    print(claro.describe())
    print('\n')
    # print(_df['server_location'].values)
    # print(_df[_df['isp'] == 'TIM Brasil'][['download', 'result_url']].values)


# download_columns = [c for c in columns if 'download' in c]
# download_columns.append('speed')
# download_columns.append('result_url')
# print(df[download_columns].values)