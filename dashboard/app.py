import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__)

# Read CSV
df = pd.read_csv("data/amazon.csv")

# Top 10 rated products
top_rated = df.sort_values(by='rating', ascending=False).head(10)
fig1 = px.bar(top_rated, x='product_name', y='rating', color='category',
              title='Top 10 Rated Products')
fig1.update_layout(xaxis_tickangle=-45)

# Most reviewed products
most_reviewed = df.sort_values(by='rating_count', ascending=False).head(10)
fig2 = px.bar(most_reviewed, x='product_name', y='rating_count', color='category',
              title='Most Reviewed Products')
fig2.update_layout(xaxis_tickangle=-45)

# Discount analysis
fig3 = px.box(df.dropna(subset=['discount_percentage']), 
              x='category', y='discount_percentage', color='category',
              title='Discount Distribution by Category')
fig3.update_layout(xaxis_tickangle=-45)

# Display product images & links (top 5)
top_images = df.head(5)
image_layout = []
for _, row in top_images.iterrows():
    # Ensure https and fallback placeholder
    img_link = row['img_link'] if str(row['img_link']).startswith("https") else "https://via.placeholder.com/150"
    
    image_layout.append(html.Div([
        html.Img(src=img_link, style={'width': '150px', 'height': '150px'}),
        html.Br(),
        html.A(row['product_name'], href=row['product_link'], target='_blank')
    ], style={'display': 'inline-block', 'margin': '10px', 'textAlign': 'center'}))  # ✅ fixed textAlign

app.layout = html.Div([
    html.H1("Amazon Products Dashboard"),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3),
    html.H2("Top Products with Images"),
    html.Div(image_layout)
])

if __name__ == "__main__":
    app.run(debug=True)
