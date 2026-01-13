import streamlit as st
import random

# 1. PERSISTENT STORAGE (The "Memory")
if "expense_history" not in st.session_state:
    st.session_state.expense_history = []
if "tip_index" not in st.session_state:
    st.session_state.tip_index = 0

# 2. PAGE SETTINGS
st.set_page_config(page_title="Expense Tracker Pro", page_icon="📈", layout="wide")

# 3. CATEGORY LIST (200 Options)
categories = [
    "Rent", "Groceries", "Dining", "Utilities", "Transport", "Shopping", 
    "Health", "Insurance", "Entertainment", "Education", "Gift", "Travel"
] + [f"Business Category {i}" for i in range(1, 189)]

# 4. DATE FORMATTING LOGIC
def auto_format_date():
    raw = st.session_state.date_in.replace("/", "")
    if len(raw) >= 4:
        st.session_state.date_in = f"{raw[:2]}/{raw[2:4]}/{raw[4:8]}"

# --- APPLICATION UI ---
st.title("📈 Personal Expense Tracker")
st.write("Enter your expenses below to build your log.")

# Input Area
with st.container():
    c1, c2 = st.columns(2)
    with c1:
        date = st.text_input("Date (DDMMYYYY)", key="date_in", on_change=auto_format_date, placeholder="DD/MM/YYYY")
        if len(date) == 10: st.markdown("<span style='color:green'>✔️ Field Ready</span>", unsafe_allow_html=True)
        
        desc = st.text_input("Description", placeholder="e.g., Weekly Groceries")
        if desc: st.markdown("<span style='color:green'>✔️ Field Ready</span>", unsafe_allow_html=True)
        
    with c2:
        cat = st.selectbox("Search Category", options=categories)
        amt = st.number_input("Amount ($)", min_value=0.0, step=0.01)
        if amt > 0: st.markdown("<span style='color:green'>✔️ Field Ready</span>", unsafe_allow_html=True)

    # ADD BUTTON
    if st.button("➕ Save Expense", use_container_width=True):
        if date and desc and amt > 0:
            st.session_state.expense_history.append({"Date": date, "Description": desc, "Category": cat, "Amount": amt})
            st.toast("Expense added to log")
            # Rotate tip automatically on button click
            st.session_state.tip_index = (st.session_state.tip_index + 1) % 20
        else:
            st.error("Please complete all fields.")

st.divider()

# 5. DATA LOG (The "Storage" View)
if st.session_state.expense_history:
    st.subheader(f"📋 Expense Log ({len(st.session_state.expense_history)} items)")
    st.dataframe(st.session_state.expense_history, use_container_width=True)
else:
    st.info("Your log is currently empty.")

# 6. FINANCIAL WISDOM SECTION
st.divider()
tips = [
    "Save 20% of your income monthly.", "Avoid impulse purchases.", "Track every expense.",
    "Build a 3-month emergency fund.", "Invest in low-cost index funds.", "Minimize high-interest debt.",
    "Review your bank statements weekly.", "Automate your savings.", "Buy quality over quantity.",
    "Negotiate your recurring bills.", "Set clear financial goals.", "Avoid lifestyle inflation.",
    "Budget for fun to avoid burnout.", "Keep business and personal funds separate.",
    "Plan for big purchases in advance.", "Diversify your income streams.", "Understand your net worth.",
    "Prioritize high-interest debt.", "Stay consistent with your tracker.", "Invest in your financial education."
]

t_col1, t_col2 = st.columns([0.9, 0.1])
with t_col1:
    st.subheader("💡 Financial Wisdom")
with t_col2:
    if st.button("➡️"):
        st.session_state.tip_index = (st.session_state.tip_index + 1) % len(tips)

# Professional Wisdom Display
st.markdown(f"""
    <div style="background-color: #f8fff9; padding: 40px; border-radius: 15px; border: 1px solid #dcf5dc; text-align: center;">
        <p style="font-size: 26px; color: #1b5e20; font-family: sans-serif;">{tips[st.session_state.tip_index]}</p>
    </div>
    """, unsafe_allow_html=True)