# Price Recommendation Engine
A search engine for getting price statistics of motorcycles sold on Blocket

This search engine takes a query and filtering arguments and performs a tf-idf based search through a dataset of motorcycle ads. The ads that match the query best have their price average, maximum and minimum taken and presented to the user.

HOW TO USE:

1. Install pillow and elasticsearch modules for python.
   - `pip install pillow`,
   - `pip install elasticsearch`

2. Download and run Elasticsearch according to these instructions: https://www.elastic.co/downloads/elasticsearch 

3. Start the program with :
`python3 SearchGUI.py`

4. What you can filter on in the fields:
   - Query: Specify the search in free text (e.g. brand, model, color, condition - whatever you want)
   - City: Enter a location/city that you want to filter the search on. **_THIS FIELD IS NOT RECOMMENDED TO USE SINCE SOME CITIES ARE DIVIDED INTO SMALLER REGIONS AND THE MAIN CITY DOES NOT GIVE ANY HITS. SHOULD BE REPLACED BY DROPDOWN._**
   - Type: Select a specific motorcycle type or search amongst all types ("All")
   - Maximum Model Year: Select how new motorcycles you want to include in the search result
   - Minimum Model Year: Select how old motorcycles you want to include in the search result
