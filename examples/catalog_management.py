import json
from os import getenv

from paddle_billing import Client, Environment, Options

from paddle_billing.Entities.Shared import (
    CountryCode,
    CurrencyCode,
    CustomData,
    Money,
    TimePeriod,
    PriceQuantity,
    UnitPriceOverride,
    Interval,
    Status,
    TaxCategory
)

from paddle_billing.Exceptions.ApiError                        import ApiError
from paddle_billing.Exceptions.SdkExceptions.MalformedResponse import MalformedResponse

from paddle_billing.Resources.Products.Operations import CreateProduct, UpdateProduct, ListProducts, ProductIncludes
from paddle_billing.Resources.Prices.Operations   import CreatePrice, UpdatePrice, PriceIncludes


# Verify your Paddle API key was provided by a PADDLE_SECRET_API_KEY environment variable
# It is strongly advised that you do not include secrets in your source code
# Use environment variables, and/or secrets management like Vault to obtain your secrets
api_key: str = getenv('PADDLE_SECRET_API_KEY', None)
if not api_key:
    raise ValueError("You must provide the PADDLE_API_KEY in your environment variables")

# Determine the environment, defaulting to sandbox
environment = getenv('PADDLE_ENVIRONMENT', 'sandbox')
paddle_environment = getattr(Environment, environment)  # E.g. Environment.sandbox

# Initialize the Paddle client
paddle = Client(api_key, options=Options(paddle_environment))


# ┌───
# │ Create Product │
# └────────────────┘
try:
    product = paddle.products.create(CreateProduct(
        name         = 'Kitten Service',
        tax_category = TaxCategory.Standard,
        description  = 'Simply an awesome product',
        image_url    = 'http://placekitten.com/200/300',
        custom_data  = CustomData({'foo': 'bar'}),
    ))
except (ApiError, MalformedResponse) as e:
    print(e)
    exit()

print(f"Created product '{product.id}': {product.description}")
print(f"product={product}\n\n")


# ┌───
# │ Update Product │
# └────────────────┘
try:
    product = paddle.products.update(product.id, UpdateProduct(
        name        = 'Bear Service',
        image_url   = 'https://placebear.com/200/300',
        custom_data = CustomData({'beep': 'boop'}),
    ))
except (ApiError, MalformedResponse) as e:
    print(e)
    exit()

print(f"Updated product '{product.id}': {product.description}")
print(f"product={product}\n\n")


# ┌───
# │ Create Price │
# └──────────────┘
try:
    price = paddle.prices.create(CreatePrice(
        description   = 'Bear Hug',
        product_id    = product.id,
        unit_price    = Money('1000', CurrencyCode.GBP),
        trial_period  = TimePeriod(Interval.Week, 1),
        billing_cycle = TimePeriod(Interval.Year, 1),
        quantity      = PriceQuantity(1, 1),
        custom_data   = CustomData({'foo': 'bar'}),

        unit_price_overrides=[
            UnitPriceOverride(
                [CountryCode.CA, CountryCode.US],
                Money('5000', CurrencyCode.USD),
            ),
        ],
    ))
except (ApiError, MalformedResponse) as e:
    print(e)
    exit()

print(f"Created price '{price.id}': {price.description}")
print(f"price={price}\n\n")


# ┌───
# │ Update Price │
# └──────────────┘
try:
    price = paddle.prices.update(price.id, UpdatePrice(
        description = 'One-off Bear Hug',
        unit_price  = Money('500', CurrencyCode.GBP),
        custom_data = CustomData({'beep': 'boop'}),
    ))
except (ApiError, MalformedResponse) as e:
    print(e)
    exit()

print(f"Updated price '{price.id}': {price.description}")
print(f"price={price}\n\n")


# ┌───
# │ Get Product with Prices │
# └─────────────────────────┘
try:
    product = paddle.products.get(product.id, [ProductIncludes.Prices])
except (ApiError, MalformedResponse) as e:
    print(e)
    exit()

print(f"Read product '{product.id}' with prices " + ', '.join([str(p.id) for p in product.prices]))


# ┌───
# │ Get Price with Product │
# └────────────────────────┘
try:
    price = paddle.prices.get(price.id, [PriceIncludes.Product])
except (ApiError, MalformedResponse) as e:
    print(e)
    exit()

print(f"Read price '{price.id}' with product {price.product.id if price.product else '????'}")


# ┌───
# │ Get Products │
# └──────────────┘
try:
    products = paddle.products.list(ListProducts(
        includes = [ProductIncludes.Prices],
        statuses = [Status.Active],
    ))
except (ApiError, MalformedResponse) as e:
    print(e)
    exit()


# ┌───
# │ Iterate Products and Prices │
# └─────────────────────────────┘
for product in products:
    print(product.name)
    print('-' * len(product.name))
    for price in product.prices:
        print(f"{price.unit_price.amount} - {price.description}")
    print()
