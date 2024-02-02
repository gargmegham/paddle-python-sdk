from datetime import datetime

from paddle_billing.Entities.Event         import Event
from paddle_billing.Entities.Events        import EventTypeName
from paddle_billing.Entities.Notifications import NotificationSubscription


class SubscriptionActivated(Event):
    def __init__(
        self,
        event_id:    str,
        event_type:  EventTypeName,
        occurred_at: datetime,
        data:        NotificationSubscription,
    ):
        super().__init__(event_id, event_type, occurred_at, data)
