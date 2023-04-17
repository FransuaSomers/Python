import tkinter as tk
from datetime import datetime

class CoffeeRatingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Coffee Rating System")
        self.master.configure(bg='#E5E5E5')
        self.fields = []
        self.average_label = None  # Initialize the average label to None
        self.add_field_button = tk.Button(self.master, text="+", bg='#007AFF', fg='#FFFFFF', font=('Impact', 14, 'bold'), command=self.add_field)
        self.calculate_button = tk.Button(self.master, text="Calculate Average", bg='#007AFF', fg='#FFFFFF', font=('Impact', 14, 'bold'), command=self.calculate_average)
        self.show_ratings_button = tk.Button(self.master, text="Show Ratings", bg='#007AFF', fg='#FFFFFF', font=('Impact', 14, 'bold'), command=self.show_ratings)
        self.add_field_button.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)
        self.calculate_button.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)
        self.add_field()
        self.add_field()
        self.show_ratings_button.pack(side=tk.BOTTOM, padx=10, pady=10, fill=tk.X)

    def add_field(self):
        if len(self.fields) >= 10:
            return
        field = tk.Entry(self.master, validate="key", font=('Impact', 14))
        field.config(validatecommand=(field.register(self.validate_field), '%P'))
        field.pack(side=tk.TOP, padx=10, pady=5, fill=tk.X)
        self.fields.append(field)
        if self.average_label:
            self.average_label.pack_forget()
        self.add_field_button.pack_forget()
        self.add_field_button.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)
        if self.average_label:
            self.average_label.pack_forget()
        self.calculate_button.pack_forget()
        self.calculate_button.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)
        self.calculate_average()


    def validate_field(self, value):
        if not value:
            return True
        try:
            val = float(value)
            return 1 <= val <= 10
        except ValueError:
            return False

    def calculate_average(self):
        values = []
        for field in self.fields:
            if field.get():
                values.append(float(field.get()))
        if len(values) < 2:
            return
        average = sum(values) / len(values)
        if self.average_label:
            self.average_label.destroy()
        self.average_label = tk.Label(self.master, text="Average: {:.2f}".format(average), bg='#E5E5E5', fg='#333333', font=('Impact', 14))
        self.average_label.pack(side=tk.TOP, padx=10, pady=10)
        self.write_to_file(average)

    def show_ratings(self):
        with open("coffee_ratings.txt", "r") as f:
            ratings = f.readlines()

        # Create a new window to display the ratings
        ratings_window = tk.Toplevel(self.master)
        ratings_window.title("Coffee Ratings")
        ratings_window.configure(bg='#E5E5E5')

        # Create a text box to display the ratings
        ratings_text = tk.Text(ratings_window, font=('Impact', 14), bg='#FFFFFF', fg='#333333')
        ratings_text.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Display the ratings in the text box
        for rating in ratings:
            ratings_text.insert(tk.END, rating)

        # Create a button to close the window
        close_button = tk.Button(ratings_window, text="Close", bg='#007AFF', fg='#FFFFFF', font=('Impact', 14, 'bold'), command=ratings_window.destroy)
        close_button.pack(side=tk.BOTTOM, padx=10, pady=10, fill=tk.X)

        
    def write_to_file(self, average):
        with open("coffee_ratings.txt", "a") as f:
            f.write("{} - {}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "{:.2f}".format(average)))
    
root = tk.Tk()
app = CoffeeRatingApp(root)
root.mainloop()
