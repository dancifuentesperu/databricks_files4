# Databricks notebook source

###############################################
#          Author: Daniel Cifuentes           #
#          Last update: 22/06/2025            #
###############################################

#01
# Definir nombres de catalog, schema, volume 

catalog_name        = "integration_catalog6"
schema_name_raw     = "raw_files"
volume_name_raw     = "files"
volume_name_tmp     = "tmp"
schema_name_tables  = "raw_tables"

# BRONZE
schema_name_bronze  = "bronze_layer"
table_name_bronze   = "titanic_bronze"
# SILVER
schema_name_silver  = "silver_layer"
table_name_silver   = "titanic_silver"
# GOLD
schema_name_gold  = "gold_layer"
table_name_gold   = "titanic_gold"

# schema 
workspace_folder       = "lab_test2"

#02
#################################################

# Definir nombres de catalog, schema, volume 

#catalog_name        = "integration_catalog"
#schema_name_raw     = "raw_files"
#volume_name_raw     = "files"
#volume_name_tmp     = "tmp"
#schema_name_tables  = "raw_tables"


#3

# Definir nombres de catalog, schema, volume 

#catalog_name        = "integration_catalog4"
#schema_name_raw     = "raw_files"
#volume_name_raw     = "files"
#volume_name_tmp     = "tmp"
#schema_name_tables  = "raw_tables"
