class Node:
    def __init__(self, key: int) -> None:
        self.left: Node | None = None  # Ponteiro para o nó à esquerda
        self.right: Node | None = None  # Ponteiro para o nó à direita
        self.value: int = key  # Valor armazenado no nó

class BST:
    def __init__(self) -> None:
        self.root: Node | None = None  # Raiz da árvore

    def insert(self, key: int) -> None:
        """Insere um valor na árvore de busca binária."""
        if self.root is None:
            self.root = Node(key)
        else:
            BST.__insert(self.root, key)

    @staticmethod
    def __insert(node: Node, key: int) -> None:
        """Função recursiva estática para inserir um nó na posição correta."""
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                BST.__insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                BST.__insert(node.right, key)

    def search(self, key: int) -> bool:
        """Método público que chama a busca na raiz da árvore."""
        return BST.__search(self.root, key)

    @staticmethod
    def __search(node: Node | None, key: int) -> bool:
        """Procura um valor na árvore de busca binária."""
        if node is None:
            return False
        if key == node.value:
            return True
        elif key < node.value:
            return BST.__search(node.left, key)
        else:
            return BST.__search(node.right, key)

    def inorder(self) -> None:
        """Método público que chama a travessia em ordem na raiz da árvore."""
        print("[ ", end="")
        BST.__inorder(self.root)
        print("]")

    @staticmethod
    def __inorder(node: Node | None) -> None:
        """Função recursiva estática para percorrer a árvore em ordem."""
        if node is not None:
            BST.__inorder(node.left)
            print(node.value, end=" ")
            BST.__inorder(node.right)

# Exemplo de uso:
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Busca por 40:", bst.search(40))  # Saída: True
print("Busca por 100:", bst.search(100))  # Saída: False

print("Traversal In-order:")
bst.inorder()  # Saída: 20 30 40 50 60 70 80
