import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QLineEdit, QTextEdit, QPushButton, QListWidget

class OrcamentoMensalApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Orçamento Mensal")
        self.setGeometry(100, 100, 400, 500)  # Aumentei a altura da janela

        self.label_mes = QLabel("Selecione o mês:", self)
        self.label_mes.move(20, 20)

        self.combo_mes = QComboBox(self)
        self.combo_mes.move(200, 20)
        self.combo_mes.activated.connect(self.atualizar_informacoes)

        self.label_valor = QLabel("Informe o valor estimado:", self)
        self.label_valor.move(20, 60)

        self.entrada_valor = QLineEdit(self)
        self.entrada_valor.move(200, 60)

        self.label_gastos = QLabel("Informe os gastos mensais:", self)
        self.label_gastos.move(20, 100)

        self.entrada_nome_gasto = QLineEdit(self)
        self.entrada_nome_gasto.setGeometry(20, 140, 200, 30)

        self.entrada_valor_gasto = QLineEdit(self)
        self.entrada_valor_gasto.setGeometry(240, 140, 100, 30)

        self.botao_adicionar_gasto = QPushButton("Adicionar Gasto", self)
        self.botao_adicionar_gasto.setGeometry(20, 180, 120, 30)
        self.botao_adicionar_gasto.clicked.connect(self.adicionar_gasto)

        self.lista_gastos = QListWidget(self)
        self.lista_gastos.setGeometry(20, 220, 360, 100)

        self.botao_atualizar = QPushButton("Atualizar", self)
        self.botao_atualizar.setGeometry(20, 360, 120, 30)
        self.botao_atualizar.clicked.connect(self.atualizar_informacoes)

        self.botao_salvar = QPushButton("Salvar", self)
        self.botao_salvar.setGeometry(260, 360, 120, 30)
        self.botao_salvar.clicked.connect(self.salvar_dados)

        self.label_total_gastos = QLabel("", self)  # Adicionei esse label
        self.label_total_gastos.setGeometry(20, 400, 200, 30)

        self.label_lucro_mensal = QLabel("", self)  # Adicionei esse label
        self.label_lucro_mensal.setGeometry(240, 400, 200, 30)

        self.atualizar_lista_meses()

    def criar_tabelas(self):
        conn = sqlite3.connect('dados_mensais.db')
        cursor = conn.cursor()

        # Criação das tabelas (incluindo as já mencionadas)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT,
                valor REAL,
                data TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS gastos_mensais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT,
                valor REAL,
                mes TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS gastos_variaveis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT,
                valor REAL,
                mes TEXT
            )
        ''')

        # Salvar e fechar a conexão
        conn.commit()
        conn.close()

    def atualizar_lista_meses(self):
        meses = [f"2023-{str(i).zfill(2)}" for i in range(11, 13)] + [f"2024-{str(i).zfill(2)}" for i in range(1, 13)]
        self.combo_mes.clear()
        self.combo_mes.addItems(meses)

    def atualizar_informacoes(self):
        mes_selecionado = self.combo_mes.currentText()

        conn = sqlite3.connect('dados_mensais.db')
        cursor = conn.cursor()

        # Buscar valor estimado para o mês
        cursor.execute("SELECT valor FROM transacoes WHERE descricao = ?",
                       (f"Entrada {mes_selecionado}",))
        valor_estimado = cursor.fetchone()

        # Buscar gastos mensais
        cursor.execute("SELECT descricao, valor FROM gastos_mensais WHERE mes = ?",
                       (mes_selecionado,))
        gastos_mensais = cursor.fetchall()

        conn.close()

        if valor_estimado:
            self.entrada_valor.setText(str(valor_estimado[0]))

    def adicionar_gasto(self):
        nome_gasto = self.entrada_nome_gasto.text()
        valor_gasto = self.entrada_valor_gasto.text()

        if nome_gasto and valor_gasto:
            gasto_text = f"{nome_gasto}: {valor_gasto}"
            self.lista_gastos.addItem(gasto_text)

            self.entrada_nome_gasto.clear()
            self.entrada_valor_gasto.clear()

    def salvar_dados(self):
        entrada_mes = self.combo_mes.currentText()
        valor_estimado = self.entrada_valor.text()

        conn = sqlite3.connect('dados_mensais.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transacoes (descricao, valor, data) VALUES (?, ?, ?)",
                       (f"Entrada {entrada_mes}", valor_estimado, f"{entrada_mes}-01"))

        for i in range(self.lista_gastos.count()):
            gasto = self.lista_gastos.item(i).text()
            descricao, valor = gasto.split(": ")
            cursor.execute("INSERT INTO gastos_mensais (descricao, valor, mes) VALUES (?, ?, ?)",
                           (descricao, valor, entrada_mes))

        conn.commit()
        conn.close()

        self.atualizar_informacoes()

        total_gastos = sum(float(self.lista_gastos.item(i).text().split(": ")[1]) for i in range(self.lista_gastos.count()))
        lucro_mensal = float(valor_estimado) - total_gastos

        # Mostrar os valores na interface
        self.label_total_gastos.setText(f"Total de Gastos: {total_gastos}")
        self.label_lucro_mensal.setText(f"Saldo Mensal: {lucro_mensal}")

def main():
    app = QApplication(sys.argv)
    window = OrcamentoMensalApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
