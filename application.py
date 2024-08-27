import tkinter as tk
from tkinter import ttk
from linked_list import LinkedList
from telemetry import generate_telemetry_data

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Corrida")

        self.telemetry_list = LinkedList()

        self.input_frame = ttk.Frame(root, padding="10")
        self.input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.label_track_size = ttk.Label(self.input_frame, text="Tamanho da Pista (km):")
        self.label_track_size.grid(row=0, column=0, sticky=tk.W)

        self.entry_track_size = ttk.Entry(self.input_frame)
        self.entry_track_size.grid(row=0, column=1)

        self.label_fuel = ttk.Label(self.input_frame, text="Combustível Inicial (L):")
        self.label_fuel.grid(row=1, column=0, sticky=tk.W)

        self.entry_fuel = ttk.Entry(self.input_frame)
        self.entry_fuel.grid(row=1, column=1)

        self.simulate_button = ttk.Button(self.input_frame, text="Simular Corrida", command=self.simulate_race)
        self.simulate_button.grid(row=2, column=0, columnspan=2)

        self.display_frame = ttk.Frame(root, padding="10")
        self.display_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.data_text = tk.Text(self.display_frame, width=80, height=20)
        self.data_text.grid(row=0, column=0, sticky=(tk.W, tk.E))

        self.calculate_button = ttk.Button(self.display_frame, text="Calcular Estatísticas", command=self.calculate_statistics)
        self.calculate_button.grid(row=1, column=0, pady=10, sticky=tk.W)

    def simulate_race(self):
        try:
            track_size = float(self.entry_track_size.get())
            initial_fuel = float(self.entry_fuel.get())
            traveled_distance = 0
            remaining_fuel = initial_fuel
            self.telemetry_list = LinkedList()

            while remaining_fuel > 0:
                data = generate_telemetry_data(traveled_distance, remaining_fuel)
                self.telemetry_list.insert(data)
                traveled_distance = data.distance
                remaining_fuel = data.fuel

            self.display_data()
        except ValueError:
            self.data_text.delete('1.0', tk.END)
            self.data_text.insert(tk.END, "Por favor, insira valores válidos para o tamanho da pista e o combustível.\n")

    def display_data(self):
        self.data_text.delete('1.0', tk.END)
        for data in self.telemetry_list.iterate():
            self.data_text.insert(tk.END, f"Distância: {data.distance:.2f} km, Velocidade: {data.speed:.2f} km/h, Aceleração: {data.acceleration:.2f} m/s², RPM: {data.rpm}, Pressão Pneus: {data.tire_pressure:.2f} PSI, Combustível: {data.fuel:.2f} L, Temp. Motor: {data.engine_temperature:.2f} °C, Frenagem: {'Sim' if data.braking else 'Não'}, Consumo Combustível: {data.fuel_consumption:.2f} L\n")

    def calculate_statistics(self):
        total_brakes = 0
        total_fuel_consumption = 0
        total_temperature = 0
        total_points = 0

        for data in self.telemetry_list.iterate():
            if data.braking:
                total_brakes += 1
            total_fuel_consumption += data.fuel_consumption
            total_temperature += data.engine_temperature
            total_points += 1

        result = (f"Total de Frenagens: {total_brakes}\n"
                  f"Consumo Médio de Combustível: {total_fuel_consumption / total_points if total_points > 0 else 0:.2f} L\n"
                  f"Temperatura Média do Motor: {total_temperature / total_points if total_points > 0 else 0:.2f} °C\n")

        self.data_text.delete('1.0', tk.END)
        self.data_text.insert(tk.END, result)

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
