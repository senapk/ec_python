# Python para ED

Após criar o Codespace ou abrir o código no VSCODE, sugiro abrir o arquivo de configurações, utilizando o atalho: Control Vírgula 

Depois clique no ícone do topo do arquivo com a setinha que possui a label **abrir JSON de configurações** e adicione as seguintes entradas.


```json
{
    "python.analysis.diagnosticMode": "workspace",
    "python.analysis.typeCheckingMode": "strict",
    "python.languageServer": "Pylance"
}
```


No cabeçalho dos códigos python, utilize

```py
from __future__ import annotations # permite referenciar o tipo nos protótipos dos métodos


class Node:
    def __init__(self, data: int, next: Node | None = None) -> None:
        self.data = data
        self.next = next
```