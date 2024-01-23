# Import stuffs
import tkinter
import customtkinter
from customtkinter import *
from tkinter import *
import winsound
import random

# Create the animals key trait
trait = random.choice(["crazy", "funny", "kind", "selfish", "angry", "stupid", "clever"])

# Create variables for the animals health
happiness_var = 100
energy_var = 100
mood_var = 100
mood_text_var = ""

# Create the variable to store the type of animal the user has chosen
animal_type = ""

# Create the animal variable image art
cat = r"""
 /\_/\ 
( o.o )
 > ^ <
"""
dog = r"""
 / \__
(    @\___
 /         O
/   (_____/
/_____/   U
"""
rabbit = r"""
 (\(\ 
 (-.-)
 o_(")(")
"""

# Create the command for saving rabbit as animal type
def animal_type_rabbit():
    # Declare animal type variable as global
    global animal_type
    # Save rabbit to the animal type variable
    animal_type = "Rabbit"
    with open ("animal_type.txt", "w") as file:
        file.write ("Rabbit")
     
# Create the command for saving rabbit as animal type
def animal_type_cat():
    # Declare animal type variable as global
    global animal_type
    # Save cat to the animal type variable
    animal_type = "Cat"
    with open ("animal_type.txt", "w") as file:
        file.write ("Cat")
            
# Create the command for saving dog as animal type
def animal_type_dog():
    # Declare animal type variable as global
    global animal_type
    # Save dog to the animal type variable
    animal_type = "Dog"
    with open ("animal_type.txt", "w") as file:
        file.write ("Dog")

# Create the function to confirm dat in terminal
def confirm_setup_terminal():

    if animal_type == "Rabbit":
        print ("Rabbit saved to var")
        with open ("animal_type.txt", "r") as file:
            content = file.read()
        if content == "Rabbit":
            print ("Rabbit saved to file")
        
    if animal_type == "Cat":
        print ("Cat saved to var")
        with open ("animal_type.txt", "r") as file:
            content = file.read()
        if content == "Cat":
            print ("Cat saved to file")
        
    if animal_type == "Dog":
        print ("Dog saved to var")
        with open ("animal_type.txt", "r") as file:
            content = file.read()
        if content == "Dog":
            print ("Dog saved to file")
            
            
    print("Animal name *" + (animal_name.get()) + "* saved to file. ")

# Create the function for the happiness window
def hap_window_func():
    
    # Create the settings for the window
    hapwindow = customtkinter.CTk()
    hapwindow.geometry("180x120")
    hapwindow.title("Happiness Menu")
    
    # Create the label displaying cats happiness in a variable
    happiness_label = CTkLabel(hapwindow, text = ("Your " + animal_type + "'s happiness is " + str(happiness_var) + "! "))
    happiness_label.pack(padx=5,pady=5)
    
    # Create the button to cuddle your animal to increase happiness
    cuddle_button = CTkButton (hapwindow, text = "Cuddle! ")
    cuddle_button.pack(padx=5, pady=5)
    
    # Create the button to stroke your animal to increase happiness
    stroke_button = CTkButton(hapwindow, text="Stroke")
    stroke_button.pack(padx=5, pady=5)
    
    # Create the mainloop
    hapwindow.mainloop()
   
# Create the function for the energy window    
def eng_window_function():
    
    # Create the settings for the window
    engwindow = customtkinter.CTk()
    engwindow.geometry("180x120")
    engwindow.title("Energy Menu")
    
    # Create the label displaying cats energy in a variable
    energy_label = CTkLabel(engwindow, text = ("Your " + animal_type + "'s energy is " + str(energy_var) + "! "))
    energy_label.pack(padx=5,pady=5)
    
    # Create the button to feed your animal to increase energy
    feed_button = CTkButton (engwindow, text = "Feed! ")
    feed_button.pack(padx=5, pady=5)
    
    # Create the button to stroke your animal to increase energy
    walk_button = CTkButton(engwindow, text="Walk!")
    walk_button.pack(padx=5, pady=5)
    
    # Create the mainloop
    engwindow.mainloop()

# Create the function for the mood window
def mood_window_function():
    
    # Create the settings for the window
    moodwindow = customtkinter.CTk()
    moodwindow.geometry("180x120")
    moodwindow.title("Mood Menu")
    
    # Create the label displaying animals mood in a variable
    mood_label = CTkLabel(moodwindow, text = ("Your " + animal_type + "'s mood is " + str(mood_var) + "! "))
    mood_label.pack(padx=5,pady=5)
    
    # Create the button to play music to your animal to increase mood
    music_button = CTkButton (moodwindow, text = "Play Music!")
    music_button.pack(padx=5, pady=5)
    
    # Create the button to give treats to your animal to increase mood
    treat_button = CTkButton(moodwindow, text="Give Treats!")
    treat_button.pack(padx=5, pady=5)
    
    # Create the mainloop
    moodwindow.mainloop()

# Create the main function
def main_screen():
    
    # Make the animal name global
    global animal_name
    
    # Use this function to confirm all the dat in terminal
    confirm_setup_terminal()
    
    # Play the cat sound if the user selected cat
    if animal_type == "Cat":
        winsound.PlaySound("cat.wav", 0)
    
    # Play the dog sound if the user selected dog
    elif animal_type == "Dog":
        winsound.PlaySound("dog.wav", 0)
    
    # Create the main window
    root = customtkinter.CTk()
    root.title("BinaryBuddy")
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("blue")
    root.geometry("230x200")
    
    animal_info = CTkLabel(root, text=("Hi! My name is " + animal_name.get() + " and I am a " + trait + " " + animal_type + "! "))
    animal_info.pack(padx=5, pady=5)
    
    # Display the cat image art on screen
    if animal_type == "Cat":
        catimage = CTkLabel(root, text=cat)
        catimage.pack(padx=5, pady=5)
    
    # Display the rabbit image art on screen
    elif animal_type == "Rabbit":
        rabbitimage = CTkLabel(root, text=rabbit)
        rabbitimage.pack(padx=5, pady=5)
    
    # Display the dog image art on screen
    elif animal_type == "Dog":
        dogimage = CTkLabel(root, text=dog)
        dogimage.pack(padx=5, pady=5)
        
    # Create the buttons for the stats of the animal
    # Button leading to the happiness menu
    hap_button = CTkButton(root, text="Happiness", command=hap_window_func)
    hap_button.pack(padx=5, pady=5)
    
    # Button leading into the energy menu
    eng_button = CTkButton(root, text="Energy", command=eng_window_function)
    eng_button.pack(padx=5, pady=5)
    
    # create the button for the animals mood
    mood_button = CTkButton(root, text="Mood", command=mood_window_function)
    mood_button.pack(padx=5, pady=5)
    
    # Create the mainloop
    root.mainloop()

# Create setup window. This is for inputting the info on the animal such as name type ect.
setup_window = customtkinter.CTk()
setup_window.geometry("160x225")
customtkinter.set_appearance_mode("system") # The user may ajust this to "light" or "dark" mode depending on their preferences 
customtkinter.set_default_color_theme("blue")
setup_window.title("Setup")

# Create the buttons, labels and entry boxes.

# Create the label telling the user to input the animals name
name_label = CTkLabel(setup_window, text="Enter Animal Name Here!")
name_label.pack (padx=5, pady=5)

# Entry widget for storing animal name
animal_name = CTkEntry(setup_window, height=20, width=140,)
animal_name.pack(padx=10, pady=5)

# Create the buttons for selecting an animal
cat_button = CTkButton(setup_window, text="Cat!", command=animal_type_cat)
cat_button.pack(padx=5, pady=5)
rabbit_button = CTkButton(setup_window, text="Rabbit!", command=animal_type_rabbit)
rabbit_button.pack(padx=5, pady=5)
dog_button = CTkButton(setup_window, text="Dog!", command=animal_type_dog)
dog_button.pack(padx=5, pady=5)

# Create the buton for saving data and moving into the next section
save_button = CTkButton(setup_window, text="Continue", command=main_screen,)
save_button.pack(padx=5, pady=5)

# Create the mainloop for the setup window
setup_window.mainloop()