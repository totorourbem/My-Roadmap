-- Ineer join, retorna o nome do aluno e a disciplina
-- IMPORTANTE apos o select, são elencadas as colunas a serem dispostas, de ambas tabelas
-- em ON, explicita a junção em si
-- retorna apenas os alunos que cursam alguma disciplina

SELECT nome_alunos, nome_disciplina FROM alunos
INNER JOIN disciplinas
ON disciplinas.id_disciplina = alunos.disciplinas_id;

-- left join, retorna  os dados da tabela à esquerda do digrama de venn
-- retorna todos os alunos (Esquerda de Venn) independente de terem curso ou não vinculados

SELECT nome_alunos, nome_disciplina FROM alunos
LEFT JOIN disciplinas
ON disciplinas.id_disciplina = alunos.disciplinas_id;

-- Right join, retorna  os dados da tabela à direita do digrama de venn
-- retorna todos as disciplinas (Direita de Venn) independente de terem alunos ou não vinculados

SELECT nome_alunos, nome_disciplina FROM alunos
RIGHT JOIN disciplinas
ON disciplinas.id_disciplina = alunos.disciplinas_id;

-- Full join/Full outer join ou Outer Join, retorna  os dados de ambas as tabelas
-- retorna todos as disciplinas (Direita de Venn) independente de terem alunos ou não vinculados
-- Em aguns SGBDs (como MySQL e SQLite), não são suportadas, sendo então representadas pelo comando union doo Letf Joine do Right Join correspondentes
-- no caso em tela, o resultado é igual ao left join.

SELECT nome_alunos, nome_disciplina FROM alunos
LEFT JOIN disciplinas
ON disciplinas.id_disciplina = alunos.disciplinas_id
UNION
SELECT nome_alunos, nome_disciplina FROM alunos
RIGHT JOIN disciplinas
ON disciplinas.id_disciplina = alunos.disciplinas_id;
