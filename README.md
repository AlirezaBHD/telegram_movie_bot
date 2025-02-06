# 🎬 Telegram Movie Bot 🎥



A Python bot that fetches movie details from OMDB API and automatically posts them to a Telegram channel. 
It also stores the movie information in an Excel file for tracking purposes.



## ✨ Features

✅ Fetch movie details (Title, Year, Genre, Director, etc.) 
✅ Send the movie information and poster to a Telegram channel 
✅ Store movie information in an Excel file 
✅ Fully automated workflow



## 📷 Screenshots

![Movie.PNG](C:\Users\msi\Pictures\Movie.PNG)

![Movie2.PNG](C:\Users\msi\Pictures\Movie2.PNG)



## 🚀 Installation 1. Clone this repository:

```bash
git clone https://github.com/AlirezaBHD/telegram_movie_bot.git
cd telegram-movie-bot
```

## 2. Install dependencies:

```bash
pip install -r requirements.txt
```

## 3. Complete `Resource.json` file and add your API credentials:

{
    "Telegram": {
        "api_id": "YOUR_API_ID",
        "api_hash": "YOUR_API_HASH",
        "channel_id": "YOUR_BOT_TOKEN"
    },
    "omdb": {
        "api_key": "YOUR_OMDB_API_KEY"
    }
}

you can get your telegram api_id, api_hash from "https://my.telegram.org/apps".

and your omdb api_key from "https://www.omdbapi.com/apikey.aspx".



## 4. Run the bot:

```bash
python main.py
```



## 🤝 Contributing

Pull requests are welcome! If you have any suggestions or improvements, feel free to contribute.
