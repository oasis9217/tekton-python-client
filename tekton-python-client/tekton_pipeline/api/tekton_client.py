# Copyright 2021 The Tekton Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from kubernetes import client, config

from tekton_pipeline.constants import constants
from tekton_pipeline.utils import utils
from tekton_pipeline.models import V1Pipeline, V1PipelineRun, V1Task, V1TaskRun


def exception_handler(exc):
    if isinstance(exc, client.exceptions.ApiException):
        exc_body = json.loads(exc.body)
        return None, {
            "status": exc.status,
            "reason": exc.reason,
            "message": exc_body["message"]
        }
    return None, {
        "status": 500,
        "message": exc
    }


def delete_keys(resource):
    del resource["metadata"]["managedFields"]
    return resource


def k8s_resource_trimmer(resource):
    if 'items' in resource:
        resource = resource["items"]
        return list(map(delete_keys, resource))

    if isinstance(resource, dict):
        return delete_keys(resource)
    return


class TektonClient(object):

    def __init__(self, config_file=None, context=None,
                 client_configuration=None, persist_config=True):
        """
        Tekton client constructor
        :param config_file: kubeconfig file, defaults to ~/.kube/config
        :param context: kubernetes context
        :param client_configuration: kubernetes configuration object
        :param persist_config:
        """
        if config_file or not utils.is_running_in_k8s():
            config.load_kube_config(
                config_file=config_file,
                context=context,
                client_configuration=client_configuration,
                persist_config=persist_config)
        else:
            config.load_incluster_config()
        self.core_api = client.CoreV1Api()
        self.app_api = client.AppsV1Api()
        self.api_instance = client.CustomObjectsApi()

    def create(self, entity, body: V1Pipeline | V1PipelineRun | V1Task | V1TaskRun, namespace=None):
        """
        Create the Tekton entity
        :param entity: the tekton entity,  currently supported values: ['task', 'taskrun', 'pipeline', 'pipelinerun', 'clustertask']. 
        :param body: Tekton entity body
        :param namespace: defaults to current or default namespace
        :return: created Tekton entity
        """
        utils.check_entity(entity)

        if namespace is None:
            namespace = utils.get_tekton_namespace(body)

        plural = str(entity).lower() + "s"

        try:
            return k8s_resource_trimmer(
                self.api_instance.create_namespaced_custom_object(
                    constants.TEKTON_GROUP,
                    constants.TEKTON_VERSION,
                    namespace,
                    plural,
                    body
                )), None
        except Exception as e:
            return exception_handler(e)

    def list(self, entity, namespace=None):
        """
        List the Tekton resources
        :param entity: the tekton entity, currently supported values: ['task', 'taskrun', 'pipeline', 'pipelinerun']
        :param namespace: defaults to current or default namespace
        :return: Tekton resources
        """
        utils.check_entity(entity)

        if namespace is None:
            namespace = utils.get_default_target_namespace()

        plural = str(entity).lower() + "s"

        try:
            return k8s_resource_trimmer(
                self.api_instance.list_namespaced_custom_object(
                    constants.TEKTON_GROUP,
                    constants.TEKTON_VERSION,
                    namespace,
                    plural,
                )), None
        except Exception as e:
            return exception_handler(e)

    def get(self, entity, name, namespace=None, timeout_seconds=600):
        """
        Get the Tekton objects
        :param entity: the tekton entity, currently supported values: ['task', 'taskrun', 'pipeline', 'pipelinerun'].
        :param name: existing Tekton objects
        :param namespace: defaults to current or default namespace
        :return: Tekton objects
        """

        utils.check_entity(entity)

        if namespace is None:
            namespace = utils.get_default_target_namespace()

        plural = str(entity).lower() + "s"

        try:
            return k8s_resource_trimmer(
                self.api_instance.get_namespaced_custom_object(
                    constants.TEKTON_GROUP,
                    constants.TEKTON_VERSION,
                    namespace,
                    plural,
                    name
                )), None
        except Exception as e:
            return exception_handler(e)

    def patch(self, entity, name, body, namespace=None):
        """
        Patch existing tekton object
        :param entity: the tekton entity, currently supported values: ['task', 'taskrun', 'pipeline', 'pipelinerun', 'clustertask'].
        :param name: existing tekton object name
        :param body: patched tekton object
        :param namespace: defaults to current or default namespace
        :return: patched tekton object
        """

        utils.check_entity(entity)

        if namespace is None:
            namespace = utils.get_tekton_namespace(body)

        plural = str(entity).lower() + "s"

        try:
            return k8s_resource_trimmer(
                self.api_instance.patch_namespaced_custom_object(
                    constants.TEKTON_GROUP,
                    constants.TEKTON_VERSION,
                    namespace,
                    plural,
                    name,
                    body
                )), None
        except Exception as e:
            return exception_handler(e)

    def delete(self, entity, name, namespace=None):
        """
        Delete the Tekton objects
        :param entity: the tekton entity, currently supported values: ['task', 'taskrun', 'pipeline', 'pipelinerun', 'clustertask'].
        :param name: Tekton object's name
        :param namespace: defaults to current or default namespace
        :return:
        """
        utils.check_entity(entity)

        if namespace is None:
            namespace = utils.get_default_target_namespace()

        plural = str(entity).lower() + "s"

        try:
            return self.api_instance.delete_namespaced_custom_object(
                constants.TEKTON_GROUP,
                constants.TEKTON_VERSION,
                namespace,
                plural,
                name
            ), None
        except Exception as e:
            return exception_handler(e)
