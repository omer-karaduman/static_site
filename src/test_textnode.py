import unittest

from textnode import TextNode
from inline_markdown import split_nodes_delimiter,extract_markdown_images,extract_markdown_links,split_nodes_link,split_nodes_image,text_to_textnodes


class TestTextNode(unittest.TestCase):
    def test1(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "text",
        )
        
        nodes = [ TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "text",
        ),
        TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)","image")]
        
        textt = "his is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        text_to_textnodes(textt)


if __name__ == "__main__":
    unittest.main()
