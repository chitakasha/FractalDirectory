from qiskit import QuantumCircuit, transpile, Aer, execute
from qiskit.algorithms import Shor
from qiskit.utils import QuantumInstance
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_image(n_qubits, n_points):
    circuit = QuantumCircuit(n_qubits)
    circuit.h(range(n_qubits))
    circuit.measure_all()

    simulator = Aer.get_backend('qasm_simulator')
    result = execute(circuit, simulator, shots=n_points).result()
    counts = result.get_counts(circuit)

    image = np.zeros((2**n_qubits, 2**n_qubits))
    for key, value in counts.items():
        x, y = map(int, key.split())
        image[x, y] = value

    number_to_factor = np.argmax(image)
    return image, number_to_factor

def factor_number_with_shor(number):
    backend = Aer.get_backend('qasm_simulator')
    q_instance = QuantumInstance(backend, shots=1024)
    shor = Shor(quantum_instance=q_instance)
    result = shor.factor(number)
    return result.factors

if __name__ == '__main__':
    image, number_to_factor = generate_fractal_image(3, 1000)
    plt.imshow(image, cmap='inferno')
    plt.colorbar()
    plt.title(f'Fractal Image with Number {number_to_factor} to Factor')
    plt.show()

    factors = factor_number_with_shor(number_to_factor)
    print(f'The factors of {number_to_factor} are {factors}')
