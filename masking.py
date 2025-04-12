import pandas as pd
from faker import Faker

fake = Faker()

def mask_column(data, column_name, mask_type='random_string'):
    if column_name not in data.columns:
        raise ValueError(f"{column_name} not found in dataset")
    
    if mask_type == 'random_string':
        data[column_name] = [fake.uuid4()[:8] for _ in range(len(data))]
    elif mask_type == 'email':
        data[column_name] = [fake.email() for _ in range(len(data))]
    elif mask_type == 'phone':
        data[column_name] = [fake.phone_number() for _ in range(len(data))]
    elif mask_type == 'name':
        data[column_name] = [fake.name() for _ in range(len(data))]
    else:
        raise ValueError(f"Unknown mask type: {mask_type}")
    
    return data
