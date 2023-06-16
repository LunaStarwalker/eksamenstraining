farm_method = ["Organic", "Free Range", "Barn", "Cage"] # En liste med farm-metoderne
countries_list = {} # En tom dict til dataen fra text-filen

f = open("eggsamen.txt", "r")
data = f.readlines() # En liste med alle linjer i filen, hvor hver linje er en string (fx. "DK,Denmark")

for line in data:
    temp = line.split(",") # Man splitter string ved kommaet, så fx "DK,Denmark" bliver til en liste ["DK", "Denmark"]

    abbr = temp[0] # fx DK
    coun = temp[1] # fx Denmark

    countries_list[abbr] = coun.strip() # Bruger strip til at fjerne whitespace og newline

code = input("Input the code as it appears on the egg (excl. the best-before date): ")

method = farm_method[int(code[0])] # første tegn svarer til index i farm_method listen, der kan angive farm metoden
country = code[1:3] # tegnene på index 1 og 2 angiver to bogstaver for et land. fx DK for Denmark
country = countries_list[country] # her bruges de to tegn fra forrige linje som key til at få det tilsvarende land
# fx countries_list["DK"] = "Denmark"
farm = code[3:] # producer ID må svare til alt i slutningen af inputtet

print("This egg originated from the", method, "farming method.", end='\n')
print("The egg was produced in", country + ".", end='\n')
print("This egg originated from a farm with the producer ID:", farm + ".")
# jeg bruger både "+" og "," da "," automatisk indsætter mellemrum mellem de forskellige dele i print()
