from dataclasses import dataclass

from src.resources.domain.models import Resource
from src.resources.domain.repositories import ResourcesRepository
from src.resources.domain.value_objects import ResourceUrl

@dataclass
class CreateResourceCommand:
    resource_url: ResourceUrl


class CreateResource:
    def __init__(self, repository: ResourcesRepository) -> None:
        self._repository = repository
    
    def execute(self, command: CreateResourceCommand) -> None:
        resource_url = ResourceUrl(value=command.resource_url)
        resource = Resource.create(resource_url=resource_url)
        self._repository.save(resource)
