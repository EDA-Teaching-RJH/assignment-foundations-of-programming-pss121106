import time

# 1
def init_database():
    names = ["Michael Townley", "Trevor Phillips", "Franklin Clinton", "Lamar Davis", "Lester Crest"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Lt. Commander"]
    divs  = ["Command", "Command", "Operations", "Security", "Engineering"]
    ids   = ["001", "002", "003", "004", "005"]
    return names, ranks, divs, ids

# 2
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

# 4
def remove_member(names, ranks, divs, ids):
    print("\n--- REMOVE CREW MEMBER ---")
    target_id = input("Enter ID to remove: ")
    if target_id in ids:
        idx = ids.index(target_id)
        removed_name = names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        ids.pop(idx)
        print(f"{removed_name} (ID: {target_id}) removed.")
    else:
        print("Error: ID not found.")

# 5
def update_rank(names, ranks, ids):
    print("\n--- UPDATE RANK ---")
    target_id = input("Enter ID to update: ")
    if target_id in ids:
        idx = ids.index(target_id)
        current_rank = ranks[idx]
        print(f"Current rank for {names[idx]}: {current_rank}")
        new_rank = input("Enter new rank: ")
        ranks[idx] = new_rank # Update only the rank list at that index
        print("Rank updated.")
    else:
        print("Error: ID not found.")

# 6
def display_roster(names, ranks, divs, ids):
    print("\n--- CURRENT ROSTER ---")
    print(f"{'ID':<10} {'Name':<20} {'Rank':<15} {'Division':<15}")
    print("-" * 60)
    for i in range(len(names)):
        print(f"{ids[i]:<10} {names[i]:<20} {ranks[i]:<15} {divs[i]:<15}")

# 7
def search_crew(names, ranks, divs, ids):
    query = input("Enter name to search: ").lower()
    found = False
    print("\nSearch Results:")
    for i in range(len(names)):
        if query in names[i].lower():
            print(f"Found: {names[i]} - {ranks[i]} - {divs[i]} (ID: {ids[i]})")
            found = True
    if not found:
        print("No matches found.")

# 8
def filter_by_division(names, divs):
    target_div = input("Enter Division to filter (Command, Operations, Sciences): ")
    print(f"\n--- {target_div.upper()} DIVISION ---")
    found_any = False
    for i in range(len(names)):
        if divs[i].lower() == target_div.lower():
            print(f"{names[i]}")
            found_any = True
    if not found_any:
        print("No crew found in this division.")

# 9
def calculate_payroll(ranks):
    total_cost = 0
    # Assign values to ranks
    pay_scale = {
        "Captain": 1000,
        "Commander": 800,
        "Lt. Commander": 700,
        "Lieutenant": 500,
        "Ensign": 200
    }
    for rank in ranks:
        # get(rank, 0) returns 0 if the rank isn't in the dictionary
        total_cost += pay_scale.get(rank, 0)
    return total_cost

# 10
def count_officers(ranks):
    count = 0
    for rank in ranks:
        # The logic fix from our previous chat
        if rank == "Captain" or rank == "Commander":
            count += 1
    return count

def run_system_monolith():
    print("BOOTING SYSTEM...")
    time.sleep(1)
    print("WELCOME TO FLEET COMMAND")
    
    names, ranks, divs, ids = init_database()
    while True:
        choice = display_menu()
        if choice == "1":
            display_roster(names, ranks, divs, ids)
        elif choice == "2":
            add_member(names, ranks, divs, ids)
        elif choice == "3":
            remove_member(names, ranks, divs, ids)
        elif choice == "4":
            update_rank(names, ranks, ids)
        elif choice == "5":
            search_crew(names, ranks, divs, ids)
        elif choice == "6":
            filter_by_division(names, divs)
        elif choice == "7":
            cost = calculate_payroll(ranks)
            print(f"Total Monthly Payroll: {cost} credits")
        elif choice == "8":
            officers = count_officers(ranks)
            print("High ranking officers: " + str(officers))
        elif choice == "9":
            print("Shutting down...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    run_system_monolith()