
from topicmod.corpora.proto.corpus_pb2 import *
from topicmod.util import flags
from topicmod.corpora.pang_lee_movie import PangLeeMovieCorpus

flags.define_string("base", "../../data/movies/", "Where we look for data")
flags.define_string("output", "/tmp/", "Where we write output")
flags.define_string("response", "rating", "Which rating format we use")
flags.define_int("doc_limit", -1, "How many documents we add")

if __name__ == "__main__":
  flags.InitFlags()
  corpus = PangLeeMovieCorpus(flags.base, flags.doc_limit)
  corpus.add_language("pang_lee/*/subj.*", flags.response, ENGLISH)
  corpus.write_proto(flags.output + "numeric", "movies", 1000)

  corpus = PangLeeMovieCorpus(flags.base, flags.doc_limit)
  corpus.add_language("filmrezension.de_lines/*/subj.*", flags.response, \
                        GERMAN)
  corpus.write_proto(flags.output + "numeric", "movies", 100)
