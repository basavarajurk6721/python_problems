def display_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

display_details(
    name = "Basavaraju R K",
    age = 21,
    course = "ECE",
    city = "mysore"
)