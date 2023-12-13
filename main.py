# encoding: utf-8
# basic usage for the library

import pathlib
import whoosh
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser


def main():
    # create schema
    schema = Schema(title=TEXT(stored=True),
                    path=ID(stored=True), content=TEXT)

    # test indexdir
    pathlib.Path("tests/indexdir").mkdir(exist_ok=True)

    # create index
    ix = create_in("tests/indexdir", schema)
    writer = ix.writer()
    writer.add_document(title=u"First document", path=u"/a",
                        content=u"This is the first document we've added!")
    writer.add_document(title=u"Second document", path=u"/b",
                        content=u"The second one is even more interesting!")
    writer.commit()

    # search
    searcher = ix.searcher()
    parser = QueryParser("content", ix.schema)
    myquery = parser.parse(u"first")
    results = searcher.search(myquery)
    print(results[0])


if __name__ == '__main__':
    main()
