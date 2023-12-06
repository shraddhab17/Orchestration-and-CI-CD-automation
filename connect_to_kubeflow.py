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
