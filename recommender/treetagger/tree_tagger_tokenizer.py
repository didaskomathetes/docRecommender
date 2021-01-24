import treetaggerwrapper

tagger = treetaggerwrapper.TreeTagger(TAGLANG='de', TAGDIR="../treetagger_linux")
invalid_chars = ['@', '-', ',', ';', ')', '(', ':', '/', '\\', '=', '--', "'", '"', '#', '‘', '*', '+']
debug=False

def tokenize(string):
    tagged_sentence = tagger.tag_text(string)
    tokens = []
    for token in tagged_sentence:
        try:
            index = token.rindex("\t")
            lemmatized_token = token[index + 1:len(token)]
            if lemmatized_token not in (invalid_chars):
                tokens.append(lemmatized_token)
        except:
            if debug==True:
                print(f"Couldn't find lemma for token:{token}. Probably Garbage. Ignoring it.")
            continue
    return tokens