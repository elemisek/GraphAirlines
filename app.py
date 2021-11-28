# -*- coding: utf-8 -*-
from api import app
import secrets
import os

app.secret_key = secrets.token_urlsafe(16)
port = int(os.environ.get('PORT', 33507))
app.run(host='0.0.0.0', port=port)
