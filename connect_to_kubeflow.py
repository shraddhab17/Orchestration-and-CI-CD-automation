# from kfp import Client
# import os
# import json
# import uuid

# # Get environment variables
# kubeflow_host = os.environ.get('KUBEFLOW_HOST')
# experiment_id = os.environ.get('KUBEFLOW_EXPERIMENT_ID')
# pipeline_id = '5eb5350c-77ad-436a-a138-d07a414efbb2'  # Replace with your pipeline ID
# version_id = 'deploy-kube-phish-6-12'  # Replace with your version ID
# pipeline_params = os.environ.get('KUBEFLOW_PIPELINE_PARAMS')

# # Parse pipeline parameters as JSON
# pipeline_params_json = json.loads(pipeline_params)

# # Create a client that connects to the Kubeflow Pipelines API
# client = Client(host=kubeflow_host)

# # Run your pipeline with the specified parameters
# client.run_pipeline(
#     experiment_id=experiment_id,
#     job_name=f'pipeline-run-{uuid.uuid4()}',  # Use a unique identifier as the job name
#     pipeline_id=pipeline_id,
#     version_id=version_id,
#     params=pipeline_params_json
# )

import kfp
from datetime import datetime
import re
import os
import mechanize
from bs4 import BeautifulSoup
import urllib
import http.cookiejar as cookielib 

# Get today's date for tags
today = str(datetime.now())

# Def
def get_id(text):
    """
    Function that retrieves a pipeline's ID from its logs
    Parameters
    ----------
    text : str
        string version of the logs.
    Returns
    -------
    str : Id of the pipeline.
    """
    match = re.search('{\'id\': \'(.+?)\',\\n', text)        
    if match:
        found = match.group(1)
        return(found)
    
def get_cookie(text):
    """
    Function that retrieves login cookie
    Parameters
    ----------
    text : str
        string version of the logs.
    Returns
    -------
    str : cookie value.
    """
    match = re.search('authservice_session=(.+?) ', text)        
    if match:
        found = match.group(1)
        return(found)

# Parameters
URL = os.getenv('URL')
pipeline_name = "advanced_pipeline"
job_name = 'job' + today
ENDPOINT = os.getenv('ENDPOINT')
EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# Run parameters
experiment_id = 'abc0d4b6-cea0-4681-a118-2d5715a0db10'
pipeline_id = '5eb5350c-77ad-436a-a138-d07a414efbb2'
version_id = 'deploy-kube-phish-6-12'
params = {'image': '871927043079.dkr.ecr.us-east-1.amazonaws.com/kubeflow'}

# Get cookie value
cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open(URL)

br.select_form(nr=0)
br.form['login'] = EMAIL
br.form['password'] = PASSWORD
br.submit()
authservice_session = 'authservice_session={}'.format(get_cookie(str(cj)))

# Connect to Kubeflow Pipelines Manager
client = kfp.Client(host=ENDPOINT, cookies=authservice_session)

# Run pipeline
client.run_pipeline(
    experiment_id=experiment_id,
    job_name=job_name,
    params=params,
    pipeline_id=pipeline_id,
    version_id=version_id
)
