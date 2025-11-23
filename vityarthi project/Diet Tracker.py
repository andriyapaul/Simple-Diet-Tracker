import datetime

# --- Configuration ---
LOG_FILE = "diet_log.txt"

class FoodEntry:
    """Represents a single food entry with date, food item, and calories."""
    def __init__(self, date_str, food_item, calories):
        self.date_str = date_str
        self.food_item = food_item
        self.calories = calories

    def __str__(self):
        """Returns a string representation for display."""
        return f"{self.date_str} - {self.food_item} ({self.calories} Cal)"

    def to_csv_line(self):
        """Returns a string in CSV format for saving to file."""
        return f"{self.date_str},{self.food_item},{self.calories}\n"

# --- Utility Functions ---

def load_entries():
    """Loads all food entries from the log file."""
    entries = []
    try:
        with open(LOG_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    try:
                        date_str, food_item, calories = parts
                        entries.append(FoodEntry(date_str, food_item, int(calories)))
                    except ValueError:
                        print(f"Warning: Skipping corrupted line in log file: {line.strip()}")
    except FileNotFoundError:
        # File will be created when the first entry is saved
        pass
    return entries

def save_entry(entry):
    """Appends a new food entry to the log file."""
    with open(LOG_FILE, 'a') as f:
        f.write(entry.to_csv_line())

def get_valid_input(prompt, input_type=str):
    """Handles basic input validation for str and int types."""
    while True:
        try:
            user_input = input(prompt).strip()
            if input_type == int:
                # Ensure it's a positive integer for calories
                value = int(user_input)
                if value < 0:
                    raise ValueError
                return value
            elif input_type == str:
                if not user_input:
                    raise ValueError
                return user_input.title() # Capitalize for consistency
            return user_input
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__} (and positive for calories).")

# --- Core Application Functions ---

def add_entry():
    """Prompts user for a new food entry and saves it."""
    print("\n--- Add New Entry ---")
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    print(f"Date: **{date_str}**")

    food_item = get_valid_input("Enter the food item/meal: ")
    calories = get_valid_input("Enter the calorie count: ", int)

    new_entry = FoodEntry(date_str, food_item, calories)
    save_entry(new_entry)
    print(f"\n✅ Entry added: {new_entry.food_item} ({new_entry.calories} Cal)")

def view_log():
    """Displays all logged entries and the total calories."""
    print("\n--- Diet Log ---")
    entries = load_entries()

    if not entries:
        print("The log is empty. Add some entries!")
        return

    # Group entries by date
    log_by_date = {}
    for entry in entries:
        if entry.date_str not in log_by_date:
            log_by_date[entry.date_str] = []
        log_by_date[entry.date_str].append(entry)

    total_calories_all_time = 0

    # Display entries date by date
    for date_str, daily_entries in sorted(log_by_date.items()):
        daily_total = sum(e.calories for e in daily_entries)
        total_calories_all_time += daily_total

        print(f"\n📅 **{date_str}** - Total: **{daily_total} Cal**")
        for entry in daily_entries:
            print(f"  - {entry.food_item}: {entry.calories} Cal")

    print("\n" + "="*30)
    print(f"🌍 **Grand Total Calories Logged: {total_calories_all_time} Cal**")
    print("="*30)

# --- Main Program Loop ---

def main():
    """The main function to run the application."""
    print("✨ Welcome to the Simple Diet Tracker! ✨")
    
    while True:
        print("\n--- Menu ---")
        print("1. **Add New Food Entry**")
        print("2. **View Log & Totals**")
        print("3. **Exit**")
        
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_log()
        elif choice == '3':
            print("\nGoodbye! Stay healthy!")
            break
        else:
            print("\n❌ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
    import datetime

# --- Configuration ---
LOG_FILE = "diet_log.txt"

class FoodEntry:
    """Represents a single food entry with date, food item, and calories."""
    def __init__(self, date_str, food_item, calories):
        self.date_str = date_str
        self.food_item = food_item
        self.calories = calories

    def __str__(self):
        """Returns a string representation for display."""
        return f"{self.date_str} - {self.food_item} ({self.calories} Cal)"

    def to_csv_line(self):
        """Returns a string in CSV format for saving to file."""
        return f"{self.date_str},{self.food_item},{self.calories}\n"

# --- Utility Functions ---

def load_entries():
    """Loads all food entries from the log file."""
    entries = []
    try:
        with open(LOG_FILE, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    try:
                        date_str, food_item, calories = parts
                        entries.append(FoodEntry(date_str, food_item, int(calories)))
                    except ValueError:
                        print(f"Warning: Skipping corrupted line in log file: {line.strip()}")
    except FileNotFoundError:
        # File will be created when the first entry is saved
        pass
    return entries

def save_entry(entry):
    """Appends a new food entry to the log file."""
    with open(LOG_FILE, 'a') as f:
        f.write(entry.to_csv_line())

def get_valid_input(prompt, input_type=str):
    """Handles basic input validation for str and int types."""
    while True:
        try:
            user_input = input(prompt).strip()
            if input_type == int:
                # Ensure it's a positive integer for calories
                value = int(user_input)
                if value < 0:
                    raise ValueError
                return value
            elif input_type == str:
                if not user_input:
                    raise ValueError
                return user_input.title() # Capitalize for consistency
            return user_input
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__} (and positive for calories).")

# --- Core Application Functions ---

def add_entry():
    """Prompts user for a new food entry and saves it."""
    print("\n--- Add New Entry ---")
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    print(f"Date: **{date_str}**")

    food_item = get_valid_input("Enter the food item/meal: ")
    calories = get_valid_input("Enter the calorie count: ", int)

    new_entry = FoodEntry(date_str, food_item, calories)
    save_entry(new_entry)
    print(f"\n✅ Entry added: {new_entry.food_item} ({new_entry.calories} Cal)")

def view_log():
    """Displays all logged entries and the total calories."""
    print("\n--- Diet Log ---")
    entries = load_entries()

    if not entries:
        print("The log is empty. Add some entries!")
        return

    # Group entries by date
    log_by_date = {}
    for entry in entries:
        if entry.date_str not in log_by_date:
            log_by_date[entry.date_str] = []
        log_by_date[entry.date_str].append(entry)

    total_calories_all_time = 0

    # Display entries date by date
    for date_str, daily_entries in sorted(log_by_date.items()):
        daily_total = sum(e.calories for e in daily_entries)
        total_calories_all_time += daily_total

        print(f"\n📅 **{date_str}** - Total: **{daily_total} Cal**")
        for entry in daily_entries:
            print(f"  - {entry.food_item}: {entry.calories} Cal")

    print("\n" + "="*30)
    print(f"🌍 **Grand Total Calories Logged: {total_calories_all_time} Cal**")
    print("="*30)

# --- Main Program Loop ---

def main():
    """The main function to run the application."""
    print("✨ Welcome to the Simple Diet Tracker! ✨")
    
    while True:
        print("\n--- Menu ---")
        print("1. **Add New Food Entry**")
        print("2. **View Log & Totals**")
        print("3. **Exit**")
        
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            add_entry()
        elif choice == '2':
            view_log()
        elif choice == '3':
            print("\nGoodbye! Stay healthy!")
            break
        else:
            print("\n❌ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
