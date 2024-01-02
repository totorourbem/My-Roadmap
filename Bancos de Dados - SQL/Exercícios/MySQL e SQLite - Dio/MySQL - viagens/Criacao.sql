CREATE DATABASE viagens;

USE viagens;

CREATE TABLE usuarios (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(255) NOT NULL UNIQUE COMMENT 'nome do usuário',
    dtnasc DATE COMMENT 'data de nascimento',
    endereco LONGTEXT NOT NULL COMMENT 'endereço completo',
    telefone_1 VARCHAR(20) COMMENT 'Telefone principal',
    telefone_2 VARCHAR(20) COMMENT 'Telefone secundário',
    telefone_3 VARCHAR(20) COMMENT 'Telefone opcional');
	
CREATE TABLE destinos (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(255) UNIQUE NOT NULL COMMENT 'local',
    descricao VARCHAR(255) NOT NULL COMMENT 'descrição detalhada');
    
CREATE TABLE reservas (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT NOT NULL COMMENT 'refere-se ao usuário',
    id_destino INT NOT NULL COMMENT 'refere-se ao destino',
	status ENUM ("pendente", "confirmado", "cancelado", "concluído") NOT NULL DEFAULT 'pendente',
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_destino) REFERENCES destinos(id)
);
    