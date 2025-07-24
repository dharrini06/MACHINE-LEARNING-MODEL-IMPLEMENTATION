import pandas as pd

# Sample data
data = {
    "text": [
        "NASA confirms water on Mars",
        "Aliens spotted by villagers in South India",
        "Government launches new health insurance scheme",
        "Actor claims COVID vaccine turns people into zombies",
        "Scientists discover new species in the Amazon rainforest",
        "Man claims to time travel using a microwave",
        "Apple announces new iPhone with holographic display",
        "Politician says eating ice cream prevents global warming",
        "New study reveals benefits of meditation on brain health",
        "Fake news website reports celebrity's fake death",
        "University researchers develop cure for common cold",
        "Article claims 5G towers cause mind control",
        "Doctors warn against viral TikTok health trend",
        "Website falsely claims end of the world is near",
        "Government approves scheme for youth entrepreneurship"
    ],
    "label": [
        "real", "fake", "real", "fake", "real",
        "fake", "real", "fake", "real", "fake",
        "real", "fake", "real", "fake", "real"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("fake_news_dataset.csv", index=False)
