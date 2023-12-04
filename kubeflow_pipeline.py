import kfp
from kfp import dsl

def fetch_code_op():
    return dsl.ContainerOp(
        name="Fetch Code",
        image="alpine/git:latest",
        command=[
            "git",
            "clone",
            "https://github.com/shraddhab17/Orchestration-and-CI-CD-automation.git",
            "/src",
        ],
    )

def deploy_op():
    return dsl.ContainerOp(
        name="Deploy",
        image="bitnami/kubectl:latest",
        command=["kubectl", "apply", "-f", "/src/kubernetes-manifests/"],
        pvolumes={"/src": fetch_code_op().pvolume},
    )

@dsl.pipeline(
    name="My pipeline",
    description="A pipeline that fetches code from GitHub and deploys it on EKS.",
)
def my_pipeline():
    fetch_code = fetch_code_op()
    deploy = deploy_op()
    deploy.after(fetch_code)

if __name__ == "__main__":
    kfp.compiler.Compiler().compile(my_pipeline, "kubeflow-pipeline.zip")
