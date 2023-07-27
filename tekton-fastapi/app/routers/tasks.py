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
        utils.JSONObject,
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
    ],
    namespace: str | None = None
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
    try:
        task = utils.parse_body_to_tekton('V1Task', task_spec)
        metadata = task.metadata

        if metadata is not None:
            if namespace is not None and namespace != metadata.namespace:
                raise ValueError("namespace in query does not match with metadata.namespace in body")

        response, err = tekton_client.create(entity='task', body=task)
        if err is not None:
            raise HTTPException(status_code=err['status'], detail=err['message'])

        return response

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{task_name}")
async def update_task(
    task_name: str,
    task_spec: Annotated[
        utils.JSONObject,
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
    try:
        task = utils.parse_body_to_tekton('V1Task', task_spec)
        metadata = task.metadata

        if metadata is not None:
            if task_name != metadata.name:
                raise ValueError("task_name in path does not match with metadata.name in body")
            if namespace is not None and namespace != metadata.namespace:
                raise ValueError("namespace in query does not match with metadata.namespace in body")

        response, err = tekton_client.patch(entity='task', name=task_name, body=task, namespace=namespace)
        if err is not None:
            raise HTTPException(status_code=err['status'], detail=err['message'])

        return response

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{task_name}")
async def delete_task(task_name: str, namespace: str | None = None):
    task, err = tekton_client.delete(entity='task', name=task_name, namespace=namespace)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return task
