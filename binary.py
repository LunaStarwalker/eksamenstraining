bin = [128, 64, 32, 16, 8, 4, 2, 1]
functions = ["BtoD", "DtoB"]

while True:
    # Brugeren vælger funktion, enten Binary til Denary konvertering eller omvendt.
    func = str(input("Enter 'BtoD' for Binary to Denary conversion, or 'DtoB' for Denary to Binary converstion: "))
    if func in functions: # inputtet skal være en af mulighederne i listen
        break
    else:
        print("Please enter a valid option.")


def convertToBinary():
    while True:
        try: # try-except bruges til at tjekke, at inputtet er en integer (int)
            denary = int(input("Enter a number between 0 and 255: "))
        except: # hvis input ikke er int køres loopet forfra
            print("Please enter a valid number.")
        else:
            if denary > 0 and denary < 255:
                break
            else:
                print("Please enter a valid number.")

    binary = ""

    for bi in bin: # bin-listen indeholder alle tallene, der udgør enkelt-byte binary.
        # Her køres et for-loop for hvert af tallene
        if denary >= bi: # her tjekkes om inputtet er større end det tal, som loopet tjekker for. fx. kan bi = 64 eller bi = 32
            binary = binary + "1"
            denary = denary - bi
        else:
            binary = binary + "0"
    print(binary)


def convertToDenary():
    b = {'0', '1'} # der laves et set med de to tal, som indgår i binary, så vi kan tjekke om inputtet er i binary

    while True:
        binary = str(input("Enter a binary using one Byte: "))
        t = set(binary) # set-funktionen laver et set af alle unikke karakterer i inputtet.
        # Hvis inputtet er binary, består det udelukkende af 1 eller 0 eller 1 og 0.

        if len(binary) == 8 and b == t or t == {'0'} or t == {'1'}:
            break
        else:
            print("Please enter a valid binary.")

    denary = 0

    for i, c in enumerate(binary): # enumerate returnerer både index og et element.
        # Hvis elementet er 1, ved vi at tallet består af en gange det tilsvarende tal i bin-listen.
        # Så hvis c = 1 ved i (index) = 3, ved vi at denary-tallet må bestå af en gang 16
        # For binary-tallet 10100000 kan vi se, at c = 1 ved i = 0 og i = 2, så elementerne i bin-listen ved disse index kan adderes for at få tallet.
        # Altså må denary-tallet være lig: bin[0] + bin[2] = 128 + 32 = 160
        if c == '1':
            denary = denary + bin[i]

    print(denary)

# Her køres den funktion, som brugeren valgte i starten
if func == "BtoD":
    convertToDenary()

if func == "DtoB":
    convertToBinary()