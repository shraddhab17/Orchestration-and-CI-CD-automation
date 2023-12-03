from kfp import Client

# Define the host URL of your Kubeflow Pipelines deployment
host_url = 'http://<your-kubeflow-pipelines-host-url>'

# Create a client that connects to the Kubeflow Pipelines API
client = Client(host=host_url)

# Run your pipeline
client.run_pipeline(
    experiment_id='<your-experiment-id>', 
    job_name='<your-job-name>', 
    pipeline_id='<your-pipeline-id>'
)   