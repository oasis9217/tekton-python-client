from typing import Annotated
from fastapi import APIRouter, Body, HTTPException

from ..internal import utils
from ..dependencies import tekton_client

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={
        200: {"description": "Success"},
        404: {"description": "Not found"},
    },
)


@router.get("/")
async def list_task(namespace: str | None = None):
    tasks, err = tekton_client.list(entity='task', namespace=namespace)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return tasks


@router.get("/{task_name}")
async def get_task(task_name: str, namespace: str | None = None):
    task, err = tekton_client.get(entity='task', name=task_name, namespace=namespace)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return task


@router.post("/")
async def create_task(
    task_spec: Annotated[
        utils.TektonResource,
        Body(examples=[
            {
                  "apiVersion": "tekton.dev/v1beta1",
                  "kind": "Task",
                  "metadata": {
                    "name": "ryu-test",
                    "namespace": "default"
                  },
                  "spec": {
                    "steps": [
                      {
                        "image": "alpine",
                        "name": "first-step",
                        "resources": {},
                        "script": "sleep 5; echo \"Hello from first step\""
                      }
                    ]
                  }
            }
        ])
    ]
):
    # task_spec = V1Task(
    #     api_version='tekton.dev/v1beta1',
    #     kind='Task',
    #     metadata=k8s_client.V1ObjectMeta(name='ryu-test'),
    #     spec=V1TaskSpec(
    #         steps=[V1Step(
    #             name='first-step',
    #             image='alpine',
    #             script='sleep 5; echo "Hello from first step"',
    #         )]
    #     )
    # )
    task, err = tekton_client.create(entity='task', body=task_spec)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return task


@router.put("/{task_name}")
async def update_task(
    task_name: str,
    task_spec: Annotated[
        utils.TektonResource,
        Body(
            examples=[
                {
                      "apiVersion": "tekton.dev/v1beta1",
                      "kind": "Task",
                      "metadata": {
                        "name": "ryu-test",
                        "namespace": "default"
                      },
                      "spec": {
                        "steps": [
                          {
                            "image": "alpine",
                            "name": "first-step",
                            "resources": {},
                            "script": "sleep 5; echo \"Hello from first step patched\""
                          }
                        ]
                      }
                }
            ]
        )
    ],
    namespace: str | None = None
):
    task, err = tekton_client.patch(entity='task', name=task_name, body=task_spec, namespace=namespace)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return task


@router.delete("/{task_name}")
async def delete_task(task_name: str, namespace: str | None = None):
    task, err = tekton_client.delete(entity='task', name=task_name, namespace=namespace)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return task
