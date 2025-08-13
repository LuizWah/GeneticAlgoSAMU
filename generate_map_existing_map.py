import SAMUS
import POSSIBLE 
import Alg_genetico

RAIO = 0.0084
#0.0056 0.0084, 0.0168, 0.0336
#1959, 2087, 1246, 748
AMBUS_NUNS = [2185, 45, 420, 1270, 2018]
AMBUS = []
NUMBER_DISTRICTS = len(POSSIBLE.DISTRICTS_POINTS)
DISTRICTS = []
DISTRICTS_SATISFACTION = [0]*NUMBER_DISTRICTS
NUMBER_POSIBLE_LOCATIONS = 5

class ambu:
    def __init__(self, *args):
        self.id = args[0]
        self.position_x = args[1]
        self.position_y = args[2]

class district:
    def __init__(self, *args):
        self.id = args[0]
        self.position_x = args[1] 
        self.position_y = args[2]
        self.demand = args[3]


solution = Alg_genetico.Solution()
for i in range(NUMBER_POSIBLE_LOCATIONS):
    solution.xA[AMBUS_NUNS[i]] = 1


def prepare_ambus():
    for i in range(NUMBER_DISTRICTS):    
        keys = list(POSSIBLE.DISTRICTS_POINTS)   
        if(i in AMBUS_NUNS):
            new_local = ambu(keys[i], POSSIBLE.DISTRICTS_POINTS[keys[i]][0], POSSIBLE.DISTRICTS_POINTS[keys[i]][1])
            AMBUS.append(new_local)

def prepare_district():
    keys = list(POSSIBLE.DISTRICTS_POINTS)   
    for i in range(NUMBER_DISTRICTS):    
        new_district = district(keys[i], POSSIBLE.DISTRICTS_POINTS[keys[i]][0], POSSIBLE.DISTRICTS_POINTS[keys[i]][1], POSSIBLE.DISTRICTS_POINTS[keys[i]][2] )
        DISTRICTS.append(new_district)



def calc_distance(points_index_1, points_index_2):
    x = pow((DISTRICTS[points_index_1].position_x - AMBUS[points_index_2].position_x), 2)
    y = pow((DISTRICTS[points_index_1].position_y - AMBUS[points_index_2].position_y), 2)
    distance = pow((x + y), 0.5)
    
    return distance

def max_satisfaction():
    sat = 0
    for i in range(NUMBER_DISTRICTS):
        if(DISTRICTS[i].demand != "nan"):
            sat += DISTRICTS[i].demand  
    return sat        


prepare_ambus()
prepare_district()

satisfaction = 0
for k in range(NUMBER_DISTRICTS):
    for l in range(NUMBER_POSIBLE_LOCATIONS):
        
        if((calc_distance(k, l) <= RAIO) ):
            DISTRICTS_SATISFACTION[k] = 1


for i in range(len(DISTRICTS)):
    if(DISTRICTS_SATISFACTION[i] == 1):
        if(DISTRICTS[i].demand != "nan"):    
            satisfaction += float(DISTRICTS[i].demand)


print(f"Percentage of demand satisfied = {(satisfaction/max_satisfaction())*100}%")

print(max_satisfaction())
print(DISTRICTS_SATISFACTION)
print(satisfaction)
Alg_genetico.plot_sol(solution, 'final-15-min-sol-5-ambus', RAIO) 