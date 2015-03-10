import multiprocessing, multiprocessing.pool, time, random, sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def compute(num_row):
    print("worker started at %d" % num_row)
    random_number = random.randint(1, 10)
    for second in range(random_number):
        progress = float(second) / float(random_number) * 100
        compute.queue.put((num_row, progress,))
        time.sleep(1)
    compute.queue.put((num_row, 100))

def pool_init(queue):
    # see http://stackoverflow.com/a/3843313/852994
    compute.queue = queue

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.toolBar = self.addToolBar("Toolbar")
        self.toolBar.addAction(QAction('Add Task', self, triggered=self.addTask))
        self.table = QTableWidget()
        self.table.verticalHeader().hide()
        self.table.setColumnCount(3)
        self.setCentralWidget(self.table)

        # Pool of Background Processes
        self.queue = multiprocessing.Queue()
        self.pool = multiprocessing.Pool(processes=4, initializer=pool_init, initargs=(self.queue,))

        # Check for progress periodically
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateProgress)
        self.timer.start(2000)

    def addTask(self):
        num_row = self.table.rowCount()
        self.pool.apply_async(func=compute, args=(num_row,))
        label = QLabel("Queued")
        bar = QProgressBar()
        bar.setValue(0)
        task = QLabel("Task")
        self.table.setRowCount(num_row + 1)
        self.table.setCellWidget(num_row, 0, task)
        self.table.setCellWidget(num_row, 1, label)
        self.table.setCellWidget(num_row, 2, bar)

    def updateProgress(self):
        if self.queue.empty(): return
        num_row, progress = self.queue.get() # unpack
        print("received progress of %s at %s" % (progress, num_row))
        task = self.table.cellWidget(num_row,0)
        task.setText('Task')
        label = self.table.cellWidget(num_row, 1)
        bar = self.table.cellWidget(num_row, 2)
        bar.setValue(progress)
        if progress == 100:
            label.setText('Finished')
        elif label.text() == 'Queued':
            label.setText('Downloading')
        self.updateProgress() # recursion

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())