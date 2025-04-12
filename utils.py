import pandas as pd
import os

def load_csv(file_path):
    return pd.read_csv(file_path)

def save_masked_data(data, output_dir, output_filename):
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_filename)
    data.to_csv(output_path, index=False)
    return output_path
