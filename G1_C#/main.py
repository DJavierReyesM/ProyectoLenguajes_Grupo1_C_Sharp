import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from analizadores.lexico import *
from analizadores.sintactico import *
from analizadores.semantico import *
from datetime import datetime, timezone

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Analizador - Proyecto G1')
        self.geometry("960x500")

        # self.code_entry = tk.Text(self, width=100, height=15)

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=3)

        self.create_widgets()

    def create_widgets(self):

        padding = {'padx': 6, 'pady': 5}
        # label
        ttk.Label(self, text="Ingreso de codigo:").grid(column=0, row=1, **padding)
        ttk.Label(self, text="Salida del programa:").grid(column=0, row=3)

        # Entry
        self.code_entry = ScrolledText(self, width=100, height=10)
        self.code_entry.grid(column=0, row=2, columnspan=3, **padding)
        self.code_entry.focus()

        # Output
        self.salida = ScrolledText(self, width=100, height=10)
        self.salida.grid(column=0, row=4, columnspan=3, **padding)

        # Button
        lexico = ttk.Button(self, text='Analizar (Léxico)', command=self.lexico)
        lexico.grid(column=0, row=0, **padding)

        sintactico = ttk.Button(self, text='Analizar (Sintáctico)', command=self.sintactico)
        sintactico.grid(column=1, row=0, **padding)

        semantico = ttk.Button(self, text='Analizar (Semántico)', command=self.semantico)
        semantico.grid(column=2, row=0, **padding)

        limpiar = ttk.Button(self, text='Limpiar', command=self.limpiar)
        limpiar.grid(column=3, row=0, **padding)

    def lexico(self):
        self.salida.delete('1.0', tk.END)
        codigo = self.code_entry.get(1.0, "end-1c")
        self.salida.insert(tk.INSERT, f'Analisis Léxico para: {codigo}\n')

        now = datetime.now()
        fecha = now.strftime("%m/%d/%Y, %H:%M:%S")
        file = open('G1_C#/logs/logPruebasGeneral.txt', 'a')
        file.write("-------------Analisis Lexico - Timestamp:" + fecha + "\nEntrada\n")

        lexer.input(codigo)

        file.write(f"Analisis Lexico para: {codigo}\n")

        texto = getTokens(lexer)

        file.write(texto)

        self.salida.insert(tk.INSERT, "\n")

        self.salida.insert(tk.INSERT, texto)
        self.salida.insert(tk.INSERT, "\n")

    def sintactico(self):
        self.salida.delete('1.0', tk.END)
        # errores.clear()
        codigo = self.code_entry.get(1.0, "end-1c")
        self.salida.insert(tk.INSERT, f'Analisis Sintáctico para: {codigo}\n')

        now = datetime.now()
        fecha = now.strftime("%m/%d/%Y, %H:%M:%S")
        file = open('G1_C#/logs/logPruebasGeneral.txt', 'a')
        file.write("-------------Analisis Sintactico - Timestamp:" + fecha + "\nEntrada\n")

        self.salida.insert(tk.INSERT, validaReglaSintactica(codigo))
        self.salida.insert(tk.INSERT, "\n")

        file.write(f"Analisis Sintactico para: {codigo}\n")
        file.write(validaReglaSintactica(codigo))

        for str_err in errores_sintactico:
            self.salida.insert(tk.INSERT, str_err)
            file.write(str_err)
        file.close()
        self.salida.insert(tk.INSERT, "\n")

    def semantico(self):
        self.salida.delete('1.0', tk.END)
        codigo = self.code_entry.get(1.0, "end-1c")
        self.salida.insert(tk.INSERT, f'Analisis Semántico para: {codigo}\n')

        now = datetime.now()
        fecha = now.strftime("%m/%d/%Y, %H:%M:%S")
        file = open('G1_C#/logs/logPruebasGeneral.txt', 'a')
        file.write("-------------Analisis Semantico - Timestamp:" + fecha + "\nEntrada\n")

        self.salida.insert(tk.INSERT, validaReglaSemantica(codigo))
        self.salida.insert(tk.INSERT, "\n")

        file.write(f"Analisis Semantico para: {codigo}\n")
        file.write(validaReglaSemantica(codigo))

        for str_err in errores_semantico:
          self.salida.insert(tk.INSERT, str_err)
          file.write(str_err)
        file.close()
        self.salida.insert(tk.INSERT, "\n")

    def limpiar(self):
        self.code_entry.delete('1.0', tk.END)
        self.salida.delete('1.0', tk.END)

if __name__ == "__main__":
    app = App()
    app.mainloop()