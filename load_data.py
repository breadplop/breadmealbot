import pandas as pd
import datetime

def load_data(month='Oct'):
    # TODO: load diff files acc to month. 
    df = pd.read_csv('/Users/brenda/Downloads/Telegram Desktop/test_oct_menu_cleaned.csv')
    return df

def format_date(tdy_raw):
    tdy_str = format(tdy_raw, '%Y-%m-%d')
    return tdy_str

tdy_raw = datetime.datetime.today()
tdy = format_date(tdy_raw)
tmr = format_date(tdy_raw + datetime.timedelta(days=1))

def format_menu(menu):
    res = menu.to_string(index=False, header=False, na_rep="")

    words_to_bold = ['Breakfast', 'Dinner']
    words_to_italicized = ['Choose 1', 'Drinks', 'Meat', 'Side Dish', 'Vegetable', 'Dessert']
    res.replace(" ","")
    for word in words_to_bold:
        res =res.replace(word, '*😊' + word.upper() + '😊*')
    for word in words_to_italicized:
        res = res.replace(word, '_-' + word + '_-')
    return res