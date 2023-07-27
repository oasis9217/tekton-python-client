import inspect
from pydantic import BaseModel
from typing import Any, Dict, AnyStr, List, Union
from ..dependencies import V1ObjectMeta
from ..dependencies import V1Task, V1TaskSpec, V1Step, V1TaskRun
from ..dependencies import V1Pipeline, V1PipelineSpec, V1PipelineTask, V1TaskRef, V1PipelineRun


JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]


def create_class(class_name, attributes):
    if class_name.startswith(('str', 'bool', 'list', 'dict', 'object')):
        return attributes

    if class_name == 'V1ObjectMeta':
        return type(class_name, (V1ObjectMeta,), attributes)
    elif class_name == 'V1Task':
        return type(class_name, (V1Task,), attributes)
    elif class_name == 'V1TaskSpec':
        return type(class_name, (V1TaskSpec,), attributes)
    elif class_name == 'V1Step':
        return type(class_name, (V1Step,), attributes)
    elif class_name == 'V1TaskRun':
        return type(class_name, (V1TaskRun,), attributes)
    elif class_name == 'V1Pipeline':
        return type(class_name, (V1Pipeline,), attributes)
    elif class_name == 'V1PipelineSpec':
        return type(class_name, (V1PipelineSpec,), attributes)
    elif class_name == 'V1PipelineTask':
        return type(class_name, (V1PipelineTask,), attributes)
    elif class_name == 'V1TaskRef':
        return type(class_name, (V1TaskRef,), attributes)
    elif class_name == 'V1PipelineRun':
        return type(class_name, (V1PipelineRun,), attributes)
    else:
        print(class_name, attributes)
        raise ValueError('Invalid class name for k8s class generation from request body')


def parse_body_to_tekton(kind: str, data: JSONObject):
    # TODO: nested classes
    # TODO: type validation
    if kind == 'V1Task':
        instance = V1Task()
    elif kind == 'V1TaskRun':
        instance = V1TaskRun()
    elif kind == 'V1Pipeline':
        instance = V1Pipeline()
    elif kind == 'V1PipelineRun':
        instance = V1PipelineRun()
    else:
        raise ValueError(f"Not supported Kind", kind)

    attr_map_key_list = list(instance.attribute_map.keys())
    attr_map_val_list = list(instance.attribute_map.values())

    for key, val in data.items():
        if key not in attr_map_val_list:
            raise ValueError(f"Invalid json key, {key}, for {kind}")
        else:
            index = attr_map_val_list.index(key)
            target_attr = attr_map_key_list[index]
            target_attr_type = instance.openapi_types[target_attr]

            _class = create_class(target_attr_type, val)
            target_attr_val = _class() if inspect.isclass(_class) else _class

            setattr(instance, target_attr, target_attr_val)
    return instance


class TektonResource(BaseModel):
    pass
