import SAMUS
import POSSIBLE 
import Alg_genetico

RAIO = 0.0084
#15min, 30min, 1h
#0.0084, 0.0168, 0.0336
AMBUS = []
NUMBER_DISTRICTS = len(POSSIBLE.DISTRICTS_POINTS)
DISTRICTS =[]
DISTRICTS_SATISFACTION = [0]*NUMBER_DISTRICTS
NUMBER_POSIBLE_LOCATIONS = len(SAMUS.PONTOS)

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

def prepare_ambus():
    keys = list(SAMUS.PONTOS)   
    for i in range(NUMBER_POSIBLE_LOCATIONS):    
        new_local = ambu(keys[i], SAMUS.PONTOS[keys[i]][0], SAMUS.PONTOS[keys[i]][1])
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
    print(sat)        
    return sat        


prepare_ambus()
prepare_district()

satisfaction = 0
for i in range(len(DISTRICTS)):
    for j in range(len(AMBUS)):
        if(calc_distance(i, j) <= RAIO):
            DISTRICTS_SATISFACTION[i] = 1


for i in range(len(DISTRICTS)):
    if(DISTRICTS_SATISFACTION[i] == 1):
        if(DISTRICTS[i].demand != "nan"):    
            satisfaction += DISTRICTS[i].demand

print(DISTRICTS_SATISFACTION)
print(satisfaction)


print(f"Percentage of demand satisfied = {(satisfaction/max_satisfaction())*100}%")

print(max_satisfaction())

Alg_genetico.plot_sol(AMBUS, '1h-min-current-model', RAIO)
