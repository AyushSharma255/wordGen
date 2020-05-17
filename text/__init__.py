import pkgutil

adj = pkgutil.get_data(__name__, "adjective.txt").decode()
noun = pkgutil.get_data(__name__, "noun.txt").decode()