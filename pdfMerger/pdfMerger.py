from PyPDF2 import PdfMerger

#Funciona arrastrando a la lista los PDF que necesitas unir
pdfs = ["pdfMerger/Actividad_4.pdf","pdfMerger/Poniendose_en_la_piel_del_atacante.pdf","pdfMerger/merged.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()