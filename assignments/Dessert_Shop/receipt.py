
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet 


DATA = [ 
	[ "Name" , "Item Cost", "Tax"], 
	[ 
		"Candy Corn", 
		"$0.38", 
		"$0.03"], 
	[ "Gummy Bears", "$0.09", "$0.01"], 
    ["Chocolate Chip", "$2.00", "$0.14"],
    ["Pistachio", "$1.58", "$0.11"],
    ["Vanilla", "$3.36", "$0.24"],
    ["Oatmeal Raisin", "$0.57", "$0.04"],
	[ "Sub Total", "$7.97","$0.58"], 
	[ "Order Total", "","$8.55"], 
	[ "Total Items in the order", "", "6"], 
] 

pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 ) 


styles = getSampleStyleSheet() 


title_style = styles[ "Heading1" ] 


title_style.alignment = 1

title = Paragraph( "Dessert Shop Reciept" , title_style ) 


style = TableStyle( 
	[ 
		( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
		( "GRID" , ( 0, 0 ), ( 8 , 8 ), 1 , colors.black ), 
		( "BACKGROUND" , ( 0, 0 ), ( 2, 0 ), colors.gray ), 
		( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
		( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
		( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
	] 
) 


table = Table( DATA , style = style ) 

pdf.build([ title , table ]) 
