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


class V1beta1ParamSpec(object):
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
        'default': 'V1beta1ArrayOrString',
        'description': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'default': 'default',
        'description': 'description',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, default=None, description=None, name='', type=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1ParamSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default = None
        self._description = None
        self._name = None
        self._type = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if description is not None:
            self.description = description
        self.name = name
        if type is not None:
            self.type = type

    @property
    def default(self):
        """Gets the default of this V1beta1ParamSpec.  # noqa: E501


        :return: The default of this V1beta1ParamSpec.  # noqa: E501
        :rtype: V1beta1ArrayOrString
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this V1beta1ParamSpec.


        :param default: The default of this V1beta1ParamSpec.  # noqa: E501
        :type: V1beta1ArrayOrString
        """

        self._default = default

    @property
    def description(self):
        """Gets the description of this V1beta1ParamSpec.  # noqa: E501

        Description is a user-facing description of the parameter that may be used to populate a UI.  # noqa: E501

        :return: The description of this V1beta1ParamSpec.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1beta1ParamSpec.

        Description is a user-facing description of the parameter that may be used to populate a UI.  # noqa: E501

        :param description: The description of this V1beta1ParamSpec.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this V1beta1ParamSpec.  # noqa: E501

        Name declares the name by which a parameter is referenced.  # noqa: E501

        :return: The name of this V1beta1ParamSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1beta1ParamSpec.

        Name declares the name by which a parameter is referenced.  # noqa: E501

        :param name: The name of this V1beta1ParamSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this V1beta1ParamSpec.  # noqa: E501

        Type is the user-specified type of the parameter. The possible types are currently \"string\" and \"array\", and \"string\" is the default.  # noqa: E501

        :return: The type of this V1beta1ParamSpec.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1beta1ParamSpec.

        Type is the user-specified type of the parameter. The possible types are currently \"string\" and \"array\", and \"string\" is the default.  # noqa: E501

        :param type: The type of this V1beta1ParamSpec.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, V1beta1ParamSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1ParamSpec):
            return True

        return self.to_dict() != other.to_dict()
