# Text Analyzer With API (Python Standard Libraries Only)
This repository consists of implementations of text anlayzer with API included.

Text analyzer includes :
  - Word count
  - Number of Letters
  - Longest word
  - Average word length
  - Reading Duration in Seconds
  - Median word length
  - Median word when sorted by length
  - Top 5 most common words
  - Language (English and Turkish only)
of the input text.

# Usage of API

- By using POST method one can find analysis of desired text.

Sample usage :

```
POST http://127.0.0.1:8080/
REQUEST BODY:
{
    "text": "Deep pressure or deep touch pressure is a form of tactile sensory input. This input is most often delivered through firm holding, cuddling, hugging, firm stroking, and squeezing.\n\nHowever, before we get into too much detail about deep touch pressure, we need to understand our body’s sensory system and why deep touch pressure emerged in the first place.\n\nNeurologically, sensory processing is how we feel. Through processing sensory input, we make sense of the world around us. In everything we do, we are receiving sensory messages from both our bodies and the surrounding world."
}

RESPONSE:
{

"wordCount": "94",

"letters": "470",

"longest": "Neurologically",

"avgLength": "5.0",

"duration": "28.2",

"medianWordLength": "4.5",

"medianWord": "('about', 'need')",

"commonWords": "['we', 'sensory', 'pressure', 'deep', 'touch']",

"language": "English"
}

```

- One can also add **"analysis"** option to request body in POST method.

Analysis option includes filtering. If there is no option given on request, program returns all fields.

**Valid parameters for "analysis":**
  - "wordCount" for Word count
  - "letters" for Number of Letters
  - "longest" for Longest word
  - "avgLength" for Average word length
  - "duration" for Reading Duration in Seconds
  - "medianWordLength" for Median word length
  - "medianWord" for Median word when sorted by length
  - "commonWords" for Top 5 most common words
  - "language" for Language

Sample Usage of Analysis Method:

```
POST http://127.0.0.1:8080/
REQUEST BODY:
{
    "text": "Deep pressure or deep touch pressure is a form of tactile sensory input. This input is most often delivered through firm holding, cuddling, hugging, firm stroking, and squeezing.\n\nHowever, before we get into too much detail about deep touch pressure, we need to understand our body’s sensory system and why deep touch pressure emerged in the first place.\n\nNeurologically, sensory processing is how we feel. Through processing sensory input, we make sense of the world around us. In everything we do, we are receiving sensory messages from both our bodies and the surrounding world.",
    "analysis": ["wordCount", "letters", "medianWordLength"]
}
RESPONSE:
{

"wordCount": "94",

"letters": "470",

"medianWordLength": "4.5"
}

```
- API adds responses for each request to db.json as well. One can check db.json file to see related responses, too.

- Finally, one can use DELETE method to delete all responses saved to db.json file.
