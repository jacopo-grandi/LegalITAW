# XLSX

Use an installed spreadsheet library when available; otherwise use OOXML
carefully. Keep raw data, calculations, and presentation separate. Prefer
formulas over pasted calculated values, assign explicit number/date formats,
freeze useful headers, and size columns. Save the final workbook under
`output/`, reopen it, verify sheet names and key cells/formulas, and inspect the
ZIP package for corruption. Do not assume formula recalculation occurred unless
the runtime actually recalculated the workbook.
