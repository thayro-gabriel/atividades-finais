INSERT INTO Clientes (ID_Cliente, Nome, Email, Telefone, Endereço) VALUES
(1, 'João Silva', 'joao@email.com', '123456789', 'Rua A, 123'),
(2, 'Maria Oliveira', 'maria@email.com', '987654321', 'Rua B, 456');

INSERT INTO Categorias (ID_Categoria, Nome) VALUES
(1, 'Camisetas'),
(2, 'Calças');

INSERT INTO Fornecedores (ID_Fornecedor, Nome, Contato) VALUES
(1, 'Fornecedor A', 'contato@fornecedora.com'),
(2, 'Fornecedor B', 'contato@fornecedorb.com');

INSERT INTO Produtos (ID_Produto, Nome, Preço, ID_Categoria, ID_Fornecedor) VALUES
(1, 'Camiseta Branca', 29.90, 1, 1),
(2, 'Calça Jeans', 99.90, 2, 2);

INSERT INTO Pedidos (ID_Pedido, Data, ID_Cliente) VALUES
(1, '2024-07-01', 1),
(2, '2024-07-02', 2);

INSERT INTO Itens_Pedido (ID_Item_Pedido, ID_Pedido, ID_Produto, Quantidade) VALUES
(1, 1, 1, 2),
(2, 2, 2, 1);

UPDATE Produtos
SET Preço = 34.90
WHERE ID_Produto = 1;

DELETE FROM Clientes
WHERE ID_Cliente = 2;

SELECT Clientes.Nome, Produtos.Nome, Itens_Pedido.Quantidade
FROM Pedidos
JOIN Itens_Pedido ON Pedidos.ID_Pedido = Itens_Pedido.ID_Pedido
JOIN Produtos ON Itens_Pedido.ID_Produto = Produtos.ID_Produto
JOIN Clientes ON Pedidos.ID_Cliente = Clientes.ID_Cliente
WHERE Clientes.ID_Cliente = 1;

SELECT ID_Cliente, COUNT(*) AS Total_Pedidos
FROM Pedidos
GROUP BY ID_Cliente
ORDER BY Total_Pedidos DESC;

