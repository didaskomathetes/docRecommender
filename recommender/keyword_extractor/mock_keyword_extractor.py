
keywords= {"Fahrtkosten":{"Benzinkosten","Fahrtkosten","Kraftstoffkosten"},
           "1%-Regel":{"1 %-Regelung","1 %-Regel","1%-Regel"},
           "Firmenwagen":{"Firmenwagen","Dienstwagen"},
           "geldwerter Vorteil":{"geldwerter Vorteil","geldwerten Vorteil","geldwerte Vorteil"},
           "Privatnutzung":{"privaten nutz","privaten Nutz","privat nutz","Privatnutz","privat genutz"}
           }

def extract_keywords(document_string):
    tags=[]
    for keyword in keywords:
        if document_string != None:
            for phrase in keywords[keyword]:
                if(document_string.__contains__(phrase)):
                    tags.append(keyword)
                    break

    return tags

def tag_with_keywords(document_iterable):
    tagged_docs=[]
    for document in document_iterable:
        tagged_docs.append((document,extract_keywords(document)))
    return tagged_docs

def score_and_recommend(input,tagged_documents,n):
    input_tags=extract_keywords(input)
    partial_score=1.0/len(input_tags)
    scored_docs=[]
    for tagged_doc in tagged_documents:
        score=0.0
        for tag in tagged_doc[1]:
            if tag in input_tags:
                score+=partial_score
        scored_docs.append((score,tagged_doc[0]))
    scored_docs.sort(reverse=True)
    return scored_docs[0:n]

with open("../../data/text-snippets-de.txt") as f:
    content = f.readlines()
tagged_docs=tag_with_keywords(content)
scored_docs=score_and_recommend("Mit meinem Arbeitgeber habe ich vereinbart, dass ich die Benzinkosten selbst bezahle, wenn ich meinen Firmenwagen privat nutze. Reduziert dies den zu versteuernden geldwerten Vorteil, den ich nach der 1%-Regel bestimme?",tagged_docs,10)
for doc in scored_docs:
    print(f"score: {doc[0]}, text:{doc[1]}")