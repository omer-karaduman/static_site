class TextNode:
    def __init__(self,text,text_type,url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: object) -> bool:
        return value.text == self.text and value.text_type== self.text_type and self.url ==value.url
    
    def __repr__(self) -> str:
        
        return f"TextNode({self.text}, {self.text_type}, {self.url})"