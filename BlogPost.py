# from wordpress_xmlrpc import Client, WordPressPost
# from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
# from wordpress_xmlrpc.methods.users import GetUserInfo

# from wordpress_xmlrpc import Client, WordPressPost
# from wordpress_xmlrpc.compat import xmlrpc_client
# from wordpress_xmlrpc.methods import media, posts

# import collections
# collections.Iterable = collections.abc.Iterable
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# import collections
# try:
#     collectionsAbc = collections.abc
# except AttributeError:
#     collectionsAbc = collections

from Blog import Blog

class BlogPost:
    def __init__(self, title = None, content = None, tags = None) -> None:
        self.title = title
        self.content = content
        self.tags = tags

    def update_to_blog(self):
        blog = Blog()
        blog.post(title=self.title,content=self.content, tags= self.tags)

def test_blog_post():
    post = BlogPost()
    post.title = 'Test'
    post.content = 'test'
    post.tags = ['auto','test']

    post.update_to_blog()

test_blog_post()