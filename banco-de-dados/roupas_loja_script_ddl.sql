CREATE TABLE Clientes (
    ID_Cliente INT PRIMARY KEY,
    Nome VARCHAR(100),
    Email VARCHAR(100),
    Telefone VARCHAR(15),
    Endereço VARCHAR(255)
);

CREATE TABLE Categorias (
    ID_Categoria INT PRIMARY KEY,
    Nome VARCHAR(100)
);

CREATE TABLE Fornecedores (
    ID_Fornecedor INT PRIMARY KEY,
    Nome VARCHAR(100),
    Contato VARCHAR(100)
);

CREATE TABLE Produtos (
    ID_Produto INT PRIMARY KEY,
    Nome VARCHAR(100),
    Preço DECIMAL(10, 2),
    ID_Categoria INT,
    ID_Fornecedor INT,
    FOREIGN KEY (ID_Categoria) REFERENCES Categorias(ID_Categoria),
    FOREIGN KEY (ID_Fornecedor) REFERENCES Fornecedores(ID_Fornecedor)
);

CREATE TABLE Pedidos (
    ID_Pedido INT PRIMARY KEY,
    Data DATE,
    ID_Cliente INT,
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente)
);

CREATE TABLE Itens_Pedido (
    ID_Item_Pedido INT PRIMARY KEY,
    ID_Pedido INT,
    ID_Produto INT,
    Quantidade INT,
    FOREIGN KEY (ID_Pedido) REFERENCES Pedidos(ID_Pedido),
    FOREIGN KEY (ID_Produto) REFERENCES Produtos(ID_Produto)
);
