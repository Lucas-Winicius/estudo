-- TOTAL POR REGIAO
select
    regiao as "Região",
    sum(populacao) as Total
from `estados`
GROUP BY regiao
order by Total desc

-- TOTAL GERAL
select sum(populacao) as Total from `estados`

-- MEDIA
select avg(populacao) as Total from `estados`