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

    The version of the OpenAPI document: v0.49.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tekton_pipeline.configuration import Configuration


class V1ParamValue(object):
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
        'array_val': 'list[str]',
        'object_val': 'dict(str, str)',
        'string_val': 'str',
        'type': 'str'
    }

    attribute_map = {
        'array_val': 'ArrayVal',
        'object_val': 'ObjectVal',
        'string_val': 'StringVal',
        'type': 'Type'
    }

    def __init__(self, array_val=None, object_val=None, string_val='', type='', local_vars_configuration=None):  # noqa: E501
        """V1ParamValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._array_val = None
        self._object_val = None
        self._string_val = None
        self._type = None
        self.discriminator = None

        self.array_val = array_val
        self.object_val = object_val
        self.string_val = string_val
        self.type = type

    @property
    def array_val(self):
        """Gets the array_val of this V1ParamValue.  # noqa: E501


        :return: The array_val of this V1ParamValue.  # noqa: E501
        :rtype: list[str]
        """
        return self._array_val

    @array_val.setter
    def array_val(self, array_val):
        """Sets the array_val of this V1ParamValue.


        :param array_val: The array_val of this V1ParamValue.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and array_val is None:  # noqa: E501
            raise ValueError("Invalid value for `array_val`, must not be `None`")  # noqa: E501

        self._array_val = array_val

    @property
    def object_val(self):
        """Gets the object_val of this V1ParamValue.  # noqa: E501


        :return: The object_val of this V1ParamValue.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._object_val

    @object_val.setter
    def object_val(self, object_val):
        """Sets the object_val of this V1ParamValue.


        :param object_val: The object_val of this V1ParamValue.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and object_val is None:  # noqa: E501
            raise ValueError("Invalid value for `object_val`, must not be `None`")  # noqa: E501

        self._object_val = object_val

    @property
    def string_val(self):
        """Gets the string_val of this V1ParamValue.  # noqa: E501

        Represents the stored type of ParamValues.  # noqa: E501

        :return: The string_val of this V1ParamValue.  # noqa: E501
        :rtype: str
        """
        return self._string_val

    @string_val.setter
    def string_val(self, string_val):
        """Sets the string_val of this V1ParamValue.

        Represents the stored type of ParamValues.  # noqa: E501

        :param string_val: The string_val of this V1ParamValue.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and string_val is None:  # noqa: E501
            raise ValueError("Invalid value for `string_val`, must not be `None`")  # noqa: E501

        self._string_val = string_val

    @property
    def type(self):
        """Gets the type of this V1ParamValue.  # noqa: E501


        :return: The type of this V1ParamValue.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1ParamValue.


        :param type: The type of this V1ParamValue.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, V1ParamValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ParamValue):
            return True

        return self.to_dict() != other.to_dict()