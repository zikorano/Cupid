from config import ConfigManager
from src.bot import *
cm = ConfigManager()

if __name__ == "__main__":
    print(dir())
    token = cm.credentials["clientToken"]
    bot.run(token)