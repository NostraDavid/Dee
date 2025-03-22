"""DeeCluster: provides a namespace for a set of DeeDatabases"""

__version__ = "0.1"
__author__ = "Greg Gaughan"
__copyright__ = "Copyright (C) 2007 Greg Gaughan"
__license__ = "GPL"  # see Licence.txt for licence information

from typing import Any, Generator
from Dee import Relation, Tuple
from DeeDatabase import Database


class Cluster(dict[str, Any]):
    """A namespace for databases"""

    def __init__(self, name: str = "nemo") -> None:
        """Create a Cluster

        Define initial databases here
        (Called once on cluster creation)
        """
        dict.__init__(self)

        self.name = name

        self.databases = Relation(["database_name"], self.vdatabases)
        # todo should really have relations, attributes etc. to define this...

    def __getattr__(self, key: str) -> Any:
        if key in self:
            return self[key]
        raise AttributeError(repr(key))

    def __setattr__(self, key: str, value: Any):
        # todo reject non-Database?
        self[key] = value

    # todo delattr

    def __contains__(self, item: Any) -> bool:
        if item in self.__dict__:
            if isinstance(self.__dict__[item], Database):
                return True
        return False

    def __iter__(self) -> Generator[tuple[str, Database], Any, None]:
        for k, v in list(self.items()):
            # for (k, v) in self.__dict__.items():
            if isinstance(v, Database):
                yield (k, v)

    def vdatabases(self) -> list[Tuple]:
        return [Tuple(database_name=k) for (k, v) in self]
