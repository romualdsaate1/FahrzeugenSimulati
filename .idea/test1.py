import pygame
from xml.etree.ElementTree import ElementTree
tree = ElementTree()
tree.parse("index.xml")
p = tree.find("body/p")     # Finds first occurrence of tag p in body
links = p.getiterator("a")  # Returns list of all links
for i in links:
    i.attrib["target"] = "blank"
    tree.write("output.xml")     # Iterates through all found links
