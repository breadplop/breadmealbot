from telegram import KeyboardButton

some_strings = ["Breakfast", "Dinner"]
button_list = [[KeyboardButton(s)] for s in some_strings]

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

menu = build_menu(button_list,2)