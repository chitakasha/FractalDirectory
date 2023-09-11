from qiskit import QuantumCircuit, transpile, Aer, execute
import numpy as np
import matplotlib.pyplot as plt

def qft_rotations(circuit, n):
    for qubit in range(n):
        circuit.h(qubit)
        for qubit2 in range(qubit+1, n):
            circuit.cp(np.pi/2**(qubit2-qubit), qubit2, qubit)

def generate_fractal_image(n_qubits, n_points):
    circuit = QuantumCircuit(n_qubits)
    qft_rotations(circuit, n_qubits)
    circuit.measure_all()

    simulator = Aer.get_backend('qasm_simulator')
    result = execute(circuit, simulator, shots=n_points).result()
    counts = result.get_counts(circuit)

    image = np.zeros((2**n_qubits, 2**n_qubits))
    for key, value in counts.items():
        x, y = map(int, key.split())
        image[x, y] = value

    plt.imshow(image, cmap='inferno')
    plt.colorbar()
    plt.title('Quantum Fourier Fractal')
    plt.show()

if __name__ == '__main__':
    generate_fractal_image(3, 1000)
