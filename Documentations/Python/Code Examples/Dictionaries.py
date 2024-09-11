monthConversions = {
	"Jan": "January",
	"Feb": "February",
	"Mar": "March",
    4: "April"
}


print(monthConversions.get("Jan"))
print(monthConversions.get(4))

input_var = input("Input Your Key ")
print(monthConversions.get(input_var, "Not a valid Key"))