from network_traffic_data_processing import process_network_traffic_data, data_preparation

# Test the processing pipeline
data_path = 'data/demandMatrix-abilene-zhang-5min-20040910-2325.xml'
demands_df = process_network_traffic_data(data_path)
final_data = data_preparation(demands_df)
print(final_data)
