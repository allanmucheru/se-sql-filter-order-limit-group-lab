
import pandas as pd
import sqlite3

##### Part I: Basic Filtering #####

# Create the connection
conn1 = sqlite3.connect('planets.db')

# Select all
pd.read_sql("""SELECT * FROM planets; """, conn1)

# STEP 1: Planets with zero moons
df_no_moons = pd.read_sql("""
    SELECT *
    FROM planets
    WHERE num_of_moons = 0;
""", conn1)

# STEP 2: Planets with names containing exactly 7 letters
df_name_seven = pd.read_sql("""
    SELECT name, mass
    FROM planets
    WHERE LENGTH(name) = 7;
""", conn1)


##### Part 2: Advanced Filtering #####

# STEP 3: Planets with mass less than or equal to 1.00
df_mass = pd.read_sql("""
    SELECT name, mass
    FROM planets
    WHERE mass <= 1.00;
""", conn1)

# STEP 4: Planets with at least one moon and mass less than 1.00
df_mass_moon = pd.read_sql("""
    SELECT *
    FROM planets
    WHERE num_of_moons >= 1 AND mass < 1.00;
""", conn1)

# STEP 5: Planets with blue in their color
df_blue = pd.read_sql("""
    SELECT name, color
    FROM planets
    WHERE color LIKE '%blue%';
""", conn1)


##### Part 3: Ordering and Limiting #####

# Create the connection
conn2 = sqlite3.connect('dogs.db')

# Select all
pd.read_sql("SELECT * FROM dogs;", conn2)

# STEP 6: Hungry dogs sorted youngest to oldest
df_hungry = pd.read_sql("""
    SELECT name, age, breed
    FROM dogs
    WHERE hungry = 1
    ORDER BY age ASC;
""", conn2)

# STEP 7: Hungry dogs aged between 2 and 7,
# sorted alphabetically
df_hungry_ages = pd.read_sql("""
    SELECT name, age, hungry
    FROM dogs
    WHERE hungry = 1 AND age BETWEEN 2 AND 7
    ORDER BY name ASC;
""", conn2)

# STEP 8: Return the 4 oldest dogs
df_4_oldest = pd.read_sql("""
    SELECT name, age, breed
    FROM dogs
    ORDER BY age DESC
    LIMIT 4;
""", conn2)




##### Part 4: Aggregation #####

# Create the connection
conn3 = sqlite3.connect('babe_ruth.db')

# Select all
pd.read_sql("""
    SELECT * FROM babe_ruth_stats;
""", conn3)

# STEP 9: Total number of years Babe Ruth played
df_ruth_years = pd.read_sql("""
    SELECT COUNT(*) AS total_years
    FROM babe_ruth_stats;
""", conn3)

# STEP 10: Total home runs in his career
df_hr_total = pd.read_sql("""
    SELECT SUM(HR) AS total_home_runs
    FROM babe_ruth_stats;
""", conn3)


##### Part 5: Grouping and Aggregation #####

# STEP 11: Number of years played for each team
df_teams_years = pd.read_sql("""
    SELECT team, COUNT(*) AS number_years
    FROM babe_ruth_stats
    GROUP BY team;
""", conn3)

# STEP 12: Teams with average at bats greater than 200
df_at_bats = pd.read_sql("""
    SELECT team, AVG(at_bats) AS average_at_bats
    FROM babe_ruth_stats
    GROUP BY team
    HAVING AVG(at_bats) > 200;
""", conn3)


# Close the connections
conn1.close()
conn2.close()
conn3.close()
