from dataclasses import asdict, dataclass

from paddle_billing_python_sdk.Undefined import Undefined

from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionEffectiveFrom    import SubscriptionEffectiveFrom
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionItems            import SubscriptionItems
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionItemsWithPrice   import SubscriptionItemsWithPrice
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionOnPaymentFailure import SubscriptionOnPaymentFailure


@dataclass
class PreviewOneTimeCharge:
    effective_from:     SubscriptionEffectiveFrom
    items:              list[SubscriptionItems | SubscriptionItemsWithPrice]
    on_payment_failure: SubscriptionOnPaymentFailure | Undefined = Undefined()


    def get_parameters(self) -> dict:
        return asdict(self)