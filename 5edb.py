from lxml import etree
from itertools import groupby
from collections import defaultdict

debug = print

debug('Parsing xml...')
parser = etree.XMLParser()
with open('FC5eXML/CoreOnly.xml', 'r') as xmlfile:
    tree = etree.parse(xmlfile, parser)
debug('...done')

spells = tree.xpath("//spell")
spell_nodes = tree.xpath("//spell/*")
print(len(spells))
print(len(spell_nodes))
print(dir(spell_nodes[0]))
print(spell_nodes[0].__class__)
print(spell_nodes[0].tag)

spell_tags = set((node.tag for node in spell_nodes))
print(spell_tags)

def group(iterable, key):
    ret = defaultdict(list)
    for i in iterable:
        ret[key(i)].append(i)
    return ret

spell_tag_groups = group(spell_nodes, lambda n: n.tag).items()
for k, g in spell_tag_groups:
    print("{0}: {1} nodes".format(k, len(g)))
    value_group = group(g, lambda n: n.text)
    if len(value_group.keys()) > 20:
        print("  {0} unique values".format(len(value_group.keys())))
    else:
        for h, i in value_group.items():
            print("  {0}: {1} nodes".format(h, len(i)))
