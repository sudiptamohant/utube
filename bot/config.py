import os


class Config:

    BOT_TOKEN = os.environ.get("6252471050:AAFlBX-EkOPRf7re1WHZnMlNyYjkOg6c8yo")

    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")

    API_ID = int(os.environ.get("5806640"))

    API_HASH = os.environ.get("127f130ad3745dbcd31aa39aa0eabcb8")

    CLIENT_ID = os.environ.get("696277737465-u279goq240bs0acl8nm3jvacpre4nh5a.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = int(os.environ.get("1375408229"))

    AUTH_USERS_TEXT = os.environ.get("1375408229", "6203460103")

    AUTH_USERS = [BOT_OWNER, 1375408229] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("THANKS FOR WATCHING THE VIDEO", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
