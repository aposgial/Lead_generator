def parse_places_id(results:list) -> list:
    places_id = []

    for result in results:
        places_id.append(result["place_id"])
    
    return places_id

def _reviews_refactor(reviews:list) -> list:
    rev = []
    for review in reviews:
        rev.append(
            {   
                "author_name": review["author_name"],
                "rate": review["rating"],
                "language": review["language"],
                "text": review["text"]
            }
        )
    return rev

def place_refactor(result:dict) -> dict:
    refactored = {}
    if "place_id" in result.keys():
        refactored["place_id"] = result["place_id"]

    if "name" in result.keys():
        refactored["name"] = result["name"]

    if "formatted_address" in result.keys():
        refactored["address"] = result["formatted_address"]

    if "formatted_phone_number" in result.keys():
        refactored["phone"] = result["formatted_phone_number"]

    if "url" in result.keys():
        refactored["maps_url"] = result["url"]

    if "types" in result.keys():
        refactored["types"] = result["types"]

    if "rating" in result.keys():
        refactored["rating"] = result["rating"]

    if "user_ratings_total" in result.keys():
        refactored["total_ratings"] = result["user_ratings_total"]

    if "reviews" in result.keys():
        refactored["reviews"] = _reviews_refactor(result["reviews"])

    if "opening_hours" in result.keys():
        schedule:dict = result["opening_hours"]
        if "weekday_text" in schedule.keys():
            refactored["open_hours"] = schedule["weekday_text"]

    return refactored
