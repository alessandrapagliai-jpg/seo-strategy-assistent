import streamlit as st

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
        maturity, strategy, num_content = "High", "Defend", "10–25"
    elif total_diff > 50:
        maturity, strategy, num_content = "Medium", "Growth", "25–50"
    else:
        maturity, strategy, num_content = "Low", "Attack", "50+"

    # === SPLIT ===
    if total_diff == 0:
        split_comp = split_pub = split_er = 0.0
    else:
        split_comp = 100 * diff_comp / total_diff
        split_pub = 100 * diff_pub / total_diff
        split_er = 100 * diff_er / total_diff

    # === OUTPUT ===
    st.subheader("Results")
    st.write(f"**Brand:** {brand_name} | **Territory:** {territory}")
    st.write(f"Difference vs Competitor: {diff_comp:.1f}%")
    st.write(f"Difference vs Publisher:  {diff_pub:.1f}%")
    st.write(f"Difference vs eRetailer:  {diff_er:.1f}%")
    st.write(f"**Sum of Differences:** {total_diff:.1f}%")

    st.write(f"**Maturity Level:** {maturity}")
    st.write(f"**Strategy:** {strategy}")
    st.write(f"**Number of Content:** {num_content}")

    st.subheader("Content Split")
    st.write(f"PdP + Hub Page: {split_comp:.1f}%")
    st.write(f"Article: {split_pub + split_er:.1f}%")


# --- STREAMLIT APP ---
st.title("Maturity Assessment Tool")
st.text("This tool will help you define the brand’s maturity level in relation to the selected territory, based on Share of Click data from the Global Share of Search. Enter the Share of Click values for the brand, the competitor brand with the highest Share of Click, and the top-ranking Publishers and eRetailers. Then, press the button.")

brand_name = st.text_input("Brand", "")
territory = st.text_input("Territory", "")
soc_brand = st.number_input("Brand's SOC (%)", min_value=0.0, max_value=100.0, value=0.0)
soc_competitor = st.number_input("1° Competitor Brand SOC (%)", min_value=0.0, max_value=100.0, value=0.0)
soc_publisher = st.number_input("1° Publisher Competitor SOC (%)", min_value=0.0, max_value=100.0, value=0.0)
soc_eretailer = st.number_input("1° eRetailer SOC (%)", min_value=0.0, max_value=100.0, value=0.0)

if st.button("Compute Strategy"):
    compute_soc_tool(brand_name, territory, soc_brand, soc_competitor, soc_publisher, soc_eretailer)
