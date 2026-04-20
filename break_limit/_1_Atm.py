import json
import datetime

def show_statement(data):
    print("\n" + "="*50)
    print(f"{'Date':<11} | {'Time':<8} | {'Amount':<10} | {'Type'}")
    print("-" * 50)
    
    if not data['statement']:
        print("No transactions yet.")
    else:
        for entry in data['statement'][-5:]:
            print(entry)
    return "="*50
    
def atm_process(choice, data):
    # Security Check: Option 1, 2 aur 4 ke liye PIN mangiye
    if choice in [1, 2, 4]:
        secure = int(input("🛡 Enter Your 4 Digit Pin: "))
        if secure != data["pin"]:
            return "❌ Wrong Pin! Access Denied."
        print("🛡 Pin Verified ✔")

    # --- Choice Logic ---
    if choice == 1:
        return f"💰 Account Balance: {data['balance']}"
    
    elif choice == 2:
        amount = int(input("Enter Withdrawal Amount: "))
        if data["balance"] >= amount:
            data["balance"] -= amount
            # Time Format Control
            now = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
            entry = f"{now} | -{amount:<7}.00 | Debit"
            data['statement'].append(entry)
            save_data(data)
            return f"✅ Withdrawal Successful! New Balance: {data['balance']}"
        else:
            return "⚠️ Insufficient Funds!"
            
    elif choice == 3:
        deposit = int(input("Enter Deposit Amount: "))
        data["balance"] += deposit
        now = datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
        entry = f"{now} | +{deposit:<7}.00 | Credit"
        data['statement'].append(entry)
        save_data(data)
        return f"✅ Deposit Successful! New Balance: {data['balance']}"
    
    elif choice == 4:
        return show_statement(data)
    
    else:
        return "❓ Invalid Choice! Please select 1-4."

def save_data(data):
    with open("card.json", "w") as f:
        json.dump(data, f, indent=4)

# --- MAIN LOOP ---
while True:
    try:
        with open("card.json", "r") as f:
            current_data = json.load(f)

        print("\n" + "═"*30)
        print("   WELCOME TO ALVEN ATM   ")
        print("═"*30)
        print("[1]: Balance Check\n[2]: Withdraw Cash\n[3]: Deposit Cash\n[4]: Bank Statement")
        
        choice = int(input("\nEnter Choice (1-4): "))
        result = atm_process(choice, current_data)
        print(result)

    except Exception as e:
        print(f"❌ Error: {e}")

    stay = input("\n[1]: Main Menu | [Any Key]: Exit: ")
    if stay != "1":
        print("Thank you for using Alven ATM! 👋")
        break
