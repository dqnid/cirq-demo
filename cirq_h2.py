import cirq
import time

# Circuito 2
print("--------------------------------------------------------")
print("Circuito con 2 mediciones consecutivas tras una puerta H")
print("--------------------------------------------------------")
q0,q1 = cirq.LineQubit.range(2)
qc = cirq.Circuit(cirq.H(q0), cirq.measure(q0, key='qbit_pre'), cirq.measure(q0, key='qbit_post'))

print(qc)

simulator = cirq.Simulator()

for i in range(15):
    result = simulator.run(qc)
    print(f"{result} ", end='\n------\n')
    time.sleep(0.5)