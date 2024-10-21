import xml.etree.ElementTree as ET
import pandas as pd


# Pipeline to extract network traffic data
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


# Test the preprocessing pipeline
data_path = 'data/demandMatrix-abilene-zhang-5min-20040910-2325.xml'
demands_df = process_network_traffic_data(data_path)
print(demands_df)
