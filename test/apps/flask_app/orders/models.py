from dataclasses import dataclass
from typing import Any

from ..schemas import OrderSchema, OrderStatus

order_schema = OrderSchema()


@dataclass
class Order:
    status: OrderStatus
    productid: int
    count: int

    @staticmethod
    def load(data: Any):
        data = order_schema.load(data)  # type: ignore[reportAssignmentType]
        return Order(**data)

    def asdict(self):
        return {"status": self.status.value, "productid": self.productid, "count": self.count}
