# import streamlit as st
# import pandas as pd

# # Exemple de données
# data = {
#     'Nom': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Âge': [24, 27, 22, 32],
#     'Ville': ['Paris', 'Lyon', 'Marseille', 'Toulouse']
# }

# df = pd.DataFrame(data)

# # Interface Streamlit
# st.title('Tableau Filtrable')

# # Filtre par ville
# ville = st.selectbox('Sélectionnez une ville', df['Ville'].unique())
# filtered_df = df[df['Ville'] == ville]

# # Affichage du tableau filtré
# st.write(filtered_df)

#==========================================================================================
# import streamlit as st
# import pandas as pd
# import numpy as np

# # Créer des données factices
# np.random.seed(42)
# data = {
#     'A': np.random.randint(0, 100, 100),
#     'B': np.random.randint(0, 100, 100),
#     'C': np.random.randint(0, 100, 100),
#     'D': np.random.choice(['Category 1', 'Category 2', 'Category 3'], 100)
# }
# df = pd.DataFrame(data)

# # Titre du tableau de bord
# st.title('Tableau de bord interactif avec Streamlit')

# # Widgets pour filtrer les données
# st.sidebar.header('Filtres')
# filter_A = st.sidebar.slider('Filtrer la colonne A', min_value=int(df['A'].min()), max_value=int(df['A'].max()), value=(int(df['A'].min()), int(df['A'].max())))
# filter_B = st.sidebar.slider('Filtrer la colonne B', min_value=int(df['B'].min()), max_value=int(df['B'].max()), value=(int(df['B'].min()), int(df['B'].max())))
# filter_C = st.sidebar.slider('Filtrer la colonne C', min_value=int(df['C'].min()), max_value=int(df['C'].max()), value=(int(df['C'].min()), int(df['C'].max())))
# filter_D = st.sidebar.multiselect('Filtrer la colonne D', options=df['D'].unique(), default=df['D'].unique())

# # Filtrer le DataFrame en fonction des widgets
# filtered_df = df[(df['A'] >= filter_A[0]) & (df['A'] <= filter_A[1]) &
#                  (df['B'] >= filter_B[0]) & (df['B'] <= filter_B[1]) &
#                  (df['C'] >= filter_C[0]) & (df['C'] <= filter_C[1]) &
#                  (df['D'].isin(filter_D))]

# # Afficher le DataFrame filtré
# st.write('Données filtrées:', filtered_df)

# # Quelques statistiques descriptives
# st.write('Statistiques descriptives:', filtered_df.describe())

# if st.button('Recharger les données'):
#     st.rerun()

# # Ajout d'un graphique interactif amélioré
# st.subheader('Graphique interactif des colonnes A, B et C')
# chart_data = filtered_df[['A', 'B', 'C']]
# st.line_chart(chart_data)

# # Ajout d'un histogramme pour la colonne A
# st.subheader('Histogramme de la colonne A')
# st.bar_chart(filtered_df['A'].value_counts())

# # Ajout de quelques boutons pour l'interaction basique
# if st.button('Afficher le nombre de catégories D'):
#     st.write('Nombre de catégories D:', filtered_df['D'].nunique())

# st.write('Catégories présentes:')
# st.write(filtered_df['D'].value_counts())
#==========================================================================================

# import streamlit as st
# from st_aggrid import AgGrid, GridOptionsBuilder
# from st_aggrid.grid_options_builder import GridOptionsBuilder
# import pandas as pd

# # Créer un exemple de DataFrame
# df = pd.DataFrame({
#     'Produit': ['A', 'B', 'C', 'D'],
#     'Quantité': [10, 20, 15, 25],
#     'Prix': [100, 200, 150, 250]
# })

# # Configurer les options du tableau
# gb = GridOptionsBuilder.from_dataframe(df)
# gb.configure_default_column(groupable=True, filterable=True)
# gb.configure_column('Prix', type=["numericColumn", "numberColumnFilter"], valueFormatter="data.Prix.toLocaleString('fr-FR') + ' €'")
# gb.configure_column('Quantité', type=["numericColumn"], aggFunc="sum")
# gb.configure_grid_options(enableRangeSelection=True, pinnedTopRowData=[{"Produit": "Total", "Prix": df['Prix'].sum()}])
# gb.configure_side_bar()

# # Rendu du tableau
# st.header("Tableau AgGrid")
# AgGrid(df, gridOptions=gb.build(), allow_unsafe_jscode=True)

#==========================================================================================


#javascript | DataTables.js

import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

def render_datatables(df):
    # Convertir le DataFrame principal en HTML
    df_html = df.to_html(index=False, table_id="datatable", border=0, classes="display nowrap")
    
    html = f"""
    <html>
    <head>
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css">
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/fixedheader/3.2.2/css/fixedHeader.dataTables.min.css">
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/fixedcolumns/4.0.2/css/fixedColumns.dataTables.min.css">
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/buttons/2.2.2/css/buttons.dataTables.min.css">
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/searchpanes/2.0.0/css/searchPanes.dataTables.min.css">
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/select/1.3.4/css/select.dataTables.min.css">
        
        <script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
        <script type="text/javascript" src="https://cdn.datatables.net/fixedheader/3.2.2/js/dataTables.fixedHeader.min.js"></script>
        <script type="text/javascript" src="https://cdn.datatables.net/fixedcolumns/4.0.2/js/dataTables.fixedColumns.min.js"></script>
        <script type="text/javascript" src="https://cdn.datatables.net/buttons/2.2.2/js/dataTables.buttons.min.js"></script>
        <script type="text/javascript" src="https://cdn.datatables.net/buttons/2.2.2/js/buttons.html5.min.js"></script>
        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
        <script type="text/javascript" src="https://cdn.datatables.net/searchpanes/2.0.0/js/dataTables.searchPanes.min.js"></script>
        <script type="text/javascript" src="https://cdn.datatables.net/select/1.3.4/js/dataTables.select.min.js"></script>
        
        <style>
            #datatable {{
                width: 100% !important;
                margin-bottom: 20px;
            }}
            .dataTables_wrapper {{
                max-width: 100%;
                overflow-x: hidden;
                padding-bottom: 50px;
            }}
            th, td {{
                text-align: center;
                vertical-align: middle;
                padding: 8px;
            }}
            .total-row {{
                background-color: #f8f9fa;
                font-weight: bold;
                border-top: 2px solid #ddd;
                position: sticky;
                bottom: 0;
                z-index: 10;
            }}
            .highlighted {{
                background-color: #fffde7 !important;
            }}
            .low-value {{
                color: red !important;
                font-weight: bold;
            }}
            #footer-container {{
                position: sticky;
                bottom: 0;
                background-color: white;
                border-top: 2px solid #ddd;
                z-index: 20;
                width: 100%;
            }}
            .dtsp-panesContainer {{
                width: 100%;
                padding: 5px;
                border: 1px solid #ddd;
                margin-bottom: 15px;
            }}
            .dtsp-searchPanes {{
                margin-bottom: 20px;
            }}
            .dtsb-group {{
                margin-bottom: 15px;
            }}
            .dt-buttons {{
                margin-bottom: 15px;
            }}
            .filter-container {{
                margin-bottom: 20px;
            }}
        </style>
    </head>
    <body>
        <div style="padding: 20px;">
            <div class="table-container">
                <div class="filter-container"></div>
                {df_html}
                <div id="footer-container">
                    <table id="totalTable" class="display" style="width:100%">
                        <tbody>
                            <tr class="total-row">
                                <td>TOTAL</td>
                                <td id="total-quantite">{df['Quantité'].sum()}</td>
                                <td id="total-prix">{df['Prix'].sum()}</td>
                                <td id="total-montant">{df['Montant'].sum()} €</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        
        <script>
            $(document).ready(function() {{
                // Configuration du tableau principal
                var table = $('#datatable').DataTable({{
                    dom: 'BPlfrtip',
                    fixedHeader: true,
                    scrollX: true,
                    scrollY: '400px',
                    scrollCollapse: true,
                    paging: false,
                    ordering: true,
                    searching: true,
                    info: false,
                    fixedColumns: {{
                        left: 1
                    }},
                    buttons: [
                        {{
                            extend: 'excel',
                            text: 'Exporter en Excel',
                            title: 'Données du tableau',
                            className: 'export-excel-btn',
                            exportOptions: {{
                                columns: ':visible',
                                format: {{
                                    body: function (data, row, column, node) {{
                                        // Nettoyer les données pour l'export Excel
                                        return data.replace(/ €/g, '');
                                    }}
                                }}
                            }},
                            customize: function(xlsx) {{
                                var sheet = xlsx.xl.worksheets['sheet1.xml'];
                                $('row c[r^="D"]', sheet).each(function() {{
                                    var value = parseInt($(this).text());
                                    if (value < 15000) {{
                                        $(this).attr('s', '26'); // Style rouge dans Excel
                                    }}
                                }});
                            }}
                        }}
                    ],
                    searchPanes: {{
                        layout: 'columns-3',
                        initCollapsed: true,
                        cascadePanes: true,
                        dtOpts: {{
                            select: {{
                                style: 'multi'
                            }}
                        }}
                    }},
                    columnDefs: [
                        {{ targets: '_all', className: 'dt-center' }},
                        {{ targets: 3, render: function(data, type, row) {{
                                if (type === 'display') {{
                                    // Pour l'affichage, on ajoute le symbole € et éventuellement la classe pour la couleur rouge
                                    var value = parseInt(data);
                                    var classAttr = value < 15000 ? ' class="low-value"' : '';
                                    return '<span' + classAttr + '>' + data + ' €</span>';
                                }}
                                return data;
                            }}
                        }},
                        {{ 
                            searchPanes: {{
                                show: true
                            }},
                            targets: [0, 1, 2]
                        }}
                    ],
                    createdRow: function(row, data, index) {{
                        // Mise en forme conditionnelle pour les valeurs élevées
                        if (parseFloat(data[3]) > 1000) {{
                            $(row).addClass('highlighted');
                        }}
                    }}
                }});
                
                // Déplacer les panneaux de recherche dans le conteneur de filtre
                $('.dtsp-panesContainer').appendTo('.filter-container');
                
                // Fonction pour mettre à jour les totaux en fonction des données visibles
                function updateTotals() {{
                    var visibleData = table.rows({{search:'applied'}}).data();
                    var totalQuantite = 0;
                    var totalPrix = 0;
                    var totalMontant = 0;
                    
                    for (var i = 0; i < visibleData.length; i++) {{
                        totalQuantite += parseInt(visibleData[i][1]) || 0;
                        totalPrix += parseInt(visibleData[i][2]) || 0;
                        // Pour le montant, on doit retirer le symbole € s'il existe
                        var montantStr = visibleData[i][3].toString().replace(' €', '');
                        totalMontant += parseInt(montantStr) || 0;
                    }}
                    
                    // Mettre à jour les cellules de totaux
                    $('#total-quantite').text(totalQuantite);
                    $('#total-prix').text(totalPrix);
                    
                    // Appliquer le style au total montant si nécessaire
                    var montantClass = totalMontant < 15000 ? ' class="low-value"' : '';
                    $('#total-montant').html('<span' + montantClass + '>' + totalMontant + ' €</span>');
                }}
                
                // Mettre à jour les totaux lors d'une recherche ou d'un tri
                table.on('search.dt draw.dt', updateTotals);
                
                // Ajuster la largeur du tableau des totaux pour correspondre au tableau principal
                $('#totalTable').css('width', $('#datatable').css('width'));
                
                // Synchroniser le scrolling horizontal entre les deux tableaux
                $('.dataTables_scrollBody').on('scroll', function() {{
                    $('#footer-container').css('margin-left', -$(this).scrollLeft());
                }});
                
                // Appel initial pour définir les totaux
                updateTotals();
            }});
        </script>
    </body>
    </html>
    """
    components.html(html, height=650, width=800, scrolling=True)

# Création d'un DataFrame avec plus de données factices
def create_sample_data(n=20):
    np.random.seed(42)
    products = ['Ordinateur', 'Téléphone', 'Tablette', 'Écran', 'Clavier', 'Souris', 
                'Imprimante', 'Casque', 'Enceinte', 'Caméra', 'Disque dur', 'Mémoire RAM']
    
    df = pd.DataFrame({
        'Produit': np.random.choice(products, n),
        'Quantité': np.random.randint(1, 50, n),
        'Prix': np.random.randint(50, 2000, n)
    })
    
    # Calculer le montant total
    df['Montant'] = df['Quantité'] * df['Prix']
    
    return df

# Utilisation
st.header("DataTables.js")
df = create_sample_data(25)  # Générer 25 lignes de données
render_datatables(df)
#==========================================================================================


# Utiliser Streamlit Components avec des bibliothèques JavaScript : Tabulator 

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import json

# Exemple avec Tabulator (bibliothèque JS)
def tabulator_component(data):
    # Convertir DataFrame en JSON
    json_data = data.to_json(orient='records')
    
    # Code HTML/JS pour Tabulator
    html = f"""
    <link href="https://unpkg.com/tabulator-tables@5.1.0/dist/css/tabulator.min.css" rel="stylesheet">
    <script type="text/javascript" src="https://unpkg.com/tabulator-tables@5.1.0/dist/js/tabulator.min.js"></script>
    
    <div id="example-table"></div>
    
    <script>
        var tableData = {json_data};
        var table = new Tabulator("#example-table", {{
            data: tableData,
            layout: "fitColumns",
            frozenRows: 1,
            columns: [
                {{title: "Produit", field: "Produit", frozen: true}},
                {{title: "Quantité", field: "Quantité", hozAlign: "right", formatter: "number"}},
                {{title: "Prix", field: "Prix", hozAlign: "right", formatter: "money", formatterParams: {{precision: 2, symbol: "€"}}}}
            ],
        }});
    </script>
    """
    components.html(html, height=400)

# Utilisation
df = pd.DataFrame({
    'Produit': ['A', 'B', 'C', 'D'],
    'Quantité': [10, 20, 15, 25],
    'Prix': [100, 200, 150, 250]
})

st.header("JavaScript : Tabulator ")
tabulator_component(df)

#==========================================================================================

import streamlit as st
import streamlit.components.v1 as components

def mui_table():
    # Code HTML avec React, Material-UI et Babel
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>MUI Table</title>
        
        <!-- Chargement des dépendances React -->
        <script src="https://unpkg.com/react@17/umd/react.production.min.js"></script>
        <script src="https://unpkg.com/react-dom@17/umd/react-dom.production.min.js"></script>
        
        <!-- Chargement de Babel pour JSX -->
        <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
        
        <!-- Chargement de Material-UI -->
        <script src="https://unpkg.com/@mui/material@5.0.0/umd/material-ui.production.min.js"></script>
        
        <!-- Styles -->
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                margin: 0;
                padding: 0;
            }
            #root {
                padding: 20px;
            }
            .MuiTableContainer-root {
                margin-top: 20px;
            }
            .MuiPaper-root {
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1) !important;
            }
            .MuiTableCell-head {
                font-weight: bold !important;
                background-color: #f5f5f5 !important;
            }
            .total-row {
                background-color: #f9f9f9 !important;
            }
        </style>
    </head>
    <body>
        <div id="root"></div>
        
        <script type="text/babel">
            // Définition des fonctions utilitaires
            const TAX_RATE = 0.07;
            
            function ccyFormat(num) {
                return `${num.toFixed(2)}`;
            }
            
            function priceRow(qty, unit) {
                return qty * unit;
            }
            
            function createRow(desc, qty, unit) {
                const price = priceRow(qty, unit);
                return { desc, qty, unit, price };
            }
            
            function subtotal(items) {
                return items.map(({ price }) => price).reduce((sum, i) => sum + i, 0);
            }
            
            // Données
            const rows = [
                createRow('Paperclips (Box)', 100, 1.15),
                createRow('Paper (Case)', 10, 45.99),
                createRow('Waste Basket', 2, 17.99),
            ];
            
            const invoiceSubtotal = subtotal(rows);
            const invoiceTaxes = TAX_RATE * invoiceSubtotal;
            const invoiceTotal = invoiceTaxes + invoiceSubtotal;
            
            // Récupération des composants Material-UI depuis window.MaterialUI
            const {
                Table,
                TableBody,
                TableCell,
                TableContainer,
                TableHead,
                TableRow,
                Paper
            } = MaterialUI;
            
            // Composant principal
            function SpanningTable() {
                return (
                    <TableContainer component={Paper}>
                        <Table sx={{ minWidth: 700 }} aria-label="spanning table">
                            <TableHead>
                                <TableRow>
                                    <TableCell align="center" colSpan={3}>
                                        Details
                                    </TableCell>
                                    <TableCell align="right">Price</TableCell>
                                </TableRow>
                                <TableRow>
                                    <TableCell>Desc</TableCell>
                                    <TableCell align="right">Qty.</TableCell>
                                    <TableCell align="right">Unit</TableCell>
                                    <TableCell align="right">Sum</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {rows.map((row) => (
                                    <TableRow key={row.desc}>
                                        <TableCell>{row.desc}</TableCell>
                                        <TableCell align="right">{row.qty}</TableCell>
                                        <TableCell align="right">{row.unit}</TableCell>
                                        <TableCell align="right">{ccyFormat(row.price)}</TableCell>
                                    </TableRow>
                                ))}
                                <TableRow className="total-row">
                                    <TableCell rowSpan={3} />
                                    <TableCell colSpan={2}>Subtotal</TableCell>
                                    <TableCell align="right">{ccyFormat(invoiceSubtotal)}</TableCell>
                                </TableRow>
                                <TableRow className="total-row">
                                    <TableCell>Tax</TableCell>
                                    <TableCell align="right">{`${(TAX_RATE * 100).toFixed(0)} %`}</TableCell>
                                    <TableCell align="right">{ccyFormat(invoiceTaxes)}</TableCell>
                                </TableRow>
                                <TableRow className="total-row">
                                    <TableCell colSpan={2}>Total</TableCell>
                                    <TableCell align="right">{ccyFormat(invoiceTotal)}</TableCell>
                                </TableRow>
                            </TableBody>
                        </Table>
                    </TableContainer>
                );
            }
            
            // Rendu du composant
            ReactDOM.render(<SpanningTable />, document.getElementById('root'));
        </script>
    </body>
    </html>
    """
    
    # Afficher le HTML via le composant Streamlit
    components.html(html, height=500, scrolling=True)

# Afficher le titre et le tableau
st.header("Table MUI avec sous-totaux")
mui_table()