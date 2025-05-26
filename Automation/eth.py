import tkinter as tk
from tkinter import ttk, messagebox

monthly = {
    "january": 1200,
    "february": 1200,
    "march": 1200,
    "april": 1200,
    "may": 1200,
    "june": 1200,
    "july": 2400,
    "august": 1200,
    "september": 1200,
    "october": 1200,
    "november": 1200,
    "december": 1200
}

def abandoned_now(dictionary, now):
    investing_sum = [6600]
    for key in dictionary:
        if key == now:
            investing_sum.append(dictionary[key])
            break
        investing_sum.append(dictionary[key])
    return sum(investing_sum)

def calculate():
    month = month_var.get().lower()
    try:
        balance = float(balance_entry.get())
        eth_price = float(eth_entry.get())
    except ValueError:
        messagebox.showerror("Fail", "Enter the correct numbers for your ETH balance and price.")
        return

    if month not in monthly:
        messagebox.showerror("Fail", f"Invalid month: {month}")
        return

    inv = abandoned_now(monthly, month)
    deviation = round(balance / inv * 100, 2)
    fell_percent = round(100 - deviation, 2)

    breakeven = eth_price * 100 / deviation

    result_var.set(
        f"💰 Invested to {month.capitalize()}: {inv}$\n"
        f"📉 Current coverage: {deviation}%\n"
        f"📈 It is necessary to grow on: {fell_percent}%\n"
        f"💸 Break-even price for ETH: {breakeven}$"
    )

# Creating the window
root = tk.Tk()
root.title("ETH Investment Tracker")
root.geometry("400x400")
root.resizable(False, False)

# Month
ttk.Label(root, text="Select the current month:").pack(pady=5)
month_var = tk.StringVar()
month_combo = ttk.Combobox(root, textvariable=month_var, values=list(monthly.keys()), state="readonly")
month_combo.current(0)
month_combo.pack()

# Balance
ttk.Label(root, text="Enter your current balance ($):").pack(pady=5)
balance_entry = ttk.Entry(root)
balance_entry.pack()

# Price ETH
ttk.Label(root, text="Enter the current price of ETH ($):").pack(pady=5)
eth_entry = ttk.Entry(root)
eth_entry.pack()

# Button
ttk.Button(root, text="Calculate", command=calculate).pack(pady=15)

# Result
result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, wraplength=380, justify="left")
result_label.pack(pady=10)

root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')

root.mainloop()
