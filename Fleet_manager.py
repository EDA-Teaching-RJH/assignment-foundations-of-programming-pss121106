#Feature 1
import time
def init_database():
    names = ["Michael Townley", "Trevor Phillips", "Franklin Clinton", "Lamar Davis", "Lester Crest"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"]
    divs  = ["Command", "Command", "Operations", "Security", "Engineering"]
    ids   = ["001", "002", "003", "004", "005"]
    return names, ranks, divs, ids

#Feature 2
def display_menu():
    print("\n--- FLEET COMMAND MENU ---")
    print("1. View Roster")
    print("2. Add Crew Member")
    print("3. Remove Crew Member")
    print("4. Update Rank")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Calculate Payroll")
    print("8. Count High Officers")
    print("9. Exit")
    return input("Select option: ")

#Feature 3
# 3
def add_member(names, ranks, divs, ids):
    print("\n--- ADD CREW MEMBER ---")
    new_id = input("Enter new ID: ")
    
    if new_id in ids:
        print("Error: ID already exists.")
        return
    new_rank = input("Enter Rank (Captain, Commander, Lieutenant, Ensign): ")
    valid_ranks = ["Captain", "Commander", "Lieutenant", "Ensign", "Lt. Commander"]
    if new_rank not in valid_ranks:
        print("Error: Invalid Rank.")
        return
    new_name = input("Enter Name: ")
    new_div = input("Enter Division: ")
    ids.append(new_id)
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    print("Crew member added successfully.")