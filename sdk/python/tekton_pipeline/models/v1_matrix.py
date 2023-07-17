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

from tekton_pipeline.configuration import Configuration


class V1Matrix(object):
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
        'include': 'list[V1IncludeParams]',
        'params': 'list[V1Param]'
    }

    attribute_map = {
        'include': 'include',
        'params': 'params'
    }

    def __init__(self, include=None, params=None, local_vars_configuration=None):  # noqa: E501
        """V1Matrix - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._include = None
        self._params = None
        self.discriminator = None

        if include is not None:
            self.include = include
        if params is not None:
            self.params = params

    @property
    def include(self):
        """Gets the include of this V1Matrix.  # noqa: E501

        Include is a list of IncludeParams which allows passing in specific combinations of Parameters into the Matrix.  # noqa: E501

        :return: The include of this V1Matrix.  # noqa: E501
        :rtype: list[V1IncludeParams]
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this V1Matrix.

        Include is a list of IncludeParams which allows passing in specific combinations of Parameters into the Matrix.  # noqa: E501

        :param include: The include of this V1Matrix.  # noqa: E501
        :type: list[V1IncludeParams]
        """

        self._include = include

    @property
    def params(self):
        """Gets the params of this V1Matrix.  # noqa: E501

        Params is a list of parameters used to fan out the pipelineTask Params takes only `Parameters` of type `\"array\"` Each array element is supplied to the `PipelineTask` by substituting `params` of type `\"string\"` in the underlying `Task`. The names of the `params` in the `Matrix` must match the names of the `params` in the underlying `Task` that they will be substituting.  # noqa: E501

        :return: The params of this V1Matrix.  # noqa: E501
        :rtype: list[V1Param]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this V1Matrix.

        Params is a list of parameters used to fan out the pipelineTask Params takes only `Parameters` of type `\"array\"` Each array element is supplied to the `PipelineTask` by substituting `params` of type `\"string\"` in the underlying `Task`. The names of the `params` in the `Matrix` must match the names of the `params` in the underlying `Task` that they will be substituting.  # noqa: E501

        :param params: The params of this V1Matrix.  # noqa: E501
        :type: list[V1Param]
        """

        self._params = params

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
        if not isinstance(other, V1Matrix):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Matrix):
            return True

        return self.to_dict() != other.to_dict()