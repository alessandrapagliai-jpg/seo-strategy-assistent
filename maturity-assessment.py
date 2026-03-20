import streamlit as st

# --- CONFIG ---
st.set_page_config(
    page_title="Maturity Assessment Tool",
    page_icon="🪴",
    layout="centered"
)

# --- LOGO ---
st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 20px;">
        <a href="https://www.navla.ai/" target="_blank">
            <img src="https://raw.githubusercontent.com/alessandrapagliai-jpg/seo-strategy-assistent/refs/heads/main/navla_logo.png" alt="Navla Agency Logo" width="180">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# --- TITLE & DESCRIPTION ---
st.title("Maturity Assessment Tool")
st.text("Use this tool to assess your brand’s maturity in the selected territory, based on Global Share of Search data. "
        "Just enter the Share of Click values for your brand, its top competitor, and the leading publishers and eRetailers — "
        "then hit the button to get your strategy.")

def parse_percentage(text):
    """Converte input tipo '45' o '45%' in float"""
    value = text.strip().replace("%", "")
    return float(value)

def compute_soc_tool(brand_name, territory, soc_brand, soc_competitor, soc_publisher, soc_eretailer):
    # === DIFFERENCES ===
    diff_comp = abs(soc_brand - soc_competitor)
    diff_pub = abs(soc_brand - soc_publisher)
    diff_er = abs(soc_brand - soc_eretailer)
    total_diff = diff_comp + diff_pub + diff_er

    # === MATURITY & STRATEGY ===
    if total_diff <= 10:
        maturity, strategy, num_content = "High", "Excel", "5-10"
    elif total_diff > 50:
        maturity, strategy, num_content = "Medium", "Growth", "10–20"
    else:
        maturity, strategy, num_content = "Low", "Core", "20+"

    # === SPLIT ===
    if total_diff == 0:
        split_comp = split_pub = split_er = 0.0
    else:
        split_comp = 100 * diff_comp / total_diff
        split_pub = 100 * diff_pub / total_diff
        split_er = 100 * diff_er / total_diff

    # === OUTPUT ===
    st.subheader("Assessment Results")
    st.write(f"**Brand:** {brand_name} | **Territory:** {territory}")
    #st.write(f"Difference vs Competitor: {diff_comp:.1f}%")
    #st.write(f"Difference vs Publisher:  {diff_pub:.1f}%")
    #st.write(f"Difference vs eRetailer:  {diff_er:.1f}%")
    #st.write(f"**Sum of Differences:** {total_diff:.1f}%")

    st.write(f"**🪴​Maturity Level:** {maturity}")
    st.write(f"**♟️Strategy:** {strategy}")
    st.write(f"**📍Number of Content:** {num_content}")

    st.subheader("Suggested Content Split")
    st.write(f"🛍️Product Pages & Hub Pages: {split_comp:.0f}%")
    st.write(f"📰Articles: {split_pub + split_er:.0f}%")

brands = [
    "Aesop",
    "Armani",
    "Carita",
    "Diesel",
    "Helena Rubinstein",
    "IT Cosmetics",
    "Kiehl's",
    "Lancôme",
    "Miu Miu",
    "Mugler",
    "Prada",
    "Ralph Lauren",
    "Shu Uemura",
    "Takami",
    "Urban Decay",
    "Valentino",
    "YSL",
    "Youth To The People"
]

brand_name = st.selectbox("Select Brand", brands, index=None, placeholder="Choose a brand")
territory = st.text_input("Territory", "")
soc_brand = st.number_input("Brand's Share of Click (%)", min_value=0.0, max_value=100.0, value=0.0)
soc_competitor = st.number_input("Top Competitor Brand Share of Click (%)", min_value=0.0, max_value=100.0, value=0.0)
soc_publisher = st.number_input("Top Publisher Competitor Share of Click (%)", min_value=0.0, max_value=100.0, value=0.0)
soc_eretailer = st.number_input("Top eRetailer Share of Click (%)", min_value=0.0, max_value=100.0, value=0.0)

if st.button("🔍Get Results"):
    compute_soc_tool(brand_name, territory, soc_brand, soc_competitor, soc_publisher, soc_eretailer)

# --- FOOTER ---
st.markdown(
    """
    <hr style="margin-top: 50px;">
    <div style="text-align: center; color: gray; font-size: 0.9em;">
        <p>© Navla - A brand of ByTek Srl - VAT IT13056731006 - REA: MI - 2562796 - ByTek is subject to the governance and coordination of Datrix S.p.A. - Built with ❤️ using Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)
