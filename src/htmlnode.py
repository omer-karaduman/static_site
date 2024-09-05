class HTMLNode:
    def __init__(self,tag= None,value=None,children=None,props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        result = ""
        for item in self.props:
            result += f' {item}="{self.props[item]}"'
        return result
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    class LeafNode:
        def __init__(self,value,tag=None,props=None) -> None:
            HTMLNode.__init__(self,tag=tag,value=value,props=props)

        def to_html(self):
            if self.value == None:
                raise ValueError
            if self.tag == None:
                return self.value
            prop =self.props_to_html()

            return f"<{self.tag}{prop}>{self.value}<{self.tag}>"
    