from typing import Type

from prm_managerx.mediator.mediator import Mediator
from prm_managerx.prm.resource_manager.manager import ResourceManager
from prm_managerx.raft.cluster.cluster import Cluster

class ClusterMediator(Mediator):

    def __init__(self, resource_manager: ResourceManager, cluster: Cluster) -> None:
        self._resource_manager = resource_manager
        self._resource_manager.mediator = self
        self._cluster = cluster
        self._cluster.mediator = self
        self._resource_manager.cache.mediator = self

    # def notify(self, sender: object, event: str, item: object, index: int = None) -> None:
    #     if event == "replicate_log":
    #         print(f"Mediator reacts on {event}")
    #         print(f"Sender is {sender}")
    #     elif event == "commit":
    #         print(f"Mediator reacts on {event}")
    #         print(f"Index to commit is {index}")
    #         print(f"Sender is {sender}")
    
    def replicate_log(self, sender: object, event: str, item: object) -> int:
            print(f"Mediator reacts on {event}")
            print(f"Item to replicate is {item}")
            print(f"Sender is {sender}")
            self._cluster.log.append(item)
            return len(self._cluster.log)

    
    def commit_log(self, sender: object, event: str, index: int) -> None:
            print(f"Mediator reacts on {event}")
            print(f"Index to commit is {index}")
            print(f"Sender is {sender}")
