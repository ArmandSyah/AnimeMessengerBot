import os
import re

import spice_api as spice

from settings import configloading as config
from anime import utilities


def get_mal_links(title):
    """Iterates through all search methods until link is constructed"""
    mal_regex = re.compile(r'http(s)?://myanimelist.net/anime/([0-9]){1,5}(/.*)?')
    link_dispatcher = {'spice': _get_mal_links_by_spice,
                       'mal': _get_mal_links_by_mal_api,
                       'brute': _get_mal_links_by_brute_force}

    for _, v in link_dispatcher.items():
        mal_url = v(title)
        if mal_url is None:
            continue
        if re.match(mal_regex, mal_url) is not None:
            return mal_url

    return


def _get_mal_links_by_spice(title):
    """Use Spice_API MAL Wrapper to retrive anime_id and use it to construct MAL link"""
    mal_config = config.load_mal_config()
    try:
        mal_credentials = spice.init_auth(mal_config['mal_username'], mal_config['mal_password'])
        mal_search = spice.search(title.strip(), spice.get_medium('anime'), mal_credentials)
        anime_id = mal_search[0].id
    except:
        return
    mal_url = f"https://myanimelist.net/anime/{anime_id}"
    return mal_url


def _get_mal_links_by_mal_api(title):
    """Use MAL's Official API to retrieve anime_id and use it to construct a MAL link"""
    mal_config = config.load_mal_config()
    try:
        mal_api_search = f"https://myanimelist.net/api/anime/search.xml?q={title.strip()}"
        mal_credentials = (mal_config['mal_username'], mal_config['mal_password'])
        mal_request = utilities.make_get_request(mal_api_search, mal_credentials)
        mal_soup = utilities.make_beatiful_soup_url(mal_request.text, 'lxml')
        mal_entries = mal_soup.anime
        anime_listings = [anime for anime in mal_entries.findAll('entry')]
        anime_id = anime_listings[0].id.get_text()
        mal_url = f"https://myanimelist.net/anime/{anime_id}"
    except:
        return
    return mal_url


def _get_mal_links_by_brute_force(title):
    """Enter anime into MAL search bar and scrape for the first available MAL anime link"""

    title = "%20".join(title.split(" "))
    mal_search_url = f"https://myanimelist.net/anime.php?q={title}"
    mal_request = utilities.make_get_request(mal_search_url)
    soup = utilities.make_beatiful_soup_url(mal_request, "html.parser")
    links = [element.get("href") for element in soup.select("a.hoverinfo_trigger.fw-b.fl-l", limit=5)]
    mal_url = links[0]
    return mal_url


def main():
    print(_get_mal_links_by_mal_api('naruto'))

if __name__ == '__main__':
    os.chdir('\\'.join(os.getcwd().split('\\')[:-1]))
    main()