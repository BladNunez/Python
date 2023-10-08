class Node:
        def __init__(self,value,next_node = None):
                self.value = value
                self.next_node = next_node

        def get_value(self):
                return self.value
        
        def get_next_node(self):
                return self.next_node

        def set_next_node(self,new_node):
                self.next_node = new_node

class LinkedList:
        def __init__(self,value = None):
                self.head_node = Node(value)
        
        def get_head_node(self):
                return self.head_node
        
        def add_to_head(self,new_value):
                new_node = Node(new_value)
                new_node.set_next_node(self.head_node)
                self.head_node = new_node
        
        def print_list(self):
                current_head = self.head_node
                string_list = " "

                while current_head:
                        if current_head.get_value() != None:
                               string_list += str(current_head.get_value()) + "\n"
                        
                        current_head = current_head.get_next_node()
                
                return string_list

node = LinkedList(44)
node.add_to_head(34)
node.add_to_head(5)

print(node.print_list())
