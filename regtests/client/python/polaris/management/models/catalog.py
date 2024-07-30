#
# Copyright (c) 2024 Snowflake Computing Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# coding: utf-8

"""
    Polaris Management Service

    Defines the management APIs for using Polaris to create and manage Iceberg catalogs and their principals

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from polaris.management.models.catalog_properties import CatalogProperties
from polaris.management.models.storage_config_info import StorageConfigInfo
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from polaris.management.models.external_catalog import ExternalCatalog
    from polaris.management.models.polaris_catalog import PolarisCatalog

class Catalog(BaseModel):
    """
    A catalog object. A catalog may be internal or external. Internal catalogs are managed entirely by an external catalog interface. Third party catalogs may be other Iceberg REST implementations or other services with their own proprietary APIs
    """ # noqa: E501
    type: StrictStr = Field(description="the type of catalog - internal or external")
    name: StrictStr = Field(description="The name of the catalog")
    properties: CatalogProperties
    create_timestamp: Optional[StrictInt] = Field(default=None, description="The creation time represented as unix epoch timestamp in milliseconds", alias="createTimestamp")
    last_update_timestamp: Optional[StrictInt] = Field(default=None, description="The last update time represented as unix epoch timestamp in milliseconds", alias="lastUpdateTimestamp")
    entity_version: Optional[StrictInt] = Field(default=None, description="The version of the catalog object used to determine if the catalog metadata has changed", alias="entityVersion")
    storage_config_info: StorageConfigInfo = Field(alias="storageConfigInfo")
    __properties: ClassVar[List[str]] = ["type", "name", "properties", "createTimestamp", "lastUpdateTimestamp", "entityVersion", "storageConfigInfo"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['INTERNAL', 'EXTERNAL']):
            raise ValueError("must be one of enum values ('INTERNAL', 'EXTERNAL')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'EXTERNAL': 'ExternalCatalog','INTERNAL': 'PolarisCatalog'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[ExternalCatalog, PolarisCatalog]]:
        """Create an instance of Catalog from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage_config_info
        if self.storage_config_info:
            _dict['storageConfigInfo'] = self.storage_config_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[ExternalCatalog, PolarisCatalog]]:
        """Create an instance of Catalog from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'ExternalCatalog':
            return import_module("polaris.management.models.external_catalog").ExternalCatalog.from_dict(obj)
        if object_type ==  'PolarisCatalog':
            return import_module("polaris.management.models.polaris_catalog").PolarisCatalog.from_dict(obj)

        raise ValueError("Catalog failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


