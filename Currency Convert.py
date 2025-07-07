import tkinter as tk
import requests

def get_conversion_rate(from_curr, to_curr):
    url = f"https://api.exchangerate.host/convert?from={from_curr}&to={to_curr}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["result"]
    else:
        return None

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_var.get()
        to_curr = to_var.get()

        if from_curr == to_curr:
            result_var.set(f"{amount:.2f} {to_curr}")
            return

        rate = get_conversion_rate(from_curr, to_curr)
        if rate:
            converted = amount * rate
            result_var.set(f"{converted:.2f} {to_curr}")
        else:
            result_var.set("❌ Error: API failed.")
    except ValueError:
        result_var.set("⚠️ Invalid amount!")

# --- GUI Setup ---
root = tk.Tk()
root.title("💱 Live Currency Converter")
root.geometry("350x300")
root.configure(bg="#f0f0f0")

currencies = ["USD", "PKR", "EUR", "INR", "GBP", "CAD", "AUD"]

# Title
tk.Label(root, text="🌍 Live Currency Converter", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# Amount Entry
tk.Label(root, text="Amount", bg="#f0f0f0").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

# From Currency
from_var = tk.StringVar(value="USD")
tk.Label(root, text="From", bg="#f0f0f0").pack()
tk.OptionMenu(root, from_var, *currencies).pack()

# To Currency
to_var = tk.StringVar(value="PKR")
tk.Label(root, text="To", bg="#f0f0f0").pack()
tk.OptionMenu(root, to_var, *currencies).pack()

# Convert Button
tk.Button(root, text="Convert", command=convert_currency).pack(pady=10)

# Result Display
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Arial", 14), bg="#f0f0f0", fg="green").pack()

root.mainloop()
