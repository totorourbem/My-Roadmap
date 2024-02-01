-- Trigger para immpedir exclusão de disciplinas usadas por alunos
-- é acionado antes da exclusão (BEFORE DELETE ON)
-- Verifca os registros na tabela disciplinas
-- O trigger é aplicado a cada linha que for afetada na operação (FOR EACH ROW)
-- BEGIN e END são palavras reservadas que delimitam a ação do trigger
-- Seleciona um erro do tipo Abortar operação (RAISE(ABORT...)
-- A sentença seguinte eé uma explicação sincrética do erro
-- a tarefa em si executa um SELECT aninhado, com as condições de wwhere
 

CREATE TRIGGER tr_impedir_exclusao_disciplina
BEFORE DELETE ON disciplinas
FOR EACH ROW
BEGIN
    SELECT RAISE(ABORT, 'Não é possível excluir disciplina associada a alunos')
    WHERE (SELECT COUNT(*) FROM alunos WHERE disciplinas_id = OLD.id_disciplina) > 0;
END;