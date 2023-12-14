import json

class Google_APIs():
    def __init__(self) -> None:
        self.places_file = "places_search.json"
        self.place_file = "place_details.json"

    def read_json_file(self, file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data


class Google_Places_API(Google_APIs):
    def __init__(self) -> None:
        super().__init__()
    
    def places_search(self):
        return self.read_json_file(self.places_file)
    
    def place_details(self):
        return self.read_json_file(self.place_file)