
def count_token_in_corpus(token):
    with open('corpus.txt', 'r') as file:
        corpus_content = file.read()
    return corpus_content.lower().count(token.lower())


def report_count(token):
    count = count_token_in_corpus(token)
    print(f"The term {token} shows up in the corpus {count} times.")