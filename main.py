import datetime
import pandas
import collections
import argparse
import os
from dotenv import load_dotenv

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_winery_age():
    now = datetime.datetime.now()
    foundation_year = 1920
    winery_age = now.year - foundation_year
    return winery_age


def get_correct_russian_year():
    winery_age = str(get_winery_age())
    set_1 = ('2', '3', '4')
    set_2 = ('5', '6', '7', '8', '9', '12', '13',
             '14', '15', '16', '17', '18', '19')
    if winery_age.endswith('1') and not winery_age.endswith('11'):
        return f"{winery_age} год"
    if winery_age.endswith(set_1) and not winery_age.endswith(set_2[5:8]):
        return f"{winery_age} года"
    if winery_age.endswith(set_2) and not winery_age.endswith('1' or set_2[5:7]):
        return f"{winery_age} лет"
    if winery_age.endswith('0') or winery_age.endswith('11'):
        return f"{winery_age} лет"


def get_new_wine_card(path_to_file):
    excel_wine_card = pandas.read_excel(
        path_to_file, na_values='nan', keep_default_na=False
    )
    raw_wine_card = excel_wine_card.to_dict(orient='records')
    complete_wine_card = collections.defaultdict(list)
    for card in raw_wine_card:
        complete_wine_card[card['Категория']].append(card)
    wine_card = sorted(complete_wine_card.items())
    return dict(wine_card)


def parse_args(default_file_path):
    parser = argparse.ArgumentParser(
        description="Используя шаблон,"
                    " обновляем винную карту сайта на основе файла с таблицей"
    )
    parser.add_argument("-user_path", type=str,
                        help="Укажите путь к файлу",
                        default=default_file_path,
                        metavar="Путь к файлу")
    args = parser.parse_args()
    return args.user_path


def main():
    load_dotenv()
    default_file_path = os.getenv('FILE_PATH')
    path_to_file = parse_args(default_file_path)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        foundation_year=f'Уже {get_correct_russian_year()} с вами',
        wine_card=get_new_wine_card(path_to_file)
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
