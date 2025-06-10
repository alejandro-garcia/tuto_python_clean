from src.resources.application.create_resource import CreateResource
from src.resources.domain.models import Resource
from src.resources.domain.repositories import ResourcesRepository
from src.resources.application.create_resource import CreateResourceCommand
from src.resources.domain.exceptions import UrlIsNotValid
import pytest

class FakeResourcesRepository(ResourcesRepository):
    def __init__(self):
        self._resources: list[Resource] = []
    
    def all(self) -> list[Resource]: 
        return self._resources
    
    def save(self, resource: Resource) -> None: 
        self._resources.append(resource)


class TestCreateResource:
    def test_creates_resource(self) -> None:
        resource_repository = FakeResourcesRepository()

        with pytest.raises(UrlIsNotValid):
            CreateResource(resource_repository).execute(
                CreateResourceCommand(
                    resource_url="https://example.com"
                )
            )

        resources = resource_repository.all()
        assert len(resources) == 1 
        assert resources[0].url() == "https://example.com"
