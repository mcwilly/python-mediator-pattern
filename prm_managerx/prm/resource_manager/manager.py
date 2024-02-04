""" Simulated Resource Manager """

from prm_managerx.prm.resource_manager.resource_cache import ResourceCache
from prm_managerx.mediator.base_component import BaseComponent


class ResourceManager(BaseComponent):

    def __init__(self):
        # super().__init__()
        self.cache = ResourceCache()
