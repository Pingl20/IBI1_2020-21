from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt

DOMTree = xml.dom.minidom.parse("D:\\Github\\IBI1_2020-21\\Practical14\\go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")

# create a dict to pair the is_a and id
go = {}

for term in terms:
    id = term.getElementsByTagName("id")[0].childNodes[0].data
    is_as = [child.childNodes[0].data for child in term.getElementsByTagName("is_a")]
    for is_a in is_as:
        if is_a in go:
            go[is_a].append(id)
        else:
            go[is_a] = [id]


def goName(terms, name):
    name_go = []
    for term in terms:
        if name in term.getElementsByTagName("defstr")[0].childNodes[0].data:
            name_go.append(term.getElementsByTagName('id')[0].childNodes[0].data)
    values = [i for value in go.values() for i in value]
    bug_child = []
    for id in name_go:
        if id not in list(go.keys()) + values:
            bug_child.append(id)
    return name_go, bug_child

def allChildren(go, name_go):
    name_child = []
    for name in name_go:
        if name not in go:
            name_child.append(name)
        else:
            name_child.append(name)
            children = [child for child in go[name]]
            name_child += allChildren(go, children)
    return name_child

def printResult(go, name_go, name, bug_name):
    name_count = len(list(set(allChildren(go, name_go)))) - len(name_go) - len(bug_name)
    return name_count
# DNA
dna, bug_dna = goName(terms, "DNA")
print("The number of childNodes for each DNA-related gene is {}".format(printResult(go, dna, "DNA", bug_dna)))
    # Output: The number of childNodes for each DNA-related gene is 7271

# RNA
rna, bug_rna = goName(terms, "RNA")
print("The number of childNodes for each RNA-related gene is {}".format(printResult(go, rna, "RNA", bug_rna)))
    # Output: The number of childNodes for each RNA-related gene is 8927

# protein
protein, bug_protein = goName(terms, "protein")
print("The number of childNodes for each protein-related gene is {}".format(printResult(go, protein, "protein", bug_protein)))
    # Output: The number of childNodes for each protein-related gene is 27771

# glycoprotein
glycoprotein, bug_glycoprotein = goName(terms, "glycoprotein")
print("The number of childNodes for each glycoprotein-related gene is {}".format(printResult(go, glycoprotein, "glycoprotein", bug_glycoprotein)))
    # Output: The number of childNodes for each glycoprotein-related gene is 150

labels = 'DNA', 'RNA', 'protein', 'glycoprotein'
values = [printResult(go, dna, "DNA", bug_dna), printResult(go, rna, "RNA", bug_rna),
          printResult(go, protein, "protein", bug_protein), printResult(go, glycoprotein, "glycoprotein", bug_glycoprotein)]
plt.pie(values, labels = labels, autopct='%1.1f%%',shadow=False)
plt.title("Child Nodes of 4 macromolecules")
plt.show()