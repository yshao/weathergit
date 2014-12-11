from PyQt4.QtGui import QApplication, QListView, QStandardItemModel, QStandardItem
import sys

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
# Create a Qt application
app = QApplication(sys.argv)
 
# Our main window will be a QListView
list = QListView()
list.setWindowTitle('Honey-Do List')
list.setMinimumSize(600, 400)
 
# Create an empty model for the list's data
model = QStandardItemModel(list)
 
# Add some textual items
foods = [
    'Cookie dough', # Must be store-bought
    'Hummus', # Must be homemade
    'Spaghetti', # Must be saucy
    'Dal makhani', # Must be spicy
    'Chocolate whipped cream' # Must be plentiful
]
 
for food in foods:
    # Create an item with a caption
    item = QStandardItem(food)
 
    # Add a checkbox to it
    item.setCheckable(True)
 
    # Add the item to the model
    model.appendRow(item)
 
def on_item_changed(item):
    # If the changed item is not checked, don't bother checking others
    if not item.checkState():
        return
 
    # Loop through the items until you get None, which
    # means you've passed the end of the list
    i = 0
    while model.item(i):
        if not model.item(i).checkState():
            return
        i += 1
 
    app.quit()
 
model.itemChanged.connect(on_item_changed)
 
# Apply the model to the list view
list.setModel(model)
 
# Show the window and run the app
list.show()
app.exec_()