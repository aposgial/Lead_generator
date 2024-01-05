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

def _open_hours_refactor(open_hours:list[str]) -> list:
    schedule = []

    for entry in open_hours:
        day, time_range = entry.split(": ")
        
        if "Closed" in time_range:
            status = "Closed"
            opening_time = None
            closing_time = None
        else:
            status = "Open"
            temp = str(time_range.encode()).replace("b'", "").replace("'", "")
            opening_time, closing_time = temp.split(" \\xce\\xb2\\xe2\\x82\\xac\\xe2\\x80\\x9c ")
            
        schedule.append({
            "day": day,
            "status": status,
            "opening_time": opening_time,
            "closing_time": closing_time
        })
    return schedule

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
            refactored["open_hours"] = _open_hours_refactor(schedule["weekday_text"])
            #print(_open_hours_refactor(schedule["weekday_text"]))
            #pass

    return refactored
