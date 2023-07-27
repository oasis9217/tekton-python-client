from typing import Annotated
from fastapi import APIRouter, Body, HTTPException

from ..internal import utils
from ..dependencies import tekton_client

router = APIRouter(
    prefix="/pipelineruns",
    tags=["pipelineruns"],
    responses={
        200: {"description": "Success"},
        404: {"description": "Not found"},
    },
)


@router.get("/")
async def list_pipelinerun(namespace: str | None = None):
    pipelineruns, err = tekton_client.list(entity='pipelinerun', namespace=namespace)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return pipelineruns


@router.get("/{pipelinerun_name}")
async def get_pipelinerun(pipelinerun_name: str, namespace: str | None = None):
    pipelinerun, err = tekton_client.get(entity='pipelinerun', name=pipelinerun_name, namespace=namespace)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return pipelinerun


@router.post("/")
async def create_pipelinerun(
    pipelinerun_spec: Annotated[
        utils.JSONObject,
        Body(examples=[
            {
              "apiVersion": "tekton.dev/v1beta1",
              "kind": "PipelineRun",
              "metadata": {
                "name": "ryu-test-run",
                "namespace": "default"
              },
              "spec": {
                "pipelineRef": {
                  "name": "ryu-test"
                }
              }
            }
        ])
    ],
    namespace: str | None = None
):
    try:
        pipelinerun = utils.parse_body_to_tekton('V1PipelineRun', pipelinerun_spec)
        metadata = pipelinerun.metadata

        if metadata is not None:
            if namespace is not None and namespace != metadata.namespace:
                raise ValueError("namespace in query does not match with metadata.namespace in body")

        response, err = tekton_client.create(entity='pipelinerun', body=pipelinerun)
        if err is not None:
            raise HTTPException(status_code=err['status'], detail=err['message'])

        return response

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{pipelinerun_name}")
async def delete_pipelinerun(pipelinerun_name: str, namespace: str | None = None):
    task, err = tekton_client.delete(entity='pipelinerun', name=pipelinerun_name, namespace=namespace)

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return task
