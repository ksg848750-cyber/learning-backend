events=[]
def event(events, name, venue, capacity):
    invalid = capacity <= 0 or venue.isnumeric() or name.isnumeric()
    if invalid:
        raise ValueError("Invalid event details")
    events.append({
        "name": name,
        "venue": venue,
        "capacity": capacity
    })
try:
    event(events, "Tech Fest", "Auditorium", 5000)
    event(events, "Concert", "Stadium", -200)
except ValueError as e:
    print("Error:", e)
print(events)