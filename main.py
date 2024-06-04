import customtkinter as ctk
from tkinter import messagebox, Listbox, END

class TemperatureConverter:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.window = ctk.CTk()
        self.window.title("Temperature Converter")
        self.window.geometry("450x550")
        self.window.resizable(False, False)
        self.window.configure(bg="yellow")  # Set the background color to yellow

        self.create_widgets()
        self.history = []

    def create_widgets(self):
        #judul
        title_label = ctk.CTkLabel(self.window, text="Temperature Converter", font=ctk.CTkFont(size=16, weight="bold"))
        title_label.pack(pady=10)

        frame = ctk.CTkFrame(self.window)
        frame.pack(pady=10)

        #input suhu
        self.entry_temp = ctk.CTkEntry(frame, width=200)
        self.entry_temp.grid(row=0, column=1, padx=5)

        label_temp = ctk.CTkLabel(frame, text="Temperature:")
        label_temp.grid(row=0, column=0, padx=5)

        #tombol clear temperatur
        clear_temp_button = ctk.CTkButton(frame, text="Clear", command=self.clear_temperature)
        clear_temp_button.grid(row=0, column=2, padx=5)

        #drop down satuan suhu 
        self.units = ['Celsius', 'Fahrenheit', 'Kelvin']
        self.from_var = ctk.StringVar(value=self.units[0])
        self.to_var = ctk.StringVar(value=self.units[1])

        #from
        label_from = ctk.CTkLabel(frame, text="From:")
        label_from.grid(row=1, column=0, padx=5)

        self.combo_from = ctk.CTkComboBox(frame, variable=self.from_var, values=self.units)
        self.combo_from.grid(row=1, column=1, padx=5)

        #to
        label_to = ctk.CTkLabel(frame, text="To:")
        label_to.grid(row=2, column=0, padx=5)

        self.combo_to = ctk.CTkComboBox(frame, variable=self.to_var, values=self.units)
        self.combo_to.grid(row=2, column=1, padx=5)

        #tombol koneversi
        convert_button = ctk.CTkButton(self.window, text="Convert", command=self.convert_temperature)
        convert_button.pack(pady=10)

        #text hasil
        self.label_result = ctk.CTkLabel(self.window, text="Result: ", font=ctk.CTkFont(size=14))
        self.label_result.pack(pady=10)

        #text history
        history_label = ctk.CTkLabel(self.window, text="Conversion History", font=ctk.CTkFont(size=14))
        history_label.pack(pady=10)
        
        #listbox history
        self.history_listbox = Listbox(self.window, width=50, height=10)
        self.history_listbox.pack(pady=10)


        clear_button = ctk.CTkButton(self.window, text="Clear History", command=self.clear_history)
        clear_button.pack(pady=5)

    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def celsius_to_kelvin(self, celsius):
        return celsius + 273.15

    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def fahrenheit_to_kelvin(self, fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15

    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15

    def kelvin_to_fahrenheit(self, kelvin):
        return (kelvin - 273.15) * 9/5 + 32

    def convert_temperature(self):
        try:
            temp = float(self.entry_temp.get())
            from_unit = self.from_var.get()
            to_unit = self.to_var.get()
            
            if from_unit == 'Kelvin' and temp < 0:
                raise ValueError("Kelvin temperature cannot be negative")

            if from_unit == to_unit:
                result = temp
            elif from_unit == 'Celsius':
                if to_unit == 'Fahrenheit':
                    result = self.celsius_to_fahrenheit(temp)
                elif to_unit == 'Kelvin':
                    result = self.celsius_to_kelvin(temp)
            elif from_unit == 'Fahrenheit':
                if to_unit == 'Celsius':
                    result = self.fahrenheit_to_celsius(temp)
                elif to_unit == 'Kelvin':
                    result = self.fahrenheit_to_kelvin(temp)
            elif from_unit == 'Kelvin':
                if to_unit == 'Celsius':
                    result = self.kelvin_to_celsius(temp)
                elif to_unit == 'Fahrenheit':
                    result = self.kelvin_to_fahrenheit(temp)
            
            self.label_result.configure(text=f"Result: {result:.2f} {to_unit}")
            self.add_to_history(temp, from_unit, result, to_unit)
        except ValueError as e:
           messagebox.showerror("Invalid input", str(e))
           self.label_result.configure(text="Error: Invalid input")

    def add_to_history(self, original_temp, from_unit, converted_temp, to_unit):
         history_entry = f"{original_temp:.2f} {from_unit} -> {converted_temp:.2f} {to_unit}"
         self.history.append(history_entry)
         self.history_listbox.insert(END, history_entry)
    
    def clear_temperature(self):
        self.entry_temp.delete(0, END)


    def clear_history(self):
        self.history.clear()
        self.history_listbox.delete(0, END)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = TemperatureConverter()
    app.run()
    
