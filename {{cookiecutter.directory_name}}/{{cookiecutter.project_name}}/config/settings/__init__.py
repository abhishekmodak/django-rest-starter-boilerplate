from .configurations import SETUP

if SETUP == "PRODUCTION":
    from .prod import *
else:
    from .dev import *
