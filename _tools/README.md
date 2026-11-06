# Rebuilding the vault from a newer PDF
Requires poppler (`pdftohtml`, `pdftotext`) and Python 3.
1. `pdftohtml -xml -i <guide>.pdf full` → `full.xml`
2. `pdftotext -bbox-layout -f 2 -l <last TOC page> <guide>.pdf toc.html` then run the TOC parser
   then `python3 make_toc.py toc.html` to produce `toc.json` = [[indent, title, page], ...]
3. `python3 parse.py` → `parsed.pkl`
4. `python3 build_vault.py` → vault under /home/claude/vault (adjust OUT/FOLDERS page ranges for the new edition)
FOLDERS in build_vault.py maps page ranges to section folders and must be re-checked per edition.
