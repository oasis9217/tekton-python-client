import inspect
from typing import Any, Dict, AnyStr, List, Union

from .camel_to_snake_keys import decode_keys
from ..dependencies import V1ObjectMeta
from ..dependencies import V1Task, V1TaskSpec, V1Step, V1TaskRun, V1TaskRunSpec, V1TaskRef
from ..dependencies import V1Pipeline, V1PipelineSpec, V1PipelineTask, V1PipelineRun, V1PipelineRunSpec


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
    elif class_name == 'V1TaskRunSpec':
        return type(class_name, (V1TaskRunSpec,), attributes)
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
    elif class_name == 'V1PipelineRunSpec':
        return type(class_name, (V1PipelineRunSpec,), attributes)
    else:
        print(class_name, attributes)
        raise ValueError(f'Invalid class name, {class_name}, for k8s class generation from request body')


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

    data = decode_keys(data)

    for key, val in data.items():
        if key not in instance.attribute_map:
            raise ValueError(f"Invalid json key, {key}, for {kind}")
        else:
            attr = key
            attr_type = instance.openapi_types[attr]

            _class = create_class(attr_type, val)
            attr_val = _class() if inspect.isclass(_class) else _class

            setattr(instance, attr, attr_val)
    return instance


