-- ALTERAR TABELA
alter table empresas modify cnpj varchar(14)

-- ----------------------------------------------------------------

insert into empresas (nome, cnpj)
values
    ('Bom Dia e CIA', 34123666000159),
    ('Vale', 52870201000143),
    ('Cielo', 68825616000135)

-- DESCREVER TABELA
desc empresas

-- INSRINDO NA TABELA EMPRESA_UNIDADES
insert into empresas_unidades (empresas_id, cidade_id, sede)
values 
    (1, 8, 1),
    (1, 9, 0),
    (2, 8, 0),
    (2, 9, 1)