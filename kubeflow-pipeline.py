import kfp
from kfp.dsl import ContainerOp

def deploy_fastapi_app(image: str):
    return ContainerOp(
        name='deploy-fastapi-app',
        image=image,
        command=[
            '/bin/sh', '-c',
            'kubectl apply -f phish-app-deployment.yaml -f phish-app-ingress.yaml && tar -czvf /tmp/output.txt.tgz -C /app/output .'
        ],
        file_outputs={'output': '/tmp/output.txt.tgz'},
    )

@kfp.dsl.pipeline(
    name='FastAPI Deployment Pipeline',
    description='Pipeline for deploying FastAPI application'
)
def deploy_pipeline(image: str):
    deploy_op = deploy_fastapi_app(image=image)

if __name__ == '__main__':
    # my ecr image
    ecr_image = '871927043079.dkr.ecr.us-east-1.amazonaws.com/kubeflow:latest'
    
    kfp.compiler.Compiler().compile(deploy_pipeline, 'deploy-pipeline.zip')
    kfp.Client().create_run_from_pipeline_func(deploy_pipeline, arguments={'image': ecr_image})
