from weasyprint import HTML

HTML("book.html").write_pdf("book.pdf")

print("PDF успешно создан.")
