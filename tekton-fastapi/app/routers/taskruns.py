from typing import Annotated
from fastapi import APIRouter, Body, HTTPException

from ..internal import utils
from ..dependencies import tekton_client

router = APIRouter(
    prefix="/taskruns",
    tags=["taskruns"],
    responses={
        200: {"description": "Success"},
        404: {"description": "Not found"},
    },
)


@router.get("/")
async def list_taskrun(namespace: str | None = None):
    taskruns, err = tekton_client.list(entity='taskrun', namespace=namespace)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return taskruns


@router.get("/{taskrun_name}")
async def get_taskrun(taskrun_name: str, namespace: str | None = None):
    taskrun, err = tekton_client.get(entity='taskrun', name=taskrun_name, namespace=namespace)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return taskrun


@router.post("/")
async def create_taskrun(
    taskrun_spec: Annotated[
        utils.JSONObject,
        Body(examples=[
            {
              "apiVersion": "tekton.dev/v1beta1",
              "kind": "TaskRun",
              "metadata": {
                "name": "ryu-test-run",
                "namespace": "default"
              },
              "spec": {
                "taskRef": {
                  "name": "ryu-test"
                }
              }
            }
        ])
    ],
    namespace: str | None = None
):
    try:
        taskrun = utils.parse_body_to_tekton('V1TaskRun', taskrun_spec)
        metadata = taskrun.metadata

        if metadata is not None:
            if namespace is not None and namespace != metadata.namespace:
                raise ValueError("namespace in query does not match with metadata.namespace in body")

        response, err = tekton_client.create(entity='taskrun', body=taskrun)
        if err is not None:
            raise HTTPException(status_code=err['status'], detail=err['message'])

        return response

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{taskrun_name}")
async def delete_taskrun(taskrun_name: str, namespace: str | None = None):
    task, err = tekton_client.delete(entity='taskrun', name=taskrun_name, namespace=namespace)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return task
