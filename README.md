# What is it for?
This tool is made to check the numbers in translations of (technical) texts of consistency. So we are expecting the translation to contain the same numbers in the same order, as in the original text. Espacially when using modern AI for translation, like ChatGPT, there can be switched or missing numbers in the translation. 

# How to Use
You need to write a Excel file with titled columns for the two languages.
e.g.:



| ANSI  | EN               | ANSI  | DE                  |
| ----- | ---------------- | ----- | ------------------- |
| 12365 | Hello World!1!11 | 12368 | Hallo Welt!1!11!!!! |
| abc   | 3 deep 5 me      | abc   | zu tief für mich    |

When starting the progaram it requires the Path to the Excel and the name of the columns to compare, in this case "EN" and "DE".

In the example the first line will pass the test the second will fail.


# How to install under Windows
If you and your admin is trustful, just download the latest .exe from the dist folder.
No further installation is needed.

# How to install under Mac/Linux
For Mac and Linux there is no simple installation. 
You need to install Python and the libary pandas (```pip install pandas```).
Clone this Reposetory and execute the main file with python (```python main.py```)