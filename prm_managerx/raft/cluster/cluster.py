from typing import List
from time import sleep
import logging

from prm_managerx.raft.cluster.grpc_server import GRPCServer
from prm_managerx.mediator.base_component import BaseComponent


class Cluster(BaseComponent):
    """ This is our cluster class """

    def __init__(self) -> None:
        # super().__init__()
        logging.info("Starting cluster")
        self.log: List = []
        logging.info("Starting GRPC Server")
        self._grpc_server = GRPCServer()
    
    def replicate_log(self, item) -> bool:
        """ Simultes replicating a log """
        sleep(.5)
        logging.info("Replication log item: %s", item)
        self.mediator.notify(sender=self, event="replicate_log", item=item)

        return True

    def commit_log(self, index: int) -> bool:
        """ Simulate committing the log entry """
        logging.info("Committed log entry: %s", index)
        self.mediator.notify(sender=self, event="commit", index=index)


        return True
