from parsivar import Normalizer
from parsivar import Tokenizer
from parsivar import FindStems
from parsivar import POSTagger

my_normalizer = Normalizer()
my_tokenizer = Tokenizer()
my_stemmer = FindStems()
my_tagger = POSTagger(tagging_model="stanford")  # tagging_model = "wapiti" or "stanford"

tokens = []
ignore = ['،', '؟']

f = open("zaban-e_atash.txt", "r")
for line in f:
    tmp_txt = line
    words = my_tokenizer.tokenize_words(my_normalizer.normalize(tmp_txt))
    for word in words:
        if word not in tokens:
            if word not in ignore:
                tokens.append(word)

f.close()

print("<table>")
print("<td>Stem</td><td>Token & POS</td>")

for token in tokens:
    stem = my_stemmer.convert_to_stem(token)
    token_pos = my_tagger.parse(my_tokenizer.tokenize_words(token))
    token_pos = token_pos[0]
    if token == stem:
        out1 = "<tr><td></td><td>%s</td></tr>" % (token_pos,)
        print(out1)
    else:
        out2 = "<tr><td>%s</td><td>%s</td></tr>" % (stem, token_pos)
        print(out2)

print("</table>")


