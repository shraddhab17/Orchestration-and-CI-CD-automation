import kfp
from kfp import dsl
from kfp.components import load_component_from_text

run_model_op = load_component_from_text("""
name: Run Model
description: Runs a model using an ECR image.
inputs:
- {name: image, type: String, description: 'ECR image'}
implementation:
  container:
    image: {inputValue: image}
    command: ['python', '/src/app.py']
""")

@dsl.pipeline(
    name='My pipeline',
    description='A pipeline that runs a model using an ECR image.'
)
def my_pipeline(image: dsl.PipelineParam = '871927043079.dkr.ecr.us-east-1.amazonaws.com/kubeflow:latest'):
    run_model = run_model_op(image)

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(my_pipeline, 'MyPipeline.yaml')