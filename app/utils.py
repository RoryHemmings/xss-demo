import re

def filter_message(message):
    banned = ['<script>', '<button>', '<img>', '<body>', '<iframe>', '<button>', '<input>', '<h1>']
    for word in banned:
        if re.search(word, message):
            message = 'nice try'
    
    return message