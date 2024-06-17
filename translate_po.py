import polib
from googletrans import Translator


def translate_po_file(po_file, source_lang='en', target_lang='es', ignore_existing=True):
    """
    Translates entries in a PO file using Google Translate.

    Args:
        po_file (str): Path to the PO file to translate.
        source_lang (str, optional): Source language code (default: 'en').
        target_lang (str, optional): Target language code (default: 'es').
        ignore_existing (bool, optional): Whether to ignore entries with existing translations (default: True).

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified PO file is not found.
    """

    try:
        po = polib.pofile(po_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"PO file '{po_file}' not found.")

    translator = Translator()

    for entry in po:
        if ignore_existing and entry.msgstr.strip():
            continue  # Skip entries with existing translations

        try:
            print(f"Translating: '{entry.msgid}'")
            translation = translator.translate(entry.msgid, src=source_lang, dest=target_lang)
            entry.msgstr = translation.text
            print(f"Translation: '{entry.msgid}' -> '{entry.msgstr}'")
        except Exception as e:
            print(f"Error translating '{entry.msgid}': {e}")

    po.save(po_file)


if __name__ == "__main__":
    po_file = "es_MX.po" #
    translate_po_file(po_file)  # Use default language codes (en -> es)

    # Example with custom language codes and ignoring existing translations
    translate_po_file(po_file, source_lang="en", target_lang="es", ignore_existing=False)
