'''Escenario de análisis 1: 
- (LISTO) Vendedores con precios.
- (LISTO)Vendedor con tipo de carro (nuevo o usado).'''

def seller_price():
    consulta='''SELECT nombre_vendedor, AVG(precio_rel) as precio_promedio
                FROM carro
                GROUP BY 1
                ORDER BY 2 DESC'''
    return consulta

def seller_used_new():
    consulta='''SELECT nombre_vendedor, estado, total,promedio
                FROM carro LEFT JOIN(
                    SELECT nombre_vendedor, count(*)
                    FROM carro
                    GROUP BY 1
                )as total(vendedort, total)
                    ON(vendedort=nombre_vendedor)
                    LEFT JOIN(
                    SELECT nombre_vendedor, AVG(precio_rel)::numeric(5,2) as precio_promedio
                    FROM carro
                    GROUP BY 1
                )as promedio(vendedor, promedio)
                    ON(vendedor=nombre_vendedor)
                ORDER BY 4 DESC'''
    return consulta


'''Escenario de análisis 2: NO SE PUEDE HACER PORQUE DESLIGAMOS EL TIPO DE COMBUSTIBLE CON EL CARRO!!!
- Estados con fuel type (si es posible hacer división para ver solo lo que son electric).'''

def fuelType_used_or_new():
    consulta=''''''
    return consulta

'''
Escenario de análisis 3:
- Marca con ComfortRating.
- Marca con InteriorDesignRating.
- Marca con PerformanceRating.
- Marca con ExteriorStylingRating.
- Marca con RealiabilityRating.
'''
def brand_comfort_asc():
    consulta='''SELECT marca, avg(comfort_rating)::numeric(2,1) as rating_promedio
                FROM carro
                GROUP BY 1
                ORDER BY 2 ASC'''
    return consulta

def brand_comfort_desc():
    consulta='''SELECT marca, avg(comfort_rating)::numeric(2,1) as rating_promedio
                FROM carro
                GROUP BY 1
                ORDER BY 2 DESC'''
    return consulta

def brand_interior_asc():
    consulta='''SELECT marca, avg(interior_design_rating)::numeric(2,1) as rating_promedio
                FROM carro
                GROUP BY 1
                ORDER BY 2 ASC'''
    return consulta

def brand_interior_desc():
    consulta='''SELECT marca, avg(interior_design_rating)::numeric(2,1) as rating_promedio
                FROM carro
                GROUP BY 1
                ORDER BY 2 DESC'''
    return consulta

def brand_performance_asc():
    consulta='''SELECT marca, avg(performance_rating)::numeric(2,1) as rating_promedio
                FROM carro
                GROUP BY 1
                ORDER BY 2 ASC'''
    return consulta

def brand_performance_desc():
    consulta='''SELECT marca, avg(performance_rating)::numeric(2,1) as rating_promedio
                FROM carro
                GROUP BY 1
                ORDER BY 2 DESC'''
    return consulta

def brand_exterior_asc():
    consulta='''SELECT marca, avg(exterior_styling_rating)::numeric(2,1) as rating_promedio
                FROM carro
                GROUP BY 1
                ORDER BY 2 ASC'''
    return consulta

def brand_exterior_desc():
    consulta='''SELECT marca, avg(exterior_styling_rating)::numeric(2,1) as rating_promedio
                FROM carro
                GROUP BY 1
                ORDER BY 2 DESC'''
    return consulta

def brand_rely_asc():
    consulta='''SELECT marca, avg(reliabilityy_rating)::numeric(2,1) as rating_promedio
                FROM carro
                GROUP BY 1
                ORDER BY 2 ASC'''
    return consulta

def brand_rely_desc():
    consulta='''SELECT marca, avg(reliabilityy_rating)::numeric(2,1) as rating_promedio
                FROM carro
                GROUP BY 1
                ORDER BY 2 DESC'''
    return consulta

'''
Escenario de análisis 4:
- Modelo con value_for_money_rating.'''

def model_value_asc():
    consulta='''SELECT modelo, avg(value_for_money_rating_rel)::numeric(2,1) as rating_promedio
                FROM carro
                GROUP BY 1
                ORDER BY 2 ASC'''
    return consulta

def model_value_desc():
    consulta='''SELECT modelo, avg(value_for_money_rating_rel)::numeric(2,1) as rating_promedio
                FROM carro
                GROUP BY 1
                ORDER BY 2 DESC'''
    return consulta