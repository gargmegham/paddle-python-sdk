from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime

from paddle_billing_python_sdk.Entities.Entity import Entity

from paddle_billing_python_sdk.Entities.Reports.ReportFilters import ReportFilters
from paddle_billing_python_sdk.Entities.Reports.ReportStatus  import ReportStatus
from paddle_billing_python_sdk.Entities.Reports.ReportType    import ReportType


@dataclass
class Report(Entity):
    id:         str
    status:     ReportStatus
    rows:       int | None
    type:       ReportType
    filters:    list[ReportFilters]
    expires_at: datetime | None
    created_at: datetime
    updated_at: datetime


    @classmethod
    def from_dict(cls, data: dict) -> Report:
        return Report(
            id         = data['id'],
            status     = ReportStatus(data['status']),
            rows       = data.get('rows'),
            type       = ReportType(data['type']),
            filters    = [ReportFilters.from_dict(a_filter) for a_filter in data.get('filters', [])],
            expires_at = datetime.fromisoformat(data['expires_at']) if 'expires_at' in data and data['expires_at'] != '' else None,
            created_at = datetime.fromisoformat(data['created_at']),
            updated_at = datetime.fromisoformat(data['updated_at']),
        )
