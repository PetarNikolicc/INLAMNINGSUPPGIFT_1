# Funktion för att översätta  text till rövarspråket
def text_till_rovarsp(text): 
    konsonanter = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"  
    text_resultat = ""  
    for bokstaven in text:  
        if bokstaven in konsonanter:    
            text_resultat += bokstaven + "o" + bokstaven   
        else:
            text_resultat += bokstaven  
    return text_resultat

# Funktion för att läsa in text från en fil
def read_from_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:   
        return file.read()  

# Funktion för att spara given text till en fil
def save_to_file(content, file_name):
    with open(file_name, "w", encoding="utf-8") as file:  
        file.write(content)  
        print(f"Resultatet har sparats i filen '{file_name}'.")  

# Specifiera filnamnet för den fil som innehåller den svenska texten
file_name = "svenskt_text.txt"  
# Läs in texten från filen med hjälp av funktionen read_from_file
input_text = read_from_file(file_name)

# Översätt den inlästa texten till rövarspråket med hjälp av funktionen text_till_rovarsp
text_resultat = text_till_rovarsp(input_text)
print("I rövarspråket blir det: ", text_resultat)  # Skriv ut den översatta texten

# Specifiera filnamnet för den fil där den översatta texten ska sparas
output_file_name = "rovarspraket.txt"  
# Spara den översatta texten till en fil med hjälp av funktionen save_to_file
save_to_file(text_resultat, output_file_name)
