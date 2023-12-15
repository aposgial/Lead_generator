from .google_API_client import Google_APIs

class Google_Places_API(Google_APIs):
    def __init__(self) -> None:
        super().__init__()
    
    def get_places(self):
        return self.read_json_file(self.places_file)
    
    def get_place_details(self):
        return self.read_json_file(self.place_file)