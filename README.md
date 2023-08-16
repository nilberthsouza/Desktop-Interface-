
# Part Manager GUI

Este é um aplicativo de gerenciamento de peças (partes) construído com Tkinter, uma biblioteca de interface gráfica em Python. O aplicativo permite que você adicione, remova e atualize informações sobre diferentes partes, como nome da peça, cliente, varejista e preço.

## Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. A biblioteca Tkinter é parte do pacote padrão do Python, então não é necessário instalar nada adicionalmente.

## Como usar

1. Clone ou faça o download deste repositório.

2. Abra o arquivo `main.py` em um editor de código ou ambiente de desenvolvimento Python.

3. Execute o script usando o seguinte comando:

```
python main.py
```

Uma janela de interface gráfica será aberta, exibindo uma interface de gerenciamento de peças.

## Funcionalidades

O aplicativo possui as seguintes funcionalidades:

- **Adicionar Parte:** Insira o nome da peça, nome do cliente, nome do varejista e preço nos campos apropriados e clique no botão "Add Part" para adicionar a parte à lista.

- **Seleção de Parte:** Clique em uma parte na lista para selecioná-la. As informações dessa parte serão exibidas nos campos de entrada acima da lista.

- **Remover Parte:** Com uma parte selecionada, clique no botão "Remove" para remover a parte selecionada da lista.

- **Atualizar Parte:** Após selecionar uma parte, você pode atualizar suas informações nos campos de entrada e, em seguida, clicar no botão "Update" para salvar as alterações.

- **Limpar Entradas:** Clique no botão "Clear Input" para limpar todos os campos de entrada.

## Interface Gráfica (GUI)

O código inclui uma interface gráfica que permite uma interação amigável com o usuário. Você pode adicionar, remover e atualizar informações sobre as partes usando a interface.

## Banco de Dados

O aplicativo utiliza um banco de dados SQLite chamado `store.db` para armazenar as informações das partes. Certifique-se de que o arquivo `db.py` esteja presente e configurado corretamente para o funcionamento adequado do banco de dados.
