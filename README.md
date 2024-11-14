# SimulatedNetData
## Overview
This project aims at generating synthetic network traffic data using a Generative Adversarial Network (GAN). 

## Project Structure
- `data`: Contains datasets that can be used for input.
- `real_data.csv`: Dataset that combines n datasets from the `data` folder.
- `synthetic_data.csv`: Generated synthetic data.
- `functions.py`: Contains custom functions for data processing.
- `synthetic_network_traffic_data_generation.ipynb`: Jupyter notebook that processes network traffic data and trains a GAN to generate synthetic data. 
- `metrics.ipynb`: Jupyter notebook dedicated to evaluating the quality of the generated synthetic data by comparing it to real data.

## Main Notebook Description
The `synthetic_network_traffic_data_generation.ipynb` notebook performs the following tasks:
1. **Imports Libraries**: Necessary libraries are imported.
2. **Data Processing**: Ingests XML data files, extracts demand information, encodes categorical variables, and normalizes numerical values for use in the GAN.
3. **GAN Architecture**: Defines the generator and discriminator architectures, including activation functions and layer configurations.
4. **Training**: Trains the GAN over a specified number of epochs to learn to generate synthetic data.
5. **Data Generation**: Generates synthetic data samples and saves them to a CSV file.
