import random
import streamlit as st

# 1. Page Configuration & Header
st.set_page_config(page_title="WealthWise Tracker", page_icon="💰")
st.title("💰 WealthWise: Personal Expense Tracker")
st.markdown("---")

# 2. Input Section in Sidebar for a cleaner look
with st.sidebar:
    st.header("➕ Add Expense")
    Date = st.text_input("Enter the Date (YYYY/MM/DD): ")
    Description = st.text_input("Enter the Description: ")
    Category = st.text_input("Enter the Category: ")
    # Using a number input to avoid errors with non-numeric text
    Amount = st.number_input("Enter the Amount: ", min_value=0.0)

# Creating the list for storing expenses
expenses = [
    {"date": Date, "description": Description, "category": Category, "amount": Amount}
]

# 3. Main Dashboard: Summarization and Metrics
col1, col2 = st.columns(2)
def summarize(Date, Category, Amount):
    return "Summary: On {}, you spent ${:.2f} on {}.".format(Date, Amount, Category)

with col1:
    st.metric(label="Last Spent", value=f"${Amount:.2f}")
with col2:
    st.metric(label="Category", value=Category)

st.info(summarize(Date, Category, Amount))
st.divider()

# 4. Filtering Logic
def filter(expenses, date=None, category=None):
    filtered = []
    for expense in expenses:
        if (not date or expense["date"] == date) and (not category or expense['category'].lower() == category.lower()):
            filtered.append(expense)
    return filtered

st.subheader("🔍 Filter Your Expenses")
f_col1, f_col2 = st.columns(2)
with f_col1:
    date_f = st.text_input("Filter by Date: ").strip()
with f_col2:
    cat_f = st.text_input("Filter by Category: ").strip()

filtered_results = filter(expenses, date=date_f if date_f else None, category=cat_f if cat_f else None)

if filtered_results:
    # Using st.dataframe makes it look like a professional table
    st.dataframe(filtered_results, use_container_width=True)
else :
    st.write("No Expenses found! ")

# 5. Categorized Financial Tips at the very tail bottom
st.divider()
st.subheader("💡 Financial Wisdom")

tips_data = {
    "Savings 🏦": [
        "Save at least 20% of your income every month.",
        "Set up automatic transfers to your savings account.",
        "Create an emergency fund for 3 months of living expenses.",
        "Review subscriptions and cancel unused ones.",
        "Shop around for the best deals on services."
    ],
    "Budgeting 📊": [
        "Create a monthly budget and stick to it.",
        "Always track your spending to avoid surprises.",
        "Use cash for discretionary spending to avoid overspending.",
        "Avoid lifestyle inflation as your income increases.",
        "Plan for holidays or special events in advance."
    ],
    "Investing & Debt 📈": [
        "Pay off high-interest debts as soon as possible.",
        "Invest early to take advantage of compound interest.",
        "Diversify your investment portfolio to reduce risk.",
        "Set specific short-term and long-term financial goals.",
        "Plan for retirement as early as possible."
    ]
}

with st.expander("Explore Financial Tips by Category"):
    tab1, tab2, tab3 = st.tabs(["Savings", "Budgeting", "Investing"])
    
    with tab1:
        for tip in tips_data["Savings 🏦"]:
            st.info(tip)
            
    with tab2:
        for tip in tips_data["Budgeting 📊"]:
            st.success(tip)
            
    with tab3:
        for tip in tips_data["Investing & Debt 📈"]:
            st.warning(tip)

# The final "Tip of the Day"
st.markdown("---")
all_tips = [tip for sublist in tips_data.values() for tip in sublist]
st.chat_message("assistant").write(f"**Random Tip of the Day:** {random.choice(all_tips)}")