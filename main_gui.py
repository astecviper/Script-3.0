import tkinter as tk
import customtkinter as ctk
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#2e2e2e")  # Set background color here

        # Window Settings
        self.title("Aztec's Speed-Up & Clean-Up")
        # Set window size
        self.geometry("800x600")

        # Button texts
        self.toolbar_button_texts = ["Help", "Shortcut", "Run", "Cancel", "Exit"]
        self.tab_button_texts = ["Dashboard", "Tests", "Presets", "Scheduled Presets", "Settings"]

        # Toolbar Section
        self.create_toolbar()

        # Tab Bar Section
        self.create_tab_bar()

        # Show the first tab by default
        self.show_tab(1)

    # Toolbar Section
    def create_toolbar(self):
        try:
            # Set toolbar frame color and size
            toolbar_frame = ctk.CTkFrame(self, fg_color="#252525", corner_radius=0, height=35)  # Removed rounded corners
            toolbar_frame.pack(side="top", fill="x", padx=0, pady=0)  # Connect to the top and edges

            # Add buttons to the toolbar
            toolbar_buttons_frame = ctk.CTkFrame(toolbar_frame, fg_color="#252525")
            toolbar_buttons_frame.pack(padx=10, pady=(5, 5))  # Adjusted pady to increase padding

            self.toolbar_buttons = []
            for i, text in enumerate(self.toolbar_button_texts, start=1):
                # Set button color and size
                button = ctk.CTkButton(toolbar_buttons_frame, text=text, fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, width=100, height=30)
                button.pack(side="left", padx=5, pady=5)
                self.toolbar_buttons.append(button)

            toolbar_buttons_frame.place(relx=0.5, rely=0.5, anchor="center")
        except Exception as e:
            logging.error(f"Error creating toolbar: {e}")

    # Tab Bar Section
    def create_tab_bar(self):
        try:
            # Set tab bar frame color and size
            self.tab_bar_frame = ctk.CTkFrame(self, fg_color="#3e3e3e", corner_radius=10, height=45)  # Increased height
            self.tab_bar_frame.pack(side="top", fill="x", padx=10, pady=(15, 10))  # Increased pady top to 15

            self.tabs = {}
            tab_buttons_frame = ctk.CTkFrame(self.tab_bar_frame, fg_color="#3e3e3e")
            tab_buttons_frame.pack(padx=10, pady=5)

            self.tab_buttons = []
            for i, text in enumerate(self.tab_button_texts, start=1):
                # Set tab button color and size
                tab_button = ctk.CTkButton(tab_buttons_frame, text=text, fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, height=35, command=lambda i=i: self.show_tab(i))  # Increased height
                tab_button.pack(side="left", padx=5, pady=5)
                self.tab_buttons.append(tab_button)

            tab_buttons_frame.place(relx=0.5, rely=0.5, anchor="center")
        except Exception as e:
            logging.error(f"Error creating tab bar: {e}")

    # Tab Management
    def show_tab(self, tab_index):
        try:
            for tab in self.tabs.values():
                tab.pack_forget()
            self.tabs[tab_index].pack(fill="both", expand=True, padx=10, pady=10)
        except Exception as e:
            logging.error(f"Error showing tab {tab_index}: {e}")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
