from abc import ABC, abstractmethod

from typing import List

from specmatic.actuator import spring_actuator_route
from specmatic.actuator.spring_actuator_route import SpringActuatorRoute


class AppRouteAdapter(ABC):
    @abstractmethod
    def to_actuator_routes(self) -> List[SpringActuatorRoute]:
        pass
