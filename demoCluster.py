"""Demo Cluster"""

from typing import Any
from DeeCluster import Cluster

from darwen import darwen_Database
from date import date
from darwen import darwen
from date import date_Database


class demo_Cluster(Cluster):
    def __init__(self, name: str) -> None:
        """Define initial databases
        (Called once on cluster creation)"""
        super().__init__(name)

        self.date: Any | date_Database = date
        self.darwen: Any | darwen_Database = darwen


# Create the cluster
demoCluster = demo_Cluster("demo")

###################################
if __name__ == "__main__":
    print((demoCluster.databases))
