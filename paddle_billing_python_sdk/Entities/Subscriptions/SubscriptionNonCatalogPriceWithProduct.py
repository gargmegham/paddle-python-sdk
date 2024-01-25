from __future__  import annotations
from dataclasses import dataclass

from paddle_billing_python_sdk.Entities.Shared.CustomData        import CustomData
from paddle_billing_python_sdk.Entities.Shared.Money             import Money
from paddle_billing_python_sdk.Entities.Shared.PriceQuantity     import PriceQuantity
from paddle_billing_python_sdk.Entities.Shared.TaxMode           import TaxMode
from paddle_billing_python_sdk.Entities.Shared.UnitPriceOverride import UnitPriceOverride

from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionNonCatalogProduct import SubscriptionNonCatalogProduct


@dataclass
class SubscriptionNonCatalogPriceWithProduct:
    description:          str
    name:                 str | None
    product:              SubscriptionNonCatalogProduct
    tax_mode:             TaxMode
    unit_price:           Money
    unit_price_overrides: list[UnitPriceOverride]
    quantity:             PriceQuantity
    custom_data:          CustomData | None


    @staticmethod
    def from_dict(data: dict) -> SubscriptionNonCatalogPriceWithProduct:
        return SubscriptionNonCatalogPriceWithProduct(
            description          = data['description'],
            name                 = data.get('name'),
            product              = SubscriptionNonCatalogProduct.from_dict(data['product']),
            tax_mode             = TaxMode(data['tax_mode']),
            unit_price           = Money.from_dict(data['unit_price']),
            unit_price_overrides = [UnitPriceOverride.from_dict(override) for override in data['unit_price_overrides']],
            quantity             = PriceQuantity.from_dict(data['quantity']),
            custom_data          = CustomData(data['custom_data']) if data.get('custom_data') else None,
        )
