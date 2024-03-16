import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import Entry, Label, Button, RAISED  # Import RAISED for relief style
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from PIL import Image, ImageTk

# Read the CSV file
df = pd.read_csv('real estate pre project.csv')
df1 = df.copy()
df1['price_per_sqft'] = df1['price'] / df1['area']

# Create the linear regression model
X = df1.drop('price', axis='columns')
y = df1.price
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
lr_clf = LinearRegression()
lr_clf.fit(X_train, y_train)

# Set up the Tkinter window
window = tk.Tk()
window.title("Real Estate Price Predictor")
window.geometry("800x600")  # Adjust the window size

# Load and resize the background image
bg_image = Image.open("proj.jpg")  # Change to your image file
bg_image = bg_image.resize((1400,800), Image.LANCZOS)  # Adjust the size as needed
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a background label for the image
background_label = tk.Label(window, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the input fields with labels
area_label = Label(window, text="Area (sqft):", bg='white')
area_label.place(x=100, y=200)
area_entry = Entry(window)
area_entry.place(x=250, y=200)

stories_label = Label(window, text="Number of Stories:", bg='white')
stories_label.place(x=100, y=250)
stories_entry = Entry(window)
stories_entry.place(x=250, y=250)

bedrooms_label = Label(window, text="Number of Bedrooms:", bg='white')
bedrooms_label.place(x=100, y=300)
bedrooms_entry = Entry(window)
bedrooms_entry.place(x=250, y=300)

# Function to predict the price and display it
def predict_price():
    area = float(area_entry.get())
    stories = float(stories_entry.get())
    bedrooms = float(bedrooms_entry.get())
    loc_index = np.where(X.columns == 'mainroad')[0][0]
    x = np.zeros(len(X.columns))
    x[0] = area
    x[1] = stories
    x[2] = bedrooms
    if loc_index >= 0:
        x[loc_index] = 1
    predicted_price = lr_clf.predict([x])[0]
    result_label.config(text="Predicted Price: $%.2f" % predicted_price)

# Button to trigger the prediction with "raised" relief style
predict_button = Button(window, text="Predict", command=predict_price, bg='white', relief=RAISED)
predict_button.place(x=300, y=350)

# Label to display the predicted price
result_label = Label(window, text="", bg='white')
result_label.place(x=300, y=400)

# Start the Tkinter event loop
window.mainloop()

