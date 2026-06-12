import streamlit as st

st.set_page_config(page_title="Telugu Guessing Game")

st.title("🎬 Telugu Guessing Game")

data = {
    "Pushpa 2": ["pushpa", "allu arjun", "smuggling", "sukumar"],
    "RRR": ["ntr", "ram charan", "rajamouli", "oscar"],
    "Kalki 2898 AD": ["prabhas", "future", "amitabh", "deepika"],
    "Salaar": ["prabhas", "kgf", "action", "prithviraj"],
    "Devara": ["ntr", "sea", "koratala", "villagers"],

    "Allu Arjun": ["icon star", "pushpa", "arya"],
    "Prabhas": ["baahubali", "darling", "salaar"],
    "Jr NTR": ["rrr", "devara", "temper"],
    "Ram Charan": ["rrr", "magadheera", "game changer"],
    "Mahesh Babu": ["srimanthudu", "pokiri", "guntur karam"],
}

clue = st.text_input("Enter clues")

if st.button("Guess"):
    clue = clue.lower()

    best_match = None
    score = 0

    for item, keywords in data.items():
        count = 0

        for word in keywords:
            if word in clue:
                count += 1

        if count > score:
            score = count
            best_match = item

    if best_match:
        st.success(f"My Guess: {best_match}")
    else:
        st.error("I couldn't guess. Try more clues!")
