
keywords= {"Fahrtkosten":{"Benzinkosten","Fahrtkosten","Kraftstoffkosten"},
           "1%-Regel":{"1 %-Regelung","1 %-Regel","1%-Regel"},
           "Firmenwagen":{"Firmenwagen","Dienstwagen"},
           "geldwerter Vorteil":{"geldwerter Vorteil","geldwerten Vorteil","geldwerten Vorteils"},
           "Privatnutzung":{"privaten nutz","privaten Nutz","privat nutz","Privatnutz"}
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

