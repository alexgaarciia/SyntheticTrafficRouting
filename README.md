# SimulatedNetData
## Overview
This project generates synthetic network traffic data using a Generative Adversarial Network (GAN). 

## Project Structure
- `input_data`: Contains datasets that can be used for input.
- `output_data`: Stores the generated synthetic data.
- `synthetic_network_traffic_data_generation.ipynb`: A Jupyter notebook that processes network traffic data and trains a GAN to generate synthetic data. 

## Notebook Description
The `synthetic_network_traffic_data_generation.ipynb` notebook performs the following tasks:
1. **Imports Libraries**: Necessary libraries such as NumPy, Pandas, and PyTorch are imported.
2. **Data Processing**: Ingests XML data files, extracts demand information, encodes categorical variables, and normalizes numerical values for use in the GAN.
3. **GAN Architecture**: Defines the generator and discriminator architectures, including activation functions and layer configurations.
4. **Training**: Trains the GAN over a specified number of epochs to learn to generate synthetic data.
5. **Data Generation**: Generates synthetic data samples and saves them to a CSV file in the `output_data` directory.
