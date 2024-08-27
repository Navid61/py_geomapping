# folium_geomapping




### Get Data address -- Downlod from here


[<h1>montreal data</h1>](https://donnees.montreal.ca/en/dataset/unites-evaluation-fonciere)

 
### Download data from url
### python script for downloading data
###


### databsae name is montreal

```sql
CREATE DATABASE montreal;
```

### Create table name montreal_properties for importing properties assessment geojosn file to that

```sql
CREATE TABLE montreal_properties (
    ID_UEV BIGINT PRIMARY KEY,
    CIVIQUE_DEBUT INTEGER,
    CIVIQUE_FIN INTEGER,
    NOM_RUE VARCHAR(255),
    SUITE_DEBUT VARCHAR(255),
    MUNICIPALITE VARCHAR(255),
    ETAGE_HORS_SOL INTEGER,
    NOMBRE_LOGEMENT INTEGER,
    ANNEE_CONSTRUCTION INTEGER,
    CODE_UTILISATION INTEGER,
    LETTRE_DEBUT VARCHAR(10),
    LETTRE_FIN VARCHAR(10),
    LIBELLE_UTILISATION VARCHAR(255),
    CATEGORIE_UEF VARCHAR(50),
    MATRICULE83 VARCHAR(50),
    SUPERFICIE_TERRAIN INTEGER,
    SUPERFICIE_BATIMENT INTEGER,
    NO_ARROND_ILE_CUM VARCHAR(50),
    geom GEOMETRY  -- This is the geometry column to store spatial data
);
```

### Postgis Installed

```sql
CREATE EXTENSION postgis;
```

### You can find out what version you have, with postgis_full_version().

```sql
SELECT PostGIS_Full_Version();
```

### You can also check to see what alternate PostGIS versions might be installed.

```sql
SELECT * FROM pg_available_extensions WHERE name = 'postgis';
```

### Create new polygon layer

```sql
CREATE TABLE study_area (
    id SERIAL PRIMARY KEY,
    geom GEOMETRY  -- This is the geometry column to store spatial data
);
```

### table name is montrieal_properties

### clip sql query

```sql
CREATE TABLE clipped_properties AS
SELECT p.*
FROM montreal_properties p
JOIN study_area s
ON ST_Intersects(ST_Transform(p.geom, 32198), s.geom)
WHERE ST_Within(ST_Transform(p.geom, 32198), s.geom);
```