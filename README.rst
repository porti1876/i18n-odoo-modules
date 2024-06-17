## PO File Translation Script (README.rst)

**English**

This script translates entries within a Portable Object (PO) file using Google Translate. It provides an efficient way to localize software applications for different languages.

**Spanish**

Este script traduce las entradas dentro de un archivo de Objeto Portátil (PO) utilizando Google Translate. Proporciona una forma eficiente de localizar aplicaciones de software para diferentes idiomas.

**Installation**

Before using this script, you need to install the required Python libraries:

```bash
pip install polib googletrans
```
**Usage**

Save the script as translate_po.py.
Open a terminal or command prompt and navigate to the directory containing the script and your PO file.
Run the script with the following command:

```
python translate_po.py <po_file>
```

Example:

```
python translate_po.py es_MX.po
```

This will translate the es_MX.po file (Spanish - Mexico) using English as the source language.

**Changing Languages**

By default, the script translates from English to the target language
specified in the PO file (e.g., Spanish in the example).
You can customize the languages using optional arguments:

```
python translate_po.py <po_file> --source <source_lang> --target <target_lang>
```

- <po_file>: Path to your PO file.
- --source <source_lang>: Source language code (e.g., 'fr' for French).
- --target <target_lang>: Target language code (e.g., 'de' for German).

**Ignoring Existing Translations**

The script by default skips entries that already have translations in the PO file. To translate even existing entries, use the --ignore-existing flag:

```
python translate_po.py <po_file> --ignore-existing
```
Documentation

For further details about the script functionality and parameters, refer to the source code within translate_po.py.

Disclaimer

Please note that Google Translate offers machine translations, which might not always be accurate or nuanced. Consider using a professional translation service for critical applications.

**Additional Notes:**

- The RST file is formatted using reStructuredText (reST), a lightweight markup language commonly used for documentation in Python projects.
- The `..` directives provide structure and styling to the content, such as headings, paragraphs, and code blocks.
- The `rst` extension in your text editor or IDE should help with syntax highlighting and formatting.
- The `README.rst` filename is a convention for documentation files in Python projects.

Feel free to ask if you have any further questions or modifications.