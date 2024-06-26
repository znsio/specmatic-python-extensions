import enum

from pydantic import BaseModel, Field, StrictInt, StrictStr


class OrderStatus(str, enum.Enum):
    FULFILLED = "fulfilled"
    PENDING = "pending"
    CANCELLED = "cancelled"


class ProductType(str, enum.Enum):
    GADGET = "gadget"
    FOOD = "food"
    BOOK = "book"
    OTHER = "other"


class Product(BaseModel):
    name: StrictStr
    type: ProductType
    inventory: StrictInt = Field(ge=1, le=101)
    id: StrictInt | None = None
    description: StrictStr | None = ""


class Order(BaseModel):
    productid: StrictInt
    count: StrictInt
    status: OrderStatus = OrderStatus.PENDING
