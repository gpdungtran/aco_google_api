import googlemaps
from datetime import datetime
from ant_colony import AntColony
import json
import numpy as np
import polyline
gmaps = googlemaps.Client(key='AIzaSyBnEczbljpLOsESpId-YPwFWQNc4YuYLEk')

# Request directions via public transit
now = datetime.now()

def path_obtain(places,traffic_mode = "walking"):
    origins = places
    destinations = places


    #Obtain distance matrix
    distance_list = []
    for i in range(len(origins)):
        distance_matrix_result = gmaps.distance_matrix(origins[i], destinations, mode=traffic_mode, language=None, avoid=None, units=None, departure_time=None, 
        arrival_time=None, transit_mode=None, transit_routing_preference=None, traffic_model=None, region=None)

    
        
        for items in distance_matrix_result["rows"]:
            for item in items["elements"]:
                if 'distance' in item.keys():
                    distance_list.append(item["distance"]["value"])
                else:
                    distance_list.append(0)
            print(distance_list) 

    distance_list = [np.inf if item == 0 else item for item in distance_list]  
    distance_matrix = np.array(distance_list)
    distance_matrix = distance_matrix.reshape(len(origins),len(origins))
    print(distance_matrix)
    

    #Apply Ant conoly optimization
    ant_colony = AntColony(distance_matrix, 10, 10, 100, 0.95, alpha=1, beta=1)
    shortest_path = ant_colony.run()
    print ("shorted_path: {}".format(shortest_path))
    
    path_name = []
    res =[]
    for item in shortest_path[0]:
    
        start_path = origins[int(item[0])]
        end_path = origins[int(item[1])]
        path_name.append((start_path,end_path))
        directions_result = gmaps.directions(start_path,end_path,mode=traffic_mode,departure_time=now)
        res_add = [val["points"] for key, val in directions_result[0].items() if "points" in val]
        res.append(decode_polyline(res_add[0]))
        """
        # Iterate through each route in the response
        for route in directions_result:
            # Iterate through each leg (sub-route) of the route
            for leg in route['legs']:
            # Iterate through each step (instruction) of the leg
                for step in leg['steps']:
                # Get the starting location of the step
                    start_location = step['start_location']
                    # Create a dictionary with latitude and longitude
                    coord_dict = {'latitude': start_location['lat'], 'longitude': start_location['lng']}
                    # Add the dictionary to the list
                    res.append(coord_dict)
        """
    
    print(res,path_name) 
    return res,path_name

def decode_polyline(encoded_polyline):
    """Decodes an encoded Google Maps polyline into a list of coordinate dictionaries.

    Args:
        encoded_polyline: The encoded polyline string.

    Returns:
        A list of dictionaries with 'latitude' and 'longitude' keys.
    """
    decoded_points = polyline.decode(encoded_polyline)
    return [{"latitude": lat, "longitude": lng} for lng, lat in decoded_points]
