from htmlnode import HTMLNode
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        props  = {
                    "href": "https://www.google.com", 
                    "target": "_blank"
                }
        tag = "p"
        value = "test1"
        htmlnode = HTMLNode(props=props,tag=tag,value=value)
        result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(htmlnode.props_to_html(),result)

        props2 = {"href": "x.com",
                  "target":"_blank"}
        value2 = "test2"
        tag2 = "h1"
        htmlnode2 = HTMLNode(props=props2,tag=tag2,value=value2)
        result2 = ' href="x.com" target="_blank"'
        self.assertEqual(htmlnode2.props_to_html(),result2)

        props3 = {"href": "xxx.com",
                  "target":"_blank"}
        value3 = "test3"
        tag3 = "h2"
        htmlnode3 = HTMLNode(props=props3,tag=tag3,value=value3)
        result3 = ' href="xxx.com" target="_blank"'
        self.assertEqual(htmlnode3.props_to_html(),result3)

    def test_leaf(self):
        props  = {
                    "href": "https://www.google.com", 
                    "target": "_blank"
                }
        tag = "p"
        value = "test1"
        htmlnode = HTMLNode.LeafNode(props=props,tag=tag,value=value)
        result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(htmlnode.to_html(),result)

        
if __name__ == "__main__":
    unittest.main()