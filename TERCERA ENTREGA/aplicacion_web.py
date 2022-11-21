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
        html.H3(children='Valentina Correa, Juliana Bermúdez, Sofía Duarte, Leonardo Luengas')]), # genera <h1>Dashboard Covid 19</h1>
    html.Br(),
    
    html.Div(className= "container", children=[
        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero."),
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
            
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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

            html.Div(className="col-12 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
            
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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

            html.Div(className="col-12 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
            ]),
        ]),
        
        html.Br(),
        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum."),

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
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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

            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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

            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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

            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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

            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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

            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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

            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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

            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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

            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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

            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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

            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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

            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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

            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
            ]),
        ]),

        html.Br(),
        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum."),

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
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
            html.Div(className="col-10 col-xl-6", children=[
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
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
                html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(), html.Br(),
                html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.")
            ]),
        ]),

        html.Br(),
        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum."),

        html.Hr(),

        html.Br(),
        html.Center(html.H2(children="Conclusiones")),
        html.Br(),
        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dolor in massa accumsan pellentesque. Nam interdum nisi vitae congue vestibulum. Nullam non volutpat odio. Mauris sed ante egestas enim dapibus malesuada. Maecenas feugiat eros diam, eget tempus nisl finibus eget. Ut condimentum semper enim id sodales. Pellentesque aliquam diam eu hendrerit mollis. Mauris commodo imperdiet ipsum, non condimentum magna tincidunt quis. Vivamus a augue erat. Cras interdum aliquam urna, eu fermentum lorem blandit sagittis. Praesent in porta massa, non dapibus lectus. Morbi sit amet enim vitae libero vehicula rutrum. Morbi lectus justo, rutrum nec viverra in, aliquam porttitor libero."),
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
