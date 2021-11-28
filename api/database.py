from neo4j import GraphDatabase


class Database:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def query(self, query):
        def do_cypher_tx(tx, cypher):
            result = tx.run(cypher)
            values = []
            for record in result:
                values.append(record.values())
            return values

        with self.driver.session() as session:
            return session.read_transaction(do_cypher_tx, query)


uri = "neo4j+s://dfeea193.databases.neo4j.io"
user = "neo4j"
password = "L0MRgXMmkrDDMTh2x0iZCz6-616wTwvBONMa8h_L9vg"
db = Database(uri, user, password)


def execute(query):
    return db.query(query)
