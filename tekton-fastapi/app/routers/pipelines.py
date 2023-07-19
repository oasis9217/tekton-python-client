from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import tekton_client

router = APIRouter(
    prefix="/pipelines",
    tags=["pipelines"],
    # dependencies=[Depends(lambda tekton: tekton_client)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def list_pipeline():
    pipelines, err = tekton_client.list(entity='pipeline', namespace='k5-tools')

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return pipelines


@router.get("/{pipeline_name}")
async def get_pipeline(pipeline_name: str):
    pipeline, err = tekton_client.get(entity='pipeline', name=pipeline_name, namespace='k5-tools')

    if err is not None:
        raise HTTPException(status_code=err['status'], detail=err['message'])

    return pipeline


