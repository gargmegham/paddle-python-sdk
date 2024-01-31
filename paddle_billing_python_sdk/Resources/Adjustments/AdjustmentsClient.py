from typing import TYPE_CHECKING

from paddle_billing_python_sdk.ResponseParser import ResponseParser

from paddle_billing_python_sdk.Entities.Adjustment                       import Adjustment
from paddle_billing_python_sdk.Entities.Collections.Paginator            import Paginator
from paddle_billing_python_sdk.Entities.Collections.AdjustmentCollection import AdjustmentCollection

from paddle_billing_python_sdk.Resources.Adjustments.Operations.CreateAdjustment import CreateAdjustment
from paddle_billing_python_sdk.Resources.Adjustments.Operations.ListAdjustments  import ListAdjustments


if TYPE_CHECKING:
    from paddle_billing_python_sdk.Client import Client


class AdjustmentsClient:
    def __init__(self, client: 'Client'):
        self.client   = client
        self.response = None


    def list(self, operation: ListAdjustments = None) -> AdjustmentCollection:
        if operation is None:
            operation = ListAdjustments()

        self.response = self.client.get_raw('/adjustments', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return AdjustmentCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), AdjustmentCollection)
        )


    def create(self, operation: CreateAdjustment) -> Adjustment:
        self.response = self.client.post_raw('/adjustments', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return Adjustment.from_dict(parser.get_data())
