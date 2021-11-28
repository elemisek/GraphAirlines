from api.database import execute


class Airport:

    def __init__(self, name, city):
        self.name = name
        self.city = city

    @staticmethod
    def index():
        result = execute("MATCH (a:Airport) RETURN a")
        return result

    def exists(self):
        result = execute("MATCH (a:Airport {name: '%s', city: '%s'}) RETURN a" % (self.name, self.city))
        return len(result) > 0

    def add(self):
        if self.exists():
            return False
        else:
            return execute("CREATE (a:Airport {name: '%s', city: '%s'}) RETURN a" % (self.name, self.city))

    def delete(self):
        if self.exists():
            return execute("MATCH (a:Airport {name: '%s', city: '%s'}) DETACH DELETE a" % (self.name, self.city))
        else:
            return False

    def distance(self, airport, distance):
        if self.exists() and airport.exists():
            return execute(
                "MATCH (a:Airport {name:'%s', city:'%s'}),(p:Airport {name:'%s', city:'%s'}) MERGE(a)-[d:DISTANCE "
                "{ flight_time: '%s' }]-(p) RETURN a,p" % (self.name, self.city, airport.name, airport.city,
                                                           distance.flight_time))
        else:
            return False

    def distance_info(self):
        if self.exists():
            return execute("OPTIONAL MATCH (a:Airport {name:'%s', city:'%s'})-[r:DISTANCE]-(p:Airport) RETURN a,r,p" % (
                self.name, self.city))
        else:
            return False

    def hub_info(self):
        if self.exists():
            return execute("OPTIONAL MATCH (a:Airport {name:'%s', city:'%s'})-[r:HUB]-(p:Airline) RETURN a,r,p" % (
                self.name, self.city))
        else:
            return False
