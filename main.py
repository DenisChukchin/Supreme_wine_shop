import datetime
import pandas
import collections

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_year():
    now = datetime.datetime.now()
    age = now.year - 1920
    return age


def get_correct_russian_year():
    year = str(get_year())
    set_1 = ('2', '3', '4')
    set_2 = ('5', '6', '7', '8', '9', '12', '13',
             '14', '15', '16', '17', '18', '19')
    if year.endswith('1') and not year.endswith('11'):
        return f"{year} год"
    if year.endswith(set_1) and not year.endswith(set_2[5:8]):
        return f"{year} года"
    if year.endswith(set_2) and not year.endswith('1' or set_2[5:7]):
        return f"{year} лет"
    if year.endswith('0') or year.endswith('11'):
        return f"{year} лет"


def get_new_wine_card():
    excel_wine_card = pandas.read_excel(
        'wine3.xlsx', sheet_name='Лист1', na_values='nan', keep_default_na=False
    )
    raw_wine_card = excel_wine_card.to_dict(orient='records')
    complete_wine_card = collections.defaultdict(list)
    for card in raw_wine_card:
        complete_wine_card[card['Категория']].append(card)
    wine_card = sorted(complete_wine_card.items())
    return dict(wine_card)


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        foundation_year=f'Уже {get_correct_russian_year()} с вами',
        wine_card=get_new_wine_card()
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
