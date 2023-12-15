from .google_API_client import Google_APIs

class Google_Places_API(Google_APIs):
    def __init__(self) -> None:
        super().__init__()
    
    def get_places(self):
        response =  self.read_json_file(self.places_file)

        if response["status"] != "OK":
            raise Exception("status code is not OK")   
             
        return response
    
    def get_place_details(self):
        response = self.read_json_file(self.place_file)
    
        if response["status"] != "OK":
            raise Exception("status code is not OK")   
             
        return response