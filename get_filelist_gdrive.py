import json
import pandas as pd
import subprocess
p = subprocess.Popen([r'C:\Users\Adeetya Tantia\Desktop\get_json.bat'],stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()  
p_status = p.wait()

filepath = r'D:\Sync\Adeetya\Dabblings\GDrive Outputs\MediaOutput.json'
with open(filepath, encoding='utf-8') as fh:
    data = json.load(fh)

table= pd.DataFrame(columns={"Top Level","Sub Level I","Sub Level II","Sub Level III","Sub Level IV","Sub Level V","Sub Level VI","Sub Level VII"})
column_names = ["Top Level","Sub Level I","Sub Level II","Sub Level III","Sub Level IV","Sub Level V","Sub Level VI","Sub Level VII"]
table = table.reindex(columns=column_names)

splits=0
for i in range(0,len(data)):
    path= data[i]['Path']
    split_path = path.split('/')
    if splits<len(split_path):
        splits = len(split_path)
        print(splits)
    table = table.append(pd.Series(split_path, index=table.columns[:len(split_path)]), ignore_index=True)
    if i%1000==0:
        print(i)

table.sort_values(["Top Level","Sub Level I","Sub Level II","Sub Level III","Sub Level IV","Sub Level V","Sub Level VI"], ascending=[True,True,True,True,True,True,True])
print(table)

table.to_csv(r'D:\Sync\Adeetya\Dabblings\GDrive Outputs\MediaOutput.csv')