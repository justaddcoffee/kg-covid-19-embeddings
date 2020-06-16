import logging
from time import time
from embiggen import Graph, GraphFactory

start = time()
factory = GraphFactory(default_directed=True)
logging.info("Reading in graph files")
graph = factory.read_csv(
    "kg-covid-19-training-data/pos_train_edges.tsv",
    "kg-covid-19-training-data/pos_train_nodes.tsv"
)
logging.info("Performing random walks")
graph.random_walk(number=10, length=80)
delta = time() - start
