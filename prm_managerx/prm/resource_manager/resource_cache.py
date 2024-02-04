""" this is our simulated resource cache """

import logging

from prm_managerx.mediator.base_component import BaseComponent

class ResourceCache(BaseComponent):

    def __init__(self) -> None:
        # super().__init__()
        logging.info("Starting Resource Cache")
        self._cache = {}
        logging.info("ResourceCache initialized")
        logging.info("Started Resource Cache")

    def modify_cache(self, item_id: str, item: str):
        logging.info("modify_cache: replicating log")
        _index = self.mediator.replicate_log(sender=self, event="replicate_log", item=item)
        logging.info("modify_cache: commiting log")
        self.mediator.commit_log(sender=self, event="commit", index=_index)
        self._cache[item_id] = item
