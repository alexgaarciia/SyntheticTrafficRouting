from preprocessing import process_network_traffic_data
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras import layers


#### DATA PREPARATION ####
def data_preparation(data):
    """
    Prepares the input data for use in a Generative Adversarial Network (GAN) by encoding categorical variables
    and scaling numerical values.

    :param data: A pandas DataFrame containing the network traffic data with 'source', 'target', and 'demand_value'
    columns.
    :return: A numpy array containing the processed data with columns for 'source', 'target',
    and 'demand_value'.
    """
    # GANs work better with numerical data, so it is better if we encode any categorical variable
    # and scale the numerical values

    # Encode categorical variables
    data['source'] = data['source'].astype('category').cat.codes
    data['target'] = data['target'].astype('category').cat.codes

    # Scale the demand values
    scaler = MinMaxScaler()
    data['demand_value'] = scaler.fit_transform(data[['demand_value']])

    # Final dataframe
    final_df = data[['source', 'target', 'demand_value']].values
    return final_df


#### GAN ARCHITECTURE ####
# Define the generator model
def build_generator(latent_dim):
    """
    The purpose of the generator is to create synthetic data that resembles the real data.

    :param latent_dim: size of the random noise vector that will serve as input
    :return: model
    """
    model = tf.keras.Sequential()
    model.add(layers.Input(shape=(latent_dim,)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(3, activation='sigmoid'))
    return model


# Define the discriminator model
def build_discriminator():
    """
    The purpose of the discriminator is to distinguish between real and synthetic data.

    :return: model
    """
    model = tf.keras.Sequential()
    model.add(layers.Input(shape=(3,)))  # Should match the output shape of the generator
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))
    return model


#### TRAINING LOOP ####


#### TESTING ####
# 1. Prepare data
data_path = 'data/demandMatrix-abilene-zhang-5min-20040910-2325.xml'
demands_df = process_network_traffic_data(data_path)
final_data = data_preparation(demands_df)

# 2. Instantiate models
latent_dim = 10
generator = build_generator(latent_dim)
discriminator = build_discriminator()

# Compile the discriminator
discriminator.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
