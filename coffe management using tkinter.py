import tkinter as tk
from tkinter import messagebox

class CoffeeShopApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Coffee Shop Management System")
        
        # Define variables
        self.menu = {"Espresso": 2.5, "Latte": 3.0, "Cappuccino": 3.5}
        self.order = {}
        self.total_cost = tk.DoubleVar()
        
        # Create widgets
        self.create_widgets()
    
    def create_widgets(self):
        # Menu Label
        menu_label = tk.Label(self.master, text="Menu")
        menu_label.grid(row=0, column=0, padx=10, pady=10)
        
        # Menu Listbox
        self.menu_listbox = tk.Listbox(self.master, width=20, height=5)
        for item in self.menu:
            self.menu_listbox.insert(tk.END, f"{item}: ${self.menu[item]}")
        self.menu_listbox.grid(row=1, column=0, padx=10, pady=5)
        
        # Order Label
        order_label = tk.Label(self.master, text="Order")
        order_label.grid(row=0, column=1, padx=10, pady=10)
        
        # Order Listbox
        self.order_listbox = tk.Listbox(self.master, width=20, height=5)
        self.order_listbox.grid(row=1, column=1, padx=10, pady=5)
        
        # Total Cost Label
        total_cost_label = tk.Label(self.master, text="Total Cost:")
        total_cost_label.grid(row=2, column=1, padx=10, pady=5)
        
        # Total Cost Display
        self.total_cost_display = tk.Label(self.master, textvariable=self.total_cost)
        self.total_cost_display.grid(row=2, column=2, padx=10, pady=5)
        
        # Add to Order Button
        add_to_order_btn = tk.Button(self.master, text="Add to Order", command=self.add_to_order)
        add_to_order_btn.grid(row=2, column=0, padx=10, pady=5)
        
        # Checkout Button
        checkout_btn = tk.Button(self.master, text="Checkout", command=self.checkout)
        checkout_btn.grid(row=3, column=1, padx=10, pady=5)
    
    def add_to_order(self):
        selected_index = self.menu_listbox.curselection()
        if selected_index:
            selected_item = self.menu_listbox.get(selected_index)
            item_name, item_price = selected_item.split(": ")
            self.order[item_name] = float(item_price[1:])
            self.update_order_listbox()
            self.update_total_cost()
        else:
            messagebox.showwarning("Error", "Please select an item from the menu.")
    
    def update_order_listbox(self):
        self.order_listbox.delete(0, tk.END)
        for item in self.order:
            self.order_listbox.insert(tk.END, f"{item}: ${self.order[item]}")
    
    def update_total_cost(self):
        self.total_cost.set(sum(self.order.values()))
    
    def checkout(self):
        messagebox.showinfo("Checkout", f"Total cost: ${self.total_cost.get()}")

def main():
    root = tk.Tk()
    app = CoffeeShopApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
