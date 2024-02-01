from dataclasses import asdict, dataclass

from paddle_billing.Undefined import Undefined

from paddle_billing.Entities.Shared.CustomData import CustomData
from paddle_billing.Entities.Shared.Status     import Status


@dataclass
class UpdateCustomer:
    email:       str        | None | Undefined = Undefined()
    name:        str        | None | Undefined = Undefined()
    custom_data: CustomData | None | Undefined = Undefined()
    locale:      str        | None | Undefined = Undefined()
    status:      Status     | None | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)