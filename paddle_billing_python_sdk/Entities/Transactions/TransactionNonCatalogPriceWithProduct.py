from __future__  import annotations
from dataclasses import dataclass

from paddle_billing_python_sdk.Entities.Shared.CustomData        import CustomData
from paddle_billing_python_sdk.Entities.Shared.Money             import Money
from paddle_billing_python_sdk.Entities.Shared.PriceQuantity     import PriceQuantity
from paddle_billing_python_sdk.Entities.Shared.TaxMode           import TaxMode
from paddle_billing_python_sdk.Entities.Shared.TimePeriod        import TimePeriod
from paddle_billing_python_sdk.Entities.Shared.UnitPriceOverride import UnitPriceOverride

from paddle_billing_python_sdk.Entities.Transactions.TransactionNonCatalogProduct import TransactionNonCatalogProduct


@dataclass
class TransactionNonCatalogPriceWithProduct:
    description:          str
    name:                 str | None
    billing_cycle:        TimePeriod | None
    trial_period:         TimePeriod | None
    tax_mode:             TaxMode
    unit_price:           Money
    unit_price_overrides: list[UnitPriceOverride]
    quantity:             PriceQuantity
    custom_data:          CustomData | None
    product:              TransactionNonCatalogProduct


    @staticmethod
    def from_dict(data: dict) -> TransactionNonCatalogPriceWithProduct:
        return TransactionNonCatalogPriceWithProduct(
            description          = data['description'],
            name                 = data.get('name'),
            billing_cycle        = TimePeriod.from_dict(data['billing_cycle']) if 'billing_cycle' in data and data['billing_cycle'] != '' else None,
            trial_period         = TimePeriod.from_dict(data['trial_period'])  if 'trial_period'  in data and data['trial_period'] != '' else None,
            tax_mode             = data['tax_mode'],
            unit_price           = Money.from_dict(data['unit_price']),
            unit_price_overrides = [UnitPriceOverride.from_dict(item) for item in data['unit_price_overrides']],
            quantity             = PriceQuantity.from_dict(data['quantity']),
            custom_data          = CustomData(data['custom_data']) if 'custom_data' in data and data['custom_data'] != '' else None,
            product              = TransactionNonCatalogProduct.from_dict(data['product_id']),
        )
