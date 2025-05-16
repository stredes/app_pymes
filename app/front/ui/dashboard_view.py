from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class DashboardView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        label = QLabel("🖥️ Dashboard: Resumen General")
        layout.addWidget(label)
        self.setLayout(layout)
