from typing import TYPE_CHECKING, Union

from paddle_billing_python_sdk.ResponseParser import ResponseParser

from paddle_billing_python_sdk.Entities.Product                                   import Product
from paddle_billing_python_sdk.Entities.ProductWithIncludes                       import ProductWithIncludes
from paddle_billing_python_sdk.Entities.Collections.Paginator                     import Paginator
from paddle_billing_python_sdk.Entities.Collections.ProductWithIncludesCollection import ProductWithIncludesCollection
from paddle_billing_python_sdk.Entities.Shared.Status                             import Status

from paddle_billing_python_sdk.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing_python_sdk.Resources.Products.Operations.CreateProduct import CreateProduct
from paddle_billing_python_sdk.Resources.Products.Operations.ListProducts  import ListProducts
from paddle_billing_python_sdk.Resources.Products.Operations.UpdateProduct import UpdateProduct
from paddle_billing_python_sdk.Resources.Products.Operations.List.Includes import Includes


if TYPE_CHECKING:
    from paddle_billing_python_sdk.Client import Client


class ProductsClient:
    def __init__(self, client: 'Client'):
        self.client   = client
        self.response = None


    def list(self, operation: ListProducts = None) -> ProductWithIncludesCollection:
        if operation is None:
            operation = ListProducts()

        self.response = self.client.get_raw('/products', operation.get_parameters())
        parser        = ResponseParser(self.response)

        return ProductWithIncludesCollection.from_list(
            parser.get_data(),
            Paginator(self.client, parser.get_pagination(), ProductWithIncludesCollection)
        )


    def get(self, product_id: str, includes = None) -> Product | ProductWithIncludes:
        if product_id is None:
            raise ValueError('product_id is required')
        if not isinstance(product_id, str):
            raise ValueError('product_id must be a string')

        if includes is None:
            includes = []

        invalid_items = [item for item in includes if not isinstance(item, Includes)]
        if invalid_items:
            raise InvalidArgumentException('includes', Includes.__name__, invalid_items)

        params         = {'include': ','.join(include.value for include in includes)} if includes else {}
        self.response = self.client.get_raw(f"/products/{product_id}", params)
        parser         = ResponseParser(self.response)

        return ProductWithIncludes.from_dict(parser.get_data()) \
            if includes \
            else Product.from_dict(parser.get_data())


    def create(self, operation: CreateProduct) -> Product:
        self.response = self.client.post_raw('/products', operation.get_parameters())
        parser         = ResponseParser(self.response)

        return Product.from_dict(parser.get_data())


    def update(self, product_id: str, operation: UpdateProduct) -> Product:
        self.response = self.client.patch_raw(f"/products/{product_id}", operation.get_parameters())
        parser         = ResponseParser(self.response)

        return Product.from_dict(parser.get_data())


    def archive(self, product_id: str) -> Product:
        return self.update(product_id, UpdateProduct(status=Status.Archived))
