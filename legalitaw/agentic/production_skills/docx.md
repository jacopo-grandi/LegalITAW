# DOCX

Use Python and `python-docx` for ordinary Word documents. Build the document in
`scratch/`, save the final file under `output/`, reopen it, and verify that all
required paragraphs and tables are present. For tracked changes or comments,
edit the OOXML package explicitly: a DOCX is a ZIP archive and changes belong
in `word/document.xml`; comments additionally require the comments part,
relationships, and content-type declarations. Never claim that revisions or
comments exist without reopening the package and checking those parts.
