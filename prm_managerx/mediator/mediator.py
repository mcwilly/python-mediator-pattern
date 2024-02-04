""" This is our mediator class """

from abc import ABC
# from queue import Queue
# from typing import Type

# from prm_managerx.prm.resource_manager.manager import ResourceManager
# from prm_managerx.raft.cluster.cluster import Cluster

class Mediator(ABC):

    def notify(self) -> None: #, sender: object, event: str, item: object, index: int = None ) -> None:
        pass

    def replicate_log(self) -> None:#, sender: object, event: str, item: object) -> int:
        pass
    
    def commit_log(self) -> None: #, sender: object, event: str, index: int) -> None:
        pass
