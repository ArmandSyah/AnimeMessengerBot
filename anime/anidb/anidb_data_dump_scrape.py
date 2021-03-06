from anime import utilities


def _scrape_anidb_data_dump():
    """
        Open up anidb dat file, containing anime titles and id's and writting them to a text file
        DO NOT RUN THIS MODULE MORE THAN ONCE A DAY
    """

    anidb_request = utilities.make_get_request("http://anidb.net/api/anime-titles.dat.gz")
    with open('AniDBTitles.txt', 'w', encoding='utf8') as ani:
        ani.write(anidb_request.text)


def _scrape_anidb_xml():
    """
        Open up AniDB's XML dump and copy it into our xml
        DO NOT RUN THIS MODULE MORE THAN ONCE A DAY
    """
    anidb_request = utilities.make_get_request("http://anidb.net/api/anime-titles.xml.gz")
    with open('AniDBTitlesXML.txt', 'w', encoding='utf8') as ani:
        ani.write(anidb_request.text)


def main():
    _scrape_anidb_data_dump()
    _scrape_anidb_xml()


if __name__ == '__main__':
    main()
