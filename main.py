from typing import Dict

# Install google-cloud-aiplatform

from google.cloud import aiplatform
from google.protobuf import json_format
import json

import os


def predict_tabular_sample(
    project: str,
    endpoint_id: str,
    instance_dict: Dict,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com"):

    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

    # for more info on the instance schema, please use get_model_sample.py
    # and look at the yaml found in instance_schema_uri

    # Parse instance_dict using the json module
    instance = json.loads(json.dumps(instance_dict))
    instances = [instance]
    parameters_dict = {}
    # Convert parameters_dict to JSON format using the json module
    # parameters = json.loads(json.dumps(parameters_dict))

    # parameters = json_format.ParseDict(parameters_dict)
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters_dict
    )

    predictions = response.predictions
    print(predictions)
    for prediction in predictions:
        print(" prediction:", dict(prediction))

# Authentication using service account.
# Please update full path of JSON file for authentication


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Users/Mahda/OneDrive/Documents/fifth-handbook-" \
                                               "387017-6f2b14e29677.json"

inputs = {'brand': 'Maruti',
          'model': 'Alto',
          'min_cost_price': '357003.861',
          'max_cost_price': '465401.5444',
          'vehicle_age': '9',
          'km_driven': '120000',
          'seller_type': 'Individual',
          'fuel_type': 'Petrol',
          'transmission_type': 'Manual',
          'mileage': '19.7',
          'engine': '796',
          'max_power': '46.3',
          'seats': '5'}
predict_tabular_sample("fifth-handbook-387017", '5397876414705827840', inputs)
