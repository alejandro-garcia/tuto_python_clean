from abc import ABC, abstractmethod
from src.resources.domain.models import Resource

class ResourcesRepository(ABC):
    @abstractmethod
    def all(self) -> list[Resource]: ...
    
    @abstractmethod
    def save(self, resource: Resource) -> None: ...