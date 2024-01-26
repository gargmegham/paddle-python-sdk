from dataclasses import dataclass, asdict

from paddle_billing_python_sdk.Undefined import Undefined

from paddle_billing_python_sdk.Entities.Shared.CatalogType import CatalogType
from paddle_billing_python_sdk.Entities.Shared.CustomData  import CustomData
from paddle_billing_python_sdk.Entities.Shared.Status      import Status
from paddle_billing_python_sdk.Entities.Shared.TaxCategory import TaxCategory


@dataclass
class UpdateProduct:
    name:         str         | None | Undefined = Undefined()
    description:  str         | None | Undefined = Undefined()
    type:         CatalogType | None | Undefined = Undefined()
    tax_category: TaxCategory | None | Undefined = Undefined()
    image_url:    str         | None | Undefined = Undefined()
    custom_data:  CustomData  | None | Undefined = Undefined()
    status:       Status      | None | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)
