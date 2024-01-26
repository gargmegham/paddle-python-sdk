from paddle_billing_python_sdk.Entities.Shared.Status      import Status

from paddle_billing_python_sdk.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing_python_sdk.Resources.Shared.Operations.List.Pager import Pager


class ListBusinesses:
    def __init__(
        self,
        pager:    Pager        = None,
        ids:      list[str]    = None,
        statuses: list[Status] = None,
        search:   str          = None,
    ):
        self.pager    = pager
        self.ids      = ids      if ids      is not None else []
        self.statuses = statuses if statuses is not None else []
        self.search   = search

        # Validation
        for field_name, field_value, field_type in [
            ('ids',      self.ids,      str),
            ('statuses', self.statuses, Status),
        ]:
            invalid_items = [item for item in field_value if not isinstance(item, field_type)]
            if invalid_items:
                raise InvalidArgumentException(field_name, field_type.__name__, invalid_items)


    def get_parameters(self) -> dict:
        enum_stringify = lambda enum: enum.value  # noqa E731

        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.ids:
            parameters['id'] = ','.join(self.ids)
        if self.statuses:
            parameters['status'] = ','.join(map(enum_stringify, self.statuses))
        if self.search:
            parameters['search'] = self.search

        return parameters