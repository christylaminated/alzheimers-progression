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
master_csv_path = 'JCalz_3_07_2025.csv'
output_file = "merged_JCalz"
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
                volume = parts[4]
                values[f"{name}_volume_mm3"] = volume
                columns.append(f"{name}_volume_mm3")
    
    return values, columns

#prepare to colelct all unique column names
all_features_names = set()

#first pass to gather all column names
with open(master_csv_path, "r", newline="") as infile: #opens 
    reader = csv.reader(infile)
    header = next(reader)
    for row in header:
        img_id = row[0]
        stats_folder = os.path.join(base_dir, img_id, "stats") #./folders, row[0], stats
        cereb_file = os.path.join(stats_folder, "cerebellum.CerebNet.stats")
        aseg_file = os.path.join(stats_folder, "aseg+DKT.stats")

        cereb_data, cereb_cols = extract_cerebellar_structure(cereb_file)
        aseg_data, aseg_cols = extract_non_cerebellar_aseg(aseg_file)

        all_features_names.update(cereb_cols)
        all_features_names.update(aseg_cols)

all_feature_names = sorted(list(all_features_names))

#second pass to write to final merged csv
with open(master_csv_path, "r", newline="") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    original_header = next(reader)
    writer.writerow(original_header + all_feature_names)

    for row in header:
        img_id = row[0]
        stats_folder = os.path.join(base_dir, img_id, "stats")
        cereb_file = os.path.join(stats_folder, "cerebellum.CerebNet.stats")
        aseg_file = os.path.join(stats_folder, "aseg+DKT.stats")

        cereb_Data, _ = extract_cerebellar_structure(cereb_file)
        aseg_data, _ = extract_non_cerebellar_aseg(aseg_file)

        all_data = {**aseg_data, **cereb_data}
        row_data = [all_data.get(col, '') for col in all_feature_names]

        writer.writerow(row + row_data)
    
import shutil
shutil.move(output_file, f"/mnt/data/{output_file}") #move from output file to /mnt






