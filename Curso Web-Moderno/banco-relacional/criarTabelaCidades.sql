-- CRIA A A TABELA SE ELA NÃO EXISTIR
create table if not exists cidades (
    id int not null AUTO_INCREMENT,
    nome varchar(255) not null,
    estado_id int unsigned not null,
    area decimal(10, 2),

    primary key (id),
    foreign key (estado_id) references `estados` (id)
)

-- DELETA TABELA SE ELA EXISTIR
drop table id exists [tabela]