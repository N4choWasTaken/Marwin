def handle_response(message: str):
    p_message = message.lower()

    if p_message == 'hey':
        return 'Helo'

    if p_message == '!help':
        return "`This is a help message`"

    if p_message == "marwin slide in my dms":
        return 'Hello! Helloo?? Oh... Hey you! Can you help me I think I am los... Nvm I am at the right place shawty'
