from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

class PDFReport:
    def __init__(self, filename):
        self.filename = filename
        self.canvas   = canvas.Canvas(filename, pagesize=A4)

    def add_title(self, title, x=50, y=800):
        self.canvas.setFont("Helvetica-Bold", 16)
        self.canvas.drawString(x, y, title)

    def add_table(self, data, start_x=50, start_y=750, row_height=20):
        y = start_y
        for row in data:
            x = start_x
            for cell in row:
                self.canvas.drawString(x, y, str(cell))
                x += 100
            y -= row_height

    def save(self):
        self.canvas.save()
