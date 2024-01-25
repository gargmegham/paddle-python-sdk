from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing_python_sdk.Entities.Entity import Entity

from paddle_billing_python_sdk.Entities.Shared.BillingDetails            import BillingDetails
from paddle_billing_python_sdk.Entities.Shared.CollectionMode            import CollectionMode
from paddle_billing_python_sdk.Entities.Shared.CurrencyCode              import CurrencyCode
from paddle_billing_python_sdk.Entities.Shared.CustomData                import CustomData
from paddle_billing_python_sdk.Entities.Shared.TimePeriod                import TimePeriod
from paddle_billing_python_sdk.Entities.Shared.TransactionDetailsPreview import TransactionDetailsPreview

from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionDiscount                         import SubscriptionDiscount
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionItem                             import SubscriptionItem
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionManagementUrls                   import SubscriptionManagementUrls
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionNextTransaction                  import SubscriptionNextTransaction
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionPreviewSubscriptionUpdateSummary import SubscriptionPreviewSubscriptionUpdateSummary
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionScheduledChange                  import SubscriptionScheduledChange
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionStatus                           import SubscriptionStatus
from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionTimePeriod                       import SubscriptionTimePeriod


@dataclass
class SubscriptionPreview(Entity):
    status:                        SubscriptionStatus
    customer_id:                   str
    address_id:                    str
    business_id:                   str | None
    currency_code:                 CurrencyCode
    created_at:                    datetime
    updated_at:                    datetime
    started_at:                    datetime | None
    first_billed_at:               datetime | None
    next_billed_at:                datetime | None
    paused_at:                     datetime | None
    canceled_at:                   datetime | None
    discount:                      SubscriptionDiscount | None
    collection_mode:               CollectionMode
    billing_details:               BillingDetails | None
    current_billing_period:        SubscriptionTimePeriod | None
    billing_cycle:                 TimePeriod
    scheduled_change:              SubscriptionScheduledChange | None
    management_urls:               SubscriptionManagementUrls
    items:                         list[SubscriptionItem]
    custom_data:                   CustomData | None
    immediate_transaction:         SubscriptionNextTransaction | None
    next_transaction:              SubscriptionNextTransaction | None
    recurring_transaction_details: TransactionDetailsPreview | None
    update_summary:                SubscriptionPreviewSubscriptionUpdateSummary | None


    @classmethod
    def from_dict(cls, data: dict) -> SubscriptionPreview:
        return SubscriptionPreview(
            status                        = SubscriptionStatus(data['status']),
            customer_id                   = data['customer_id'],
            address_id                    = data['address_id'],
            business_id                   = data.get('business_id'),
            currency_code                 = CurrencyCode(data['currency_code']),
            created_at                    = datetime.fromisoformat(data['created_at']),
            updated_at                    = datetime.fromisoformat(data['updated_at']),
            started_at                    = datetime.fromisoformat(data['started_at']) if 'started_at' in data and data['started_at'] != '' else None,
            first_billed_at               = datetime.fromisoformat(data['first_billed_at']) if 'first_billed_at' in data and data['first_billed_at'] != '' else None,
            next_billed_at                = datetime.fromisoformat(data['next_billed_at']) if 'next_billed_at' in data and data['next_billed_at'] != '' else None,
            paused_at                     = datetime.fromisoformat(data['paused_at']) if 'paused_at' in data and data['paused_at'] != '' else None,
            canceled_at                   = datetime.fromisoformat(data['canceled_at']) if 'canceled_at' in data and data['canceled_at'] != '' else None,
            discount                      = SubscriptionDiscount.from_dict(data['discount']) if 'discount' in data and data['discount'] != '' else None,
            collection_mode               = CollectionMode(data['collection_mode']),
            billing_details               = BillingDetails.from_dict(data['billing_details']) if 'billing_details' in data and data['billing_details'] != '' else None,
            current_billing_period        = SubscriptionTimePeriod.from_dict(data['current_billing_period']) if 'current_billing_period' in data and data['current_billing_period'] != '' else None,
            billing_cycle                 = TimePeriod.from_dict(data['billing_cycle']),
            scheduled_change              = SubscriptionScheduledChange.from_dict(data['scheduled_change']) if 'scheduled_change' in data and data['scheduled_change'] != '' else None,
            management_urls               = SubscriptionManagementUrls.from_dict(data['management_urls']) if 'management_urls' in data and data['management_urls'] != '' else None,
            items                         = [SubscriptionItem.from_dict(item) for item in data['items']],
            custom_data                   = CustomData(data['custom_data']) if 'custom_data' in data and data['custom_data'] != '' else None,
            immediate_transaction         = SubscriptionNextTransaction.from_dict(data['immediate_transaction']) if 'immediate_transaction' in data and data['immediate_transaction'] != '' else None,
            next_transaction              = SubscriptionNextTransaction.from_dict(data['next_transaction']) if 'next_transaction' in data and data['next_transaction'] != '' else None,
            recurring_transaction_details = TransactionDetailsPreview.from_dict(data['recurring_transaction_details']) if 'recurring_transaction_details' in data and data['recurring_transaction_details'] != '' else None,
            update_summary                = SubscriptionPreviewSubscriptionUpdateSummary.from_dict(data['update_summary']) if 'update_summary' in data and data['update_summary'] != '' else None,
        )
