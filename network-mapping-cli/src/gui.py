import tkinter as tk
from tkinter import messagebox
from ip_tracker import IPTracker

class NetworkMappingGUI:
    def __init__(self, root):
        self.tracker = IPTracker()
        self.root = root
        self.root.title("Network Mapping GUI")
        self.root.geometry("300x300")  # Set the default window size

        self.ip_label = tk.Label(root, text="IP Address:")
        self.ip_label.pack()

        self.ip_entry = tk.Entry(root)
        self.ip_entry.pack()

        self.add_button = tk.Button(root, text="Add IP", command=self.add_ip)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove IP", command=self.remove_ip)
        self.remove_button.pack()

        self.list_button = tk.Button(root, text="List IPs", command=self.list_ips)
        self.list_button.pack()

        self.ip_listbox = tk.Listbox(root)
        self.ip_listbox.pack()

    def add_ip(self):
        ip_address = self.ip_entry.get()
        if ip_address:
            self.tracker.add_ip(ip_address)
            self.ip_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Added IP address: {ip_address}")
        else:
            messagebox.showwarning("Input Error", "Please enter an IP address.")

    def remove_ip(self):
        ip_address = self.ip_entry.get()
        if ip_address:
            self.tracker.remove_ip(ip_address)
            self.ip_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Removed IP address: {ip_address}")
        else:
            messagebox.showwarning("Input Error", "Please enter an IP address.")

    def list_ips(self):
        self.ip_listbox.delete(0, tk.END)
        ips = self.tracker.list_ips()
        for ip in ips:
            self.ip_listbox.insert(tk.END, ip)

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkMappingGUI(root)
    root.mainloop()