'''
goal: merge JCalz csv file with the .stats file based on the Image Data ID, which is the same name as the folder names inside folders
1. loop through the folders file.
- per folder, find the corresponding Image DataID row in JCalz csv file and 
2. 
'''


import os
import csv
import pandas as pd

#defining base paths
base_dir = "./folders" #where the Image ID files are located
master_csv_path = 'test.csv'
output_file = "merged_JCalz.csv"
df_master = pd.read_csv(master_csv_path)



#extract cerebellar structures from cerebellum.CerebNet.stats
def extract_cerebellar_structure(stats_path):
    if not os.path.isfile(stats_path):
        return {}, []
    
    #read the stats_path file and store in lines
    with open(stats_path, "r") as f:
        lines = f.readlines()

    data_lines = [line for line in lines if not line.startswith('#')]
    values = {}
    columns =[]

    for line in data_lines:
        parts = line.split()
        if len(parts) >= 6:
            name = parts[4]
            volume = parts[3]
            values[f"{name}_volume_mm3"] = volume
            columns.append(f"{name}_volume_mm3")
    return values, columns

# list of cerebellar structure keywords to skip in aseg_DKT
cerebellar_keywords = ['Cerebellum', 'cerebellum']

def extract_non_cerebellar_aseg(stats_path):
    if not os.path.isfile(stats_path):
        return {}, []
    with open(stats_path, "r") as f:
        lines = f.readlines()
    
    data_lines = [line for line in lines if not line.startswith('#')]
    values = {}
    columns = []

    for line in data_lines:
        parts = line.split()
        if len(parts) >= 6:
            name = parts[4]
            if not any(keyword in name for keyword in cerebellar_keywords):
                volume = parts[3]
                values[f"{name}_volume_mm3"] = volume
                columns.append(f"{name}_volume_mm3")
    return values, columns

#prepare to colelct all unique column names
all_features_names = set()

#first pass to gather all column names
with open(master_csv_path, "r", newline="") as infile: #opens JCalz_3_07_2025.csv and reads each row
    reader = csv.reader(infile) #create a csv reader object using infile created above
    print("reader is ", reader)
    header = next(reader) #go to next row

    #print(f"header is {header}")
    for row in reader: 
        img_id = row[0] 
        #print(f"cheking {img_id}")
        if (img_id == 'I13722'):
            print("found!")
        stats_folder = os.path.join(base_dir, img_id, "stats") #./folders, /I13722, /stats
        cereb_file = os.path.join(stats_folder, "cerebellum.CerebNet.stats")
        aseg_file = os.path.join(stats_folder, "aseg+DKT.stats")

        cereb_data, cereb_cols = extract_cerebellar_structure(cereb_file) #if file not found, will return {},[]
        aseg_data, aseg_cols = extract_non_cerebellar_aseg(aseg_file)

        all_features_names.update(cereb_cols)
        all_features_names.update(aseg_cols)
        '''
        my_set = {'a', 'b'}
        my_set.update([])
        print(my_set) #still {'a', 'b'}
        my_set.update(['banana', 'cherry'])
        print(my_set) #{'apple', 'banana', 'cherry'}
        '''

all_feature_names = sorted(list(all_features_names)) #list of features from cereb then aseg
#print(all_feature_names)

#second pass to write to final merged csv
with open(master_csv_path, "r", newline="") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    original_header = next(reader)
    writer.writerow(original_header + all_feature_names)
    #we now have 

    for row in reader:
        #looping through each Image ID in JCalz row[0]
        img_id = row[0] #Image ID at this iteration
        stats_folder = os.path.join(base_dir, img_id, "stats")
        cereb_file = os.path.join(stats_folder, "cerebellum.CerebNet.stats")
        aseg_file = os.path.join(stats_folder, "aseg+DKT.stats")

        cereb_data, _ = extract_cerebellar_structure(cereb_file) #cereb data for this row
        aseg_data, _ = extract_non_cerebellar_aseg(aseg_file) #aseg data for this row
        '''if cereb_data:
            print("cereb_data is ", cereb_data, "for ", cereb_file)
            print("aseg_data is ", aseg_data, "for ", aseg_file)'''

        all_data = {**aseg_data, **cereb_data} #combines aseg_data and cereb_data into one all_data dictionary
        #using the dictionary, put the value in the column with the same name as key
        #dictionary column:value pair this row
        row_data = [all_data.get(col, '') for col in all_feature_names]
        
        '''for col in all_feature_names:
            if all_data.get(col, ''):
                print(f"col: {col}")
                print(f"all_data.get: {all_data.get(col,'')}")'''
            #all_data.get(col, '') #dictionary.get(key, default_value)
            #all_data would be in the order of all_feature_names

        

        writer.writerow(row + row_data)
    
'''import shutil
shutil.move(output_file, f"/mnt/data/{output_file}") #move from output file to /mnt'''






