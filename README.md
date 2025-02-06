# 🎬 Telegram Movie Bot 🎥



A Python bot that fetches movie details from OMDB API and automatically posts them to a Telegram channel. 
It also stores the movie information in an Excel file for tracking purposes.



## ✨ Features

✅ Fetch movie details (Title, Year, Genre, Director, etc.)   
✅ Send the movie information and poster to a Telegram channel   
✅ Store movie information in an Excel file   
✅ Fully automated workflow



## 📷 Screenshots

![Movie](https://github.com/user-attachments/assets/b2f36eec-f17f-4fb7-be6c-d1bee3ed5f6d)

![Movie2](https://github.com/user-attachments/assets/ea765465-cf88-4f11-a596-8e542e496e4a)



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
```json
{
  "Telegram":
  {
    "api_id" : "",
    "api_hash" : "",
    "channel_id" : ""
  },
  "omdb" : {
    "api_key" : ""
  }
}
```
you can get your telegram api_id, api_hash from "https://my.telegram.org/apps".

and your omdb api_key from "https://www.omdbapi.com/apikey.aspx".



## 4. Run the bot:

```bash
python main.py
```



## 🤝 Contributing

Pull requests are welcome! If you have any suggestions or improvements, feel free to contribute.
