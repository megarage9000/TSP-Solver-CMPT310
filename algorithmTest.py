import tsp

#TODO implement Boruvka's algorithm?
# - Make an algorithm/class to construct a minimum spanning tree given the cities
# - Source: https://www.geeksforgeeks.org/boruvkas-algorithm-greedy-algo-9/


class BoruvkaTree():
    
    def __init__(self, fname):
        self.cities = tsp.load_city_locs(fname)
        self.edges = []
        self.tree = []
        self.generateEdges()
        
    def generateEdges(self):
        for i in range(1, len(self.cities) + 1):
            for j in range(i + 1, len(self.cities) + 1):
                edgeWeight = tsp.city_dist(i, j, self.cities)
                edge = Edge(i, j, edgeWeight)
                self.edges.append(edge)

    
        
        
        
class Edge():
    
    def __init__(self, city1, city2, weight):
        self.city1 = city1
        self.city2 = city2   
        self.weight = weight
    
    def getWeight(self):
        weight = self.weight
        return weight
    
    def toString(self):
        return "Cities{" + str(self.city1) + ", " + str(self.city2) + "}, total distance: " + str(self.weight) 
        
        
class Component():
    def __init__(self):
        self.num = -1
              
    
def test():
    tree = BoruvkaTree("cities1000.txt")
    print("done!")
    
test()
    