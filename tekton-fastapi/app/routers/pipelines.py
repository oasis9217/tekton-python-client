from typing import Annotated
from fastapi import APIRouter, Body, HTTPException

from ..internal import utils
from ..dependencies import tekton_client

router = APIRouter(
    prefix="/pipelines",
    tags=["pipelines"],
    responses={
        200: {"description": "Success"},
        404: {"description": "Not found"},
    },
)


@router.get("/")
async def list_pipeline(namespace: str | None = None):
    pipelines, err = tekton_client.list(entity='pipeline', namespace=namespace)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return pipelines


@router.get("/{pipeline_name}")
async def get_pipeline(pipeline_name: str, namespace: str | None = None):
    pipeline, err = tekton_client.get(entity='pipeline', name=pipeline_name, namespace=namespace)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return pipeline


@router.post("/")
async def create_pipeline(
    pipeline_spec: Annotated[
        utils.TektonResource,
        Body(examples=[
            {
                "apiVersion": "tekton.dev/v1beta1",
                "kind": "Pipeline",
                "metadata": {
                    "name": "ryu-test",
                    "namespace": "default"
                },
                "spec": {
                    "tasks": [
                        {
                            "name": "first-task",
                            "taskRef": {
                                "kind": "Task",
                                "name": "ryu-test"
                            }
                        }
                    ]
                }
            },
        ])
    ]
):
    # pipeline_spec = V1Pipeline(
    #     api_version='tekton.dev/v1beta1',
    #     kind='Pipeline',
    #     metadata=k8s_client.V1ObjectMeta(name='ryu-test'),
    #     spec=V1PipelineSpec(tasks=[
    #         V1PipelineTask(
    #             name='hello',
    #             task_ref=V1TaskRef(name='hello')
    #         )
    #     ])
    # )
    pipeline, err = tekton_client.create(entity='pipeline', body=pipeline_spec)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return pipeline


@router.put("/{pipeline_name}")
async def update_pipeline(
    pipeline_name: str,
    pipeline_spec: Annotated[
        utils.TektonResource,
        Body(examples=[
            {
                "apiVersion": "tekton.dev/v1beta1",
                "kind": "Pipeline",
                "metadata": {
                    "name": "ryu-test",
                    "namespace": "default"
                },
                "spec": {
                    "tasks": [
                        {
                            "name": "first-task",
                            "taskRef": {
                                "kind": "Task",
                                "name": "ryu-test"
                            }
                        }
                    ]
                }
            },
        ])
    ],
    namespace: str | None = None
):
    pipeline, err = tekton_client.create(entity='pipeline', name=pipeline_name, body=pipeline_spec, namespace=namespace)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return pipeline


@router.delete("/{pipeline_name}")
async def delete_pipeline(pipeline_name: str, namespace: str | None = None):
    pipeline, err = tekton_client.delete(entity='pipeline', name=pipeline_name, namespace=namespace)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return pipeline
