from datetime import date
from Model.model import Model
from view import View
from APIs.google_APIs_controller import Google_APIs_Controller

from APIs.google_API_client import Google_APIs


class Controller():
    def __init__(self) -> None:
        self.model = Model()
        self.view = View(self)
        self.google_APIs_controller = Google_APIs_Controller()


    def main_window_search_leads_button(self):
        self.view.search_leads_window()

    def main_window_view_searched_lead_button(self, lead_id):
        self.view.leads_window(lead_id)

    def search_leads_window_submit_button(self, query):
        temp = query.get()
        print(temp)

        places = self.google_APIs_controller.places_search(query="OK..")
        google_api = Google_APIs()
        google_api.write_dict_to_json_file(places)

    def search(self):
        ...

        #self.model.insert_searches({
        #    "location_searched": "volos",
        #    "type_searched": "bar",
        #    "result_sum": 211,
        #    "date_searched": str(date.today()),
        #    "suggestions": 2
        #})


    def get_searches_info(self):
        return self.model.select_searches()
    
    def get_places_info(self, lead_id):
        places_info = []
        places_data = self.model.select_places(lead_id)

        for place in places_data:
            result_id = place[1]
            types_data = self.model.select_types(result_id)
            operating_hours_data = self.model.select_operating_hours(result_id)
            reviews_data = self.model.select_reviews(result_id)
            suggestions_data = self.model.select_suggestions(result_id)

            places_info.append(places_data +
                               types_data +
                               operating_hours_data +
                               reviews_data +
                               suggestions_data)
        return places_info


    def run(self):
        self.view.mainloop()