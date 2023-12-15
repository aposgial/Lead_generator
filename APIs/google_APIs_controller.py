from .google_APIs import Google_Places_API

class Google_APIs_Controller():
    def __init__(self) -> None:
        self.con = Google_Places_API()

    def places_search(self, query:str):
        places = self.con.get_places()
        print(places)
        print(query)