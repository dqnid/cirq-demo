import cirq
import time

# Circuito 3
print("Circuito con dos puertas H consecutivas que parte de 0")
q1,q2 = cirq.LineQubit.range(2)
qc = cirq.Circuit(cirq.H(q1), cirq.H(q1), cirq.measure(q1, key='qbit-0'))

print(qc)

simulator = cirq.Simulator()
for i in range(15):
    result = simulator.run(qc)
    print(f"{result} ", end='\n------\n')
    time.sleep(0.5)

print("Circuito con dos puertas H consecutivas que parte de 1")
q1,q2 = cirq.LineQubit.range(2)
qc = cirq.Circuit(cirq.X(q1),cirq.H(q1), cirq.H(q1), cirq.measure(q1, key='qbit-1'))

print(qc)

simulator = cirq.Simulator()
for i in range(15):
    result = simulator.run(qc)
    print(f"{result} ", end='\n------\n')
    time.sleep(0.5)
