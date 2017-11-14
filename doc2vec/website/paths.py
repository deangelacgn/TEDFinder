import os

def url_docs(instance, filename):
    return "docs/%d/%s"%(instance.user.pk, filename.encode('utf-8'))
