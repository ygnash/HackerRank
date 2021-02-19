############################################################################
#   Hackerrank Language
"""very submission at HackerRank has a field called language which indicates 
the programming language which a hacker used to code his solution.

C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:
ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART: GROOVY:OBJECTIVEC

Sometimes, error-prone API requests can have an invalid language field.
Could you find out if a given submission has a valid language field or not?
"""
#---------------------------------------------------------------------------
import re

lang_ls ='^\d{4,5}\s(C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC)$'
regex = re.compile(lang_ls.replace(':','|'))

print(*['VALID' if re.search(regex, input()) else 'INVALID' for _ in range(int(input()))], sep='\n')
#---------------------------------------------------------------------------
