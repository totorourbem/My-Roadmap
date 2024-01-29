CREATE TABLE aluno(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(50) NOT NULL,
  matricula INTEGER NOT NULL,
  email VARCHAR(50) NOT NULL,
  endereco VARCHAR(255),
  telefone VARCHAR(13)
)

INSERT INTO aluno (nome, matricula, email, endereco, telefone) VALUES
	("Joao Carlos", 1234, "jcarlos@gmail.com", "Rua 13 de Maio", "(11)7825-4489"),
    ("Joao Vitor", 2345, "jvitor@gmail.com", "Rua da Saudade", "(11)7825-6589"),
    ("Paulo Andre", 3456, "pandre@gmail.com", "Rua do Sol", "(11)7825-4495");

CREATE TABLE emprestimo(
  codigo INTEGER PRIMARY KEY AUTOINCREMENT,
  data_hora TIMESTAMP,
  matric_aluno INTEGER NOT NULL,
  data_devolucao DATE,
  FOREIGN KEY (matric_aluno) REFERENCES aluno(matricula)
)

INSERT INTO emprestimo (matric_aluno, data_devolucao) VALUES
	(1234, "2024-03-03"),
    (2345, "2024-03-02"),
    (3456, "2024-03-04");

CREATE TABLE sessao(
  codigo_sessao INTEGER PRIMARY KEY AUTOINCREMENT,
  descricao VARCHAR(50),
  localizacao VARCHAR(50)
)

INSERT INTO sessao (codigo_sessao, descricao,localizacao) VALUES
	("Sessão01", "Prateleira 15A"),
    ("Sessão01", "Prateleira 15B"),
    ("Sessão02", "Prateleira 13A");

CREATE TABLE livro(
  codigo_livro INTEGER PRIMARY KEY AUTOINCREMENT,
  titulo VARCHAR(255) NOT NULL,
  autor VARCHAR(255) NOT NULL,
  cod_sessao_liv INTEGER NOT NULL,
  FOREIGN KEY (cod_sessao_liv) REFERENCES sessao(codigo_sessao)
)

INSERT INTO livro (titulo, autor, cod_sessao_liv) VALUES
	("Modelos conceituais e diagramas de ER", "Prassmann, Roger S.", 03),
    ("Álgebra Relacional Básica", "Hauser, Carlos A.", 01),
    ("A linguagem SQL", "Beighley, Lynn", 02);

CREATE TABLE livro_emprestimo(
  cod_livro_emp INTEGER,
  cod_emprestimo INTEGER,
  FOREIGN KEY (cod_livro_emp) REFERENCES livro(cod_livro),
  FOREIGN KEY (cod_emprestimo) REFERENCES emprestimo(codigo)
)

INSERT INTO livro_emprestimo (cod_livro_emp, cod_emprestimo) VALUES
	(03, 01),
    (01, 03),
    (02, 02);
 
