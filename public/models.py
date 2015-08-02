from datetime import datetime
from elasticsearch_dsl import DocType, String, Date, Integer
from elasticsearch_dsl.connections import connections


connections.create_connection()

#example class
'''
class Article(DocType):
    title = String(analyzer='snowball', fields={'raw': String(index='not_analyzed')})
    body = String(analyzer='snowball')
    tags = String(index='not_analyzed')
    created_at = Date()
    lines = Integer()

    class Meta:
        index = 'articles'

    def save(self, ** kwargs):
        self.lines = len(self.body.split())
        return super(Article, self).save(** kwargs)

    def is_published(self):
        return datetime.now() < self.published_from
'''


#example search

#Article.search().filter().sort().execute()





