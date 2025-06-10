from dataclasses import dataclass

from src.resources.domain.models import Resource
from src.resources.domain.repositories import ResourcesRepository

@dataclass
class CreateResourceCommand:
    resource_url: str


class CreateResource:
    def __init__(self, repository: ResourcesRepository) -> None:
        self._repository = repository
    
    def execute(self, command: CreateResourceCommand) -> None:
        resource = Resource.create(resource_url=command.resource_url)
        self._repository.save(resource)