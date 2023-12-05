import kfp
from kfp import dsl
from kfp.components import load_component_from_text

# Define the Run Model component as a YAML string
run_model_component_yaml = """
name: Run Model
description: Runs a model using an ECR image.
inputs:
- {name: image, type: String, description: 'ECR image'}
implementation:
  container:
    image: '{{inputs.image}}'
    command: ['python', '/src/app.py']
"""

# Load the Run Model component from the YAML string
run_model_op = load_component_from_text(run_model_component_yaml)

@dsl.pipeline(
    name='My pipeline',
    description='A pipeline that runs a model using an ECR image.'
)
def my_pipeline(image: str = '871927043079.dkr.ecr.us-east-1.amazonaws.com/kubeflow:latest'):
    run_model = run_model_op(image=image)

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(my_pipeline, 'MyPipeline.yaml')
