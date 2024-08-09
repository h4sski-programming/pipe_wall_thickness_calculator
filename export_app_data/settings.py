import json
from kivy.metrics import dp

TITLE_LABEL_SIZE_HINT = 1, None
TITLE_LABEL_SIZE = 1, dp(30)
TITLE_LABEL_BG_COLOR = (1, 0.8, 0, 1)

MESSAGE_COLOR = (.0, .5, .0, 1)
MESSAGE_ERROR_COLOR = (1, 0.2, 0.2, 1)
MESSAGE_GREEN_COLOR = (0.2, 0.7, 0.2, 1)



def get_db_json() -> json:
    with open('data_input.json', mode='r') as json_file:
        db_json = json.load(json_file)
    return db_json
DB_JSON = get_db_json()