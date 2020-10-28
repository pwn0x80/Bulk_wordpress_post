from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
import login
import sys
                         

try:
    website_url = sys.argv[1]
except:
    sys.exit()




path = website_url
post = WordPressPost()

post.post_status = 'publish' # to publish post


wp = Client(login.website, login.username, login.password)


post.title = a[1]
a = open(path, "r")
z = a.read()
post.content = z

post.terms_names = {
    'post_tag': ['demo', 'hello world'],
    'category': ['demo']
 }

wp.call(NewPost(post))
