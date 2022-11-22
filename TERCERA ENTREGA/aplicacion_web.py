import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from coneccion import Connection
import consultas_sql as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Vendedores con precios
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.seller_price(), con.connection)
con.closeConnection()
dfPrices = pd.DataFrame(query, columns=["nombre_vendedor", "precio_promedio"])

figBarPrices = px.bar(dfPrices.head(5), x="nombre_vendedor", y="precio_promedio", height=450)
figPiePrices = px.pie(dfPrices.head(5), names="nombre_vendedor", values="precio_promedio")
figLinePrices = px.line(dfPrices.head(5), x="nombre_vendedor", y="precio_promedio")

# Vendedores con UsedOrNew
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.seller_used_new(), con.connection)
con.closeConnection()
dfUsedNew = pd.DataFrame(query, columns=["nombre_vendedor", "estado", "total"])

figBarUsedNew = px.bar(dfUsedNew.head(5), x="nombre_vendedor", y="total", color="estado", height=450)
figPieUsedNew = px.pie(dfUsedNew.head(5), names="nombre_vendedor", values="total")
figLineUsedNew = px.line(dfUsedNew.head(5), x="nombre_vendedor", y="estado")

#Marca-ComfortRating
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.brand_comfort_asc(), con.connection)
con.closeConnection()
dfComfortA = pd.DataFrame(query, columns=["marca", "rating_promedio"])

figBarComfortA = px.bar(dfComfortA.head(5), x="marca", y="rating_promedio", height=450)
figPieComfortA = px.pie(dfComfortA.head(5), names="marca", values="rating_promedio")
figLineComfortA = px.line(dfComfortA.head(5), x="marca", y="rating_promedio")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.brand_comfort_desc(), con.connection)
con.closeConnection()
dfComfortD = pd.DataFrame(query, columns=["marca", "rating_promedio"])

figBarComfortD = px.bar(dfComfortD.head(5), x="marca", y="rating_promedio", height=450)
figPieComfortD = px.pie(dfComfortD.head(5), names="marca", values="rating_promedio")
figLineComfortD = px.line(dfComfortD.head(5), x="marca", y="rating_promedio")

#Marca-PerformanceRating
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.brand_performance_desc(), con.connection)
con.closeConnection()
dfPerformance = pd.DataFrame(query, columns=["marca", "rating_promedio"])

figBarPerformance = px.bar(dfPerformance.head(5), x="marca", y="rating_promedio", height=450)
figPiePerformance = px.pie(dfPerformance.head(5), names="marca", values="rating_promedio")
figLinePerformance = px.line(dfPerformance.head(5), x="marca", y="rating_promedio")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.brand_performance_asc(), con.connection)
con.closeConnection()
dfPerformance = pd.DataFrame(query, columns=["marca", "rating_promedio"])

figBarPerformanceA = px.bar(dfPerformance.head(5), x="marca", y="rating_promedio", height=450)
figPiePerformanceA = px.pie(dfPerformance.head(5), names="marca", values="rating_promedio")
figLinePerformanceA = px.line(dfPerformance.head(5), x="marca", y="rating_promedio")

#Marca-InteriorDesignRating
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.brand_interior_desc(), con.connection)
con.closeConnection()
dfInterior = pd.DataFrame(query, columns=["marca", "rating_promedio"])

figBarInterior= px.bar(dfInterior.head(5), x="marca", y="rating_promedio", height=450)
figPieInterior = px.pie(dfInterior.head(5), names="marca", values="rating_promedio")
figLineInterior = px.line(dfInterior.head(5), x="marca", y="rating_promedio")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.brand_interior_asc(), con.connection)
con.closeConnection()
dfInterior = pd.DataFrame(query, columns=["marca", "rating_promedio"])

figBarInteriorA= px.bar(dfInterior.head(5), x="marca", y="rating_promedio", height=450)
figPieInteriorA = px.pie(dfInterior.head(5), names="marca", values="rating_promedio")
figLineInteriorA = px.line(dfInterior.head(5), x="marca", y="rating_promedio")
#Marca-ExteriorStylingRating
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.brand_exterior_desc(), con.connection)
con.closeConnection()
dfExterior = pd.DataFrame(query, columns=["marca", "rating_promedio"])

figBarExterior= px.bar(dfExterior.head(5), x="marca", y="rating_promedio", height=450)
figPieExterior = px.pie(dfExterior.head(5), names="marca", values="rating_promedio")
figLineExterior = px.line(dfExterior.head(5), x="marca", y="rating_promedio")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.brand_exterior_asc(), con.connection)
con.closeConnection()
dfExterior = pd.DataFrame(query, columns=["marca", "rating_promedio"])

figBarExteriorA= px.bar(dfExterior.head(5), x="marca", y="rating_promedio", height=450)
figPieExteriorA = px.pie(dfExterior.head(5), names="marca", values="rating_promedio")
figLineExteriorA = px.line(dfExterior.head(5), x="marca", y="rating_promedio")

#Marca-RealiabilityRating
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.brand_rely_desc(), con.connection)
con.closeConnection()
dfRely = pd.DataFrame(query, columns=["marca", "rating_promedio"])

figBarRely= px.bar(dfRely.head(5), x="marca", y="rating_promedio", height=450)
figPieRely = px.pie(dfRely.head(5), names="marca", values="rating_promedio")
figLineRely = px.line(dfRely.head(5), x="marca", y="rating_promedio")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.brand_rely_asc(), con.connection)
con.closeConnection()
dfRely = pd.DataFrame(query, columns=["marca", "rating_promedio"])

figBarRelyA= px.bar(dfRely.head(5), x="marca", y="rating_promedio", height=450)
figPieRelyA = px.pie(dfRely.head(5), names="marca", values="rating_promedio")
figLineRelyA = px.line(dfRely.head(5), x="marca", y="rating_promedio")

#Modelo-ValueForMoneyRating
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.model_value_desc(), con.connection)
con.closeConnection()
dfModel = pd.DataFrame(query, columns=["modelo", "rating_promedio"])

figBarModel= px.bar(dfModel.head(5), x="modelo", y="rating_promedio", height=450)
figPieModel = px.pie(dfModel.head(5), names="modelo", values="rating_promedio")
figLineModel = px.line(dfModel.head(5), x="modelo", y="rating_promedio")

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.model_value_asc(), con.connection)
con.closeConnection()
dfModel = pd.DataFrame(query, columns=["modelo", "rating_promedio"])

figBarModelA= px.bar(dfModel.head(5), x="modelo", y="rating_promedio", height=450)
figPieModelA = px.pie(dfModel.head(5), names="modelo", values="rating_promedio")
figLineModelA = px.line(dfModel.head(5), x="modelo", y="rating_promedio")

app.layout = html.Div(children=[
    html.Br(),
    html.Center(children=[
        html.H1(children='Proyecto Final - Ingeniería de Datos'),
        html.H1(children='DashBoard de CarSale'),
        html.H3(children=' Juliana Bermúdez, Valentina Correa, Sofía Duarte, Leonardo Luengas')]), # genera <h1>Dashboard Covid 19</h1>
    html.Br(),
    
    html.Div(className= "container", children=[
        html.Center(html.H2(children="Discusión: Gráficas y análisis")),
        html.Br(),
        # Row for Prices
        html.I(html.H3(children='Escenario de análisis 1: Precios y Estados por vendedor')),
        html.Br(),
        html.H3(children='Precio promedio por vendedor'),
        html.Br(),
        html.Div(className= "row", children=[
            # Col for pie
            html.Div(className= "col-13 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Pie'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='piePricesBySeller',
                                    figure=figPiePrices
                                ), 
                    ]),    
                    
                ]),
            ]),
                
             # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Línea'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                  dcc.Graph(
                                      id='linePricesBySeller',
                                      figure=figLinePrices
                                  ),
                    ]),    
                    
                ]),
            ]),
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Barras'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barPricesBySeller',
                                    figure=figBarPrices
                                ),    
                    ]),    
                    
                ]),
            ]),

            html.Div(className="col-12 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P(style={'font-size':'130%','text-align':'justify'},children="Consideramos que para evaluar los precios promedio por vendedor, la gráfica de línea y la de barras permiten hacer las mejores interpretaciones, dado que es evidente la variación del precio según el vendedor y nos muestra los valores de cada uno. Sin embargo, dado que la variable de vendedor no es continua, la gráfica de línea no sería la adecuada, razón por la cual la gráfica de barras es la mejor opción. Así mismo, vemos que la gráfica de pie nos muestra porcentajes que no son tan dicientes dado que no podemos relacionarlos con los precios promedio, por lo que descartamos está visualización."),
            ]),
        ]),

        html.Br(),
        html.H3(children='Estado por vendedor'),
        html.Br(),
        html.Div(className= "row", children=[
            html.Div(className= "col-13 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Pie'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='piePricesBySeller',
                                    figure=figPieUsedNew
                                ), 
                    ]),    
                    
                ]),
            ]),
             # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Línea'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                  dcc.Graph(
                                      id='linePricesBySeller',
                                      figure=figLineUsedNew
                                  ),
                    ]),    
                    
                ]),
            ]),

            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Barras'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barUsedBySeller',
                                    figure=figBarUsedNew
                                ),    
                    ]),    
                    
                ]),
            ]),

            html.Div(className="col-12 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P(style={'font-size':'130%','text-align':'justify'},children="En cuanto al estado de los carros por vendedor, la gráfica de línea y la de barras permiten la mejor visualización porque nos muestran que todos los carros de los vendedores son usados. La gráfica de pie se descarta porque los porcentajes no deja claro cuantos carros por vendedor son nuevos y cuantos son usados. ")
            ]),
        ]),
        
        html.Br(),
        html.H3(children="Análisis de los resultados"),
        html.P(style={'font-size':'130%','text-align':'justify'},children="En cuanto a la interpretación de los datos para resolver el escenario propuesto, partimos de que todos los carros son usados y por tanto el estado no tiene incidencia en los precios que maneja cada vendedor. Posteriormente, vemos que McLaren Charlotte maneja el precio promedio más alto, mientras que Ferrari Maseratti of Central New Jersey y O’Gara Coach Beverly Hills tienen el mismo precio promedio que es el más bajo. Luego, esto podría indicar que la ubicación y la marca de carros que vende McLaren Charlotte hace que sus precios promedios sean más altos en comparación con los demás. Sin embargo, la gráfica nos muestra que la diferencia entre todos los vendedores no es significativa. Esta información podría ser útil para las personas que desean vender carros en los mismos sectores y de marcas parecidas, ya que pueden usar estos datos como referencia para ser más competitivos y garantizar que sus carros se vendan en mayor proporción."),

        html.Hr(),
        html.I(html.H3(children='Escenario de análisis 2: Vendedores y Ratings')),

        html.Br(),
        html.H3(children='Marca-ComfortRating: Mayores Ratings'),
        html.Br(),
        html.Div(className= "row", children=[
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Pie'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieComfortByBrand',
                                    figure=figPieComfortD
                                ), 
                    ]),    
                    
                ]),
            ]),
             # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Línea'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                  dcc.Graph(
                                      id='lineComfortByBrand',
                                      figure=figLineComfortD
                                  ),
                    ]),    
                    
                ]),
            ]),
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Barras'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barComfortByBrand',
                                    figure=figBarComfortD
                                ),    
                    ]),    
                    
                ]),
            ]),
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P(style={'font-size':'130%','text-align':'justify'},children="Podemos observar que el top 5 de marcas con mejores ratings tienen puntuaciones de 4,9 y 5. Esto indica que la calidad de estos fabricantes en cuanto a comodidad es muy buena, y a la vez muy similar entre las 5 mejores marcas. Vemos que Ferrari tiene una puntuación de 5. Es probable que esta puntuación tan alta se deba a una baja cantidad de calificaciones en la base de datos.")
            ]),
        ]),
        
        html.Br(),
        html.H3(children='Marca-ComfortRating: Menores Ratings'),
        html.Br(),
        html.Div(className= "row", children=[
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Pie'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieComfortByBrand',
                                    figure=figPieComfortA
                                ), 
                    ]),    
                    
                ]),
            ]),
             # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Línea'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                  dcc.Graph(
                                      id='lineComfortByBrand',
                                      figure=figLineComfortA
                                  ),
                    ]),    
                    
                ]),
            ]),
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Barras'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barComfortByBrand',
                                    figure=figBarComfortA
                                ),    
                    ]),    
                    
                ]),
            ]),
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P(style={'font-size':'130%','text-align':'justify'},children="Vemos que el top 5 de las marcas con peores calificaciones tienen puntuaciones entre 4,2 y 4,5. Esto indica que, en general, la calidad de los carros en la base de datos es buena, esto en cuanto al aspecto de comodidad. Vemos que la marca con peor puntuación es Tesla. Considerando que esta es una marca reciente en comparación con muchas de las demás en la base de datos, es probable que hayan decidido disminuir la calidad de este aspecto con el fin de ser más competitivos a nivel de precios.")
            ]),
        ]),

        html.Br(),
        html.H3(children='Marca-PerformanceRating: Mayores Ratings'),
        html.Br(),
        html.Div(className= "row", children=[
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Pie'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='piePerformanceByBrand',
                                    figure=figPiePerformance
                                ), 
                    ]),    
                    
                ]),
            ]),

             # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Línea'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                  dcc.Graph(
                                      id='linePerformanceByBrand',
                                      figure=figLinePerformance
                                  ),
                    ]),    
                    
                ]),
            ]),

            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Barras'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barPerformanceByBrand',
                                    figure=figBarPerformance
                                ),    
                    ]),    
                    
                ]),
            ]),

            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), 
                html.P(style={'font-size':'130%','text-align':'justify'},children="En el top 5 de mejores ratings respecto al rendimiento se encuentran las marcas más lujosas del mercado. Es lógico evidenciar el uso de los mejores componentes del mercado para permitir justificar su estatus de productos de lujo y, por lo tanto, va a tener un gran rendimiento. Aun así, también es importante mencionar que la experiencia del lujo de estas marcas en los consumidores afecta la percepción del rendimiento, inflando la experiencia del carro a causa de su estatus legendario como un producto de lujo (también conocido como fetichismo).")
            ]),
        ]),
        
        html.Br(),
        html.H3(children='Marca-PerformanceRating: Menores Ratings'),
        html.Br(),
        html.Div(className= "row", children=[
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Pie'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='piePerformanceByBrand',
                                    figure=figPiePerformanceA
                                ), 
                    ]),    
                    
                ]),
            ]),
             # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Línea'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                  dcc.Graph(
                                      id='linePerformanceByBrand',
                                      figure=figLinePerformanceA
                                  ),
                    ]),    
                    
                ]),
            ]),
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Barras'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barPerformanceByBrand',
                                    figure=figBarPerformanceA
                                ),    
                    ]),    
                    
                ]),
            ]),

            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P(style={'font-size':'130%','text-align':'justify'},children="En el grupo de los peores perfomance rating tenemos a un grupo de marcas en su mayoría de carros de gama media. Por lo tanto, no es raro ver que estas son las que tenegan los peores perfomance rating. Lo sorprendente es ver la ausencia de Tesla en este grupo. De cierta forma, podríamos pensar que la tecnología de los motores de los carros eléctricos puede ser considerada incluso mejor que la de algunas marcas de carros de gasolina.")
            ]),
        ]),
        
        html.Br(),
        html.H3(children='Marca-InteriorDesignRating: Mayores Ratings'),
        html.Br(),
        html.Div(className= "row", children=[
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Pie'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieInteriorByBrand',
                                    figure=figPieInterior
                                ), 
                    ]),    
                    
                ]),
            ]),

             # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Línea'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                  dcc.Graph(
                                      id='lineInteriorByBrand',
                                      figure=figLineInterior
                                  ),
                    ]),    
                    
                ]),
            ]),
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Barras'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barInteriorByBrand',
                                    figure=figBarInterior
                                ),    
                    ]),    
                    
                ]),
            ]),

            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P(style={'font-size':'130%','text-align':'justify'},children="Podemos observar que el top 5 de marcas con mejores ratings tienen puntuaciones entre 4,9 y 5. Esto indica que la calidad del diseño interior de estas marcas es muy bueno y a la vez muy similar. Vemos que Ferrari y Lamborghini tienen una puntuación de 5. Tal como se describió antes, es posible que esto se deba a una baja cantidad de calificaciones en la base de datos.")
            ]),
        ]),

        html.Br(),
        html.H3(children='Marca-InteriorDesignRating: Menores Ratings'),
        html.Br(),
        html.Div(className= "row", children=[
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Pie'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieInteriorByBrand',
                                    figure=figPieInteriorA
                                ), 
                    ]),    
                    
                ]),
            ]),
             # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Línea'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                  dcc.Graph(
                                      id='lineInteriorByBrand',
                                      figure=figLineInteriorA
                                  ),
                    ]),    
                    
                ]),
            ]),
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Barras'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barInteriorByBrand',
                                    figure=figBarInteriorA
                                ),    
                    ]),    
                    
                ]),
            ]),

            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P(style={'font-size':'130%','text-align':'justify'},children="Vemos que el top 5 de marcas con peores ratings tienen calificaciones entre 4,2 y 4,5. Esto indica que, en general, la calidad del diseño interior de todas las marcas es bueno. Además, notamos que Tesla tiene el tercer peor rating en esta categoría. Es posible que, al ser una marca nueva, se hayan tomado decisiones de diseño poco convencionales, resultando en una calificación relativamente baja.")
            ]),
        ]),
 
        html.Br(),
        html.H3(children='Marca-ExteriorDesignRating: Mayores Ratings'),
        html.Br(),
        html.Div(className= "row", children=[
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Pie'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieExteriorByBrand',
                                    figure=figPieExterior
                                ), 
                    ]),    
                    
                ]),
            ]),
             # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Línea'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                  dcc.Graph(
                                      id='lineExteriorByBrand',
                                      figure=figLineExterior
                                  ),
                    ]),    
                    
                ]),
            ]),
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Barras'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barExteriorByBrand',
                                    figure=figBarExterior
                                ),    
                    ]),    
                    
                ]),
            ]),
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P(style={'font-size':'130%','text-align':'justify'},children="Podemos ver que el top 5 de marcas con mejores ratings tienen puntuaciones entre 4,9 y 5. Esto indica que la calidad del diseño exterior de estas marcas es muy bueno y similar. De nuevo, vemos que Ferrari y Lamborghini tienen calificaciones de 5. Esto va de acuerdo con la posibilidad planteada anteriormente, en la que estas marcas pueden tener menor cantidad de calificaciones en la base de datos.")
            ]),
        ]),

        html.Br(),
        html.H3(children='Marca-ExteriorDesignRating: Menores Ratings'),
        html.Br(),
        html.Div(className= "row", children=[
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Pie'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieExteriorByBrand',
                                    figure=figPieExteriorA
                                ), 
                    ]),    
                    
                ]),
            ]),
             # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Línea'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                  dcc.Graph(
                                      id='lineExteriorByBrand',
                                      figure=figLineExteriorA
                                  ),
                    ]),    
                    
                ]),
            ]),

            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Barras'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barExteriorByBrand',
                                    figure=figBarExteriorA
                                ),    
                    ]),    
                    
                ]),
            ]),
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P(style={'font-size':'130%','text-align':'justify'},children="Vemos que el top 5 de marcas con peores calificaciones tienen entre 4,2 y 4,6. Esto indica que, en general, la calidad del diseño exterior de las marcas de la base de datos son buenas. De nuevo, Tesla se encuentra en el peor puesto en cuanto a diseño exterior. Es posible que, al ser una marca nueva, se hayan tomado decisiones de diseño poco convencionales, resultando en una calificación relativamente baja.")
            ]),
        ]),

        html.Br(),
        html.H3(children='Marca-RealiabilityRating: Mayores Ratings'),
        html.Br(),
        html.Div(className= "row", children=[
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Pie'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieRelyByBrand',
                                    figure=figPieRely
                                ), 
                    ]),    
                    
                ]),
            ]),
             # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Línea'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                  dcc.Graph(
                                      id='lineRelyByBrand',
                                      figure=figLineRely
                                  ),
                    ]),    
                    
                ]),
            ]),
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Barras'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barRelyByBrand',
                                    figure=figBarRely
                                ),    
                    ]),    
                    
                ]),
            ]),
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P(style={'font-size':'130%','text-align':'justify'},children="Vemos que el top 5 de marcas con mejores ratings tienen calificaciones entre 5 y 4,8. Esto indica que la confiabilidad de los carros de las marcas en el top 5 son muy buenas, pero no tanto como los demás ratings, donde las calificaciones se encontraron entre 4,9 y 5. De nuevo, Ferrari tiene una calificación de 5. Esto va de acuerdo con lo mencionado anteriormente. Es posible que exista una menor cantidad de calificaciones para esta marca, resultando en puntuaciones muy buenas.")
            ]),
        ]),

        html.Br(),
        html.H3(children='Marca-RealiabilityRating: Menores Ratings'),
        html.Br(),
        html.Div(className= "row", children=[
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Pie'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieRelyByBrand',
                                    figure=figPieRelyA
                                ), 
                    ]),    
                    
                ]),
            ]),
             # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Línea'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                  dcc.Graph(
                                      id='lineRelyByBrand',
                                      figure=figLineRelyA
                                  ),
                    ]),    
                    
                ]),
            ]),
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Barras'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barRelyByBrand',
                                    figure=figBarRelyA
                                ),    
                    ]),    
                    
                ]),
            ]),
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P(style={'font-size':'130%','text-align':'justify'},children="Vemos que el top 5 de las marcas con peores ratings tienen calificaciones entre 3,8 y 4,4. Esto indica que, en general, la confiabilidad de los carros de las marcas de la base de datos es buena. Sin embargo, comparando con los demás ratings, la calidad en este aspecto es relativamente baja. Observamos que Tesla tiene la peor calificación en este aspecto. Es probable que, al ser una marca relativamente nueva y con mecanismos de manejo experimentales, no tenga una reputación tan buena como las demás marcas en la base de datos.")
            ]),
        ]),

        html.Br(),
        html.H3(children='Análisis de los Resultados'),
        html.P(style={'font-size':'130%','text-align':'justify'},children="Aproximándonos de manera general a las representaciones realizadas de los datos, es evidente a primera vista que las marcas con los mejores ratings corresponden a Lamborghini y a Ferrari, manteniendo un promedio de 5 en la mayoría de los Ratings. Una posible explicación puede ser dada gracias a la exclusividad de estas marcas, lo cual indica que en el mercado existen una pequeña cantidad de ejemplares. En la práctica, esto facilita una calidad constante en los pocos ejemplares que hay y, en consecuencia, un mejor promedio general. Considerando el conjunto de las representaciones gráficas que escogimos para este escenario de análisis, los gráficos de barras presentan una clara limitación al momento de querer comparar las sutiles diferencias entre los promedios de los ratings de las diferentes marcas. Esto se debe que la escala de las gráficas está en numeros enteros. Por otro lado, respecto a los gráficos de linea, la continuidad de la línea en columnas con un dominio discreto causa confusión al momento de interpretar la gráfica. No tiene mucho sentido hablar de un valor entre marca y marca, mucho menos de un orden respecto a los valores del dominio. Por último, la información que busca comunicar el gráfico de pie no es muy clara; en la mayoría de los gráficos se ven porcentajes similares respecto a varias marcas pero que, dentro del contexto del problema, no parecen representar nada signicativo que nos lleve a concluir sobre la base de datos."),

        html.Hr(),
        html.I(html.H3(children='Escenario de análisis 3: Modelos y Calidad-Precio')),

        html.Br(),
        html.H3(children='Marca-ValueForMoneyRating: Mayores Ratings'),
        html.Br(),
        html.Div(className= "row", children=[
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Pie'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieRelyByBrand',
                                    figure=figPieModel
                                ), 
                    ]),    
                    
                ]),
            ]),
             # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Línea'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                  dcc.Graph(
                                      id='lineRelyByBrand',
                                      figure=figLineModel
                                  ),
                    ]),    
                    
                ]),
            ]),
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Barras'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barRelyByBrand',
                                    figure=figBarModel
                                ),    
                    ]),    
                    
                ]),
            ]),
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P(style={'font-size':'130%','text-align':'justify'},children="De las visualizaciones obtenidas, consideramos que tanto los gráficos de barras como las de líneas nos brindan información de fácil interpretación. Podemos decir esto, dado que nos muestran los ratings obtenidos por cada modelo en una escala de 1 a 5, mientras que el de pie nos muestra porcentajes pero no se ve el rating de cada modelo. Por ejemplo, en este caso de mayores ratings, se ve que todos son iguales, pero no podemos saber que puntuación tienen todos. Por tanto, concluimos que la de barras nos da la mejor visualización dado que la variable modelo no es continua.")
            ]),
        ]),

        html.Br(),
        html.H3(children='Marca-ValueForMoneyRating: Menores Ratings'),
        html.Br(),
        html.Div(className= "row", children=[
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Pie'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='pieRelyByBrand',
                                    figure=figPieModelA
                                ), 
                    ]),    
                    
                ]),
            ]),
             # Col for line
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Línea'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                  dcc.Graph(
                                      id='lineRelyByBrand',
                                      figure=figLineModelA
                                  ),
                    ]),    
                    
                ]),
            ]),
            # Col for vertical bars
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gráfico de Barras'),    
                    ]),
                    html.Div(className= "card-body", children=[
                                dcc.Graph(
                                    id='barRelyByBrand',
                                    figure=figBarModelA
                                ),    
                    ]),    
                    
                ]),
            ]),
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P(style={'font-size':'130%','text-align':'justify'},children="De las visualizaciones obtenidas, consideramos que tanto los gráficos de barras como las de líneas nos brindan información de fácil interpretación. Podemos decir esto, dado que nos muestran los ratings obtenidos por cada modelo en una escala de 1 a 5, mientras que el de pie nos muestra porcentajes pero no se ve el rating de cada modelo. En este caso de los menores ratings, hay ratings diferentes pero no sabemos cuales son, solo cuales son mayores y menores. Por tanto, concluimos que la de barras nos da la mejor visualización dado que la variable modelo no es continua. ")
            ]),
        ]),

        html.Br(),
        html.H3(children="Análisis de los Resultados"),
        html.P(style={'font-size':'130%','text-align':'justify'},children="En cuanto a los datos obtenidos a la luz del escenario de análisis, vemos que A4 40 Premium Plus, Escalade ESV premium Luxury, 228 Gran Couple I xDrive, Escalade ESV Luxury, Model S Plaid tienen la puntuación más alta por ser las ofertas más justas y XC50 BS Inscription las más bajas. Cabe resaltar, que el value_for_money rating evalúa que el precio sea acorde a las condiciones en las que se encuentra el carro en términos de comodidad, diseño, eficiencia, modelo, etc. Esta información es útil para las personas que están buscando comprar carro, ya que se les muestra cuales modelos les conviene más comprar y cuales definitivamente deberían evitar comprar."),

        html.Hr(),

        html.Br(),
        html.Center(html.H2(children="Conclusiones de los miembros del equipo")),
        html.Br(),
        html.H4("Juliana Bermudez:"),
        html.P(style={'font-size':'130%','text-align':'justify'},children="A grandes rasgos, considero que la base de datos permite generar varios escenarios de análisis gracias a todos los ratings y características de los carros que ofrece. Sin embargo, al momento de preparar los datos en Excel nos dimos cuenta que son poco homogéneos y por tanto tocó limpiar bastante, lo cual fue bastante dispendioso e hizo que normalizar no fuese posible por los seriales. En cuanto a la conexión y dash, la conexión se pudo hacer sin problema, pero tocó replantear un escenario de análisis dado que las gráficas no salieron con datos concluyentes."),
        html.Br(),
        html.H4("Valentina Correa:"),
        html.P(style={'font-size':'130%','text-align':'justify'},children="En cuanto a la base de datos, considero que fue una muy buena elección ya que los datos eran muy interesantes y los análisis con dash que pudimos concluir para los interesados en comprar carro en EE.UU son de gran ayuda al momento de evaluar precio y características, al igual que con quién sería mejor comprarlos. Sobre las herramientas utilizadas durante el desarrollo del proyecto, dash es una herramienta fácil de usar que nos permite visualizar todos los datos obtenidos, lo cual es de gran ayuda para llegar a conclusiones más contundentes. Las conexiones con Python servirían bastante en caso de que necesitemos obtener los datos organizados en tablas y no tengamos a la mano SQL."),
        html.Br(),
        html.H4("Sofía Duarte:"),
        html.P(style={'font-size':'130%','text-align':'justify'},children="Personalmente, la base de datos me pareció bastante completa. Tenía muchas columnas con datos de fácil interpretación y que nos generaban información importante sobre los carros y los vendedores. Sin embargo, tuvo que ser modificada y ajustada porque había varios valores que no se ajustaban al contexto, lo cual hizo más difícil la carga de datos. El diseño de la base de datos fue muy claro, lo cual ayudó al momento de normalizarla. La herramienta de dash fue fácil de usar, teniendo una plantilla y experiencia previa con html. El desarrollo de las gráficas fue interesante, aunque el diagrama de pie no fue muy útil en nuestro análisis."),
        html.Br(),
        html.H4("Leonardo Luengas:"),
        html.P(style={'font-size':'130%','text-align':'justify'},children="La estructura de los datos permitieron una fácil identificación de las reglas de negocio, su posterior traducción al diagrama E-R y, finalmente, al diagrama relacional implementado en la base de datos. La abundancia de información relevante para el consumidor, como los ratings en las diferentes categorías, hace de la base de datos generada una herramienta útil para futuros consumidores en su búsqueda del mejor uso de su dinero en el mercado. En mi opinión, las gráficas que dispone el dash no son muy útiles para nuestro análisis, ya que no permiten sacar conclusiones interesantes sobre la base de datos. "),
        html.Br(),

        html.Footer(children=[
            html.Center(children=[
                html.A("Base de datos original: CarsForSale- Chance V", href="https://www.kaggle.com/datasets/chancev/carsforsale"),
            ]),
        ]),
    ]),

])

if __name__ == '__main__':
    app.run_server(debug=True)
