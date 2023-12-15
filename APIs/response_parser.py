def parse_places_id(results:list) -> list:
    places_id = []

    for result in results:
        places_id.append(result["place_id"])
    
    return places_id


def place_refactor(result:dict) -> dict:
    return{
        "address": result["formatted_address"],
        "phone": result["formatted_phone_number"],
        "name": result["name"],
        "rating": result["rating"],
        "total_ratings": result["user_ratings_total"]
    }
