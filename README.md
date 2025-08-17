# 🤖 UnityNetwork Discord Bot

A modular Discord bot designed for the UnityNetwork community.
The bot is **feature-packed, organized, and easy to extend** using cogs for each functionality.

---

## ✨ Features

* **Moderation** – Manage users with commands like mod tools, ranking, and ticket handling.
* **Fun & Utility** – Meme commands, status updates, and welcome messages.
* **Ticket System** – Handle support tickets easily with dedicated commands.
* **Error Handling** – Built-in error tracking for smoother bot operation.
* **Configurable** – Centralized configuration for easy setup.

---

## 📂 Project Structure

```
unitynetwork-discord-bot/
 ├── cogs/
 │   ├── error.py        # Error handling for commands
 │   ├── meme.py         # Meme/fun commands
 │   ├── mod.py          # Moderation commands
 │   ├── rank.py         # Ranking system
 │   ├── sat.py          # Status/activity commands
 │   ├── ticket.py       # Ticket system commands
 │   └── wel.py          # Welcome messages
 ├── app.py              # Main bot runner
 └── config.py           # Configuration (token, prefixes, etc.)
```

---

## ⚙️ Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/unitynetwork-discord-bot.git
cd unitynetwork-discord-bot
```

2. **Install dependencies**

```bash
pip install discord.py asyncio
```

3. **Configure your bot**

* Edit `config.py` with your **bot token, prefix, and settings**.

4. **Run the bot**

```bash
python app.py
```

---

## 🚀 About

UnityNetwork Discord Bot is built to **support community servers** with moderation, fun commands, and automated systems like tickets and welcome messages.
Using **cogs**, it keeps features modular and easy to maintain.
Perfect for **gaming communities, SMP servers, or any active Discord server** that wants a reliable multipurpose bot.
