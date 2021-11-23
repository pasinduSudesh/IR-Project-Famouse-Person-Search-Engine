# IR-Project-Famouse-Person-Search-Engine
This is a search engine that can seach famouse book writer's details

## Stup Environment
- Download and Install the ElasticSearch 7.15.1
- Install the ICU_Tokenizer 
- clone the repogitory from https://github.com/pasinduSudesh/IR-Project-Famouse-Person-Search-Engine
- Activare virtual environment using  env/Scripts/activate
- Install the packages using pip install -r requirements.txt

## Run the Project
- Start ElasticSearch by running elasticsearch Windows Batch File
- Its running on http://localhost:9200
- Go to the project directory and run python create_index.py for the create index
- Run main.py for the srart server
- It is running on http://localhost:5000
- Now search queries can run in UI

## About Search Engine
### File Structure
- data - Preprocessed data that used for index creation
- data_collect - collected data and script for preprocess the data
- templates - HTML file for User Interface
- create_index.py - create index in ElasticSearch
- queries.py - Contain queries that can read Elastic search
- search.py - Search functionality
- main.py - flask server

### Book Writer Details
Data is contained in jason file.All data in sinhala language. Writer name is in both Sinhala and English language. Writer details feilds are
 - writer_name - Name of the writer in Sinhala
 - writer_name_eng - Name of the writer in English
 - writer_dob - writer date of birth
 - writer_birth_place - Writer birth place or birth state
 - book_list - List of books that writer wrote
 - writer_life_story - Small description of writer's life story
 - writtern_language - book writtern languages
 - wrote_categories - Book categorios
 - education - Schools and Universities writer went
 
 Eg:
         
         {
            "writer_name": "විමලරත්න කුමාරගම",
            "writer_name_eng": "Vimalarathne Kumaragama",
            "writer_dob": "1919 ජනවාරි 18",
            "writer_birth_place": "පාතදුම්බර",
            "education": [
                "කටුගස්තොට ශ්‍රී රාහුල විද්‍යාලය"
            ],
            "book_list": [
                "නිල්සීනය",
                "ඔරුව",
                "සංවේග වේදනා",
                "සපුමලී",
                "සුරතල්ලු",
                "ආරච්චිරාළ"
            ],
            "writer_life_story": "විමලරත්න කුමාරගම 1919 ජනවාරි 18......",
            "writtern_language": [
                "සිංහල"
            ],
            "wrote_categories": [
                "කාව්‍ය",
                "ළමා කවි"
            ]
        }
 
 ### Functionalities
 - Can search by using writer_name, writer_name_eng, writer_dob, writer_birth_place, book_list, writer_life_story, writtern_language, wrote_categories

  - ඇලන් මුවර්, ජී‍.බී. සේනානායක, දැල් කවුළුව, පේරාදෙණිය විශ්වවිද්‍යාලය

- Search engine can understand some synonyms related to writer name, writer birth place, writer wrote books, writer education level
  - Writer Name - රැයිපියෙල් තෙන්නකෝන් රචකයා, මහගම සේකර ගත්කරු
  - Writer Birth Place - කොළඹ උපන් රචකයෝ
  - Writer wrote books - රතු රෝස ලියූ රචකයා
  - Writer education level - රද්දොළුවේ බුදුනු පාසල ඉගෙනගත් රචකයා

- Writer can search their name in English language

  - author mahagama sekara 

- Search Query can be in both sinhala and English languagr

  - author මහගම සේකර

### Indexing Techniques
- 'ICU_Tokenizer is used for sinhala languahge tokenizer
-  'edge_ngram' filter is used for buils n-grams

### Query Techniques
Rule based text mining method is used to identify the quey strings
Used synonyms for identify the search fields

Usef following query types in ElasticSearch
1. cross_field queries
2. phrase_prefix queries


