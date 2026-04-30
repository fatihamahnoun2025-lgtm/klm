import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Luxury Booking App", page_icon="💎", layout="wide")

# =========================
# LANGUAGE TOGGLE
# =========================
if "lang" not in st.session_state:
    st.session_state.lang = "English"

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown("### 🌐 Language / اللغة")

    lang_choice = st.radio(
        "",
        ["🇬🇧 English", "🇸🇦 العربية"],
        horizontal=True
    )

    if lang_choice == "🇬🇧 English":
        st.session_state.lang = "English"
    else:
        st.session_state.lang = "Arabic"


def t(en, ar):
    return en if st.session_state.lang == "English" else ar


# =========================
# STYLE (LUXURY UI)
# =========================
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #f8fafc, #eef2ff);
}

.title {
    font-size: 52px;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(90deg, #f59e0b, #3b82f6, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 18px;
    margin-bottom: 20px;
}

.card {
    background: white;
    border-radius: 22px;
    padding: 15px;
    box-shadow: 0px 12px 30px rgba(0,0,0,0.08);
    transition: 0.3s;
    border: 1px solid #f1f5f9;
}

.card:hover {
    transform: translateY(-6px);
}

.stButton>button {
    background: linear-gradient(90deg, #f59e0b, #3b82f6);
    color: white;
    border-radius: 12px;
    padding: 10px 16px;
    border: none;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


# =========================
# HEADER + LOGO
# =========================
st.image("https://i.imgur.com/4M7IWwP.png", width=120)

st.markdown("<div class='title'>Luxury Booking Experience</div>", unsafe_allow_html=True)
st.markdown(f"<div class='subtitle'>{t('Premium Services • Instant Booking • Luxury Experience', 'خدمات فاخرة • حجز فوري • تجربة راقية')}</div>", unsafe_allow_html=True)

st.markdown("---")


# =========================
# HERO IMAGE
# =========================
st.image("https://images.unsplash.com/photo-1522199710521-72d69614c702", use_container_width=True)


# =========================
# SERVICES
# =========================
services = [
    ("🌸 Perfumes", "https://images.unsplash.com/photo-1615634260167-c8cdede054de"),
    ("🍽 Catering", "https://images.unsplash.com/photo-1551218808-94e220e084d2"),
    ("🎉 Events", "https://images.unsplash.com/photo-1505236858219-8359eb29e329"),
    ("💄 Beauty", "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e"),
    ("🪧 Decorations", "https://images.unsplash.com/photo-1506744038136-46273834b3fb"),
    ("🎁 Offers", "https://images.unsplash.com/photo-1523275335684-37898b6baf30")
]


st.markdown(f"## 🧭 {t('Choose Your Service', 'اختر الخدمة')}")

selected_service = None

cols = st.columns(3)

for i, (name, img) in enumerate(services):
    with cols[i % 3]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.image(img, use_container_width=True)
        st.markdown(f"### {name}")
        st.write(t("Premium curated experience", "تجربة فاخرة مختارة"))

        if st.button(t("Select", "اختيار") + f" {name}"):
            selected_service = name
            st.success(t("Selected ✔", "تم الاختيار ✔"))

        st.markdown("</div>", unsafe_allow_html=True)


# =========================
# BOOKING FORM
# =========================
st.markdown("---")

st.markdown(f"## 📅 {t('Booking Details', 'تفاصيل الحجز')}")

with st.container():
    name = st.text_input(t("Full Name", "الاسم الكامل"))
    phone = st.text_input(t("Phone Number", "رقم الهاتف"))

    col1, col2 = st.columns(2)

    with col1:
        date = st.date_input(t("Select Date", "اختيار التاريخ"))

    with col2:
        time = st.time_input(t("Select Time", "اختيار الوقت"))

    notes = st.text_input(t("Notes (optional)", "ملاحظات (اختياري)"))

    st.markdown("---")

    st.markdown(f"## 💳 {t('Payment Section', 'الدفع')}")

    payment = st.radio(
        t("Choose Payment Method", "اختر طريقة الدفع"),
        ["💳 Credit Card", "💵 Cash", "🏦 Bank Transfer"]
    )

    card = st.text_input(t("Card Number (demo)", "رقم البطاقة (تجريبي)"))

    if st.button(t("Confirm Booking & Pay 💎", "تأكيد الحجز والدفع 💎")):
        st.success(t("Booking sent successfully (UI Demo)", "تم إرسال الحجز بنجاح (واجهة فقط)"))


# =========================
# SUMMARY PANEL
# =========================
st.markdown("---")

st.markdown(f"## 🧾 {t('Summary', 'ملخص')}")
st.info(
    t(
        "This is a premium frontend prototype without backend integration.",
        "هذا نموذج واجهة فقط بدون ربط خلفي"
    )
)


# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown(
    "<center>💎 Luxury Booking App | Frontend Prototype | Streamlit</center>",
    unsafe_allow_html=True
)