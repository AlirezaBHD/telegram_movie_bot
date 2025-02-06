
genre_translations = {
    "Action": "اکشن",
    "Adventure": "ماجراجویی",
    "Animation": "انیمیشن",
    "Biography": "زندگینامه",
    "Comedy": "کمدی",
    "Crime": "جنایی",
    "Documentary": "مستند",
    "Drama": "درام",
    "Family": "خانوادگی",
    "Fantasy": "فانتزی",
    "Film Noir": "فیلم نوآر",
    "History": "تاریخی",
    "Horror": "ترسناک",
    "Music": "موزیکال",
    "Musical": "موزیکال",
    "Mystery": "معمایی",
    "Romance": "عاشقانه",
    "Sci-Fi": "علمی-تخیلی",
    "Short": "کوتاه",
    "Sport": "ورزشی",
    "Superhero": "ابرقهرمانی",
    "Thriller": "هیجان‌انگیز",
    "War": "جنگی",
    "Western": "وسترن"
}

country_translations = {
    "South Korea": "کره جنوبی",
    "United States": "ایالات متحده آمریکا",
    "United Kingdom": "بریتانیا",
    "Germany": "آلمان",
    "France": "فرانسه",
    "Japan": "ژاپن",
    "China": "چین",
    "India": "هند",
    "Brazil": "برزیل",
    "Canada": "کانادا",
    "Australia": "استرالیا",
    "Russia": "روسیه",
    "Italy": "ایتالیا",
    "Spain": "اسپانیا",
    "Mexico": "مکزیک",
    "Argentina": "آرژانتین",
    "South Africa": "آفریقای جنوبی",
    "Egypt": "مصر",
    "Turkey": "ترکیه",
    "Iran": "ایران",
    "Saudi Arabia": "عربستان سعودی",
    "Thailand": "تایلند",
    "Indonesia": "اندونزی",
    "Vietnam": "ویتنام",
    "Pakistan": "پاکستان",
    "Nigeria": "نیجریه",
    "Kenya": "کنیا",
    "Greece": "یونان",
    "Sweden": "سوئد",
    "Netherlands": "هلند",
    "Belgium": "بلژیک",
    "Ireland": "ایرلند",
    "West Germany": "آلمان غربی",
    "Norway": "نروژ"
}

def translate_genres(genre_string):
    genres = [g.strip() for g in genre_string.split(",")]
    translated_genres = [genre_translations.get(genre, genre) for genre in genres]
    return ", ".join(translated_genres)

def translate_countries(country_string):
    countries = [c.strip() for c in country_string.split(",")]
    translated_countries = [country_translations.get(country, country) for country in countries]
    return ", ".join(translated_countries)


