import json

class Google_APIs():
    def __init__(self) -> None:
        self.places_file = "places_search.json"
        self.place_file = "place_details.json"

    def read_json_file(self, file_name) -> dict:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data