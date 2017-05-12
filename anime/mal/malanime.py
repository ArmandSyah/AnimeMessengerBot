from anime.mal import malsoup


class MalAnime(object):
    def __init__(self, url):
        """Computation of fields only done when necessary"""
        self._url = url
        self._synopsis = None
        self._names = None
        self._anime_type = None
        self._episodes = None
        self._status = None
        self._airdate = None
        self._source = None
        self._genres = None
        self._duration = None

    @property
    def synopsis(self):
        """Get Synopsis of anime from MAL anime page"""
        if self._synopsis is None:
            self._synopsis = malsoup.scrape_synopsis(self._url)
        return self._synopsis

    @property
    def names(self):
        """
        Get the different names of the anime from MAL anime page
        Returns a Dictionary in this form {'Main':, 'English':, 'Synonyms', 'Japanese'}
        Note: The value of 'Synonyms' is a list
        """
        if self._names is None:
            self._names = malsoup.scrape_names(self._url)
        return self._names

    @property
    def anime_type(self):
        """Get the anime's type from MAL anime page"""
        if self._anime_type is None:
            self._anime_type = malsoup.scrape_anime_type(self._url)
        return self._anime_type

    @property
    def episodes(self):
        """Get anime's number of episode from MAL anime page"""
        if self._episodes is None:
            self._episodes = malsoup.scrape_episodes(self._url)
        return self._episodes

    @property
    def status(self):
        """Get anime's airing status from MAL anime page"""
        if self._status is None:
            self._status = malsoup.scrape_status(self._url)
        return self._status

    @property
    def airdate(self):
        """Get anime's airdate from MAL anime page"""
        if self._airdate is None:
            self._airdate = malsoup.scrape_airdate(self._url)
        return self._airdate

    @property
    def source(self):
        """Get an anime's original source from MAL anime page"""
        if self._source is None:
            self._source = malsoup.scrape_source(self._url)
        return self._source

    @property
    def genres(self):
        """Get an anime's genre's from it's MAL anime page"""
        if self._genres is None:
            self._genres = malsoup.scrape_genres(self._url)
        return self._genres

    @property
    def duration(self):
        """Get the duration of an anime"""
        if self._duration is None:
            self._duration = malsoup.scrape_duration(self._url)
        return self._duration



