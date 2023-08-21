#Упрощенный вариант - бинарное дерево с балансировкой, добавление, удалением элементов.
#Необходимо превратить собранное на семинаре дерево поиска в полноценное левостороннее красно-черное дерево. 
#И реализовать в нем метод добавления новых элементов с балансировкой.

# вершина бинарного дерева, инициализируем данные, левый потомк, правый потомок, значение в узле
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
# класс для работы с бинарным деревом, 
# обьявляем указатель root, который по умолчанию изначльно принимает значение None
class Tree:
    def __init__(self):
        self.root = None

    def find(self,node, parent, value):         # если добавл.знач меньше знач в род.узле, 
                                                    # то новую вершину добавляем в левую ветвь, 
                                                    # иначе в правую. если знач уже есть то оно игнорируется.
        if node is None:
            return None, parent, False
        if value == node.data:
            return node, parent, True
        if value < node.data:
            if node.left:
                return self.find(node.left, node, value)
        if value > node.data:
            if node.right:
                return self.find(node.right, node, value)
            return node, parent, False       # если мы не нашли вершину соотв.значению value
        
        
# Метод который добавляет новые вершины в бинарное дерево
    
    def append(self, key: Node) -> Node:
        if self.root is None:
         self.root = key
         return key

        s, p, fl_find = self.find(self.root, None, key.data)
        if not fl_find and s:
            if key.data < s.data:
                s.left = key
            else:
                s.right =key
        return key
    
# метод отображения(печати) бинарного дерева
def show_tree(self, node):
    
    if node is None:
        return
    self.show_tree(node.left)
    print(node.data)
    self.show_tree(node.right)

# метод удаления листа (s- удаляемая вершина, p-родительская вершина для удаляемого s)

def del_list(self, s, p): 
    if p.left == s:
        p.left = None
    elif p.right == s:
        p.right = None
        
# метод удаления узла с одним потомком(если сущ-ет левый потомок или отсутствует правый потомок, тогда вершина s имеет одного потомка)        
def del_one_child(self, s, p): 
    if p.left ==s:
        if s.left is None:
            p.left = s.right
        elif s.right is None:
            p.left = s.left
    elif p.right == s:          # вершина подцеплена к правой ветве
        if s.left is None:
            p.right = s.right
        elif s.right is None:
            p.right = s.left
            
# метод нахождения минимального значения и его родителя
def search_min(self, node, parent):
    if node.left:
        return self.__search_min(node.left, node)
    return node, parent

# метод удаления вершины бинарного дерева                  
def delete_node(self, mark):
    s, p, fl_find = self.find(self.root, None, mark)
    if not fl_find:
        return None
    
    if s.left is None and s.right is None:
        self.del_list(s, p)
    elif s.left is None or s.right is None:
        self.del_one_child(s, p)
    else:
        sr, pr = self.search_min(s.right, s)
        s.date = sr.data
        self.del_one_child(sr, pr)

a = [10, 3, 7, 15, 14, 2, 25]
b = Tree()
for c in a:
    b.append(Node(c))
b.delete_node(3)
b.show_tree(b.root)
            