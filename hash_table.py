class Node:
    def __init__(self, key: str, value: int) -> None:
        """Construtor para a classe Node.
        
        Args:
            key (str): A chave associada ao valor.
            value (int): O valor associado à chave.
        """
        self.key: str = key
        self.value: int = value
        self.next: Node | None = None


class HashTable:
    def __init__(self, size: int) -> None:
        """Construtor para a Tabela Hash.
        
        Args:
            size (int): O número de buckets na tabela hash.
        """
        self.size: int = size
        self.table: list[Node | None] = [None] * size
    
    def _hash(self, key: str) -> int:
        """Função hash simples para mapear a chave a um índice da tabela.
        
        Args:
            key (str): A chave a ser mapeada.
        
        Returns:
            int: O índice calculado para a chave.
        """
        return sum(ord(char) for char in key) % self.size
    
    def insert(self, key: str, value: int) -> None:
        """Insere um par chave-valor na tabela hash.
        
        Se a chave já existir, atualiza o valor.
        
        Args:
            key (str): A chave a ser inserida.
            value (int): O valor a ser associado à chave.
        """
        index: int = self._hash(key)
        new_node: Node = Node(key, value)
        
        if not self.table[index]:
            self.table[index] = new_node
        else:
            current: Node | None = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if not current.next:
                    current.next = new_node
                    break
                current = current.next
    
    def search(self, key: str) -> int | None:
        """Busca um valor pela chave na tabela hash.
        
        Args:
            key (str): A chave a ser buscada.
        
        Returns:
            int | None: O valor associado à chave, ou None se não encontrado.
        """
        index: int = self._hash(key)
        current: Node | None = self.table[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        return None
    
    def remove(self, key: str) -> bool:
        """Remove um par chave-valor da tabela hash.
        
        Args:
            key (str): A chave a ser removida.
        
        Returns:
            bool: True se o item foi removido, False caso contrário.
        """
        index: int = self._hash(key)
        current: Node | None = self.table[index]
        previous: Node | None = None
        
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                return True
            previous = current
            current = current.next
        
        return False
    
    def display(self) -> None:
        """Exibe a tabela hash com suas chaves e valores."""
        for index, node in enumerate(self.table):
            if node:
                current: Node | None = node
                print(f"Bucket {index}: ", end="")
                while current:
                    print(f"({current.key}, {current.value})", end=" -> ")
                    current = current.next
                print("None")
            else:
                print(f"Bucket {index}: None")
