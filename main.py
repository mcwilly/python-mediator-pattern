### this is a test structure using the mediator pattern ###

import logging

from prm_managerx.raft.cluster.cluster import Cluster
from prm_managerx.prm.resource_manager.manager import ResourceManager
from prm_managerx.raft.cluster.cluster_mediator import ClusterMediator

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def main():
    cluster = Cluster()
    rm = ResourceManager()
    mediator = ClusterMediator(resource_manager=rm, cluster=cluster)

    rm.cache.modify_cache(item_id="my_object", item="abc")

    print(rm.cache)


if __name__ == "__main__":
    main()
