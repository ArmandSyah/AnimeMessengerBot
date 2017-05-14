def get_animeid(title):
    """Searches through AniDB Titles found in AniDBTitles.txt"""
    with open('AniDBTitles.txt', 'r', encoding='utf8') as ani:
        anidb_titles = ani.read()
        anidb_titles = anidb_titles.split("\n")
        anidb_titles = [t.lower() for t in anidb_titles if "|en|" in t or "|x-jat|" in t]
    anime_dict = {}
    for anime in anidb_titles:
        anime = anime.split("|")
        anime_dict[anime[3].lower()] = anime[0]
    return anime_dict[title.lower()]


def get_animeid_xml(title, anidb_soup):
    anidb_id = None
    for anime in anidb_soup.findAll('anime'):
        for anidb_title in anime.findAll('title'):
            if anidb_title.get_text().lower() == title.lower():
                anidb_id = anime['aid']
                break
        if anidb_id is not None:
            break
    return anidb_id