"""
Based on data from lyrics.com, tell me which album has
the most songs for a given artist.

"""
BASE = 'http://lyrics.wikia.com/api.php?'
QS_BASE = {
    'action': 'lyrics',
    'fmt': 'realjson',
    'func': 'getSong',
    'limit': 1000,
}



if __name__ == '__main__':
    import json
    import sys
    from operator import itemgetter
    from urllib import request, parse

    artist = sys.argv[1]
    qs_args = {
        'artist': artist,
        **QS_BASE
    }

    url = BASE + parse.urlencode(qs_args) 

    with request.urlopen(url) as response:
        content = response.read().decode('ascii')
        data = json.loads(content)
        counts = {}
        for album in filter(lambda a: a['year'] is not None, data['albums']):
            counts[album['album']] = len(album['songs'])

    fewest_to_most_songs = sorted(counts.items(), key=itemgetter(1))
    name, count = fewest_to_most_songs[0]
    print(
        'The album from {artist} with fewest songs is "{name}", with {count}'
        .format(**locals())
    )

