import json
from constants import default_preferences


class Preferences:
    def __init__(self, filename="preferences.json"):
        self.filename = filename
        self.prefs = self.load_preferences()
        if self.prefs is None or self.prefs.keys() != default_preferences.keys():
            self.prefs = default_preferences
            self.save_preferences(self.prefs)
        self.from_json(self.prefs)

    def from_json(self, preferences):
        self.difficulty = preferences["difficulty"]
        self.user_resolution = preferences["user_resolution"]
        self.save_history = preferences["save_history"]
        self.font_family = preferences["font_family"]
        self.font_size = preferences["font_size"]

    def save_preferences(self, preferences):
        with open(self.filename, "w") as file:
            json.dump(preferences, file, indent=4)

    # kwargs is a dictionary of the new preferences passed as keyword arguments.
    def update_preferences(self, **kwargs):
        self.prefs.update(kwargs)
        self.save_preferences(self.prefs, self.filename)

    def load_preferences(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return None
