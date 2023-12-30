-- Criação da tabela Alunos
CREATE TABLE Alunos (
    Id SERIAL PRIMARY KEY,
    Nome VARCHAR(255) NOT NULL,
    Idade VARCHAR(50),
    IdadePadronizada VARCHAR(50),
    Estado VARCHAR(50),
    UF VARCHAR(2),
    Graduacao VARCHAR(255),
    Hobby VARCHAR(255),
    ProfissaoAtual VARCHAR(255),
    ProfissaoPretendida VARCHAR(255),
    SalarioPretendidoMin INT,
    SalarioPretendidoMax INT
);

-- Criação da tabela Nomes
CREATE TABLE Nomes (
    ID_Aluno INT PRIMARY KEY,
    Nome_Aluno VARCHAR(255),
    Nome_Zoom VARCHAR(255),
    FOREIGN KEY (ID_Aluno) REFERENCES Alunos (ID)
);

-- Criação da tabela Presencas
CREATE TABLE Presencas (
    PresencaID SERIAL PRIMARY KEY,
    Full_Name VARCHAR(255),
    First_Seen TIMESTAMP,
    Time_in_Call INTERVAL
);

-- Importar os dados clicando com o botão direito na Tabela e em seguida em Import Data

-- Verificação
SELECT * FROM alunos;
SELECT * FROM nomes;
SELECT * FROM presencas;