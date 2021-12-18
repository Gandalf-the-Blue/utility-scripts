import pandas as pd

def split_list(test_list,splitter):
    size = len(test_list)
    idx_list = [idx + 1 for idx, val in
            enumerate(test_list) if val == splitter]
  
    res = [test_list[i: j] for i, j in
            zip([0] + idx_list, idx_list + 
            ([size] if idx_list[-1] != size else []))]
    return res

def read_vcf(path):
    with open(path) as f:
        lines = f.readlines()
    keys = {'TEL;TYPE=WORK':'Work Phone', 'TEL;TYPE=OTHER':'Other Phone','TEL;TYPE=Mobile':"Mobile Phone", 'EMAIL;TYPE=Personal':"Personal Email", 'TEL;TYPE=HOME':"Home Phone", 'TITLE':"Title", 'BDAY':"Birthday", 'ADR;TYPE=HOME':"Home Address", 'ORG':"Organisation", 'ADR;TYPE=WORK':"Office Address", 'EMAIL;TYPE=HOME':"Home Email", 'EMAIL;TYPE=WORK':"Work Email",'CATEGORIES':"Categories", 'NOTE':"Notes", 'N':"Name", 'EMAIL;TYPE=OTHER':"Other Email", 'TEL;TYPE=CELL':"Cell Phone", 'TEL;TYPE=Home':"Home Phone"}
            
    rows = split_list(lines,"END:VCARD\n")
    contacts_df=pd.DataFrame()
    for row in rows:
        contact={}
        for fields in row:
            key = fields.split(":")[0]
            val = fields.split(":")[1].replace('\n','')    
            try:
                formal_key = keys[key]
                if key=="N":
                    first_name = val.split(";")[1]
                    last_name = val.split(";")[0]
                    contact["First Name"] = first_name
                    contact["Last Name"] = last_name
                else:
                    contact[formal_key]=val
            except KeyError:
                continue
        contact_df = pd.DataFrame.from_dict([contact])
        contacts_df = contacts_df.append(contact_df,ignore_index=True,sort=True)
    return contacts_df
