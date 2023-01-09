-- Criando a tabela estado
create table estados (
    -- VALOR NUMERICO FORMADO AUTOMATICAMENTE PELO "AUTO_INCREMENT" 
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    -- CONTER NO MAXIOMO 45 CARACTERS
    nome VARCHAR(45) NOT NULL,
    sigla VARCHAR(2) NOT NULL,
    -- O VALOR DEVERA SER ALGUM DESSES
    regiao ENUM('Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul') NOT NULL,
    populacao DECIMAL(5, 2) NOT NULL,

    -- DEFININDO A CHAVE PRIMARIA
    PRIMARY KEY (id),
    -- DEFININDO OS VALORES UNICOS QUE NÃO PODEM SE REPETIR
    UNIQUE KEY (nome),    
    UNIQUE KEY (sigla)
)