from cypher_query_loader import CypherQueries
from pathlib import Path
import os

def test_query_loader():
    cypher_dir = Path(__file__).parent / 'cypher'
    queries = CypherQueries(cypher_dir)
    assert queries.fetch_k_nodes.query == 'MATCH (n) RETURN n LIMIT $limit;'
    assert queries.fetch_k_nodes.params == {'limit':None}