-- Procedure para listar todos os alunos de uma disciplina
-- Finalidade evitar que Naives e usuários tenham acesso direto aas tabelas do banco
-- Exemplo de uso [CALL sp_listaralunos_por_disciplina('POO')]
-- Basiccamente, encapsula um inner join no procedure

CREATE PROCEDURE sp_listar_alunos_por_disciplina(
    IN p_nome_disciplina VARCHAR(50)
)

BEGIN
    SELECT nome_alunos 
    FROM alunos
    INNER JOIN disciplinas
    ON disciplinas.id_disciplina = alunos.disciplinas_id
    WHERE disciplinas.nome_disciplina = p_nome_disciplina;
END;

