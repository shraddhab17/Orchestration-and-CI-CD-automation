from kfp import Client
import os
import json
import uuid

# Get environment variables
kubeflow_host = os.environ.get('KUBEFLOW_HOST')
experiment_id = os.environ.get('KUBEFLOW_EXPERIMENT_ID')
pipeline_id = '5eb5350c-77ad-436a-a138-d07a414efbb2'  # Replace with your pipeline ID
version_id = 'deploy-kube-phish-6-12'  # Replace with your version ID
pipeline_params = os.environ.get('KUBEFLOW_PIPELINE_PARAMS')

# Parse pipeline parameters as JSON
pipeline_params_json = json.loads(pipeline_params)

# Create a client that connects to the Kubeflow Pipelines API
client = Client(host=kubeflow_host)

# Run your pipeline with the specified parameters
client.run_pipeline(
    experiment_id=experiment_id,
    job_name=f'pipeline-run-{uuid.uuid4()}',  # Use a unique identifier as the job name
    pipeline_id=pipeline_id,
    version_id=version_id,
    params=pipeline_params_json
)

# import kfp
# from datetime import datetime
# import os

# # Get today's date for tags
# today = str(datetime.now())

# # Parameters
# URL = os.getenv('URL')
# pipeline_name = "advanced_pipeline"
# job_name = 'job' + today
# ENDPOINT = os.getenv('ENDPOINT')
# EMAIL = os.getenv('EMAIL')
# PASSWORD = os.getenv('PASSWORD')

# # Run parameters
# experiment_id = 'abc0d4b6-cea0-4681-a118-2d5715a0db10'
# pipeline_id = '5eb5350c-77ad-436a-a138-d07a414efbb2'
# version_id = 'deploy-kube-phish-6-12'
# params = {'image': '871927043079.dkr.ecr.us-east-1.amazonaws.com/kubeflow'}

# # Hardcoded cookie value
# authservice_session = 'authservice_session=MTcwMTk2NDkyNXxOd3dBTkVWRFZWRkRTVmxZVGt4TFZrVlZURFpMTTBOWFNVTTJXVkJXTlV4VVdUSkZTRGN6UmxCWlJGUlNXRFpVVWtOUk5GRlVWa0U9fCtfhX73aWl3vWpxqQZ4DX-SvWS31ypeW_xCYA20NT9D'

# # Append the desired API version to the endpoint URL
# # endpoint_with_version = f'{ENDPOINT}/v1beta1'

# # Connect to Kubeflow Pipelines Manager
# client = kfp.Client(host=f"http://{ENDPOINT}/pipeline", cookies=authservice_session)

# # Run pipeline
# client.run_pipeline(
#     experiment_id=experiment_id,
#     job_name=job_name,
#     params=params,
#     pipeline_id=pipeline_id,
#     version_id=version_id
# )
