# Import necessary packages
import pandas as pd
import numpy as np

# Import CSV for prices
airbnb_price = pd.read_csv('data/airbnb_price.csv')

# Import Excel file for room types
airbnb_room_type = pd.read_excel('data/airbnb_room_type.xlsx')

# Import TSV for review dates
airbnb_last_review = pd.read_csv('data/airbnb_last_review.tsv', sep='\t')

# Join the three data frames together into one
listings = pd.merge(airbnb_price, airbnb_room_type, on='listing_id')
listings = pd.merge(listings, airbnb_last_review, on='listing_id')

# Convert last_review to datetime
listings['last_review_date'] = pd.to_datetime(listings['last_review'], format='%B %d %Y')

# Find earliest and most recent review dates
first_reviewed = listings['last_review_date'].min()
last_reviewed = listings['last_review_date'].max()

# Count private rooms
# Make capitalization consistent
listings['room_type'] = listings['room_type'].str.lower()
nb_private_rooms = listings[listings['room_type'] == 'private room'].shape[0]

# Calculate average price
# Remove " dollars" and convert to float
listings['price_clean'] = listings['price'].str.replace(' dollars', '').astype(float)
avg_price = listings['price_clean'].mean()

# Create the review_dates DataFrame
review_dates = pd.DataFrame({
    'first_reviewed': [first_reviewed],
    'last_reviewed': [last_reviewed],
    'nb_private_rooms': [nb_private_rooms],
    'avg_price': [round(avg_price, 2)]
})

print(review_dates)