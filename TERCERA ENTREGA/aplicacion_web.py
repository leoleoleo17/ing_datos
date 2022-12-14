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
        html.H1(children='Proyecto Final - Ingenier??a de Datos'),
        html.H1(children='DashBoard de CarSale'),
        html.H3(children=' Juliana Berm??dez, Valentina Correa, Sof??a Duarte, Leonardo Luengas')]), # genera <h1>Dashboard Covid 19</h1>
    html.Br(),
    
    html.Div(className= "container", children=[
        html.Center(html.H2(children="Discusi??n: Gr??ficas y an??lisis")),
        html.Br(),
        # Row for Prices
        html.I(html.H3(children='Escenario de an??lisis 1: Precios y Estados por vendedor')),
        html.Br(),
        html.H3(children='Precio promedio por vendedor'),
        html.Br(),
        html.Div(className= "row", children=[
            # Col for pie
            html.Div(className= "col-13 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gr??fico de Pie'),    
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
                            html.H4(children='Gr??fico de L??nea'),    
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
                            html.H4(children='Gr??fico de Barras'),    
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
                html.P(style={'font-size':'130%','text-align':'justify'},children="Consideramos que para evaluar los precios promedio por vendedor, la gr??fica de l??nea y la de barras permiten hacer las mejores interpretaciones, dado que es evidente la variaci??n del precio seg??n el vendedor y nos muestra los valores de cada uno. Sin embargo, dado que la variable de vendedor no es continua, la gr??fica de l??nea no ser??a la adecuada, raz??n por la cual la gr??fica de barras es la mejor opci??n. As?? mismo, vemos que la gr??fica de pie nos muestra porcentajes que no son tan dicientes dado que no podemos relacionarlos con los precios promedio, por lo que descartamos est?? visualizaci??n."),
            ]),
        ]),

        html.Br(),
        html.H3(children='Estado por vendedor'),
        html.Br(),
        html.Div(className= "row", children=[
            html.Div(className= "col-13 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gr??fico de Pie'),    
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
                            html.H4(children='Gr??fico de L??nea'),    
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
                            html.H4(children='Gr??fico de Barras'),    
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
                html.P(style={'font-size':'130%','text-align':'justify'},children="En cuanto al estado de los carros por vendedor, la gr??fica de l??nea y la de barras permiten la mejor visualizaci??n porque nos muestran que todos los carros de los vendedores son usados. La gr??fica de pie se descarta porque los porcentajes no deja claro cuantos carros por vendedor son nuevos y cuantos son usados. ")
            ]),
        ]),
        
        html.Br(),
        html.H3(children="An??lisis de los resultados"),
        html.P(style={'font-size':'130%','text-align':'justify'},children="En cuanto a la interpretaci??n de los datos para resolver el escenario propuesto, partimos de que todos los carros son usados y por tanto el estado no tiene incidencia en los precios que maneja cada vendedor. Posteriormente, vemos que McLaren Charlotte maneja el precio promedio m??s alto, mientras que Ferrari Maseratti of Central New Jersey y O???Gara Coach Beverly Hills tienen el mismo precio promedio que es el m??s bajo. Luego, esto podr??a indicar que la ubicaci??n y la marca de carros que vende McLaren Charlotte hace que sus precios promedios sean m??s altos en comparaci??n con los dem??s. Sin embargo, la gr??fica nos muestra que la diferencia entre todos los vendedores no es significativa. Esta informaci??n podr??a ser ??til para las personas que desean vender carros en los mismos sectores y de marcas parecidas, ya que pueden usar estos datos como referencia para ser m??s competitivos y garantizar que sus carros se vendan en mayor proporci??n."),

        html.Hr(),
        html.I(html.H3(children='Escenario de an??lisis 2: Vendedores y Ratings')),

        html.Br(),
        html.H3(children='Marca-ComfortRating: Mayores Ratings'),
        html.Br(),
        html.Div(className= "row", children=[
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gr??fico de Pie'),    
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
                            html.H4(children='Gr??fico de L??nea'),    
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
                            html.H4(children='Gr??fico de Barras'),    
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
                html.P(style={'font-size':'130%','text-align':'justify'},children="Podemos observar que el top 5 de marcas con mejores ratings tienen puntuaciones de 4,9 y 5. Esto indica que la calidad de estos fabricantes en cuanto a comodidad es muy buena, y a la vez muy similar entre las 5 mejores marcas. Vemos que Ferrari tiene una puntuaci??n de 5. Es probable que esta puntuaci??n tan alta se deba a una baja cantidad de calificaciones en la base de datos.")
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
                            html.H4(children='Gr??fico de Pie'),    
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
                            html.H4(children='Gr??fico de L??nea'),    
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
                            html.H4(children='Gr??fico de Barras'),    
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
                html.P(style={'font-size':'130%','text-align':'justify'},children="Vemos que el top 5 de las marcas con peores calificaciones tienen puntuaciones entre 4,2 y 4,5. Esto indica que, en general, la calidad de los carros en la base de datos es buena, esto en cuanto al aspecto de comodidad. Vemos que la marca con peor puntuaci??n es Tesla. Considerando que esta es una marca reciente en comparaci??n con muchas de las dem??s en la base de datos, es probable que hayan decidido disminuir la calidad de este aspecto con el fin de ser m??s competitivos a nivel de precios.")
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
                            html.H4(children='Gr??fico de Pie'),    
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
                            html.H4(children='Gr??fico de L??nea'),    
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
                            html.H4(children='Gr??fico de Barras'),    
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
                html.P(style={'font-size':'130%','text-align':'justify'},children="En el top 5 de mejores ratings respecto al rendimiento se encuentran las marcas m??s lujosas del mercado. Es l??gico evidenciar el uso de los mejores componentes del mercado para permitir justificar su estatus de productos de lujo y, por lo tanto, va a tener un gran rendimiento. Aun as??, tambi??n es importante mencionar que la experiencia del lujo de estas marcas en los consumidores afecta la percepci??n del rendimiento, inflando la experiencia del carro a causa de su estatus legendario como un producto de lujo (tambi??n conocido como fetichismo).")
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
                            html.H4(children='Gr??fico de Pie'),    
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
                            html.H4(children='Gr??fico de L??nea'),    
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
                            html.H4(children='Gr??fico de Barras'),    
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
                html.P(style={'font-size':'130%','text-align':'justify'},children="En el grupo de los peores perfomance rating tenemos a un grupo de marcas en su mayor??a de carros de gama media. Por lo tanto, no es raro ver que estas son las que tenegan los peores perfomance rating. Lo sorprendente es ver la ausencia de Tesla en este grupo. De cierta forma, podr??amos pensar que la tecnolog??a de los motores de los carros el??ctricos puede ser considerada incluso mejor que la de algunas marcas de carros de gasolina.")
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
                            html.H4(children='Gr??fico de Pie'),    
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
                            html.H4(children='Gr??fico de L??nea'),    
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
                            html.H4(children='Gr??fico de Barras'),    
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
                html.P(style={'font-size':'130%','text-align':'justify'},children="Podemos observar que el top 5 de marcas con mejores ratings tienen puntuaciones entre 4,9 y 5. Esto indica que la calidad del dise??o interior de estas marcas es muy bueno y a la vez muy similar. Vemos que Ferrari y Lamborghini tienen una puntuaci??n de 5. Tal como se describi?? antes, es posible que esto se deba a una baja cantidad de calificaciones en la base de datos.")
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
                            html.H4(children='Gr??fico de Pie'),    
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
                            html.H4(children='Gr??fico de L??nea'),    
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
                            html.H4(children='Gr??fico de Barras'),    
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
                html.P(style={'font-size':'130%','text-align':'justify'},children="Vemos que el top 5 de marcas con peores ratings tienen calificaciones entre 4,2 y 4,5. Esto indica que, en general, la calidad del dise??o interior de todas las marcas es bueno. Adem??s, notamos que Tesla tiene el tercer peor rating en esta categor??a. Es posible que, al ser una marca nueva, se hayan tomado decisiones de dise??o poco convencionales, resultando en una calificaci??n relativamente baja.")
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
                            html.H4(children='Gr??fico de Pie'),    
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
                            html.H4(children='Gr??fico de L??nea'),    
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
                            html.H4(children='Gr??fico de Barras'),    
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
                html.P(style={'font-size':'130%','text-align':'justify'},children="Podemos ver que el top 5 de marcas con mejores ratings tienen puntuaciones entre 4,9 y 5. Esto indica que la calidad del dise??o exterior de estas marcas es muy bueno y similar. De nuevo, vemos que Ferrari y Lamborghini tienen calificaciones de 5. Esto va de acuerdo con la posibilidad planteada anteriormente, en la que estas marcas pueden tener menor cantidad de calificaciones en la base de datos.")
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
                            html.H4(children='Gr??fico de Pie'),    
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
                            html.H4(children='Gr??fico de L??nea'),    
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
                            html.H4(children='Gr??fico de Barras'),    
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
                html.P(style={'font-size':'130%','text-align':'justify'},children="Vemos que el top 5 de marcas con peores calificaciones tienen entre 4,2 y 4,6. Esto indica que, en general, la calidad del dise??o exterior de las marcas de la base de datos son buenas. De nuevo, Tesla se encuentra en el peor puesto en cuanto a dise??o exterior. Es posible que, al ser una marca nueva, se hayan tomado decisiones de dise??o poco convencionales, resultando en una calificaci??n relativamente baja.")
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
                            html.H4(children='Gr??fico de Pie'),    
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
                            html.H4(children='Gr??fico de L??nea'),    
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
                            html.H4(children='Gr??fico de Barras'),    
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
                html.P(style={'font-size':'130%','text-align':'justify'},children="Vemos que el top 5 de marcas con mejores ratings tienen calificaciones entre 5 y 4,8. Esto indica que la confiabilidad de los carros de las marcas en el top 5 son muy buenas, pero no tanto como los dem??s ratings, donde las calificaciones se encontraron entre 4,9 y 5. De nuevo, Ferrari tiene una calificaci??n de 5. Esto va de acuerdo con lo mencionado anteriormente. Es posible que exista una menor cantidad de calificaciones para esta marca, resultando en puntuaciones muy buenas.")
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
                            html.H4(children='Gr??fico de Pie'),    
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
                            html.H4(children='Gr??fico de L??nea'),    
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
                            html.H4(children='Gr??fico de Barras'),    
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
                html.P(style={'font-size':'130%','text-align':'justify'},children="Vemos que el top 5 de las marcas con peores ratings tienen calificaciones entre 3,8 y 4,4. Esto indica que, en general, la confiabilidad de los carros de las marcas de la base de datos es buena. Sin embargo, comparando con los dem??s ratings, la calidad en este aspecto es relativamente baja. Observamos que Tesla tiene la peor calificaci??n en este aspecto. Es probable que, al ser una marca relativamente nueva y con mecanismos de manejo experimentales, no tenga una reputaci??n tan buena como las dem??s marcas en la base de datos.")
            ]),
        ]),

        html.Br(),
        html.H3(children='An??lisis de los Resultados'),
        html.P(style={'font-size':'130%','text-align':'justify'},children="Aproxim??ndonos de manera general a las representaciones realizadas de los datos, es evidente a primera vista que las marcas con los mejores ratings corresponden a Lamborghini y a Ferrari, manteniendo un promedio de 5 en la mayor??a de los Ratings. Una posible explicaci??n puede ser dada gracias a la exclusividad de estas marcas, lo cual indica que en el mercado existen una peque??a cantidad de ejemplares. En la pr??ctica, esto facilita una calidad constante en los pocos ejemplares que hay y, en consecuencia, un mejor promedio general. Considerando el conjunto de las representaciones gr??ficas que escogimos para este escenario de an??lisis, los gr??ficos de barras presentan una clara limitaci??n al momento de querer comparar las sutiles diferencias entre los promedios de los ratings de las diferentes marcas. Esto se debe que la escala de las gr??ficas est?? en numeros enteros. Por otro lado, respecto a los gr??ficos de linea, la continuidad de la l??nea en columnas con un dominio discreto causa confusi??n al momento de interpretar la gr??fica. No tiene mucho sentido hablar de un valor entre marca y marca, mucho menos de un orden respecto a los valores del dominio. Por ??ltimo, la informaci??n que busca comunicar el gr??fico de pie no es muy clara; en la mayor??a de los gr??ficos se ven porcentajes similares respecto a varias marcas pero que, dentro del contexto del problema, no parecen representar nada signicativo que nos lleve a concluir sobre la base de datos."),

        html.Hr(),
        html.I(html.H3(children='Escenario de an??lisis 3: Modelos y Calidad-Precio')),

        html.Br(),
        html.H3(children='Marca-ValueForMoneyRating: Mayores Ratings'),
        html.Br(),
        html.Div(className= "row", children=[
            # Col for pie
            html.Div(className= "col-12 col-xl-6", children=[
                html.Div(className= "card border-info", children=[
                    html.Div(className= "card-header", children=[
                            html.H4(children='Gr??fico de Pie'),    
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
                            html.H4(children='Gr??fico de L??nea'),    
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
                            html.H4(children='Gr??fico de Barras'),    
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
                html.P(style={'font-size':'130%','text-align':'justify'},children="De las visualizaciones obtenidas, consideramos que tanto los gr??ficos de barras como las de l??neas nos brindan informaci??n de f??cil interpretaci??n. Podemos decir esto, dado que nos muestran los ratings obtenidos por cada modelo en una escala de 1 a 5, mientras que el de pie nos muestra porcentajes pero no se ve el rating de cada modelo. Por ejemplo, en este caso de mayores ratings, se ve que todos son iguales, pero no podemos saber que puntuaci??n tienen todos. Por tanto, concluimos que la de barras nos da la mejor visualizaci??n dado que la variable modelo no es continua.")
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
                            html.H4(children='Gr??fico de Pie'),    
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
                            html.H4(children='Gr??fico de L??nea'),    
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
                            html.H4(children='Gr??fico de Barras'),    
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
                html.P(style={'font-size':'130%','text-align':'justify'},children="De las visualizaciones obtenidas, consideramos que tanto los gr??ficos de barras como las de l??neas nos brindan informaci??n de f??cil interpretaci??n. Podemos decir esto, dado que nos muestran los ratings obtenidos por cada modelo en una escala de 1 a 5, mientras que el de pie nos muestra porcentajes pero no se ve el rating de cada modelo. En este caso de los menores ratings, hay ratings diferentes pero no sabemos cuales son, solo cuales son mayores y menores. Por tanto, concluimos que la de barras nos da la mejor visualizaci??n dado que la variable modelo no es continua. ")
            ]),
        ]),

        html.Br(),
        html.H3(children="An??lisis de los Resultados"),
        html.P(style={'font-size':'130%','text-align':'justify'},children="En cuanto a los datos obtenidos a la luz del escenario de an??lisis, vemos que A4 40 Premium Plus, Escalade ESV premium Luxury, 228 Gran Couple I xDrive, Escalade ESV Luxury, Model S Plaid tienen la puntuaci??n m??s alta por ser las ofertas m??s justas y XC50 BS Inscription las m??s bajas. Cabe resaltar, que el value_for_money rating eval??a que el precio sea acorde a las condiciones en las que se encuentra el carro en t??rminos de comodidad, dise??o, eficiencia, modelo, etc. Esta informaci??n es ??til para las personas que est??n buscando comprar carro, ya que se les muestra cuales modelos les conviene m??s comprar y cuales definitivamente deber??an evitar comprar."),

        html.Hr(),

        html.Br(),
        html.Center(html.H2(children="Conclusiones de los miembros del equipo")),
        html.Br(),
        html.H4("Juliana Bermudez:"),
        html.P(style={'font-size':'130%','text-align':'justify'},children="A grandes rasgos, considero que la base de datos permite generar varios escenarios de an??lisis gracias a todos los ratings y caracter??sticas de los carros que ofrece. Sin embargo, al momento de preparar los datos en Excel nos dimos cuenta que son poco homog??neos y por tanto toc?? limpiar bastante, lo cual fue bastante dispendioso e hizo que normalizar no fuese posible por los seriales. En cuanto a la conexi??n y dash, la conexi??n se pudo hacer sin problema, pero toc?? replantear un escenario de an??lisis dado que las gr??ficas no salieron con datos concluyentes."),
        html.Br(),
        html.H4("Valentina Correa:"),
        html.P(style={'font-size':'130%','text-align':'justify'},children="En cuanto a la base de datos, considero que fue una muy buena elecci??n ya que los datos eran muy interesantes y los an??lisis con dash que pudimos concluir para los interesados en comprar carro en EE.UU son de gran ayuda al momento de evaluar precio y caracter??sticas, al igual que con qui??n ser??a mejor comprarlos. Sobre las herramientas utilizadas durante el desarrollo del proyecto, dash es una herramienta f??cil de usar que nos permite visualizar todos los datos obtenidos, lo cual es de gran ayuda para llegar a conclusiones m??s contundentes. Las conexiones con Python servir??an bastante en caso de que necesitemos obtener los datos organizados en tablas y no tengamos a la mano SQL."),
        html.Br(),
        html.H4("Sof??a Duarte:"),
        html.P(style={'font-size':'130%','text-align':'justify'},children="Personalmente, la base de datos me pareci?? bastante completa. Ten??a muchas columnas con datos de f??cil interpretaci??n y que nos generaban informaci??n importante sobre los carros y los vendedores. Sin embargo, tuvo que ser modificada y ajustada porque hab??a varios valores que no se ajustaban al contexto, lo cual hizo m??s dif??cil la carga de datos. El dise??o de la base de datos fue muy claro, lo cual ayud?? al momento de normalizarla. La herramienta de dash fue f??cil de usar, teniendo una plantilla y experiencia previa con html. El desarrollo de las gr??ficas fue interesante, aunque el diagrama de pie no fue muy ??til en nuestro an??lisis."),
        html.Br(),
        html.H4("Leonardo Luengas:"),
        html.P(style={'font-size':'130%','text-align':'justify'},children="La estructura de los datos permitieron una f??cil identificaci??n de las reglas de negocio, su posterior traducci??n al diagrama E-R y, finalmente, al diagrama relacional implementado en la base de datos. La abundancia de informaci??n relevante para el consumidor, como los ratings en las diferentes categor??as, hace de la base de datos generada una herramienta ??til para futuros consumidores en su b??squeda del mejor uso de su dinero en el mercado. En mi opini??n, las gr??ficas que dispone el dash no son muy ??tiles para nuestro an??lisis, ya que no permiten sacar conclusiones interesantes sobre la base de datos. "),
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
