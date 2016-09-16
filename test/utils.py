import os

TEST_DATA = os.path.join(os.path.dirname(__file__), 'data')


def load_song(title, extension='txt'):
    filename = '{}.{}'.format(title.lower().replace(' ', '-'), extension)
    filepath = os.path.join(TEST_DATA, filename)

    with open(filepath) as f:
        content = f.read()

    return content.strip()
