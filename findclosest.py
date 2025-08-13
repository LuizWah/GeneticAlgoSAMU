import math
import SAMUS
import POSSIBLE
def euclidean_distance(coord1, coord2):
    """Calculates the Euclidean distance between two coordinates."""
    return math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)

def find_closest_district(point, districts):
    """Finds the closest district to a given point."""

    closest_district = None
    min_distance = float('inf')  # Initialize with a very large number

    for district_id, district_coord in districts.items():
        distance = euclidean_distance(point, district_coord)
        if distance < min_distance:
            min_distance = distance
            closest_district = district_id
    return closest_district, min_distance


for ponto, coord in SAMUS.PONTOS.items():
    closest_id, distance = find_closest_district(coord[:2], POSSIBLE.DISTRICTS_POINTS)  # Only use lat/lon
    print(f"{ponto}: Closest District ID = {closest_id}, Distance = {distance:.4f}")