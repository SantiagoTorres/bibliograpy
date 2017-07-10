#!/usr/bin/env python
#
# Copyright 2014-2017 Philipp Winter <phw@nymity.ch>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Helper module to write an atom/RSS feed for the given bibliography
"""
import sys

import os.path as path


try:
    from feedgen.feed import FeedGenerator
except ImportError:
    print >> sys.stderr, ("[+] In order to use the feed feature you need "
                          "feedgen\n\t (Did you run pip install feedgen?)")

from bibliogra import format_authors, format_url
    
def create_feed(bibdata, output_directory, filename="feed"):

    feed = FeedGenerator()

    def get_year(key):
        try:
            return bibdata.entries[key].fields["year"]
        except KeyError:
            return 0

    def get_venue(key):
        try:
            return bibdata.entries[key].fields["booktitle"]
        except KeyError:
            return 0

    for entry in sorted(bibdata.entries.keys(),
            key=lambda k: (get_year(k), get_venue(k)), reverse=True):
        _add_entry(bibdata.entries[entry], feed)


    # FIXME: probably a param to set the title would be convenient
    feed.title(filename)
    feed.description("Feed")
    feed.link({"href": "/"})

    feed.rss_file(path.join(output_directory, filename), pretty=True)

def _add_entry(bibentry, feed):
    entry = feed.add_entry()
    entry.title(bibentry.fields['title'].decode("latex"))
    entry.author(_format_authors(bibentry.persons))
    entry.guid(bibentry.key)
    entry.link({'href': "#%s" % bibentry.key})

def _format_authors(persons):

    author_str = format_authors(persons, None).replace("</br>", "")
    return [{'name': name} for name in author_str.split(",")]
