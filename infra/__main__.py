"""An Azure RM Python Pulumi program"""

import pulumi
import yaml
import json
from pulumi_azure_native import resources
from resources_dir.storage import StorageResource
from resources_dir.keyvault import KeyvaultResource
from resources_dir.security import SecurityResource
from resources_dir.networking import VirtualNetworkResource
from resources_dir.bastion import BastionHostResource
from resources_dir.compute import VirtualMachineResource
from dto import ConfigDTO



# Create an Azure Resource Group
# Naming convention is
# rg = resource group
# ac = Applied Curiosity
# cus = Central US
# adb = Azure Databricks
# acclrtor = Accelerator


resource_group = resources.ResourceGroup('rg-ac-cus-adb-acclrtor') # I reckon I need to put this in its own python file

config_path = 'config/dev.yml'

with open(config_path, 'r') as file:
     config_data = yaml.safe_load(file)

config_dto = ConfigDTO.from_dict(config_data)

storage_resource = StorageResource(config_dto.storage)
keyvault_resource = KeyvaultResource(config_dto.keyvault)
nsg_resource = SecurityResource(config_dto.nsg)
vnet_resource = VirtualNetworkResource(config_dto.vnet)
# vm_resource = VirtualMachineResource(config_dto.vm)


# exporting pulumi resources


pulumi.export('storage_resource_outputs', storage_resource.output_dto().outputs)
pulumi.export('keyvault_resources_outputs', keyvault_resource.output_dto().outputs)
