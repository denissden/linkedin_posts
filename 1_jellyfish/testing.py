from pathlib import Path
from difflib import SequenceMatcher
import os

import jellyfish
from peewee import SqliteDatabase, Model, TextField
import openai


db = SqliteDatabase('places.sqlite')


class Place(Model):
    name_and_description = TextField()
    tags = TextField(null=True)

    class Meta:
        database = db




def search_sequence_matcher(search_str: str, n_results=5):
    lower_search_str = search_str.lower()

    def score(product):
        product_str = product['Product Details']
        return SequenceMatcher(a=lower_search_str, b=product_str.lower()).real_quick_ratio()

    # return list(sorted(all_lines, key=score, reverse=True))[:n_results]


def search_levenshtein(search_str: str):
    pass


if __name__ == '__main__':
    print(jellyfish.levenshtein_distance("coffee", "coffee"))

    create_memory_database("gpt_places.txt")
    print(search_sequence_matcher("Toys"))

    openai.api_key = os.environ.get("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": open("gpt_places.txt").read()}]
    )
