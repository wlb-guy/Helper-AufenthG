en_remove:
	python ./tools/en_md_remove.py

en_title:
	python ./tools/en_mdtitle.py

en: en_remove en_title

de_remove:
	python ./tools/de_md_remove.py

de: de_remove

