import uuid  
from nicegui import ui 

messages = []

def generate_user():
    user_id = str(uuid.uuid4())  
    avatar_url = f'https://robohash.org/{user_id}?set=set2'  
    return user_id, avatar_url

@ui.refreshable
def display_messages(current_user):

    for sender_id, avatar_url, message_text in messages:
        ui.chat_message(
            avatar=avatar_url,
            text=message_text,
            sent=sender_id == current_user
        )

def create_input_section(on_send, avatar_url):

    with ui.footer().classes('bg-lightgray'):
        with ui.row().classes('items-center w-full'):
            ui.image(avatar_url).classes('rounded-full w-12 h-12')  
            message_input = ui.input(placeholder='Type a message...') \
                .props('outlined') \
                .classes('flex-grow') \
                .on('keydown.enter', on_send) 
    return message_input

@ui.page('/')
def chat_page():

    user_id, avatar_url = generate_user()


    def send_message():

        if message_input.value.strip():
            messages.append((user_id, avatar_url, message_input.value.strip()))
            display_messages.refresh()  
            message_input.value = '' 

    with ui.column().classes('w-full h-full'):
        display_messages(user_id)

    message_input = create_input_section(send_message, avatar_url)

ui.run()
