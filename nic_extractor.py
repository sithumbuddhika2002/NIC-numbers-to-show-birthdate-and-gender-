import tkinter as tk
from tkinter import messagebox  # For error popups
from datetime import datetime, timedelta
def process_nic():
    nic = entry_nic.get().strip()  # Get NIC and remove extra spaces
    
    try:
 
        if len(nic) == 10 and nic[9].upper() == 'V': 
            year = int("19" + nic[0:2])  # Add "19" to get full year (e.g., 1992)
            days = int(nic[2:5])  # Days portion (e.g., 123)
        
        elif len(nic) == 12: 
            year = int(nic[0:4])  # Full year (e.g., 1992)
            days = int(nic[4:7])  # Days portion (e.g., 123)
        
        else:
            raise ValueError("Invalid NIC format. Use 10-digit (YYMMDDXXXV) or 12-digit (YYYYMMDDXXXX)")


        gender = "Female" if days > 500 else "Male"
        
        # Adjust days for females (subtract 500 if > 500)
        actual_days = days - 500 if days > 500 else days
        
        # Calculate birthdate (start at Jan 1, add days)
        birth_date = datetime(year, 1, 1) + timedelta(days=actual_days - 1)
        

        result = f"Birthdate: {birth_date.strftime('%Y-%m-%d')}\nGender: {gender}"
        result_label.config(text=result)
    
    except ValueError as e:
        messagebox.showerror("Error", str(e))  # Show error popup
    except Exception:
        messagebox.showerror("Error", "Invalid NIC number")

# Create the main window
window = tk.Tk()
window.title("NIC Information Extractor")
window.geometry("300x200")

tk.Label(window, text="Enter NIC Number:").pack(pady=5)

entry_nic = tk.Entry(window, width=20)
entry_nic.pack(pady=5)

tk.Button(window, text="Process", command=process_nic).pack(pady=5)

result_label = tk.Label(window, text="", justify="left")
result_label.pack(pady=10)

window.mainloop()