from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def make_receipt(data, out_file_name):
    pdf = canvas.Canvas(out_file_name, pagesize=letter)
    pdf.setTitle("Receipt")
    width, height = letter
    y = height - 50

    # Generate receipt content
    for row in data:
        text = f"{row[0]:<20} {row[2]:<11} {row[3]}"
        pdf.drawString(72, y, text)
        y -= 20

    pdf.save()

def main():
    data = [
        ["     Name     ", "   Item Cost", "Tax"],
        ["Candy Corn    ", "      $0.38", "$0.03"],
        ["Gummy Bears   ", "      $0.09", "$0.01"],
        ["Chocolate Chip", "      $2.00", "$0.14"],
        ["Pistachio     ", "      $1.58", "$0.11"],
        ["Vanilla       ", "      $3.36", "$0.24"],
        ["Oatmeal Raisin", "      $0.57", "$0.04"],
        ["--------------------"],
        ["Order Subtotals", "     $7.97", "$0.58"],
        ["Order Total", "", "              $8.55"],
        ["Total items in the order", "", "     6"]
    ]
    make_receipt(data, "receipt.pdf")

if __name__ == "__main__":
    main()