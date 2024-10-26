import pandas as pd
import xml.etree.ElementTree as ET
from sklearn.preprocessing import LabelEncoder, MinMaxScaler


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


def data_preparation(data):
    # Prepares the input data for use in a Generative Adversarial Network (GAN) by encoding categorical variables
    # and scaling numerical values

    # Encode categorical variables
    le_source = LabelEncoder()
    le_target = LabelEncoder()
    data['source'] = le_source.fit_transform(data['source'])
    data['target'] = le_target.fit_transform(data['target'])

    # Normalize the demand values
    scaler = MinMaxScaler()
    data['demand_value'] = scaler.fit_transform(data[['demand_value']])

    return data
