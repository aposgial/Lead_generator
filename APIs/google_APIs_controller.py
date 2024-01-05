from .google_APIs import Google_Places_API
from.response_parser import *

class Google_APIs_Controller():
    def __init__(self) -> None:
        self.con = Google_Places_API()


    def places_search(self, query:str) -> list:
        try:
            response = self.con.get_places() #TODO pass the query into the get_places
            places_id = parse_places_id(response["results"])
            
            places = []
            for place_id in places_id[:1]:
                place:dict = self.con.get_place_details()["result"] #TODO pass the place_id into the get_place_details
                
                if "website" in place.keys():
                    refactored = place_refactor(place)
                    places.append(refactored)
                    
            return places
        except Exception as e:
            print(e)