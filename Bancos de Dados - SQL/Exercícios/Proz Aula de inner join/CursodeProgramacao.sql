CREATE TABLE disciplinas (
    id_disciplina INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_disciplina VARCHAR(50) NOT NULL,
    nome_professor VARCHAR(50) NOT NULL
);

INSERT INTO disciplinas (nome_disciplina, nome_professor) VALUES
    ('Banco de dados', 'Maria Alves'),
    ('Python', 'Pietro Souza'),
    ('POO', 'Bia Tavares');

CREATE TABLE alunos (
    id_alunos INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_alunos VARCHAR(50) NOT NULL,
    disciplinas_id INTEGER,
    CONSTRAINT fk_disciplinas 
        FOREIGN KEY (disciplinas_id)
        REFERENCES disciplinas (id_disciplina)
);

INSERT INTO alunos (nome_alunos, disciplinas_id) VALUES
    ('Cleiton', 2),
    ('Carol', null),
    ('Ruan', 2),
    ('Gabi', 1),
    ('Ryan', null),
    ('Mia', 2),
    ('Malu', 1);