<div style="text-align:center">
        <img    src="https://www.nylas.com/wp-content/uploads/JSON_Blog_Hero.png"
                title="JSON" 
                width="40%" 
                height="40%" />
</div>
<br>

# [Module 6: Objects and the JSON Format](https://www.geeksforgeeks.org/convert-class-object-to-json-in-python)

<br>

## [What is JSON](https://www.w3schools.com/whatis/whatis_json.asp).
JSON is a format that encodes objects into a string.
* https://realpython.com/python-json/
  
<br>

## [How to define an object](https://www.geeksforgeeks.org/convert-class-object-to-json-in-python/).
* ### [What is an object constructor](https://www.geeksforgeeks.org/constructors-in-python)
  * An object constructor is like a function. It's function is included by default in all classes. it is used by writing a function called `__init__`.You define how many parameters it includes. You also define what variables are stored into your object by assigning them to `self`.

```python

class Student:
  def __init__(self,  id:str, name:str):
    self.id = id
    self.name = name

s = Student("14-146", "Carlos Cobian")

```

<br>

## [Serialization and Deserialization](https://medium.com/swlh/object-serialization-and-deserialization-in-python-5fad3c2970a4)
 Serialization means to convert an object into a string representing an object, and deserialization is its inverse operation (convert string -> object). 
 * [Search winklerrr](https://stackoverflow.com/questions/3316762/what-is-deserialize-and-serialize-in-json)

### json.dump() vs. json.dumps()
* <u>json.dump</u> serializes an object into a file. It takes 2 parameters, the object and the destination file.
* <u>json.dumps</u> or *dump string* serializes an object into a string, that may then be stored into a variable for future use. It's only parameter is the object.

### Serialization of an object into a file
This file will be placed in the same directory as the script being executed.

```python
# Determine output Directory
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'student.json')

# Serialization
with open(myOutputFilePath, 'w') as outfile:
  json.dump(s.__dict__, outfile)
```

### Deserializing using a class
Passing each parameter to a constructor is tedious work. By using the two asterisks `**` we may take a JSON object and load it into a class. This will automatically match each class parameter with the equally named one found on the JSON object. 
```python
# Load file as JSON
file = open('student.json',)
studentJson = json.load(file)

# Construct Student Object
myStudent = Student(**studentJson)
```

<br>

# Class Discussion
## Answer the questions on the Markdown file located within your <u>`Module6`</u> directory (Module6.md)`(20pts)`
<!-- Welcome! These are your questions. -->
<!-- Answer using full sentences to receive all points. -->
<!-- 

What does JSON Stand for?

 - Answer: JavaScript Object Notation

Why are JSON formats important?

 - Answer: Helps transfer data from a server

Create an example of a JSON object with at least 4 values. It may represent anything but it must be original.

 - Answer: 
"car": "Toyota",
"school": "Colegio San Ignacio",
"video_game": "Minecraft"
"phone": "iPhone 13 Pro Max"


What is the difference between serialization and deserialization?

 - Answer: Serialization is a mechanism of converting the state of an object into a byte stream. Deserialization is the opposite process where the byte stream is used to recreate the actual Java object in memory.

Research data persistance. What did you find?

 - Answer: the continuance of an effect after its cause is removed

Type down any class notes below this sentence:



Lackluster responses may result in point deductions.
-->

<br>

## [Next Module ->](/../../tree/main/Modules/Module7/Module7.md)
