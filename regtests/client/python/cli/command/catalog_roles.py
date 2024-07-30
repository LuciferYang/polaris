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
from dataclasses import dataclass
from typing import Dict, Optional

from pydantic import StrictStr

from cli.command import Command
from cli.constants import Subcommands
from polaris.management import PolarisDefaultApi, CreateCatalogRoleRequest, CatalogRole, UpdateCatalogRoleRequest, \
    GrantCatalogRoleRequest


@dataclass
class CatalogRolesCommand(Command):
    """
    A Command implementation to represent `polaris catalog-roles`. The instance attributes correspond to parameters
    that can be provided to various subcommands, except `catalog_roles_subcommand` which represents the subcommand
    itself.

    Example commands:
        * ./polaris catalog-roles create --catalog bronze_catalog cat_role
        * ./polaris catalog-roles list --catalog bronze_catalog --principal-role data-analyst
        * ./polaris catalog-roles grant --catalog bronze_catalog --principal-role data-engineer etl_role
    """

    catalog_roles_subcommand: str
    catalog_name: str
    catalog_role_name: str
    principal_role_name: str
    properties: Optional[Dict[str, StrictStr]]

    def validate(self):
        if not self.catalog_name:
            raise Exception("Missing required argument: --catalog")
        if self.catalog_roles_subcommand in {Subcommands.GRANT, Subcommands.REVOKE}:
            if not self.principal_role_name:
                raise Exception("Missing required argument: --principal")

    def execute(self, api: PolarisDefaultApi) -> None:
        if self.catalog_roles_subcommand == Subcommands.CREATE:
            request = CreateCatalogRoleRequest(
                catalog_role=CatalogRole(
                    name=self.catalog_role_name,
                    properties=self.properties
                )
            )
            api.create_catalog_role(self.catalog_name, request)
        elif self.catalog_roles_subcommand == Subcommands.DELETE:
            api.delete_catalog_role(self.catalog_name, self.catalog_role_name)
        elif self.catalog_roles_subcommand == Subcommands.GET:
            print(api.get_catalog_role(self.catalog_name, self.catalog_role_name).to_json())
        elif self.catalog_roles_subcommand == Subcommands.LIST:
            if self.principal_role_name:
                for catalog_role in api.list_catalog_roles_for_principal_role(
                        self.principal_role_name, self.catalog_name).roles:
                    print(catalog_role.to_json())
            else:
                for catalog_role in api.list_catalog_roles(self.catalog_name).roles:
                    print(catalog_role.to_json())
        elif self.catalog_roles_subcommand == Subcommands.UPDATE:
            catalog_role = api.get_catalog_role(self.catalog_name, self.catalog_role_name)
            request = UpdateCatalogRoleRequest(
                current_entity_version=catalog_role.entity_version,
                properties=self.properties
            )
            api.update_catalog_role(self.catalog_name, self.catalog_role_name, request)
        elif self.catalog_roles_subcommand == Subcommands.GRANT:
            request = GrantCatalogRoleRequest(
                catalog_role=CatalogRole(
                    name=self.catalog_role_name
                ),
                properties=self.properties
            )
            api.assign_catalog_role_to_principal_role(self.principal_role_name, self.catalog_name, request)
        elif self.catalog_roles_subcommand == Subcommands.REVOKE:
            api.revoke_catalog_role_from_principal_role(
                self.principal_role_name, self.catalog_name, self.catalog_role_name)
        else:
            raise Exception(f"{self.catalog_roles_subcommand} is not supported in the CLI")
