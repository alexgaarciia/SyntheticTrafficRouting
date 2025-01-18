import os
import pandas as pd
import xml.etree.ElementTree as ET


def process_network_traffic_data(path):
    # Ingest the XML data
    tree = ET.parse(path)
    root = tree.getroot()

    # Define the namespace
    ns = {'net': 'http://sndlib.zib.de/network'}

    # Extract demand information
    demands = []
    for demand in root.findall('net:demands/net:demand', ns):
        source = demand.find('net:source', ns).text
        target = demand.find('net:target', ns).text
        demand_value = float(demand.find('net:demandValue', ns).text)
        demands.append({'source': source, 'target': target, 'demand_value': demand_value})

    df = pd.DataFrame(demands)
    return df

def combine_first_n_datasets(folder_path, n_files=100):
    all_data = []  
    count = 0  
    
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".xml"):
            # Process the file and add to the list of dataframes
            file_path = os.path.join(folder_path, filename)
            data = process_network_traffic_data(file_path)
            all_data.append(data)
            count += 1
            
            # Stop once we have processed n_files
            if count >= n_files:
                break
    
    # Concatenate all DataFrames into one large DataFrame
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df
    
def rescale_demand(data, factor):
    data["demand_value"] = data["demand_value"] * factor
    return data
