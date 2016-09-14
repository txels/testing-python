"""
Retrieve lyrics from songs and count most used words

python -m songs.lyrics "Beatles" "All you need is love"
python -m songs.lyrics "The Police" "Roxanne"
python -m songs.lyrics "Alter Bridge" "Blackbird"
python -m songs.lyrics "Yes" "Close to the Edge"
python -m songs.lyrics "Bruce Springsteen" "The River"
python -m songs.lyrics "Marillion" "Kayleigh"

"""

BASE = 'http://api.chartlyrics.com/apiv1.asmx/SearchLyricDirect?'


if __name__ == '__main__':
    import json
    import sys
    from collections import Counter
    from operator import itemgetter
    from urllib import request, parse
    import xml.etree.ElementTree as ET

    artist, song = sys.argv[1:]

    qs_args = {
        'artist': artist,
        'song': song,
    }

    url = BASE + parse.urlencode(qs_args)

    with request.urlopen(url) as response:
        content = response.read().decode('ascii')
        data = ET.fromstring(content)

    lyric_elem = data.find('{http://api.chartlyrics.com/}Lyric')
    lyric = lyric_elem.text

    print(lyric, '\n\n\n')
    print('-' * 80)

    clean_lyrics = lyric.lower()
    words = clean_lyrics.split()
    word_count = Counter(words)

    print('"{}" by {} has {} words'.format(song, artist, len(words)))
    print('Distinct words:', len(word_count.keys()))
    print('Most used words:')
    print(word_count.most_common(5))
    print('-' * 80)
    print('This song is about', word_count.most_common(1)[0][0])
