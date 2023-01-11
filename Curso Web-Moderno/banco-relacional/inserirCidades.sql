insert into cidades (nome, area, estado_id)
values ('Campinas', 795, 25)


insert into cidades (nome, area, estado_id)
values ('Niterói', 133.9, 19)

-- ----------------------------------------------------------------

insert into cidades (nome, area, estado_id)
-- SELECIONA O ID QUE CONTEM A SIGLA "PE"
values(
    'Caruaru',
    920.6,
    (select id from estados where sigla = "PE")
)

-- ----------------------------------------------------------------

insert into cidades (nome, area, estado_id)
values(
    'Juazeiro do Norte',
    248.2,
    -- SELECIODE O ID DO [ESTADO] SE A SIGLA FOR [CE]
    (select id from estados where sigla = "CE")
)

-- ----------------------------------------------------------------

insert into cidades (nome, area, estado_id)
values(
    'Luiziânia',
    166.58,
    (select id from estados where sigla = "SP")
)

-- ----------------------------------------------------------------

-- LIMPAR AS CIDADES SALVAS
delete from cidades
-- EXIBIR TODAS AS CIDADES SALVAS
select * from cidades