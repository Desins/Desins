import streamlit as st
import folium
from streamlit_folium import st_folium

# Language translation dictionary
translations = {
    "Deutsch": {
        "title": "Erkunde Wilhelmshaven - Dein digitaler Küstenführer",
        "description": "Entdecke die Highlights von Wilhelmshaven! Interaktive Karten, historische Infos, Restaurants und praktische Tipps helfen dir, die Stadt zu erleben.",
        "features": [
            "Interaktive Karte",
            "Sehenswürdigkeiten",
            "Historische Fakten",
            "Hotels",
            "Restaurants",
            "Fotos und Videos hochladen",
        ],
    },
    "English": {
        "title": "Explore Wilhelmshaven - Your Digital Coastal Guide",
        "description": "Discover Wilhelmshaven's highlights! Interactive maps, historical info, restaurants, and practical tips to explore the city.",
        "features": [
            "Interactive Map",
            "Attractions",
            "Historical Facts",
            "Hotels",
            "Restaurants",
            "Upload Photos and Videos",
        ],
    },
}

# Language settings
language = st.sidebar.selectbox("Sprache / Language", ["Deutsch", "English"])
text = translations[language]

# Title and Description
st.title(text["title"])
st.write(text["description"])

# Navigation between different features
feature = st.sidebar.selectbox("Select Feature", text["features"])

# Historical Facts Feature
# Data for map markers
locations = {
    "Sehenswürdigkeiten": [
        {
            "Name": "Kaiser-Wilhelm-Brücke",
            "Latitude": 53.5086,
            "Longitude": 8.1079,
            "Description": "Die älteste Drehbrücke Deutschlands und ein Wahrzeichen der Stadt." if language == "Deutsch" else "The oldest swing bridge in Germany and a landmark of the city.",
            "Image": "https://brueckenzug.de/wp-content/uploads/Wilhelmshaven_Kaiser-Wilhelm-Bruecke.webp",
            "Link": "https://maps.app.goo.gl/C8P7NPmcbhsTHxHw7",
        },
        {
            "Name": "Deutsches Marinemuseum",
            "Latitude": 53.5137,
            "Longitude": 8.1168,
            "Description": "Tauchen Sie ein in die Geschichte der Deutschen Marine." if language == "Deutsch" else "Dive into the history of the German Navy.",
            "Image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/14/68/dd/8f/img-20180824-121545-largejpg.jpg?w=1200&h=-1&s=1",
            "Link": "https://maps.app.goo.gl/NLQFquFvKcyrgE3j7",
        },
        {
            "Name": "Südstrand",
            "Latitude": 53.5037,
            "Longitude": 8.1121,
            "Description": "Ein beliebter Ort, um am Wasser zu entspannen." if language == "Deutsch" else "A popular spot to relax and walk along the waterfront.",
            "Image": "https://dam.destination.one/928449/df187e33dc168fdbd2b7532885d2a1f375314eea132708a6bb2eaa88f2d3dba6/b-nke-auf-der-s-dstrandpromenade.jpg",
            "Link": "https://g.co/kgs/s7rrv5J",
        },
        {
            "Name": "Wattenmeer Besucherzentrum",
            "Latitude": 53.5146,
            "Longitude": 8.1034,
            "Description": "Ein Nationalparkzentrum mit interaktiven Ausstellungen über das Wattenmeer." if language == "Deutsch" else "A visitor center with interactive exhibits about the Wadden Sea.",
            "Image": "https://www.wattenmeer-besucherzentrum.de/images/Wattenmeer-Besucherzentrum1.png",
            "Link": "https://maps.app.goo.gl/C8P7NPmcbhsTHxHw7",
        },
    ],
    "Hotels": [
        {
            "Name": "Atlantic Hotel Wilhelmshaven",
            "Latitude": 53.5112,
            "Longitude": 8.1041,
            "Description": "Luxushotel mit Blick auf den Hafen." if language == "Deutsch" else "Luxury hotel overlooking the harbor.",
            "Image": "https://www.atlantic-hotels.de/fileadmin/_processed_/5/b/csm_atlantic-hotel-wilhelmshaven-aussenansicht-mit-logo_c97ce07495.jpg",
            "Link": "https://maps.app.goo.gl/PBZWwtRsj9VENcP57",
            "Stars": 5,
            "Price": "ab 150€ pro Nacht",
            "Rating": "4.6/5",
        },
        {
            "Name": "Tide Hotel",
            "Latitude": 53.5142,
            "Longitude": 8.1001,
            "Description": "Modernes Hotel nahe dem Südstrand." if language == "Deutsch" else "Modern hotel near the southern beach.",
            "Image": "https://www.hotel-am-stadtpark.de/files/stadtpark/images/Tide-Hotel-Aussen/Tide-Hotel-Frontansicht.jpg",
            "Link": "https://maps.app.goo.gl/dvtbmLBsNKTzwXUAA",
            "Stars": 4,
            "Price": "ab 100€ pro Nacht",
            "Rating": "4.4/5",
        },
        {
            "Name": "City Hotel Valois",
            "Latitude": 53.5201,
            "Longitude": 8.1064,
            "Description": "Zentral gelegenes Hotel in der Nähe des Bahnhofs." if language == "Deutsch" else "Centrally located hotel near the train station.",
            "Image": "https://cf.bstatic.com/xdata/images/hotel/max1024x768/12665667.jpg?k=2019e057a2f241cdca711f456a0d963297dbdf192afc9f1d7b9801ec9a6913c2&o=",
            "Link": "https://maps.app.goo.gl/oiUajn2RPh8emp3K7",
            "Stars": 3,
            "Price": "ab 80€ pro Nacht",
            "Rating": "4.2/5",
        },
    ],
    "Restaurants": [
        {
            "Name": "CaOs",
            "Latitude": 53.5158,
            "Longitude": 8.1015,
            "Description": "Einzigartige, kreative Küche mit regionalen Zutaten." if language == "Deutsch" else "Unique, creative cuisine with regional ingredients.",
            "Image": "https://lh3.googleusercontent.com/p/AF1QipM4m5Q-ieQqb-Ckih0InKjBmkH0AXI1qrINL2iv=s1360-w1360-h1020",
            "Link": "https://maps.app.goo.gl/fu9UBw5u9MYk25t4A",
            "Rating": "4.7/5",
            "Price": "25-50€ pro Person",
        },
        {
            "Name": "L' Orient Libanesisches Restaurant",
            "Latitude": 53.5182,
            "Longitude": 8.1101,
            "Description": "Authentische libanesische Gerichte in gemütlicher Atmosphäre." if language == "Deutsch" else "Authentic Lebanese dishes in a cozy atmosphere.",
            "Image": "https://lh5.googleusercontent.com/p/AF1QipPw6KF-92Osg2g5gBbO65fmUN-VEyWMpDRk3BHP=w750-h606-p-k-no",
            "Link": "https://goo.gl/maps/LkP5z7VbMeN2",
            "Rating": "4.5/5",
            "Price": "20-40€ pro Person",
        },
    ],
}

# Interactive Map Feature
if feature == text["features"][0]:
    st.header(text["features"][0])

    # Create map
    m = folium.Map(location=[53.515, 8.118], zoom_start=13)

    # Add markers for all locations
    for category, places in locations.items():
        for place in places:
            icon_color = "blue" if category == "Sehenswürdigkeiten" else "green" if category == "Hotels" else "red"
            icon = "cutlery" if category == "Restaurants" else "info-sign"
            folium.Marker(
                location=[place["Latitude"], place["Longitude"]],
                popup=f"<b>{place['Name']}</b><br>{place['Description']}<br><a href='{place['Link']}' target='_blank'>Mehr erfahren</a>",
                icon=folium.Icon(color=icon_color, icon=icon),
            ).add_to(m)

    # Display map
    st_folium(m, width=700, height=500)

# Displaying details for other features
elif feature == text["features"][1]:  # Sehenswürdigkeiten
    st.header(text["features"][1])
    for place in locations["Sehenswürdigkeiten"]:
        st.image(place["Image"], use_container_width=True)
        st.subheader(f"[{place['Name']}]({place['Link']})")
        st.write(place["Description"])
        st.write("---")

elif feature == text["features"][3]:  # Hotels
    st.header(text["features"][3])
    for place in locations["Hotels"]:
        st.image(place["Image"], use_container_width=True)
        st.subheader(f"[{place['Name']}]({place['Link']})")
        st.write(place["Description"])
        st.write(f"⭐ {place['Stars']} | 💶 {place['Price']} | ✨ {place['Rating']}")
        st.write("---")

elif feature == text["features"][4]:  # Restaurants
    st.header(text["features"][4])
    for place in locations["Restaurants"]:
        st.image(place["Image"], use_container_width=True)
        st.subheader(f"[{place['Name']}]({place['Link']})")
        st.write(place["Description"])
        st.write(f"⭐ {place['Rating']} | 💶 {place['Price']}")
        st.write("---")

elif feature == text["features"][5]:  # Fotos und Videos hoch
 st.header(text["features"][5])
 uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True, type=["png", "jpg", "jpeg", "mp4"])
 if uploaded_files:
        for file in uploaded_files:
            if file.type.startswith("image"):
                st.image(file)
            elif file.type.startswith("video"):
                st.video(file)