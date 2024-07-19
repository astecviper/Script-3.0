import tkinter as tk
import customtkinter as ctk
from utils.logger import logger, logging, finalize_logging
import subprocess
from utils.settings import load_settings, update_settings

# Configure logging
logger.debug("Starting main GUI")

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#1e1e1e")  # Set background color to a dark theme
        
        # Track the naming window
        self.naming_window = None

        # Window Settings
        self.title("Aztec's Speed-Up & Clean-Up")
        self.geometry("1000x700")  # Set window size

        # Button texts
        self.toolbar_button_texts = ["Help", "Shortcut", "Run", "Cancel", "Exit"]
        self.tab_button_texts = ["Dashboard", "Tests", "Presets", "Scheduled Presets", "Settings"]

        # Toolbar Section
        self.create_toolbar()

        # Tab Bar Section
        self.create_tab_bar()

        # Show the first tab by default
        self.show_tab(1)

        # Create dashboard widgets
        self.create_dashboard_widgets()

        # Create tests tab widgets
        self.create_tests_widgets()
        
        # Create presets tab widgets
        self.create_presets_widgets()
        
        # Create scheduled presets tab widgets
        self.create_scheduled_presets_widgets()
        
        # Create settings tab widgets
        self.create_settings_widgets()
        
        # Bind the close event to finalize logging
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def on_closing(self):
        finalize_logging()
        self.destroy()

    # Toolbar Section
    def create_toolbar(self):
        try:
            # Set toolbar frame color and size
            toolbar_frame = ctk.CTkFrame(self, fg_color="#2e2e2e", corner_radius=0, height=50)  # Darker toolbar
            toolbar_frame.pack(side="top", fill="x", padx=0, pady=0)  # Connect to the top and edges

            # Add buttons to the toolbar
            toolbar_buttons_frame = ctk.CTkFrame(toolbar_frame, fg_color="#2e2e2e")
            toolbar_buttons_frame.pack(padx=10, pady=(5, 5))  # Adjusted pady to increase padding

            self.toolbar_buttons = []
            for i, text in enumerate(self.toolbar_button_texts, start=1):
                if text == "Help":
                    # Create a dropdown menu for the Help button
                    help_button = ctk.CTkButton(toolbar_buttons_frame, text=text, fg_color="#3e3e3e", hover_color="#4e4e4e", corner_radius=10, width=100, height=30, command=self.show_help_menu)
                    help_button.pack(side="left", padx=5, pady=5)
                    self.toolbar_buttons.append(help_button)

                    # Create a menu for the Help button
                    self.help_menu = tk.Menu(self, tearoff=0)
                    self.help_menu.add_command(label="Example 1", command=lambda: self.help_option_selected("Example 1"))
                    self.help_menu.add_command(label="Example 2", command=lambda: self.help_option_selected("Example 2"))
                    self.help_menu.add_command(label="Example 3", command=lambda: self.help_option_selected("Example 3"))
                else:
                    # Set button color and size
                    button = ctk.CTkButton(toolbar_buttons_frame, text=text, fg_color="#3e3e3e", hover_color="#4e4e4e", corner_radius=10, width=100, height=30)
                    button.pack(side="left", padx=5, pady=5)
                    self.toolbar_buttons.append(button)

            toolbar_buttons_frame.place(relx=0.5, rely=0.5, anchor="center")
        except Exception as e:
            logger.error(f"Error creating toolbar: {e}")

    def show_help_menu(self):
        try:
            # Get the position of the Help button
            help_button = self.toolbar_buttons[0]
            x = help_button.winfo_rootx()
            y = help_button.winfo_rooty() + help_button.winfo_height()

            # Show the help menu
            self.help_menu.tk_popup(x, y)
        except Exception as e:
            logger.error(f"Error showing help menu: {e}")

    def help_option_selected(self, option):
        logger.info(f"Help option selected: {option}")
        # Add your logic for handling the selected help option here

    # Tab Bar Section
    def create_tab_bar(self):
        try:
            # Set tab bar frame color and size
            self.tab_bar_frame = ctk.CTkFrame(self, fg_color="#3e3e3e", corner_radius=10, height=50)  # Increased height
            self.tab_bar_frame.pack(side="top", fill="x", padx=10, pady=(15, 10))  # Increased pady top to 15

            self.tabs = {}
            tab_buttons_frame = ctk.CTkFrame(self.tab_bar_frame, fg_color="#3e3e3e")
            tab_buttons_frame.pack(padx=10, pady=5)

            self.tab_buttons = []
            for i, text in enumerate(self.tab_button_texts, start=1):
                # Set tab button color and size
                tab_button = ctk.CTkButton(tab_buttons_frame, text=text, fg_color="#1f6aa5", hover_color="#1f6aa5", corner_radius=10, height=35, command=lambda i=i: self.show_tab(i))  # Updated color to blue
                tab_button.pack(side="left", padx=5, pady=5)
                self.tab_buttons.append(tab_button)

            tab_buttons_frame.place(relx=0.5, rely=0.5, anchor="center")

            # Create tab frames
            for i, text in enumerate(self.tab_button_texts, start=1):
                tab_frame = ctk.CTkFrame(self, fg_color="#1e1e1e", corner_radius=10)
                self.tabs[i] = tab_frame

        except Exception as e:
            logger.error(f"Error creating tab bar: {e}")

    # Tab Management
    def show_tab(self, tab_index):
        try:
            for tab in self.tabs.values():
                tab.pack_forget()
            self.tabs[tab_index].pack(fill="both", expand=True, padx=10, pady=10)

            # Ensure background frame is always present
            if not hasattr(self.tabs[tab_index], 'background_frame'):
                self.tabs[tab_index].background_frame = ctk.CTkFrame(self.tabs[tab_index], fg_color="#2e2e2e", corner_radius=10)
                self.tabs[tab_index].background_frame.pack(fill="both", expand=True, padx=10, pady=10)
        except Exception as e:
            logger.error(f"Error showing tab {tab_index}: {e}")

    # Add this method to create the dashboard widgets
    def create_dashboard_widgets(self):
        try:
            # Create a frame for Enabled Tests inside the background frame
            enabled_tests_frame = ctk.CTkFrame(self.tabs[1].background_frame, fg_color="#2e2e2e", corner_radius=10, width=200)
            enabled_tests_frame.pack(side="right", fill="y", padx=10, pady=10)

            # Create a label for Enabled Tests title with background and rounded edges
            enabled_tests_label = ctk.CTkLabel(enabled_tests_frame, text="Enabled Tests", font=("Arial", 16, "bold"), fg_color="#3e3e3e", corner_radius=10)
            enabled_tests_label.pack(fill="x", pady=(10, 0), padx=10)

            # Create a vertical frame for Enabled Tests content
            enabled_tests_content_frame = ctk.CTkFrame(enabled_tests_frame, fg_color="#3e3e3e", corner_radius=10)
            enabled_tests_content_frame.pack(fill="both", expand=True, padx=10, pady=10)

            # Create a frame for Settings inside the background frame
            settings_frame = ctk.CTkFrame(self.tabs[1].background_frame, fg_color="#2e2e2e", corner_radius=10, width=200)
            settings_frame.pack(side="right", fill="y", padx=10, pady=10)

            # Create a label for Settings title with background and rounded edges
            settings_label = ctk.CTkLabel(settings_frame, text="Settings", font=("Arial", 16, "bold"), fg_color="#3e3e3e", corner_radius=10)
            settings_label.pack(fill="x", pady=(10, 0), padx=10)

            # Create a vertical frame for Settings content
            settings_content_frame = ctk.CTkFrame(settings_frame, fg_color="#3e3e3e", corner_radius=10)
            settings_content_frame.pack(fill="both", expand=True, padx=10, pady=10)

            # Load actual presets from settings
            settings = load_settings()
            custom_presets = settings.get("custom_presets", [])
            self.preset_options = [preset["name"] for preset in custom_presets]
            self.preset_options.insert(0, "Enabled Tests")  # Add "Enabled Tests" option
            self.selected_preset = tk.StringVar(value="Enabled Tests")

            # Create a dropdown for selecting presets
            self.preset_dropdown = ctk.CTkOptionMenu(
                self.tabs[1].background_frame, 
                variable=self.selected_preset, 
                values=self.preset_options, 
                fg_color="#3e3e3e", 
                button_color="#5e5e5e", 
                button_hover_color="#4e4e4e", 
                corner_radius=10, 
                width=200
            )
            self.preset_dropdown.pack(side="top", fill="x", padx=10, pady=10)

            # Create a frame to hold the dropdown options
            self.dropdown_frame = ctk.CTkFrame(self.tabs[1].background_frame, fg_color="#3e3e3e", corner_radius=10)
            self.dropdown_frame.pack_forget()  # Hide the frame initially

            # Create a frame for Terminal inside the background frame
            terminal_frame = ctk.CTkFrame(self.tabs[1].background_frame, fg_color="#2e2e2e", corner_radius=10)
            terminal_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

            # Create a label for Terminal title with background and rounded edges
            terminal_label = ctk.CTkLabel(terminal_frame, text="Terminal", font=("Arial", 16, "bold"), fg_color="#3e3e3e", corner_radius=10)
            terminal_label.pack(fill="x", pady=(10, 0), padx=10)

            # Create a vertical frame for Terminal content
            terminal_content_frame = ctk.CTkFrame(terminal_frame, fg_color="#3e3e3e", corner_radius=10)
            terminal_content_frame.pack(fill="both", expand=True, padx=10, pady=10)

            # Create a scrollable text box for Terminal content
            self.terminal_textbox = ctk.CTkTextbox(terminal_content_frame, state="disabled", wrap="word")
            self.terminal_textbox.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)

            # Create a scrollbar for the text box
            terminal_scrollbar = ctk.CTkScrollbar(terminal_content_frame, command=self.terminal_textbox.yview)
            terminal_scrollbar.pack(side="right", fill="y", padx=(0, 10), pady=(20, 20))
            self.terminal_textbox.configure(yscrollcommand=terminal_scrollbar.set)
        except Exception as e:
            logger.error(f"Error creating dashboard widgets: {e}")

        # Add options to the dropdown frame
        for option in self.preset_options:
            option_button = ctk.CTkButton(
                self.dropdown_frame, 
                text=option, 
                fg_color="#3e3e3e", 
                hover_color="#4e4e4e", 
                corner_radius=10, 
                width=200, 
                command=lambda opt=option: self.select_option(opt)
            )
            option_button.pack(fill="x", padx=10, pady=5)

    def update_preset_dropdown(self):
        logger.debug("Updating preset dropdown")
        settings = load_settings()
        custom_presets = settings.get("custom_presets", [])
        preset_names = [preset["name"] for preset in custom_presets]
        preset_names.insert(0, "Enabled Tests")  # Add "Enabled Tests" option
        self.preset_dropdown.configure(values=preset_names)
        self.selected_preset.set("Enabled Tests")
        logger.debug(f"Preset dropdown updated with values: {preset_names}")

    def toggle_dropdown(self):
        if self.dropdown_frame.winfo_ismapped():
            self.dropdown_frame.pack_forget()
        else:
            self.dropdown_frame.pack(side="top", fill="x", padx=10, pady=10)

    def select_option(self, option):
        self.selected_preset.set(option)
        self.preset_button.configure(text=option)
        self.dropdown_frame.pack_forget()

    # Method to print messages to the terminal
    def print_to_terminal(self, message):
        self.terminal_textbox.configure(state="normal")
        self.terminal_textbox.insert("end", message + "\n")
        self.terminal_textbox.configure(state="disabled")
        self.terminal_textbox.yview("end")

    # Add this method to create the tests tab widgets
    def create_tests_widgets(self):
        try:
            # Ensure background frame is always present for the Tests tab
            if not hasattr(self.tabs[2], 'background_frame'):
                self.tabs[2].background_frame = ctk.CTkFrame(self.tabs[2], fg_color="#2e2e2e", corner_radius=10)
                self.tabs[2].background_frame.pack(fill="both", expand=True, padx=10, pady=10)

            # Load current settings
            settings = load_settings()
            enabled_tests = settings.get("enabled_tests", [])

            # Create a frame for Computer tests
            computer_frame = ctk.CTkFrame(self.tabs[2].background_frame, fg_color="#2e2e2e", corner_radius=10)
            computer_frame.pack(side="top", fill="x", padx=10, pady=10)

            # Create a label for Computer tests title with background and rounded edges
            computer_label = ctk.CTkLabel(computer_frame, text="Computer", font=("Arial", 16, "bold"), fg_color="#3e3e3e", corner_radius=10)
            computer_label.pack(fill="x", pady=(10, 0), padx=10)

            # Create a frame for Computer test checkboxes
            computer_tests_frame = ctk.CTkFrame(computer_frame, fg_color="#2e2e2e")
            computer_tests_frame.pack(fill="x", padx=10, pady=10)

            # Create checkboxes for Computer tests
            self.computer_test1 = ctk.CTkCheckBox(computer_tests_frame, text="Disk Cleanup", fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, onvalue="Disk Cleanup", offvalue="", command=self.save_enabled_tests)
            self.computer_test1.pack(side="left", padx=10, pady=5)
            self.computer_test2 = ctk.CTkCheckBox(computer_tests_frame, text="Defragment Hard Drive", fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, onvalue="Defragment Hard Drive", offvalue="", command=self.save_enabled_tests)
            self.computer_test2.pack(side="left", padx=10, pady=5)
            self.computer_test3 = ctk.CTkCheckBox(computer_tests_frame, text="Check for System File Corruptions", fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, onvalue="Check for System File Corruptions", offvalue="", command=self.save_enabled_tests)
            self.computer_test3.pack(side="left", padx=10, pady=5)
            self.computer_test4 = ctk.CTkCheckBox(computer_tests_frame, text="Check Disk for Errors", fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, onvalue="Check Disk for Errors", offvalue="", command=self.save_enabled_tests)
            self.computer_test4.pack(side="left", padx=10, pady=5)
            self.computer_test5 = ctk.CTkCheckBox(computer_tests_frame, text="Clear Temporary Files", fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, onvalue="Clear Temporary Files", offvalue="", command=self.save_enabled_tests)
            self.computer_test5.pack(side="left", padx=10, pady=5)

            # Set initial state of checkboxes based on settings
            self.computer_test1.select() if "Disk Cleanup" in enabled_tests else self.computer_test1.deselect()
            self.computer_test2.select() if "Defragment Hard Drive" in enabled_tests else self.computer_test2.deselect()
            self.computer_test3.select() if "Check for System File Corruptions" in enabled_tests else self.computer_test3.deselect()
            self.computer_test4.select() if "Check Disk for Errors" in enabled_tests else self.computer_test4.deselect()
            self.computer_test5.select() if "Clear Temporary Files" in enabled_tests else self.computer_test5.deselect()

            # Create a frame for Network tests
            network_frame = ctk.CTkFrame(self.tabs[2].background_frame, fg_color="#2e2e2e", corner_radius=10)
            network_frame.pack(side="top", fill="x", padx=10, pady=10)

            # Create a label for Network tests title with background and rounded edges
            network_label = ctk.CTkLabel(network_frame, text="Network", font=("Arial", 16, "bold"), fg_color="#3e3e3e", corner_radius=10)
            network_label.pack(fill="x", pady=(10, 0), padx=10)

            # Create a frame for Network test checkboxes
            network_tests_frame = ctk.CTkFrame(network_frame, fg_color="#2e2e2e")
            network_tests_frame.pack(fill="x", padx=10, pady=10)

            # Create checkboxes for Network tests
            self.network_test1 = ctk.CTkCheckBox(network_tests_frame, text="Flush DNS Cache", fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, onvalue="Flush DNS Cache", offvalue="", command=self.save_enabled_tests)
            self.network_test1.pack(side="left", padx=10, pady=5)
            self.network_test2 = ctk.CTkCheckBox(network_tests_frame, text="Renew IP Address", fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, onvalue="Renew IP Address", offvalue="", command=self.save_enabled_tests)
            self.network_test2.pack(side="left", padx=10, pady=5)
            self.network_test3 = ctk.CTkCheckBox(network_tests_frame, text="Test Network Speed", fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, onvalue="Test Network Speed", offvalue="", command=self.save_enabled_tests)
            self.network_test3.pack(side="left", padx=10, pady=5)
            self.network_test4 = ctk.CTkCheckBox(network_tests_frame, text="Reset Network Settings", fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, onvalue="Reset Network Settings", offvalue="", command=self.save_enabled_tests)
            self.network_test4.pack(side="left", padx=10, pady=5)
            self.network_test5 = ctk.CTkCheckBox(network_tests_frame, text="Ping Test", fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, onvalue="Ping Test", offvalue="", command=self.save_enabled_tests)
            self.network_test5.pack(side="left", padx=10, pady=5)

            # Set initial state of checkboxes based on settings
            self.network_test1.select() if "Flush DNS Cache" in enabled_tests else self.network_test1.deselect()
            self.network_test2.select() if "Renew IP Address" in enabled_tests else self.network_test2.deselect()
            self.network_test3.select() if "Test Network Speed" in enabled_tests else self.network_test3.deselect()
            self.network_test4.select() if "Reset Network Settings" in enabled_tests else self.network_test4.deselect()
            self.network_test5.select() if "Ping Test" in enabled_tests else self.network_test5.deselect()

            # Create a frame for Miscellaneous tests
            misc_frame = ctk.CTkFrame(self.tabs[2].background_frame, fg_color="#2e2e2e", corner_radius=10)
            misc_frame.pack(side="top", fill="x", padx=10, pady=10)

            # Create a label for Miscellaneous tests title with background and rounded edges
            misc_label = ctk.CTkLabel(misc_frame, text="Miscellaneous", font=("Arial", 16, "bold"), fg_color="#3e3e3e", corner_radius=10)
            misc_label.pack(fill="x", pady=(10, 0), padx=10)

            # Create checkboxes for Miscellaneous tests
            self.misc_test1 = ctk.CTkCheckBox(misc_frame, text="Monitor Resource Usage", fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, onvalue="Monitor Resource Usage", offvalue="", command=self.save_enabled_tests)
            self.misc_test1.pack(fill="x", padx=10, pady=5)

            # Set initial state of checkboxes based on settings
            self.misc_test1.select() if "Monitor Resource Usage" in enabled_tests else self.misc_test1.deselect()

        except Exception as e:
            logger.error(f"Error creating tests widgets: {e}")

    def save_enabled_tests(self):
        enabled_tests = []
        if self.computer_test1.get() == "Disk Cleanup":
            enabled_tests.append("Disk Cleanup")
        if self.computer_test2.get() == "Defragment Hard Drive":
            enabled_tests.append("Defragment Hard Drive")
        if self.computer_test3.get() == "Check for System File Corruptions":
            enabled_tests.append("Check for System File Corruptions")
        if self.computer_test4.get() == "Check Disk for Errors":
            enabled_tests.append("Check Disk for Errors")
        if self.computer_test5.get() == "Clear Temporary Files":
            enabled_tests.append("Clear Temporary Files")
        if self.network_test1.get() == "Flush DNS Cache":
            enabled_tests.append("Flush DNS Cache")
        if self.network_test2.get() == "Renew IP Address":
            enabled_tests.append("Renew IP Address")
        if self.network_test3.get() == "Test Network Speed":
            enabled_tests.append("Test Network Speed")
        if self.network_test4.get() == "Reset Network Settings":
            enabled_tests.append("Reset Network Settings")
        if self.network_test5.get() == "Ping Test":
            enabled_tests.append("Ping Test")
        if self.misc_test1.get() == "Monitor Resource Usage":
            enabled_tests.append("Monitor Resource Usage")

        update_settings("enabled_tests", enabled_tests)
            
    def create_presets_widgets(self):
        try:
            # Ensure background frame is always present for the Presets tab
            if not hasattr(self.tabs[3], 'background_frame'):
                self.tabs[3].background_frame = ctk.CTkFrame(self.tabs[3], fg_color="#2e2e2e", corner_radius=10)
                self.tabs[3].background_frame.pack(fill="both", expand=True, padx=10, pady=10)

            # Load current settings
            settings = load_settings()
            custom_presets = settings.get("custom_presets", [])

            # Create a frame for Save Preset if it doesn't already exist
            if not hasattr(self, 'save_preset_frame'):
                self.save_preset_frame = ctk.CTkFrame(self.tabs[3].background_frame, fg_color="#2e2e2e", corner_radius=10, width=200)
                self.save_preset_frame.pack(side="left", fill="y", padx=10, pady=10)

                # Create a label for Save Preset title
                save_preset_label = ctk.CTkLabel(self.save_preset_frame, text="Save Preset", font=("Arial", 16, "bold"), fg_color="#3e3e3e", corner_radius=10)
                save_preset_label.pack(fill="x", pady=(10, 0), padx=10)

                # Create a button to open the naming window
                save_preset_button = ctk.CTkButton(self.save_preset_frame, text="Save", command=self.open_naming_window, fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10)
                save_preset_button.pack(pady=10, padx=10)

                # Create a label for Delete Preset title
                delete_preset_label = ctk.CTkLabel(self.save_preset_frame, text="Delete Preset", font=("Arial", 16, "bold"), fg_color="#3e3e3e", corner_radius=10)
                delete_preset_label.pack(fill="x", pady=(10, 0), padx=10)

                # Create a dropdown to select a preset to delete
                self.delete_preset_var = tk.StringVar(value="Select Preset")
                self.delete_preset_dropdown = ctk.CTkOptionMenu(self.save_preset_frame, variable=self.delete_preset_var, values=[preset["name"] for preset in custom_presets], fg_color="#3e3e3e", button_color="#5e5e5e", button_hover_color="#4e4e4e", corner_radius=10)
                self.delete_preset_dropdown.pack(pady=10, padx=10)

                # Create a button to delete the selected preset
                delete_preset_button = ctk.CTkButton(self.save_preset_frame, text="Delete", command=self.delete_preset, fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10)
                delete_preset_button.pack(pady=10, padx=10)

                # Create a label for View Preset Details title
                view_preset_label = ctk.CTkLabel(self.save_preset_frame, text="View Preset Details", font=("Arial", 16, "bold"), fg_color="#3e3e3e", corner_radius=10)
                view_preset_label.pack(fill="x", pady=(10, 0), padx=10)

                # Create a dropdown to select a preset to view details
                self.view_preset_var = tk.StringVar(value="Select Preset")
                self.view_preset_dropdown = ctk.CTkOptionMenu(self.save_preset_frame, variable=self.view_preset_var, values=[preset["name"] for preset in custom_presets], fg_color="#3e3e3e", button_color="#5e5e5e", button_hover_color="#4e4e4e", corner_radius=10, command=self.show_preset_details)
                self.view_preset_dropdown.pack(pady=10, padx=10)

                # Create a frame to display the preset details
                self.preset_details_frame = ctk.CTkFrame(self.save_preset_frame, fg_color="#3e3e3e", corner_radius=10)
                self.preset_details_frame.pack(fill="both", expand=True, padx=10, pady=10)

                # Add a scrollable text box for preset details
                self.preset_details_textbox = ctk.CTkTextbox(self.preset_details_frame, state="disabled", wrap="word")
                self.preset_details_textbox.pack(side="left", fill="both", expand=True, padx=(10, 10), pady=10)

            # Create a frame for Current Presets if it doesn't already exist
            if not hasattr(self, 'current_presets_frame'):
                self.current_presets_frame = ctk.CTkFrame(self.tabs[3].background_frame, fg_color="#2e2e2e", corner_radius=10, width=200)
                self.current_presets_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

                # Create a label for Current Presets title
                current_presets_label = ctk.CTkLabel(self.current_presets_frame, text="Current Presets", font=("Arial", 16, "bold"), fg_color="#3e3e3e", corner_radius=10)
                current_presets_label.pack(fill="x", pady=(10, 0), padx=10)

                # Create a vertical frame for Current Presets content
                self.current_presets_content_frame = ctk.CTkFrame(self.current_presets_frame, fg_color="#3e3e3e", corner_radius=10)
                self.current_presets_content_frame.pack(fill="both", expand=True, padx=10, pady=10)

            # Clear existing widgets in the current presets content frame
            for widget in self.current_presets_content_frame.winfo_children():
                widget.destroy()

            # Display current presets with the number of tests
            for preset in custom_presets:
                preset_name = preset.get("name", "Unnamed Preset")
                num_tests = len(preset.get("tests", []))
                preset_label = ctk.CTkLabel(self.current_presets_content_frame, text=f"{preset_name} ({num_tests} tests)", font=("Arial", 12), fg_color="#3e3e3e", corner_radius=10)
                preset_label.pack(fill="x", pady=5, padx=10)

            # Update dropdowns
            self.update_dropdowns()

        except Exception as e:
            logger.error(f"Error creating presets widgets: {e}")

    def open_naming_window(self):
        if self.naming_window is None or not self.naming_window.winfo_exists():
            self.naming_window = ctk.CTkToplevel(self)
            self.naming_window.title("Name Preset")
            self.naming_window.geometry("300x150")
            self.naming_window.attributes('-topmost', True)  # Ensure the window is always on top

            # Create a label for the text box
            name_label = ctk.CTkLabel(self.naming_window, text="Preset Name:", font=("Arial", 12))
            name_label.pack(pady=(10, 0), padx=10)

            # Create a text box for entering the preset name
            self.name_entry = ctk.CTkEntry(self.naming_window, width=250)
            self.name_entry.pack(pady=10, padx=10)

            # Create a button to save the preset name and close the window
            save_button = ctk.CTkButton(self.naming_window, text="Save", command=self.save_preset, fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10)
            save_button.pack(pady=10, padx=10)
        else:
            self.naming_window.lift()  # Bring the existing window to the front

    def update_dropdowns(self):
        settings = load_settings()
        custom_presets = settings.get("custom_presets", [])
        preset_names = [preset["name"] for preset in custom_presets]

        self.delete_preset_dropdown.configure(values=preset_names)
        self.view_preset_dropdown.configure(values=preset_names)
    
    def save_preset(self):
        preset_name = self.name_entry.get()
        if preset_name:
            settings = load_settings()
            custom_presets = settings.get("custom_presets", [])
            
            # Get the currently enabled tests
            enabled_tests = []
            if self.computer_test1.get() == "Disk Cleanup":
                enabled_tests.append("Disk Cleanup")
            if self.computer_test2.get() == "Defragment Hard Drive":
                enabled_tests.append("Defragment Hard Drive")
            if self.computer_test3.get() == "Check for System File Corruptions":
                enabled_tests.append("Check for System File Corruptions")
            if self.computer_test4.get() == "Check Disk for Errors":
                enabled_tests.append("Check Disk for Errors")
            if self.computer_test5.get() == "Clear Temporary Files":
                enabled_tests.append("Clear Temporary Files")
            if self.network_test1.get() == "Flush DNS Cache":
                enabled_tests.append("Flush DNS Cache")
            if self.network_test2.get() == "Renew IP Address":
                enabled_tests.append("Renew IP Address")
            if self.network_test3.get() == "Test Network Speed":
                enabled_tests.append("Test Network Speed")
            if self.network_test4.get() == "Reset Network Settings":
                enabled_tests.append("Reset Network Settings")
            if self.network_test5.get() == "Ping Test":
                enabled_tests.append("Ping Test")
            if self.misc_test1.get() == "Monitor Resource Usage":
                enabled_tests.append("Monitor Resource Usage")

            # Save the preset with the name and enabled tests
            custom_presets.append({"name": preset_name, "tests": enabled_tests})
            update_settings("custom_presets", custom_presets)
            self.naming_window.destroy()
            self.naming_window = None
            self.create_presets_widgets()  # Refresh the presets display
            self.update_scheduled_presets_dropdown()
            self.update_preset_dropdown()

    def delete_preset(self):
        preset_name = self.delete_preset_var.get()
        if preset_name and preset_name != "Select Preset":
            settings = load_settings()
            custom_presets = settings.get("custom_presets", [])
            scheduled_presets = settings.get("scheduled_presets", [])
            
            # Remove the custom preset
            custom_presets = [preset for preset in custom_presets if preset["name"] != preset_name]
            
            # Remove associated scheduled presets
            scheduled_presets = [preset for preset in scheduled_presets if preset["preset_name"] != preset_name]
            
            update_settings("custom_presets", custom_presets)
            update_settings("scheduled_presets", scheduled_presets)
            self.create_presets_widgets()  # Refresh the presets display
            self.create_scheduled_presets_widgets()  # Refresh the scheduled presets display
            self.update_scheduled_presets_dropdown()
            self.update_preset_dropdown()

    def show_preset_details(self, preset_name):
        if preset_name and preset_name != "Select Preset":
            settings = load_settings()
            custom_presets = settings.get("custom_presets", [])
            preset = next((preset for preset in custom_presets if preset["name"] == preset_name), None)
            if preset:
                # Clear existing text in the preset details textbox
                self.preset_details_textbox.configure(state="normal")
                self.preset_details_textbox.delete("1.0", "end")

                # Display the test names for the selected preset
                for test in preset.get("tests", []):
                    self.preset_details_textbox.insert("end", test + "\n")

                self.preset_details_textbox.configure(state="disabled")

    def close_naming_window(self):
        if self.naming_window is not None:
            self.naming_window.destroy()
            self.naming_window = None

    def create_scheduled_presets_widgets(self):
        try:
            # Ensure background frame is always present for the Scheduled Presets tab
            if not hasattr(self.tabs[4], 'background_frame'):
                self.tabs[4].background_frame = ctk.CTkFrame(self.tabs[4], fg_color="#2e2e2e", corner_radius=10)
                self.tabs[4].background_frame.pack(fill="both", expand=True, padx=10, pady=10)

            # Load current settings
            settings = load_settings()
            scheduled_presets = settings.get("scheduled_presets", [])
            custom_presets = settings.get("custom_presets", [])

            # Create a frame for Save Scheduled Preset if it doesn't already exist
            if not hasattr(self, 'save_scheduled_preset_frame'):
                self.save_scheduled_preset_frame = ctk.CTkFrame(self.tabs[4].background_frame, fg_color="#2e2e2e", corner_radius=10, width=200)
                self.save_scheduled_preset_frame.pack(side="left", fill="y", padx=10, pady=10)

                # Create a label for Save Scheduled Preset title
                save_scheduled_preset_label = ctk.CTkLabel(self.save_scheduled_preset_frame, text="Save Scheduled Preset", font=("Arial", 16, "bold"), fg_color="#3e3e3e", corner_radius=10)
                save_scheduled_preset_label.pack(fill="x", pady=(10, 0), padx=10)

                # Create a dropdown for selecting a preset to schedule
                self.selected_preset = tk.StringVar(value=custom_presets[0]["name"] if custom_presets else "")
                self.preset_dropdown = ctk.CTkOptionMenu(
                    self.save_scheduled_preset_frame, 
                    variable=self.selected_preset, 
                    values=[preset["name"] for preset in custom_presets], 
                    fg_color="#3e3e3e", 
                    button_color="#5e5e5e", 
                    button_hover_color="#4e4e4e", 
                    corner_radius=10, 
                    width=200
                )
                self.preset_dropdown.pack(pady=10, padx=10)

                # Create a dropdown for selecting time frequency
                time_frequency_options = ["Daily", "Weekly", "Monthly"]
                self.selected_time_frequency = tk.StringVar(value=time_frequency_options[0])
                time_frequency_dropdown = ctk.CTkOptionMenu(
                    self.save_scheduled_preset_frame, 
                    variable=self.selected_time_frequency, 
                    values=time_frequency_options, 
                    fg_color="#3e3e3e", 
                    button_color="#5e5e5e", 
                    button_hover_color="#4e4e4e", 
                    corner_radius=10, 
                    width=200
                )
                time_frequency_dropdown.pack(pady=10, padx=10)

                # Create a frame for hours and minutes entry
                time_entry_frame = ctk.CTkFrame(self.save_scheduled_preset_frame, fg_color="#2e2e2e", corner_radius=10)
                time_entry_frame.pack(fill="x", padx=10, pady=10)

                # Create text boxes for hours and minutes
                hours_label = ctk.CTkLabel(time_entry_frame, text="Hours:", font=("Arial", 12), fg_color="#3e3e3e", corner_radius=10)
                hours_label.pack(side="left", padx=(0, 5))
                self.hours_entry = ctk.CTkEntry(time_entry_frame, width=90)
                self.hours_entry.pack(side="left", padx=(0, 10))
                self.hours_entry.configure(validate="key", validatecommand=(self.register(self.validate_hours), '%P'))

                minutes_label = ctk.CTkLabel(time_entry_frame, text="Minutes:", font=("Arial", 12), fg_color="#3e3e3e", corner_radius=10)
                minutes_label.pack(side="left", padx=(10, 5))
                self.minutes_entry = ctk.CTkEntry(time_entry_frame, width=90)
                self.minutes_entry.pack(side="left", padx=(0, 10))
                self.minutes_entry.configure(validate="key", validatecommand=(self.register(self.validate_minutes), '%P'))

                # Create a checkbox for saving a summary
                save_summary_checkbox = ctk.CTkCheckBox(self.save_scheduled_preset_frame, text="Save Summary", fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10)
                save_summary_checkbox.pack(pady=10, padx=10)

                # Create a button to save the scheduled preset
                save_scheduled_preset_button = ctk.CTkButton(self.save_scheduled_preset_frame, text="Save", command=self.save_scheduled_preset, fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, width=200)
                save_scheduled_preset_button.pack(pady=10, padx=10)

                # Create a label for Delete Scheduled Preset title
                delete_scheduled_preset_label = ctk.CTkLabel(self.save_scheduled_preset_frame, text="Delete Scheduled Preset", font=("Arial", 16, "bold"), fg_color="#3e3e3e", corner_radius=10)
                delete_scheduled_preset_label.pack(fill="x", pady=(10, 0), padx=10)

                # Create a dropdown to select a scheduled preset to delete
                self.delete_scheduled_preset_var = tk.StringVar(value="Select Scheduled Preset")
                self.delete_scheduled_preset_dropdown = ctk.CTkOptionMenu(self.save_scheduled_preset_frame, variable=self.delete_scheduled_preset_var, values=[f"{preset['preset_name']} - {preset['frequency']} at {preset['hours']}:{preset['minutes']}" for preset in scheduled_presets], fg_color="#3e3e3e", button_color="#5e5e5e", button_hover_color="#4e4e4e", corner_radius=10, width=200)
                self.delete_scheduled_preset_dropdown.pack(pady=10, padx=10)

                # Create a button to delete the selected scheduled preset
                delete_scheduled_preset_button = ctk.CTkButton(self.save_scheduled_preset_frame, text="Delete", command=self.delete_scheduled_preset, fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, width=200)
                delete_scheduled_preset_button.pack(pady=10, padx=10)

            # Create a frame for Scheduled Presets if it doesn't already exist
            if not hasattr(self, 'scheduled_presets_frame'):
                self.scheduled_presets_frame = ctk.CTkFrame(self.tabs[4].background_frame, fg_color="#2e2e2e", corner_radius=10, width=200)
                self.scheduled_presets_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

                # Create a label for Scheduled Presets title
                scheduled_presets_label = ctk.CTkLabel(self.scheduled_presets_frame, text="Scheduled Presets", font=("Arial", 16, "bold"), fg_color="#3e3e3e", corner_radius=10)
                scheduled_presets_label.pack(fill="x", pady=(10, 0), padx=10)

                # Create a vertical frame for Scheduled Presets content
                self.scheduled_presets_content_frame = ctk.CTkFrame(self.scheduled_presets_frame, fg_color="#3e3e3e", corner_radius=10)
                self.scheduled_presets_content_frame.pack(fill="both", expand=True, padx=10, pady=10)

            # Clear existing widgets in the scheduled presets content frame
            for widget in self.scheduled_presets_content_frame.winfo_children():
                widget.destroy()

            # Display scheduled presets
            for scheduled_preset in scheduled_presets:
                preset_name = scheduled_preset.get("preset_name", "Unnamed Preset")
                frequency = scheduled_preset.get("frequency", "Unknown Frequency")
                time = f"{scheduled_preset.get('hours', '00')}:{scheduled_preset.get('minutes', '00')}"
                scheduled_preset_label = ctk.CTkLabel(self.scheduled_presets_content_frame, text=f"{preset_name} - {frequency} at {time}", font=("Arial", 12), fg_color="#3e3e3e", corner_radius=10)
                scheduled_preset_label.pack(fill="x", pady=5, padx=10)

            # Update dropdowns
            self.update_scheduled_presets_dropdown()

        except Exception as e:
            logger.error(f"Error creating scheduled presets widgets: {e}")

    def update_scheduled_presets_dropdown(self):
        settings = load_settings()
        custom_presets = settings.get("custom_presets", [])
        scheduled_presets = settings.get("scheduled_presets", [])
        preset_names = [preset["name"] for preset in custom_presets]
        scheduled_preset_names = [f"{preset['preset_name']} - {preset['frequency']} at {preset['hours']}:{preset['minutes']}" for preset in scheduled_presets]

        self.preset_dropdown.configure(values=preset_names)
        self.delete_scheduled_preset_dropdown.configure(values=scheduled_preset_names)

    def save_scheduled_preset(self):
        preset_name = self.selected_preset.get()
        frequency = self.selected_time_frequency.get()
        hours = self.hours_entry.get()
        minutes = self.minutes_entry.get()

        if preset_name and frequency and hours.isdigit() and minutes.isdigit():
            settings = load_settings()
            scheduled_presets = settings.get("scheduled_presets", [])
            
            # Save the scheduled preset
            scheduled_presets.append({
                "preset_name": preset_name,
                "frequency": frequency,
                "hours": hours,
                "minutes": minutes
            })
            update_settings("scheduled_presets", scheduled_presets)
            self.update_scheduled_presets_dropdown()  # Update the dropdowns immediately
            self.create_scheduled_presets_widgets()  # Refresh the scheduled presets display

    def delete_scheduled_preset(self):
        scheduled_preset_name = self.delete_scheduled_preset_var.get()
        if scheduled_preset_name and scheduled_preset_name != "Select Scheduled Preset":
            settings = load_settings()
            scheduled_presets = settings.get("scheduled_presets", [])
            scheduled_presets = [preset for preset in scheduled_presets if f"{preset['preset_name']} - {preset['frequency']} at {preset['hours']}:{preset['minutes']}" != scheduled_preset_name]
            update_settings("scheduled_presets", scheduled_presets)
            self.update_scheduled_presets_dropdown()  # Update the dropdowns immediately
            self.create_scheduled_presets_widgets()  # Refresh the scheduled presets display

    def validate_hours(self, value_if_allowed):
        if value_if_allowed.isdigit() and 0 <= int(value_if_allowed) <= 24:
            return True
        elif value_if_allowed == "":
            return True
        else:
            return False

    def validate_minutes(self, value_if_allowed):
        if value_if_allowed.isdigit() and 0 <= int(value_if_allowed) <= 59:
            return True
        elif value_if_allowed == "":
            return True
        else:
            return False

    # Add this method to create the settings tab widgets
    def create_settings_widgets(self):
        try:
            # Ensure background frame is always present for the Settings tab
            if not hasattr(self.tabs[5], 'background_frame'):
                self.tabs[5].background_frame = ctk.CTkFrame(self.tabs[5], fg_color="#2e2e2e", corner_radius=10)
                self.tabs[5].background_frame.pack(fill="both", expand=True, padx=10, pady=10)

            # Load current settings
            settings = load_settings()
            logging_level = settings.get("settings", {}).get("logging_level", "DEBUG")
            save_logs = settings.get("settings", {}).get("save_logs", False)
            save_summaries = settings.get("settings", {}).get("save_summaries", False)

            # Create a frame for Logging Level
            logging_level_frame = ctk.CTkFrame(self.tabs[5].background_frame, fg_color="#2e2e2e", corner_radius=10)
            logging_level_frame.pack(side="top", fill="x", padx=10, pady=10)

            # Create a label for Logging Level title
            logging_level_label = ctk.CTkLabel(logging_level_frame, text="Logging Level", font=("Arial", 16, "bold"), fg_color="#3e3e3e", corner_radius=10)
            logging_level_label.pack(fill="x", pady=(10, 0), padx=10)

            # Create a slider for selecting logging level
            self.logging_level_slider = ctk.CTkSlider(logging_level_frame, from_=0, to=4, number_of_steps=4, command=self.update_logging_level)
            self.logging_level_slider.pack(fill="x", padx=10, pady=10)

            # Set the initial value of the slider based on the loaded settings
            levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
            self.logging_level_slider.set(levels.index(logging_level))

            # Create a label to display the current logging level
            self.logging_level_display = ctk.CTkLabel(logging_level_frame, text=logging_level, font=("Arial", 12), fg_color="#3e3e3e", corner_radius=10)
            self.logging_level_display.pack(fill="x", padx=10, pady=10)

            # Create a checkbox for enabling saved logs
            self.enable_saved_logs_checkbox = ctk.CTkCheckBox(self.tabs[5].background_frame, text="Enable Saved Logs", fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, command=self.toggle_save_logs)
            self.enable_saved_logs_checkbox.pack(pady=10, padx=10)
            self.enable_saved_logs_checkbox.select() if save_logs else self.enable_saved_logs_checkbox.deselect()

            # Create a checkbox for saving summaries
            self.enable_save_summary_checkbox = ctk.CTkCheckBox(self.tabs[5].background_frame, text="Enable Save Summary", fg_color="#5e5e5e", hover_color="#4e4e4e", corner_radius=10, command=self.toggle_save_summaries)
            self.enable_save_summary_checkbox.pack(pady=10, padx=10)
            self.enable_save_summary_checkbox.select() if save_summaries else self.enable_save_summary_checkbox.deselect()

        except Exception as e:
            logger.error(f"Error creating settings widgets: {e}")

    def update_logging_level(self, value):
        levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        level = levels[int(value)]
        self.logging_level_display.configure(text=level)
        logger.setLevel(getattr(logging, level))
        update_settings("settings.logging_level", level)

    def toggle_save_logs(self):
        save_logs = self.enable_saved_logs_checkbox.get()
        update_settings("settings.save_logs", save_logs)

    def toggle_save_summaries(self):
        save_summaries = self.enable_save_summary_checkbox.get()
        update_settings("settings.save_summaries", save_summaries)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
