"""
Bertalign initialization
"""

__author__ = "Jason (bfsujason@163.com)"
__version__ = "1.1.0"

# configure logging for libraries, so that we don't
# interfere with the client code, see:
# https://docs.python.org/3/howto/logging.html
import logging

logging.getLogger("bertalign").addHandler(logging.NullHandler())

from bertalign.encoder import Encoder

# See other cross-lingual embedding models at
# https://www.sbert.net/docs/pretrained_models.html

model_name = "LaBSE"
model = Encoder(model_name)

from bertalign.aligner import Bertalign
