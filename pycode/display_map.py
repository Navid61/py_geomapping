import folium
import psycopg2
import json
# from folium.utilities import JsCode
# from folium.elements import EventHandler

# Create a Folium map centered at an initial location
m = folium.Map(location=[45.5017, -73.5673], zoom_start=12)  # Centered on Montreal

# Database connection parameters
db_params = {
    'host': 'localhost',  # Update if needed
    'port': 5432,
    'dbname': 'montreal',
    'user': 'postgres',  # Update if needed
    'password': 'postgres'  # Update if needed
}

# Connect to the PostgreSQL database
try:
    db_conn = psycopg2.connect(**db_params)
    cursor = db_conn.cursor()

    # Query to retrieve GeoJSON data from the table
    query = """
SELECT json_build_object(
    'type', 'Feature',
    'geometry', ST_AsGeoJSON(geom)::json,
    'properties', json_build_object(
        'ID_UEV', ID_UEV,
        'NOM_RUE', NOM_RUE,
        'MUNICIPALITE', MUNICIPALITE
    )
) AS feature
FROM montreal_properties
WHERE ST_Intersects(
    geom,
    ST_MakeEnvelope(%s, %s, %s, %s, 4326)  -- Adjust the SRID as per your data
);
"""
    # Define bbbox
    # for findin bbox you can use bbox finder website
    
    # http://bboxfinder.com/

    bounds = (-73.793964,45.500933,-73.475189,45.613197)

    cursor.execute(query,bounds)
    features = [row[0] for row in cursor.fetchall()]

    # Close the cursor and connection
    cursor.close()
    db_conn.close()

    # Create GeoJSON FeatureCollection
    geo_json_data = {
        "type": "FeatureCollection",
        "features": features
    }

    # Add GeoJSON data to the Folium map
    g = folium.GeoJson(geo_json_data).add_to(m)

    # # JavaScript code for highlighting features
    # highlight = JsCode(
    #     """
    #     function highlight(e) {
    #         e.target.original_color = e.layer.options.color;
    #         e.target.setStyle({ color: "green" });
    #     }
    #     """
    # )

    # reset = JsCode(
    #     """
    #     function reset(e) {
    #         e.target.setStyle({ color: e.target.original_color });
    #     }
    #     """
    # )

    # g.add_child(EventHandler("mouseover", highlight))
    # g.add_child(EventHandler("mouseout", reset))
    

   
except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)
m
