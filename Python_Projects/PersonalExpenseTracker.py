# Personal Expense Tracker

# importing random and streamlit 
import random
import streamlit as st

# Expense
Date = st.text_input("Enter the Date : ")
Description = st.text_input("Enter the Description : ")
Category = st.text_input("Enter the Category : ")
Amount = float(st.text_input("Enter the Amount : "))

# Creating a Dictionary for storing all the expenses done by user
expenses = [
    {"date": Date, "description": Description, "category": Category, "amount": Amount}
]

# now to show all these inputs, using print function to display them all.
st.button(Date)
st.button(Description)
st.button(Category)
st.button(Amount)

# Creating a function that prints the summarization
def summarize(Date, Category, Amount):
    return "Summary: On {}, you spent ${:.2f} on {}.".format(Date, Amount, Category)

Summarization = summarize(Date, Category, Amount)
st.write(Summarization)

# now to filter the expenses by date and category we use
def filter(expenses, date=None, category=None):
    filtered = []
    for expense in expenses:
        if (not date or expense["date"] == date) and (not category or expense['category'].lower() == category.lower()):
            filtered.append(expense)
    return filtered

# Now asking user for filtered options
st.write('Filter Your Expenses : ')
date = st.text_input("To use filter, Please Enter The Date in (YYYY/MM/DD) format or Press Enter Key to Skip : ").strip()
category = st.text_input("To use filter, Enter the category to filter or press Enter Key to skip : ").strip()

# Filtering the user expenses according to their input
filtered_results = filter(expenses, date=date if date else None, category=category if category else None)

# Now Printing the results
st.write ("Filtered Expenses : ")
if filtered_results:
    for expense in filtered_results:
        st.write("Date : " + expense["date"] + ", Description : " + expense["description"] + ", Category : " + expense["category"] + ", Amount : $" + '{:.2f}'.format(expense["amount"]))
else :
    st.write("No Expenses found! ")


# Adding a list and a function for showing 3 financial tips to the user.

# List of financial tips
financial_tips = [
    "1. Create a monthly budget and stick to it.",
    "2. Always track your spending to avoid surprises.",
    "3. Save at least 20% of your income every month.",
    "4. Use cash for discretionary spending to avoid overspending.",
    "5. Pay off high-interest debts as soon as possible.",
    "6. Set up automatic transfers to your savings account.",
    "7. Create an emergency fund to cover at least 3 months of living expenses.",
    "8. Don't buy things on impulse - always think before purchasing.",
    "9. Review your subscriptions and cancel the ones you don't use.",
    "10. Avoid lifestyle inflation - try to maintain your standard of living even when your income increases.",
    "11. Invest early to take advantage of compound interest.",
    "12. Diversify your investment portfolio to reduce risk.",
    "13. Set specific financial goals, both short-term and long-term.",
    "14. Use a financial app to help track your spending and investments.",
    "15. Avoid taking loans for non-essential items.",
    "16. Plan for retirement as early as possible.",
    "17. Avoid paying for unnecessary insurance coverage.",
    "18. Shop around for the best deals on services and products.",
    "19. Set aside money for holidays or special events in advance.",
    "20. Avoid co-signing loans for others to protect your credit."
]

# Function to give 3 random tips about finance to the user.
def get_random_tips(tips):
    return random.sample(tips, 3)
