# https://stackoverflow.com/questions/8826965/converting-a-qtreewidge-in-pyqt-to-a-table-in-reportlab

from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

pdf = SimpleDocTemplate("TreeWidgetPDF.pdf", pagesize = letter)
data = []
tStyle = []

for x in QTreeWidgetData.findItems("*", Qt.MatchWildcard, 0):
    project = str(x.text(0))
    data.append([project, x.text(1)])
    tStyle.append(('BACKGROUND', (0, cell), (1, cell), 'YELLOW'))
    tStyle.append(('FONTSIZE', (0, cell), (1, cell), 12))
    cell+=1

    for y in range(x.childCount()):
        data.append([str(x.child(y).text(0)), str(x.child(y).text(1))])
        tStyle.append(('ALIGN', (1, cell), (1, cell), 'RIGHT'))
        tStyle.append(('LEFTPADDING', (0, cell), (0, cell), 15))
        cell+=1

        for z in range(x.child(y).childCount()):
            data.append([x.child(y).child(z).text(0), x.child(y).child(z).text(1)])
            tStyle.append(('ALIGN', (1, cell), (1, cell), 'RIGHT'))
            tStyle.append(('LEFTPADDING', (0, cell), (0, cell), 30))
            cell+=1

        # And so on and so forth. You could probably iterate through this in a
        # While loop so you don't have to manually nest your for statements.

parts = []
styledTable = Table(data, [6 * inch, 1 * inch, 0])
styledTable.setStyle(TableStyle(tStyle))
parts.append(table_with_style)
pdf.build(parts)