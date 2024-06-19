from dataclasses import dataclass
from typing import Any

from ..schemas import AvailableProductSchema, ProductSchema, ProductType

avail_prod_schema = AvailableProductSchema()
product_schema = ProductSchema()


@dataclass
class Product:
    name: str
    type: ProductType
    inventory: int
    id: int | None = None
    description: str | None = ""

    @staticmethod
    def validate_args(page_size: str | None, p_type: str | None) -> tuple[int, ProductType | None]:
        args = {"page_size": page_size, "type": p_type}
        data: dict = avail_prod_schema.load(args)  # type: ignore[reportAssignmentType]
        return data.get("page_size"), data.get("type")  # type: ignore[reportReturnType]

    @staticmethod
    def load(data: Any):
        data = product_schema.load(data)  # type: ignore[reportAssignmentType]
        return Product(**data)

    @staticmethod
    def load_many(data: Any):
        data = product_schema.load(data, many=True)  # type: ignore[reportAssignmentType]
        return [Product(**d) for d in data]

    @staticmethod
    def dump(products: "list[Product] | Product", status_code: int = 200):
        return product_schema.dump(products, many=isinstance(products, list)), status_code

    def asdict(self):
        return {
            "name": self.name,
            "type": self.type.value,
            "inventory": self.inventory,
        }
