#! /usr/bin/env python

import os
from app import app
from dotenv import dotenv_values

port = 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
