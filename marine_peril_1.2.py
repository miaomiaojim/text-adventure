import random
import time
import sys


def slow_print(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write("\n")


def print_pause(text, delay=1.5):
    print(text)
    time.sleep(delay)


def pause():
    input(f"{yellow}Press enter to continue....{color_end}")


def color():
    global red, green, yellow, blue, color_end
    red = "\033[1;31;40m"
    green = "\033[1;32;40m"
    yellow = "\033[1;33;40m"
    blue = "\033[1;34;40m"
    color_end = "\033[0m"


class Valid_input():

    def valid_choice_input(self, prompt, minimum, maximum):
        while True:
            choice = input(f"{prompt}\n")
            if choice.isnumeric():
                choice = int(choice)
                if minimum <= choice <= maximum:
                    return choice
                else:
                    print(f"Choice must be >= {minimum} and <= {maximum}.")
            else:
                print(
                    "Your input must be natural number(non-negative integer).")

    def valid_amount_input(self, prompt):
        while True:
            amount = input(f"{prompt}\n")
            if amount.isnumeric():
                amount = int(amount)
                return amount
            else:
                print(
                    "Your input must be natural number(non-negative integer).")


def introduction():
    slow_print(f"""\
On the sea,there is a ship drifting. That's your ship, Black Pearl, captain.
You and your sailors are heading home, {blue}Frostford Port{color_end}, \
after 10 years' adventures on the sea.""")
    pause()
    slow_print(f"""\
But on the trip to home, there are somthings hindering your progress to home,
{red}storms, pirates, diseases and even sea monster{color_end}.""")
    pause()
    slow_print(f"""\
On the sea, {blue}freshwater storage{color_end} is requisiste.
You consume 10 units water everyday.
Without freshwater you will die in {red}3 days{color_end}.
Fresh water can be replenished in the {blue}port{color_end}.""")
    pause()
    slow_print(f"""\
There are also probabilities to get {blue}malaria and gastroenteritis\
{color_end} in your tailors on the sea.
So you can consider to {blue}hire a doctor{color_end} at port cities.
If your sailors can not get treatments \
in time after getting malaria or gastroenteritis,
after {red}4 days{color_end}, the sailor with disease will die.""")
    pause()
    slow_print(f"""\
On the sea, it's possible to come across {red}pirates{color_end}.
If you beat pirates, you will acquire money and fresh water.
And your sailers can level up to be more stronger. {blue}
The maximum level of every sailor is 10{color_end}.
But your sailors may get hurt or even die.
If they get hurt, them need time to recover.
You can also {blue}buy weapons and armors{color_end} \
to strengthen your sailors.""")
    pause()
    slow_print(f"""\
{blue}New sailers can be recruited from port cities or  dismissed.
There is a probability to come across \
some drifting sailors or doctors on the ocean.
The maximum amount of your tailors is 15.
If your tailors die out, game will be over{color_end}.""")
    pause()
    slow_print(f"Initially, you have {blue}7 tailors{color_end}. Good luck.")


def creature():
    global crew, Noah, Oliver, Elijah, James, William, Benjamin, Lucas,\
           doctor, disease_people, pirate, sea_monster, enemy_dictionary, \
           enemy_crew, Jett, Karson, Clayton, Finley, Bradley, Drake, \
           Sutton, Denver, Wesdin, Kingsley, Wayne, Dane, sailors_drifting, \
           Eli, Cooper, Kai, Lando, Wesley, sailor_icemeet, sailors_list
    Noah = [
        "Noah", 11, 11, 5, 5, 0, "without weapon", "", "without armor", "", "",
        "", 1, 10
    ]
    Oliver = [
        "Oliver", 10, 10, 6, 4, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    Elijah = [
        "Elijah", 11, 11, 5, 4, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    James = [
        "James", 12, 12, 4, 4, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    William = [
        "William", 9, 9, 6, 5, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    Benjamin = [
        "Benjamin", 10, 10, 5, 6, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    Lucas = [
        "Lucas", 10, 10, 3, 7, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    crew = [Noah, Oliver, Elijah, James, William, Benjamin, Lucas]
    doctor = [
        "doctor", 10, 10, 5, 5, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    Eli = [
        "Eli", 10, 10, 6, 5, 0, "without weapon", "", "without armor", "", "",
        "", 1, 10
    ]
    Cooper = [
        "Cooper", 10, 10, 5, 6, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    Kai = [
        "Kai", 11, 11, 5, 5, 0, "without weapon", "", "without armor", "", "",
        "", 1, 10
    ]
    Lando = [
        "Lando", 12, 12, 4, 4, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    Wesley = [
        "Wesley", 10, 10, 6, 5, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    sailor_icemeet = [Eli, Cooper, Kai, Lando, Wesley]
    Jett = [
        "Jett", 11, 11, 6, 5, 0, "without weapon", "", "without armor", "", "",
        "", 1, 10
    ]
    Karson = [
        "Karson", 10, 10, 6, 5, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    Clayton = [
        "Clayton", 11, 11, 5, 5, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    Finley = [
        "Finley", 12, 12, 5, 4, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    Bradley = [
        "Bradley", 9, 9, 6, 6, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    Drake = [
        "Drake", 10, 10, 6, 6, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    Sutton = [
        "Sutton", 10, 10, 4, 7, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    Denver = [
        "Denver", 11, 11, 5, 6, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    Wesdin = [
        "Wesdin", 12, 12, 4, 5, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    Kingsley = [
        "Kingsley", 9, 9, 7, 5, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    Wayne = [
        "Wayne", 10, 10, 6, 7, 0, "without weapon", "", "without armor", "",
        "", "", 1, 10
    ]
    Dane = [
        "Dane", 10, 10, 4, 7, 0, "without weapon", "", "without armor", "", "",
        "", 1, 10
    ]
    sailors_drifting = [
        Jett, Karson, Clayton, Finley, Bradley, Drake, Sutton, Denver, Wesdin,
        Kingsley, Wayne, Dane
    ]
    pirate = ["Pirate", 10, 10, 5, 5, 10, 40, 50]
    sea_monster = ["Sea Monster", 20, 20, 10, 7, 70, 100]
    enemy_dictionary = ["Pirate", "Sea Monster"]
    enemy_crew = []
    disease_people = []
    sailors_list = Sailors_list()


class Sailors_list():

    def Disease_feedback(self, sailor_index):
        if "malaria" in crew[sailor_index - 1]:
            return "malaria"
        elif "gastroenteritis" in crew[sailor_index - 1]:
            return "gastroenteritis"
        else:
            return "healthy"

    def sailor_list(self):
        for index, sailor in enumerate(crew, 1):
            disease = self.Disease_feedback(index)
            print(index, sailor[0], "HP:" + str(sailor[1]),
                  "MaxHP:" + str(sailor[2]), "Attack:" + str(sailor[3]),
                  "Defense:" + str(sailor[4]), "Experimence:" + str(sailor[5]),
                  sailor[6] + "," + sailor[8], disease,
                  "Level:" + str(sailor[12]))
        print(f"Hydropenia:{thirst_countdown}")

    def sailor_list_no_index(self):
        for index, sailor in enumerate(crew, 1):
            disease = self.Disease_feedback(index)
            print(sailor[0], "HP:" + str(sailor[1]), "MaxHP:" + str(sailor[2]),
                  "Attack:" + str(sailor[3]), "Defense:" + str(sailor[4]),
                  "Experimence:" + str(sailor[5]), sailor[6] + "," + sailor[8],
                  disease, "Level:" + str(sailor[12]))
        print(f"Hydropenia:{thirst_countdown}")

    def sailor_list_icemeet(self):
        for index, sailor in enumerate(sailor_icemeet, 1):
            disease = self.Disease_feedback(index - 1)
            print(index, sailor[0], "HP:" + str(sailor[1]),
                  "MaxHP:" + str(sailor[2]), "Attack:" + str(sailor[3]),
                  "Defense:" + str(sailor[4]), "Experimence:" + str(sailor[5]),
                  sailor[6] + "," + sailor[8], disease,
                  "Level:" + str(sailor[12]))

    def single_sailor_list(self, sailor_index):
        disease = self.Disease_feedback(sailor_index)
        print(crew[sailor_index - 1][0],
              "HP:" + str(crew[sailor_index - 1][1]),
              "MaxHP:" + str(crew[sailor_index - 1][2]),
              "Attack:" + str(crew[sailor_index - 1][3]),
              "Defense:" + str(crew[sailor_index - 1][4]),
              "Experimence:" + str(crew[sailor_index - 1][5]),
              crew[sailor_index - 1][6] + "," + crew[sailor_index - 1][8],
              disease)


def sailor_dismiss():
    while True:
        sailors_list.sailor_list_no_index()
        choice = valid_input.valid_choice_input(
            f"""\
{yellow}Do you want to dismiss a sailor?   \
1.yes   2.no and back
Please input the serial number of choice \
and press enter.{color_end}""", 1, 2)
        if choice == 1:
            sailors_list.sailor_list()
            choice = valid_input.valid_choice_input(
                f"""\
{yellow}Please input the serial number of the sailor to dismiss \
and press enter.
Or if you don't to dismis pleaser input 0 to back.{color_end}""", 0, len(crew))
            if choice == 0:
                return
            else:
                if crew[choice - 1][6] != "without weapon":
                    Inventory[crew[choice - 1][6]] += 1
                if crew[choice - 1][8] != "without armor":
                    Inventory[crew[choice - 1][8]] += 1
                crew.pop(choice - 1)
                sailors_list.sailor_list()
                choice = valid_input.valid_choice_input(
                    f"""\
{yellow}continue to dismiss?  1.continue  2.back
Please input the serial number and press enter.{color_end}""", 1, 2)
                if choice == 2:
                    return
        elif choice == 2:
            return


def map():
    print("""\
Map:Icemeet Port------------------>>Frostford Port""")


class Inventory_wallet_item_equipment_list():

    def inventory(self):
        global Inventory, thirst_countdown
        Inventory = {
            "freshwater": 150,
            "bronze sword": 0,
            "steel sword": 0,
            "chainmail": 0,
            "plate armor": 0
        }
        thirst_countdown = "none"

    def wallet(self):
        global Wallet
        Wallet = 500

    def items(self):
        global freshwater, Items, bronze_sword, steel_sword, Weapon, \
               chainmail, plate_armor, Armor
        freshwater = ["freshwater", "other item", 2, 0, 0]
        bronze_sword = ["bronze sword", "weapon", 50, 8, 0]
        steel_sword = ["steel sword", "weapon", 100, 12, 0]
        chainmail = ["chainmail", "armor", 50, 0, 7]
        plate_armor = ["plate armor", "armor", 100, 0, 11]
        Weapon = {1: bronze_sword, 2: steel_sword}
        Armor = {1: chainmail, 2: plate_armor}
        Items = [freshwater, bronze_sword, steel_sword, chainmail, plate_armor]

    def items_list(self):
        for index, thing in enumerate(Items, 1):
            if thing[1] == "weapon":
                bonus = thing[3]
                print(
                    index,
                    thing[0] + f"(Attack+{bonus}):" + str(Inventory[thing[0]]))
            elif thing[1] == "armor":
                bonus = thing[4]
                print(
                    index, thing[0] + f"(Defense+{bonus}):" +
                    str(Inventory[thing[0]]))
            else:
                print(index, thing[0] + ":" + str(Inventory[thing[0]]))

    def equipment_list(self):
        global Equipment
        Equipment = [bronze_sword, steel_sword, chainmail, plate_armor]
        for index, item in enumerate(Equipment, 1):
            if item[1] == "weapon":
                bonus = item[3]
                print(index,
                      item[0] + f"(Attack+{bonus}):" + str(Inventory[item[0]]))
            elif item[1] == "armor":
                bonus = item[4]
                print(
                    index,
                    item[0] + f"(Defense+{bonus}):" + str(Inventory[item[0]]))

    def equipment_list_no_index(self):
        Equipment = [bronze_sword, steel_sword, chainmail, plate_armor]
        for item in enumerate(Equipment):
            if item[1] == "weapon":
                bonus = item[3]
                print(item[0] + f"(Attack+{bonus}):" + str(Inventory[item[0]]))
            elif item[1] == "armor":
                bonus = item[4]
                print(item[0] + f"(Defense+{bonus}):" +
                      str(Inventory[item[0]]))


class Equip_unequip():

    def equip_ask(self):
        while True:
            choice = valid_input.valid_choice_input(
                f"""\
{yellow}Do you want to change equipments of your sailors?     \
1. Yes   2.No
Please input the serial number to choose \
and press enter.{color_end}""", 1, 2)
            if choice == 1:
                self.equip_enquiry()
            elif choice == 2:
                return

    def equip_enquiry(self):
        while True:
            sailors_list.sailor_list_no_index()
            choice = valid_input.valid_choice_input(
                f"""\
{yellow}You can choose a sailer to change equipments\
(equip, replace, unequip) or back.
1.choose a sailer to change equipments     2.back
Please input the serial number of choice \
and press enter.{color_end}""", 1, 2)
            if choice == 1:
                while True:
                    sailors_list.sailor_list()
                    sailor_index = valid_input.valid_choice_input(
                        f"""\
{yellow}Please input the serial number of the sailor \
to change equipments and press enter.
Or if you want to get back, please press 0 \
and press enter{color_end}""", 0, len(crew))
                    if sailor_index == 0:
                        return
                    else:
                        sailors_list.single_sailor_list(sailor_index)
                        thing.equipment_list_no_index()
                        choice = valid_input.valid_choice_input(
                            f"""\
{yellow}Do you want to--?:   1.equip(replace)  \
2.unequip   3.choose another sailor  4.back
Please input the serial number \
to choose and press enter.{color_end}""", 1, 4)
                        if choice == 1:
                            self.equip(sailor_index)
                        elif choice == 2:
                            self.unequip(sailor_index)
                        elif choice == 4:
                            return
            elif choice == 2:
                return

    def equip(self, sailor_index):
        while True:
            thing.equipment_list()
            equipment_index = valid_input.valid_choice_input(
                f"""\
{yellow}Please input the serial number of equipment and press enter.
Or if you want to get back, please press 0 \
and press enter{color_end}""", 0, 4)
            if equipment_index == 0:
                return
            else:
                if Inventory[Equipment[equipment_index - 1][0]] == 0:
                    print("You don't have enough amount of this item.")
                else:
                    if Equipment[equipment_index - 1][1] == "weapon":
                        if crew[sailor_index - 1][6] == "without weapon":
                            crew[sailor_index -
                                 1][3] += Equipment[equipment_index - 1][3]
                            crew[sailor_index -
                                 1][6] = Equipment[equipment_index - 1][0]
                            crew[sailor_index -
                                 1][7] = Equipment[equipment_index - 1]
                            Inventory[Equipment[equipment_index - 1][0]] -= 1
                        else:
                            crew[sailor_index - 1][3] -= crew[sailor_index -
                                                              1][7][3]
                            Inventory[crew[sailor_index - 1][6]] += 1
                            crew[sailor_index -
                                 1][3] += Equipment[equipment_index - 1][3]
                            crew[sailor_index -
                                 1][6] = Equipment[equipment_index - 1][0]
                            crew[sailor_index -
                                 1][7] = Equipment[equipment_index - 1]
                            Inventory[Equipment[equipment_index - 1][0]] -= 1
                    elif Equipment[equipment_index - 1][1] == "armor":
                        if crew[sailor_index - 1][8] == "without armor":
                            crew[sailor_index -
                                 1][4] += Equipment[equipment_index - 1][4]
                            crew[sailor_index -
                                 1][8] = Equipment[equipment_index - 1][0]
                            crew[sailor_index -
                                 1][9] = Equipment[equipment_index - 1]
                            Inventory[Equipment[equipment_index - 1][0]] -= 1
                        else:
                            crew[sailor_index - 1][4] -= crew[sailor_index -
                                                              1][9][4]
                            Inventory[crew[sailor_index - 1][8]] += 1
                            crew[sailor_index -
                                 1][4] += Equipment[equipment_index - 1][4]
                            crew[sailor_index -
                                 1][8] = Equipment[equipment_index - 1][0]
                            crew[sailor_index -
                                 1][9] = Equipment[equipment_index - 1]
                            Inventory[Equipment[equipment_index - 1][0]] -= 1
                    sailors_list.single_sailor_list(sailor_index)
                    print(f"your inventory:{Inventory}")
                    choice = valid_input.valid_choice_input(
                        f"""\
{yellow}continue to equip this sailor?  \
1.continue  2.back and choose another sailor
Please in put the serial number and \
press enter{color_end}""", 1, 2)
                    if choice == 2:
                        return

    def unequip(self, sailor_index):
        sailors_list = Sailors_list()
        disease = sailors_list.Disease_feedback(sailor_index)
        print(crew[sailor_index - 1][0],
              "HP:" + str(crew[sailor_index - 1][1]),
              "MaxHP:" + str(crew[sailor_index - 1][2]),
              "Attack:" + str(crew[sailor_index - 1][3]),
              "Defense:" + str(crew[sailor_index - 1][4]),
              "Experimence:" + str(crew[sailor_index - 1][5]),
              crew[sailor_index - 1][6] + "," + crew[sailor_index - 1][8],
              disease)
        while True:
            index = valid_input.valid_choice_input(
                f"""\
{yellow}Unequip:  1.{crew[sailor_index-1][6]}    \
2.{crew[sailor_index-1][8]}   3. back
Please input the serial number of which equipment to unequip \
and press enter.{color_end}""", 1, 3)
            if index == 1:
                if crew[sailor_index - 1][6] == "without weapon":
                    print("This sailor don't have a weapon.")
                else:
                    Inventory[crew[sailor_index - 1][6]] += 1
                    crew[sailor_index - 1][6] = "without weapon"
                    crew[sailor_index - 1][7] = ""
            elif index == 2:
                if crew[sailor_index - 1][8] == "without armor":
                    print("This sailor don't have a armor.")
                else:
                    Inventory[crew[sailor_index - 1][8]] += 1
                    crew[sailor_index - 1][8] = "without armor"
                    crew[sailor_index - 1][9] = ""
            elif index == 3:
                return


class Blacksmith():

    def blacksmith_menu(self):
        while True:
            choice = valid_input.valid_choice_input(
                f"""
{yellow}You are in the blacksmith's shop
1.buy     2.sell     3.go back to port center{color_end}
your money:{Wallet}
your inventory:{Inventory}
{yellow}Please input the serial number \
and press enter.{color_end}""", 1, 3)
            if choice == 1:
                self.blacksmith_buy()
            elif choice == 2:
                sell()
            elif choice == 3:
                return

    def blacksmith_buy(self):
        global Wallet
        while True:
            choice = valid_input.valid_choice_input(
                f"""\
{yellow}1.bronze sword(Attack+8):50 coins  \
2.steel sword(Attack+12):100 coins  3.back{color_end}
your wallet:{Wallet}
your inventory:{Inventory}
{yellow}Please input the serial number of which item to buy \
and press enter.{color_end}""", 1, 3)
            if choice in [1, 2]:
                choice_amount = valid_input.valid_amount_input(f"{yellow}\
Please input the amount of item to buy and press enter.{color_end}")
                if Weapon[choice][2] * choice_amount <= Wallet:
                    Inventory[Weapon[choice][0]] += choice_amount
                    Wallet = Wallet - Weapon[choice][2] * choice_amount
                    choice = valid_input.valid_choice_input(
                        f"""\
{yellow}your inventory:{Inventory}
your wallet:{Wallet}
Continue to buy?   1.buy   2.back
Please input the serial number to choose and press enter.{color_end}""", 1, 2)
                    if choice == 2:
                        return
                else:
                    print_pause("No enough money.")
            elif choice == 3:
                return


def sell():
    global Wallet
    while True:
        thing.items_list()
        choice = valid_input.valid_choice_input(
            f"""\
{yellow}Please input the serial number of items \
which you want yo sell and press enter. your wallet:{Wallet}
Or if you want to get back pleae press 6 \
and press enter.{color_end}""", 1, 6)
        if choice == 6:
            return
        else:
            choice_amount = valid_input.valid_amount_input(f"{yellow}\
Please input the amount of the item to sell and press enter.{color_end}")
            if Inventory[Items[choice - 1][0]] < choice_amount:
                print_pause("you don't have enough amount of this item.")
            else:
                Inventory[Items[choice - 1][0]] -= choice_amount
                Wallet = Wallet + Items[choice - 1][2] * choice_amount
                choice = valid_input.valid_choice_input(
                    f"""\
your inventory:{Inventory}
your wallet:{Wallet}
{yellow}Continue to sell?   1.sell   2.back
Please input the serial number to choose \
and press enter.{color_end}""", 1, 2)
                if choice == 2:
                    return


class Armorer():

    def armorer_menu(self):
        while True:
            choice = valid_input.valid_choice_input(
                f"""
{yellow}You are in the armorer's shop
1.buy     2.sell     3.go back to port center{color_end}
your money:{Wallet}
your inventory:{Inventory}
{yellow}Please input the serial number \
and press enter.{color_end}""", 1, 3)
            if choice == 1:
                self.armorer_buy()
            elif choice == 2:
                sell()
            elif choice == 3:
                return

    def armorer_buy(self):
        global Wallet
        while True:
            choice = valid_input.valid_choice_input(
                f"""\
{yellow}1.chainmail:50 coins  2.plate armor:100 coins  3.back{color_end}
your wallet:{Wallet}
your inventory:{Inventory}
{yellow}Please input the serial number of which item to buy \
and press enter.{color_end}""", 1, 3)
            if choice in [1, 2]:
                choice_amount = valid_input.valid_amount_input(f"{yellow}\
Please input the amount of item to buy and press enter.{color_end}")
                if Armor[choice][2] * choice_amount <= Wallet:
                    Inventory[Armor[choice][0]] += choice_amount
                    Wallet = Wallet - Weapon[choice][2] * choice_amount
                    choice = valid_input.valid_choice_input(
                        f"""\
your inventory:{Inventory}
your wallet:{Wallet}
{yellow}Continue to buy?   1.buy   2.back
Please input the serial number to choose and press enter.{color_end}""", 1, 2)
                    if choice == 2:
                        return
                else:
                    print_pause("no enough money.")
            elif choice == 3:
                return


class Trader():

    def trader_menu(self):
        global Wallet
        while True:
            choice = valid_input.valid_choice_input(
                f"""
{yellow}You are in the trader's shop
1.buy     2.sell     3.go back to port center{color_end}
your money:{Wallet}
your inventory:{Inventory}
{yellow}Please input the serial number \
and press enter.{color_end}""", 1, 3)
            if choice == 1:
                self.trader_buy()
            elif choice == 2:
                sell()
            elif choice == 3:
                return

    def trader_buy(self):
        global Wallet
        while True:
            choice = valid_input.valid_choice_input(
                f"""\
{yellow}1.fresh water:2 coins/unit      2.back{color_end}
your wallet:{Wallet}
you inventory:{Inventory}
{yellow}Please input the serial number of choice \
and press enter.{color_end}""", 1, 2)
            if choice == 1:
                choice_amount = valid_input.valid_amount_input(f"{yellow}\
Please input the amount of fresh water to buy and press enter.{color_end}")
                if freshwater[2] * choice_amount <= Wallet:
                    Inventory["freshwater"] += choice_amount
                    Wallet = Wallet - freshwater[2] * choice_amount
                    choice = valid_input.valid_choice_input(
                        f"""\
your inventory:{Inventory}
your wallet:{Wallet}
{yellow}Continue to buy?   1.buy   2.back
Please input the serial number to choose \
and press enter.{color_end}""", 1, 2)
                    if choice == 2:
                        return
                else:
                    print_pause("no enough money.")
            elif choice == 2:
                return


def clinic():
    global Wallet
    while True:
        choice = valid_input.valid_choice_input(
            f"""
{yellow}You are in the clinic. \
Do you want to cure your sailors or recruit a doctor?
1. Cure all sailors:10 coins
2. Recruit a doctor:100 coins
3. back to the port center{color_end}
your wallet:{Wallet}
{yellow}Please input the serial number of what to do \
and press enter.{color_end}""", 1, 3)
        if choice == 1:
            if Wallet < 10:
                print("no enough money")
            else:
                for person in crew:
                    person[1] = person[2]
                    if "malaria" in person:
                        person.remove("malaria")
                    if "gastroenteritis" in person:
                        person.remove("gastroenteritis")
                Wallet = Wallet - 10
                sailors_list.sailor_list_no_index()
        if choice == 2:
            if len(crew) >= 15:
                print("The seats of ship are full. \
                    Maybe you need dismiss a sailor.")
            elif doctor in crew:
                print("You have already had a doctor in your ship")
            elif Wallet < 100:
                print("You don't have enough money.")
            else:
                crew.append(doctor)
                Wallet -= 100
                sailors_list.sailor_list_no_index()
        if choice == 3:
            return


def tavern_icemeet():
    global Wallet
    while True:
        choice = valid_input.valid_choice_input(
            f"""
{yellow}You are in the tavern. There are some sailors here.
What do you want to do?
1. Recruit new sailors(30 coins/sailor)
2. back to port center{color_end}
your wallet:{Wallet}
{yellow}Please input the serial number and press enter.{color_end}""", 1, 2)
        if choice == 1:
            if len(crew) >= 15:
                print_pause("The seats of ship are full. \
Maybe you need dismiss a sailor.")
            else:
                if Wallet < 30:
                    print_pause("No enough money.")
                else:
                    sailors_list.sailor_list_icemeet()
                    choice = valid_input.valid_choice_input(
                        f"""\
{yellow}Please input the serial numbe of the new sailor \
you want to recruit and press enter.
If you want to cancel and back, please input 0 and press enter.\
{color_end}""", 0, len(sailor_icemeet))
                    crew.append(sailor_icemeet[choice - 1])
                    sailor_icemeet.pop(choice - 1)
                    Wallet = Wallet - 30
        elif choice == 2:
            return


def inn():
    sailors_list.sailor_list_no_index()
    Inventory()
    while True:
        choice = valid_input.valid_choice_input(
            f"""
{yellow}1.relax(recover hp of all sailors with spending 1 day)   \
2.back{color_end}
{yellow}Please input the serial number to choose \
and press enter.{color_end}""", 1, 2)
        if choice == 1:
            for sailor in crew:
                sailor[1] = sailor[2]
                if check_water_disease.fresh_water_use_check() \
                   == "play_again" \
                   or check_water_disease.disease_check() == "play_again":
                    return "play_again"
        elif choice == 2:
            return


class Navigation():

    def navigation_panel(self, day, days_remained):
        print_pause(
            f"""
{blue}You are heading to {destination} from {start_point}.
distance to {start_point}:{distance_past}km
disatance to {destination}:{distance}km   ship speed today:{true_speed}km/day
sail day:{day}                days remained estimated:{days_remained}days
today weather:{weather}{color_end}""", 2)
        print_pause("Your sailors:")
        sailors_list.sailor_list_no_index()
        print_pause(f"""\
your inventory:{Inventory}
your wallet:{Wallet}""")
        map()

    def navigation_direction_inquiry(self):
        global destination, start_point, true_speed, distance, distance_past
        while True:
            choice = valid_input.valid_choice_input(
                f"""\
{yellow}choice:  1.sail to {destination}   \
2.back to {start_point}   3. stay where you are
Please input the serial number to choose \
and press enter.{color_end}""", 1, 3)
            if choice == 1:
                distance_past += true_speed
                distance -= true_speed
                break
            elif choice == 2:
                destination, start_point = start_point, destination
                distance, distance_past = distance_past, distance
                distance_past += true_speed
                distance -= true_speed
                break
            elif choice == 3:
                break

    def recover_hp_everyday(self):
        for sailor in crew:
            if sailor[1] < sailor[2]:
                sailor[1] += 1

    def arrival(self):
        if distance <= 0:
            if destination == "Icemeet":
                return "icemeet"
            elif destination == "Frostford":
                return "frostford"


class Speed():

    def windy_storm_speed(self):
        Windy_storm_speed = round(random.uniform(5.0, 15.0), 2)
        return Windy_storm_speed

    def speed(self, weather):
        if weather == "calm":
            return 10
        elif weather == "cloudy":
            return 10
        elif weather == "windy" or weather == "storm":
            speed = self.windy_storm_speed()
            return speed


class Weather_event_disease_generator():

    def __init__(self):
        self.weather_name = ["calm", "windy", "cloudy", "storm"]

    def weather_generator(self):
        return random.choices(self.weather_name,
                              cum_weights=[10, 14, 17, 20],
                              k=1)[0]

    def random_event_generator(self, weather):
        fight_spoils_levelup = Fight_spoils_levelup()
        event = [
            "nothing", "Pirate", "come across a new sailor",
            "come across a new doctor"
        ]
        random_event = random.choices(event,
                                      cum_weights=[60, 90, 98, 100],
                                      k=1)[0]
        if weather == "storm":
            event = [
                "nothing", "Pirate", "come across a new sailor",
                "come across a new doctor", "Sea Monster"
            ]
            random_event = random.choices(event,
                                          cum_weights=[60, 90, 98, 100, 102],
                                          k=1)[0]
        if random_event == "nothing":
            print_pause(event[0])
        elif random_event == "Pirate":
            if fight_spoils_levelup.fight(event[1]) == "play_again":
                return "play_again"
        elif random_event == "come across a new sailor":
            if len(crew) < 15:
                random_drifting_sailor = random.choice(sailors_drifting)
                crew.append(random_drifting_sailor)
                sailors_drifting.remove(random_drifting_sailor)
                print_pause(event[2])
                sailors_list.single_sailor_list(0)
            else:
                print_pause(event[0])
        elif random_event == "come across a new doctor":
            if len(crew) < 15:
                if doctor not in crew:
                    crew.append(doctor)
                    print_pause(event[3])
                else:
                    print_pause(event[0])
            else:
                print_pause(event[0])
        elif random_event == "Sea Monster":
            if fight_spoils_levelup.fight(event[4]) == "play_again":
                return "play_agaiin"

    def disease_generator(self, weather):
        if weather == "calm":
            calm_disease_index = random.uniform(0.0, 100.0)
            if calm_disease_index > 95.0:
                self.disease_print(self.disease_append())
        if weather == "windy":
            windy_disease_index = random.uniform(0.0, 100.0)
            if windy_disease_index > 99.0:
                self.disease_print(self.disease_append())
        if weather == "cloudy":
            cloudy_disease_index = random.uniform(0.0, 100.0)
            if cloudy_disease_index > 80:
                self.disease_print(self.disease_append())
        if weather == "storm":
            storm_disease_index = random.uniform(0.0, 100.0)
            if storm_disease_index > 70:
                self.disease_print(self.disease_append())

    def disease_append(self):
        random_person_to_disease = random.choice(crew)
        if "malaria" in random_person_to_disease \
           or "gastroenteritis" in random_person_to_disease:
            return
        else:
            random_person_to_disease[10] = random.choice(
                ["malaria", "gastroenteritis"])
            random_person_to_disease[11] = 4
            disease_people.append(random_person_to_disease)
            print_pause(f"{random_person_to_disease[0]} got disease")
            return "disease"

    def disease_print(self, state):
        if state == "disease":
            print_pause("Some sailors have gotten disease. \
You can check states of your sailors.")
            if doctor in crew:
                print_pause("Although your sailors have gotton diseases, \
your doctor can cure them in one day.")


class Fight_spoils_levelup():

    def fight(self, Enemy):
        amount_previous_sailor = len(crew)
        if Enemy == enemy_dictionary[0]:
            single_enemy = pirate
            amount_pirate = random.randint(1, 6)
            for everytime in range(amount_pirate):
                enemy_crew.append(pirate)
        elif Enemy == enemy_dictionary[1]:
            single_enemy = sea_monster
            enemy_crew.append(sea_monster)
        amount_enemy = len(enemy_crew)
        while True:
            for sailor in crew:
                random_enemy = random.choice(enemy_crew)
                random_enemy[1] -= sailor[3] - random_enemy[4]
                if random_enemy[1] <= 0:
                    enemy_crew.remove(random_enemy)
                    if enemy_crew == []:
                        if amount_previous_sailor == len(crew):
                            print_pause(f"You encountered {Enemy}\
(amount:{amount_enemy}), but your sailors survived.")
                        if amount_previous_sailor != len(crew):
                            print_pause(f"""\
You encountered {Enemy}(amount:{amount_enemy}) and your sailors survived.
But some of your sailors died.""")
                        self.level_up(single_enemy, amount_enemy)
                        sailors_list.sailor_list_no_index()
                        self.spoils(single_enemy, amount_enemy)
                        print_pause(f"your inventory:{Inventory}")
                        return
            for every_enemy in enemy_crew:
                random_sailor = random.choice(crew)
                random_sailor[1] -= every_enemy[3] - random_sailor[4]
                if random_sailor[1] <= 0:
                    crew.remove(random_sailor)
                    if crew == []:
                        print_pause(
                            f"You encountered {Enemy}(amount:{amount_enemy})\
. Unluckily, you were annihilated.")
                        return "play_again"

    def spoils(self, single_enemy, amount):
        global Wallet
        freshwater_spoils = single_enemy[5] * amount
        money_spoils = single_enemy[6] * amount
        Inventory["freshwater"] += freshwater_spoils
        Wallet = Wallet + money_spoils
        print_pause(f"You got {freshwater_spoils} freshwater \
and {money_spoils} coins from enemies")

    def level_up(self, single_enemy, amount):
        every_sailor_xp_acquire = round(single_enemy[5] * amount / len(crew))
        for sailor in crew:
            sailor[5] += every_sailor_xp_acquire
            while sailor[5] >= sailor[13]:
                if sailor[12] < 10:
                    sailor[12] += 1
                    sailor[5] -= sailor[13]
                    sailor[13] = round(sailor[13] * 1.5)
                    sailor[2] += 2
                    sailor[3] += 2
                    sailor[4] += 2
                if sailor[12] == 10:
                    sailor[5] = 0
                    sailor[13] = 0


class Check_water_disease():

    def fresh_water_use_check(self):
        global thirst_countdown
        if Inventory["freshwater"] >= 10:
            Inventory["freshwater"] -= 10
            thirst_countdown = "none"
        if Inventory["freshwater"] < 10:
            Inventory["freshwater"] = 0
            print_pause(
                "You don't have enough fresh water. Your sailors is thirsty. \
They will die in 3 days without fresh water.")
            if thirst_countdown == "none":
                thirst_countdown = 3
            else:
                thirst_countdown -= 1
                if thirst_countdown == 0:
                    print_pause("You died of thirst.")
                    return "play_again"

    def disease_check(self):
        if disease_people != []:
            if doctor in crew:
                for every_disease_people in disease_people:
                    every_disease_people[10] = ""
                    every_disease_people[11] = ""
                    disease_people.remove(every_disease_people)
                    print_pause("Your sailor is cured by your doctor.")
            else:
                for every_disease_people in disease_people:
                    every_disease_people[11] -= 1
                    if every_disease_people[11] == 0:
                        crew.remove(every_disease_people)
                        disease_people.remove(every_disease_people)
                        print_pause("One of your sailors has died of disease.")
                        if crew == []:
                            print_pause("Your sailors died of Disease.")
                            return "play_again"


class Icemeet_port():

    def icemeet_port_menu(self):
        print_pause(
            f"""\
{yellow}You can choose where to go:
1. blacksmith's shop (buy weapons)
2. armorer's shop (buy armors)
3. traders (buy freshwater)
4. clinic (cure disease as well as recover hp ,recruit a doctor)
5. tavern (recruit new tailors)
6. inn(recover hp with spending one day.)

or what to do:
7. check states of sailors(Hp, Attack, Defense, Experience, Weapon, Armor)\
(You can equip tailors here)
8. dismiss sailors
9. sail to Frostford Port(100km){color_end}
You ship nomal speed:10km/day
your money:{Wallet}
your inventory:{Inventory}""", 0.5)

    def icemeet_port(self):
        while True:
            self.icemeet_port_menu()
            map()
            choice = valid_input.valid_choice_input(
                f"{yellow}Please input the serial number of your choice \
and press enter.{color_end}", 1, 9)
            if choice == 1:
                blacksmith = Blacksmith()
                blacksmith.blacksmith_menu()
            elif choice == 2:
                armorer = Armorer()
                armorer.armorer_menu()
            elif choice == 3:
                trader = Trader()
                trader.trader_menu()
            elif choice == 4:
                clinic()
            elif choice == 5:
                tavern_icemeet()
            elif choice == 6:
                if inn() == "play_again":
                    return "play_again"
            elif choice == 7:
                equip_unequip.equip_enquiry()
            elif choice == 8:
                sailor_dismiss()
            elif choice == 9:
                return


def frostford():
    print_pause(f"{blue}Finally you got home.\\^o^/{color_end}")


def ocean():
    global Wallet, distance, distance_past, destination, start_point, \
           true_speed, weather
    distance = 100
    start_point = "Icemeet"
    destination = "Frostford"
    day = 0
    distance_past = 0
    weather_event_disease_generator = Weather_event_disease_generator()
    ship_speed = Speed()
    navigation = Navigation()
    while True:
        if distance % 10 == 0:
            days_remained = distance / 10
        else:
            days_remained = round(distance // 10 + 1)
        weather = weather_event_disease_generator.weather_generator()
        true_speed = ship_speed.speed(weather)
        navigation.navigation_panel(day, days_remained)
        equip_unequip.equip_ask()
        print_pause("today event:")
        if weather_event_disease_generator.random_event_generator(weather) \
           == "play_again":
            return "play_again"
        pause()
        weather_event_disease_generator.disease_generator(weather)
        navigation.navigation_direction_inquiry()
        day += 1
        print_pause("A new day comes")
        if check_water_disease.fresh_water_use_check() == "play_again" \
           or check_water_disease.disease_check() == "play_again":
            return "play_again"
        navigation.recover_hp_everyday
        if navigation.arrival() == "icemeet":
            return
        if navigation.arrival() == "frostford":
            return "frostford"


def game_start():
    while True:
        introduction()
        slow_print("""\
After undergoing the baptism of wind and rain of several days,
you arrive at the center of Icemeet Port. """)
        while True:
            icemeet_return = icemeet.icemeet_port()
            if icemeet_return == "play_again":
                return "play_again"
            ocean_return = ocean()
            if ocean_return == "play_again":
                return "play_again"
            if ocean_return == "frostford":
                frostford()
                return "play_again"


def play_again():
    choice = valid_input.valid_choice_input(
        f"""\
{yellow}Do you want to play again?   1.Yes    2.No
Please input the serial number to choose \
and press enter{color_end}""", 1, 2)
    if choice == 2:
        exit(0)


def game():
    while True:
        global valid_input, thing, equip_unequip, icemeet, check_water_disease
        color()
        valid_input = Valid_input()
        thing = Inventory_wallet_item_equipment_list()
        equip_unequip = Equip_unequip()
        icemeet = Icemeet_port()
        check_water_disease = Check_water_disease()
        thing.wallet()
        thing.inventory()
        thing.items()
        creature()
        if game_start() == "play_again":
            play_again()


if __name__ == "__main__":
    game()
