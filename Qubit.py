import numpy as np

class Qubit:
    def __init__(self, alpha=1+0j, beta=0+0j):
        # state = alpha|0> + beta|1>
        state = np.array([alpha, beta], dtype=complex)
        norm = np.linalg.norm(state)
        if norm == 0:
            raise ValueError("State vector cannot be zero")
        self.state = state / norm  # normalize so |alpha|^2 + |beta|^2 = 1

    def apply_gate(self, gate_matrix):
        self.state = gate_matrix @ self.state

    def measure(self):
        probs = np.abs(self.state) ** 2
        outcome = np.random.choice([0, 1], p=probs)
        # collapse the state
        self.state = np.array([1, 0], dtype=complex) if outcome == 0 else np.array([0, 1], dtype=complex)
        return outcome

    def __repr__(self):
        a, b = self.state
        return f"({a:.3f})|0> + ({b:.3f})|1>"


qubit = Qubit(1, 0)

print(qubit.measure())
