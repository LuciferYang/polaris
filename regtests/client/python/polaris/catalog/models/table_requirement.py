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
    Apache Iceberg REST Catalog API

    Defines the specification for the first version of the REST Catalog API. Implementations should ideally support both Iceberg table specs v1 and v2, with priority given to v2.

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from importlib import import_module
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from polaris.catalog.models.assert_create import AssertCreate
    from polaris.catalog.models.assert_current_schema_id import AssertCurrentSchemaId
    from polaris.catalog.models.assert_default_sort_order_id import AssertDefaultSortOrderId
    from polaris.catalog.models.assert_default_spec_id import AssertDefaultSpecId
    from polaris.catalog.models.assert_last_assigned_field_id import AssertLastAssignedFieldId
    from polaris.catalog.models.assert_last_assigned_partition_id import AssertLastAssignedPartitionId
    from polaris.catalog.models.assert_ref_snapshot_id import AssertRefSnapshotId
    from polaris.catalog.models.assert_table_uuid import AssertTableUUID

class TableRequirement(BaseModel):
    """
    TableRequirement
    """ # noqa: E501
    type: StrictStr
    __properties: ClassVar[List[str]] = ["type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'assert-create': 'AssertCreate','assert-current-schema-id': 'AssertCurrentSchemaId','assert-default-sort-order-id': 'AssertDefaultSortOrderId','assert-default-spec-id': 'AssertDefaultSpecId','assert-last-assigned-field-id': 'AssertLastAssignedFieldId','assert-last-assigned-partition-id': 'AssertLastAssignedPartitionId','assert-ref-snapshot-id': 'AssertRefSnapshotId','assert-table-uuid': 'AssertTableUUID'
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
    def from_json(cls, json_str: str) -> Optional[Union[AssertCreate, AssertCurrentSchemaId, AssertDefaultSortOrderId, AssertDefaultSpecId, AssertLastAssignedFieldId, AssertLastAssignedPartitionId, AssertRefSnapshotId, AssertTableUUID]]:
        """Create an instance of TableRequirement from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[AssertCreate, AssertCurrentSchemaId, AssertDefaultSortOrderId, AssertDefaultSpecId, AssertLastAssignedFieldId, AssertLastAssignedPartitionId, AssertRefSnapshotId, AssertTableUUID]]:
        """Create an instance of TableRequirement from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'AssertCreate':
            return import_module("polaris.catalog.models.assert_create").AssertCreate.from_dict(obj)
        if object_type ==  'AssertCurrentSchemaId':
            return import_module("polaris.catalog.models.assert_current_schema_id").AssertCurrentSchemaId.from_dict(obj)
        if object_type ==  'AssertDefaultSortOrderId':
            return import_module("polaris.catalog.models.assert_default_sort_order_id").AssertDefaultSortOrderId.from_dict(obj)
        if object_type ==  'AssertDefaultSpecId':
            return import_module("polaris.catalog.models.assert_default_spec_id").AssertDefaultSpecId.from_dict(obj)
        if object_type ==  'AssertLastAssignedFieldId':
            return import_module("polaris.catalog.models.assert_last_assigned_field_id").AssertLastAssignedFieldId.from_dict(obj)
        if object_type ==  'AssertLastAssignedPartitionId':
            return import_module("polaris.catalog.models.assert_last_assigned_partition_id").AssertLastAssignedPartitionId.from_dict(obj)
        if object_type ==  'AssertRefSnapshotId':
            return import_module("polaris.catalog.models.assert_ref_snapshot_id").AssertRefSnapshotId.from_dict(obj)
        if object_type ==  'AssertTableUUID':
            return import_module("polaris.catalog.models.assert_table_uuid").AssertTableUUID.from_dict(obj)

        raise ValueError("TableRequirement failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


