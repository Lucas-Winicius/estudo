create table if not exists empresas (
    id int unsigned not null auto_increment,
    nome varchar(255),
    cnpj int unsigned,

    primary key (id),
    unique key (cnpj)
)

-- ----------------------------------------------------------------

create table if not exists empresas_unidades (
    empresas_id int unsigned not null,
    cidade_id int unsigned not null,
    sede tinyint(1) not null,

    primary key (empresas_id, cidade_id)
)