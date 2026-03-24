import streamlit as st
from hello import Bank

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NeoBank",
    page_icon="💳",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Root & body ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* ── Hide default Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }

/* ── Dark background ── */
.stApp {
    background: #0a0a0f;
    color: #e8e8f0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #0f0f1a !important;
    border-right: 1px solid #1e1e35;
}
[data-testid="stSidebar"] .stSelectbox label {
    color: #7b7b9a !important;
    font-size: 0.7rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}

/* ── Hero header ── */
.hero {
    text-align: center;
    padding: 2.5rem 0 1.5rem;
}
.hero-tag {
    display: inline-block;
    background: linear-gradient(135deg, #6c63ff22, #00d4aa22);
    border: 1px solid #6c63ff44;
    color: #a09fff;
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    padding: 0.3rem 1rem;
    border-radius: 100px;
    margin-bottom: 1rem;
}
.hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    background: linear-gradient(135deg, #ffffff 30%, #a09fff 70%, #00d4aa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
    margin: 0;
}
.hero p {
    color: #5a5a7a;
    font-size: 0.95rem;
    margin-top: 0.5rem;
}

/* ── Section title ── */
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 1.5rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid #1e1e35;
}

/* ── Card ── */
.card {
    background: #111120;
    border: 1px solid #1e1e35;
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 1.5rem;
}

/* ── Account badge ── */
.acc-badge {
    background: linear-gradient(135deg, #6c63ff15, #00d4aa10);
    border: 1px solid #6c63ff33;
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    margin-top: 1rem;
    display: flex;
    align-items: center;
    gap: 1rem;
}
.acc-badge .icon { font-size: 2rem; }
.acc-badge .label {
    font-size: 0.65rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #5a5a7a;
}
.acc-badge .value {
    font-family: 'Syne', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: #a09fff;
    letter-spacing: 0.05em;
}

/* ── Detail rows ── */
.detail-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.85rem 0;
    border-bottom: 1px solid #1a1a2e;
}
.detail-row:last-child { border-bottom: none; }
.detail-key {
    font-size: 0.75rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #4a4a6a;
}
.detail-value {
    font-weight: 500;
    color: #c8c8e0;
}
.detail-value.balance {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    color: #00d4aa;
}

/* ── Inputs ── */
.stTextInput input, .stNumberInput input {
    background: #0a0a14 !important;
    border: 1px solid #1e1e35 !important;
    border-radius: 10px !important;
    color: #e8e8f0 !important;
    padding: 0.6rem 0.9rem !important;
    font-family: 'DM Sans', sans-serif !important;
    transition: border-color 0.2s;
}
.stTextInput input:focus, .stNumberInput input:focus {
    border-color: #6c63ff !important;
    box-shadow: 0 0 0 3px #6c63ff18 !important;
}
.stTextInput label, .stNumberInput label {
    color: #6a6a8a !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.05em !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #6c63ff, #5a52e0) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.6rem 1.8rem !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: 0.03em !important;
    transition: all 0.2s !important;
    width: 100% !important;
    margin-top: 0.5rem;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 24px #6c63ff44 !important;
}

/* ── Alert boxes ── */
.stSuccess {
    background: #00d4aa12 !important;
    border: 1px solid #00d4aa44 !important;
    border-radius: 10px !important;
    color: #00d4aa !important;
}
.stError {
    background: #ff5f5f12 !important;
    border: 1px solid #ff5f5f44 !important;
    border-radius: 10px !important;
}
.stWarning {
    background: #ffb74412 !important;
    border: 1px solid #ffb74444 !important;
    border-radius: 10px !important;
}
.stInfo {
    background: #6c63ff12 !important;
    border: 1px solid #6c63ff44 !important;
    border-radius: 10px !important;
    color: #a09fff !important;
}

/* ── Selectbox ── */
.stSelectbox > div > div {
    background: #0a0a14 !important;
    border: 1px solid #1e1e35 !important;
    border-radius: 10px !important;
    color: #e8e8f0 !important;
}

/* ── Divider ── */
hr { border-color: #1e1e35 !important; }

/* ── Sidebar nav pills ── */
.nav-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.7rem 1rem;
    border-radius: 10px;
    margin-bottom: 0.25rem;
    cursor: pointer;
    color: #5a5a7a;
    font-size: 0.9rem;
    font-weight: 500;
    transition: all 0.15s;
}
.nav-item:hover { background: #1a1a2e; color: #c8c8e0; }
.nav-item.active { background: #6c63ff22; color: #a09fff; border: 1px solid #6c63ff33; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 1.5rem 0 1rem;">
        <div style="font-family:'Syne',sans-serif; font-size:1.4rem; font-weight:800;
                    background:linear-gradient(135deg,#a09fff,#00d4aa);
                    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
                    background-clip:text;">
            💳 NeoBank
        </div>
        <div style="font-size:0.7rem; color:#3a3a5a; margin-top:0.2rem; letter-spacing:0.1em; text-transform:uppercase;">
            Digital Banking
        </div>
    </div>
    <hr style="margin-bottom:1.2rem;">
    """, unsafe_allow_html=True)

    menu = st.selectbox(
        "NAVIGATION",
        ["🆕  Create Account", "💰  Deposit", "💸  Withdraw",
         "📋  Account Details", "✏️  Update Info", "🗑️  Delete Account"],
    )

    st.markdown("""
    <div style="position:absolute; bottom:2rem; left:1.5rem; right:1.5rem;">
        <div style="font-size:0.65rem; color:#2a2a4a; text-align:center; letter-spacing:0.08em;">
            SECURED · ENCRYPTED · TRUSTED
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── Hero ──────────────────────────────────────────────────────────────────────
page_titles = {
    "🆕  Create Account": ("Open an Account", "Join thousands of smart savers today."),
    "💰  Deposit":        ("Deposit Funds",    "Add money to your account securely."),
    "💸  Withdraw":       ("Withdraw Funds",   "Access your money anytime."),
    "📋  Account Details":("Your Details",     "View your account information."),
    "✏️  Update Info":    ("Update Profile",   "Keep your information current."),
    "🗑️  Delete Account": ("Close Account",    "We're sorry to see you go."),
}
h1, sub = page_titles[menu]

st.markdown(f"""
<div class="hero">
    <div class="hero-tag">NeoBank Portal</div>
    <h1>{h1}</h1>
    <p>{sub}</p>
</div>
""", unsafe_allow_html=True)


# ── Pages ─────────────────────────────────────────────────────────────────────

if menu == "🆕  Create Account":
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", placeholder="e.g. Arjun Sharma")
            email = st.text_input("Email Address", placeholder="you@example.com")
        with col2:
            age  = st.number_input("Age", min_value=0, max_value=120, step=1)
            pin  = st.text_input("4-digit PIN", type="password", placeholder="••••")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Create My Account →"):
            if name and email and pin:
                user, msg = Bank.create_account(name, int(age), email, int(pin))
                if user:
                    st.success(f"✅ {msg}")
                    st.markdown(f"""
                    <div class="acc-badge">
                        <div class="icon">🪪</div>
                        <div>
                            <div class="label">Your Account Number</div>
                            <div class="value">{user['accountNo.']}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.info("📌 Save your account number — you'll need it to log in.")
                else:
                    st.error(f"❌ {msg}")
            else:
                st.warning("⚠️ Please fill in all fields before continuing.")


elif menu == "💰  Deposit":
    col1, col2 = st.columns(2)
    with col1:
        acc_no = st.text_input("Account Number", placeholder="Your account ID")
        pin    = st.text_input("PIN", type="password", placeholder="••••")
    with col2:
        amount = st.number_input("Deposit Amount (₹)", min_value=1, max_value=10000, step=100)
        st.markdown("<small style='color:#4a4a6a'>Maximum single deposit: ₹10,000</small>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Deposit →"):
        success, msg = Bank.deposit(acc_no, int(pin), int(amount))
        if success:
            st.success(f"✅ {msg} — ₹{amount:,} added to your balance.")
        else:
            st.error(f"❌ {msg}")


elif menu == "💸  Withdraw":
    col1, col2 = st.columns(2)
    with col1:
        acc_no = st.text_input("Account Number", placeholder="Your account ID")
        pin    = st.text_input("PIN", type="password", placeholder="••••")
    with col2:
        amount = st.number_input("Withdraw Amount (₹)", min_value=1, step=100)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Withdraw →"):
        success, msg = Bank.withdraw(acc_no, int(pin), int(amount))
        if success:
            st.success(f"✅ {msg} — ₹{amount:,} withdrawn.")
        else:
            st.error(f"❌ {msg}")


elif menu == "📋  Account Details":
    col1, col2 = st.columns(2)
    with col1:
        acc_no = st.text_input("Account Number", placeholder="Your account ID")
    with col2:
        pin = st.text_input("PIN", type="password", placeholder="••••")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("View Details →"):
        user = Bank.find_user(acc_no, int(pin))
        if user:
            st.markdown(f"""
            <div class="card">
                <div class="detail-row">
                    <span class="detail-key">Name</span>
                    <span class="detail-value">{user['name']}</span>
                </div>
                <div class="detail-row">
                    <span class="detail-key">Email</span>
                    <span class="detail-value">{user['email']}</span>
                </div>
                <div class="detail-row">
                    <span class="detail-key">Age</span>
                    <span class="detail-value">{user['age']} yrs</span>
                </div>
                <div class="detail-row">
                    <span class="detail-key">Account No.</span>
                    <span class="detail-value">{user['accountNo.']}</span>
                </div>
                <div class="detail-row">
                    <span class="detail-key">Balance</span>
                    <span class="detail-value balance">₹ {user['balance']:,}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ No account found. Check your account number and PIN.")


elif menu == "✏️  Update Info":
    col1, col2 = st.columns(2)
    with col1:
        acc_no  = st.text_input("Account Number", placeholder="Your account ID")
        pin     = st.text_input("Current PIN", type="password", placeholder="••••")
    with col2:
        name    = st.text_input("New Name", placeholder="Leave blank to keep current")
        email   = st.text_input("New Email", placeholder="Leave blank to keep current")
        new_pin = st.text_input("New PIN", type="password", placeholder="Leave blank to keep current")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Save Changes →"):
        success, msg = Bank.update_user(acc_no, int(pin), name, email, new_pin)
        if success:
            st.success(f"✅ {msg}")
        else:
            st.error(f"❌ {msg}")


elif menu == "🗑️  Delete Account":
    st.markdown("""
    <div style="background:#ff5f5f10; border:1px solid #ff5f5f33; border-radius:12px;
                padding:1rem 1.25rem; margin-bottom:1.5rem; color:#ff8a8a; font-size:0.9rem;">
        ⚠️ <strong>Warning:</strong> This action is permanent and cannot be undone.
        All your data and balance history will be erased.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        acc_no = st.text_input("Account Number", placeholder="Your account ID")
    with col2:
        pin = st.text_input("PIN", type="password", placeholder="••••")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Delete Account →"):
        success, msg = Bank.delete_user(acc_no, int(pin))
        if success:
            st.success(f"✅ {msg} — We hope to see you again.")
        else:
            st.error(f"❌ {msg}")