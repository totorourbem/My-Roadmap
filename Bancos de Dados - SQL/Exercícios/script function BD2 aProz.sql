-- Função para somar clientes cadastrados em um dia específico

CREATE FUNCTION contar_clientes_por_data(p_data DATE)
RETURNS INTEGER
AS
$$
    DECLARE
        total_clientes INTEGER;
    BEGIN
        SELECT COUNT(*) INTO total_clientes
        FROM clientes
        WHERE DATE(data_cadastro) = DATE(p_data);
        
        RETURN total_clientes;
    END;
$$
LANGUAGE PLSQL; -- Defina a linguagem como PLSQL para usar a sintaxe da linguagem procedural

-- Obs: A tabela clientes é criada com colunas para o ID do cliente, o nome do cliente e a data de cadastro.
-- A função contar_clientes_por_data recebe uma data como parâmetro e retorna o total de clientes cadastrados nessa data.

-- Exemplo de uso da função
SELECT contar_clientes_por_data('2024-02-01') AS total_clientes_cadastrados;
