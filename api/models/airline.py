from api.database import execute


class Airline:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def index():
        result = execute("MATCH (a:Airline) RETURN a")
        return result

    def exists(self):
        result = execute("MATCH (a:Airline {name: '%s'}) RETURN a" % self.name)
        return len(result) > 0

    def add(self):
        if self.exists():
            return False
        else:
            execute("CREATE (a:Airline {name: '%s'}) RETURN a" % self.name)
            return True

    def delete(self):
        if self.exists():
            execute("MATCH (a:Airline {name: '%s'}) DETACH DELETE a" % self.name)
            return True
        else:
            return False

    def hub(self, airport):
        if self.exists() and airport.exists():
            execute(
                "MATCH (a:Airline {name: '%s'}),(p:Airport {name:'%s', city:'%s'}) MERGE(a)-[r:HUB]->(p) RETURN a,p" % (
                    self.name, airport.name, airport.city))
            return True
        else:
            return False

    def alliance(self, airline):
        if self.exists() and airline.exists():
            return execute(
                "MATCH (a:Airline {name: '%s'}),(p:Airline {name:'%s'}) MERGE(a)<-[r:ALLIANCE]->(p) RETURN a,p" % (
                    self.name, airline.name))
        else:
            return False

    def hub_info(self):
        if self.exists():
            return execute("OPTIONAL MATCH (a:Airline {name:'%s'})-[r:HUB]-(p:Airport) RETURN a, r, p" % self.name)
        else:
            return False

    def alliance_info(self):
        if self.exists():
            return execute("OPTIONAL MATCH (a:Airline {name:'%s'})-[r:ALLIANCE]-(p:Airline) RETURN a, r, p" % self.name)
        else:
            return False
