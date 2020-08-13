# Copyright 2020 The Tekton Authors
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

# coding: utf-8

"""
    Tekton

    Tekton Pipeline  # noqa: E501

    The version of the OpenAPI document: v0.17.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tekton.configuration import Configuration


class V1beta1SidecarState(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'container': 'str',
        'image_id': 'str',
        'name': 'str',
        'running': 'V1ContainerStateRunning',
        'terminated': 'V1ContainerStateTerminated',
        'waiting': 'V1ContainerStateWaiting'
    }

    attribute_map = {
        'container': 'container',
        'image_id': 'imageID',
        'name': 'name',
        'running': 'running',
        'terminated': 'terminated',
        'waiting': 'waiting'
    }

    def __init__(self, container=None, image_id=None, name=None, running=None, terminated=None, waiting=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1SidecarState - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._container = None
        self._image_id = None
        self._name = None
        self._running = None
        self._terminated = None
        self._waiting = None
        self.discriminator = None

        if container is not None:
            self.container = container
        if image_id is not None:
            self.image_id = image_id
        if name is not None:
            self.name = name
        if running is not None:
            self.running = running
        if terminated is not None:
            self.terminated = terminated
        if waiting is not None:
            self.waiting = waiting

    @property
    def container(self):
        """Gets the container of this V1beta1SidecarState.  # noqa: E501


        :return: The container of this V1beta1SidecarState.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this V1beta1SidecarState.


        :param container: The container of this V1beta1SidecarState.  # noqa: E501
        :type: str
        """

        self._container = container

    @property
    def image_id(self):
        """Gets the image_id of this V1beta1SidecarState.  # noqa: E501


        :return: The image_id of this V1beta1SidecarState.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this V1beta1SidecarState.


        :param image_id: The image_id of this V1beta1SidecarState.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def name(self):
        """Gets the name of this V1beta1SidecarState.  # noqa: E501


        :return: The name of this V1beta1SidecarState.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1beta1SidecarState.


        :param name: The name of this V1beta1SidecarState.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def running(self):
        """Gets the running of this V1beta1SidecarState.  # noqa: E501


        :return: The running of this V1beta1SidecarState.  # noqa: E501
        :rtype: V1ContainerStateRunning
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this V1beta1SidecarState.


        :param running: The running of this V1beta1SidecarState.  # noqa: E501
        :type: V1ContainerStateRunning
        """

        self._running = running

    @property
    def terminated(self):
        """Gets the terminated of this V1beta1SidecarState.  # noqa: E501


        :return: The terminated of this V1beta1SidecarState.  # noqa: E501
        :rtype: V1ContainerStateTerminated
        """
        return self._terminated

    @terminated.setter
    def terminated(self, terminated):
        """Sets the terminated of this V1beta1SidecarState.


        :param terminated: The terminated of this V1beta1SidecarState.  # noqa: E501
        :type: V1ContainerStateTerminated
        """

        self._terminated = terminated

    @property
    def waiting(self):
        """Gets the waiting of this V1beta1SidecarState.  # noqa: E501


        :return: The waiting of this V1beta1SidecarState.  # noqa: E501
        :rtype: V1ContainerStateWaiting
        """
        return self._waiting

    @waiting.setter
    def waiting(self, waiting):
        """Sets the waiting of this V1beta1SidecarState.


        :param waiting: The waiting of this V1beta1SidecarState.  # noqa: E501
        :type: V1ContainerStateWaiting
        """

        self._waiting = waiting

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1SidecarState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1SidecarState):
            return True

        return self.to_dict() != other.to_dict()
