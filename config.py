import json

class ConfigManager:
    def __init__(self):
        self.credentials  = {}
        self.dbParams     = {}
        self.botAttrs     = {}

        self.loadDBParams()
        self.loadCredentials()
        self.loadBotAttributes()
    
    def loadDBParams(self):
        with open("_config/cockroach_params.json") as f:
            self.dbParams = json.load(f)
            f.close()

    def loadCredentials(self):
        with open("_config/credentials.json", "r") as f:
            self.credentials = json.load(f)
            f.close()
    
    def loadBotAttributes(self):
        with open("_config/bot_attributes.json") as f:
            self.botAttrs = json.load(f)
            f.close()