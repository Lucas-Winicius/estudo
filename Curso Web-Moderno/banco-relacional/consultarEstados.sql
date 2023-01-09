-- NOTA: SQL E CASE INSENSITIVE
-- SELECIONA TODAS AS COLUNAS DE ESTADO
select * from `estados`

-- SELECIONA COLUNAS ESPECIFICAS
select nome, sigla from `estados`
select sigla, nome from `estados`
select sigla, nome as 'Nome Do Estado' from `estados`

-- EXIBE APENAS ESTADOS DA REGIÃO SUL
select sigla, nome as 'Nome Do Estado' from `estados`
where regiao = 'Sul'

-- EXIBE POPULAÇÃO MAIOR IGUAL A 10
select nome, regiao from `estados`
where populacao >= 10
-- ORDENA DE FORMA DECRESCENTE
-- AO REMOVER O ( desc ) IRA ORDENAR DO MENOR PARA O MAIOR
order by populacao desc