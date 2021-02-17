############################################################################
#    XML 1 - Find the score
#---------------------------------------------------------------------------
import sys
import xml.etree.ElementTree as etree


# Sample I/P
xml ="""<feed xml:lang='en'>
        <title>HackerRank</title>
        <subtitle lang='en'>Programming challenges</subtitle>
        <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
        <updated>2013-12-25T12:00:00</updated>
        <entry>
            <author gender='male'>Harsh</author>
            <question type='hard'>XML 1</question>
            <description type='text'>This is related to XML parsing</description>
        </entry>
</feed>
"""

# SOLUTION 1
def get_attr_number(node):
    """This method take an XML element as a parameter and iterates over its child elements and return the total 
    sum of attributes in all the iterated elements
    """
    return len(node.attrib)+ sum(len(elm.attrib) if len(elm) == 0 else get_attr_number(elm) for elm in node)

# SOLUTION 2 - NAIVE SOLUTION
def get_attr_number_naive(node):
    """This method take an XML element as a parameter and iterates over its child elements and return the total 
    sum of attributes in all the iterated elements
    """
    total = len(node.attrib)
    for elm in node:
        if len(elm) == 0:
            total += len(elm.attrib)
        else:
            total += find_attrib(elm)
    return total

if __name__ == '__main__':
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
#---------------------------------------------------------------------------
