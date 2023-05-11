import cirq
import time

# Circuito 1

print("------------------------------------------------------------")
print("Circuito simple con una sola puerta H partiendo del estado 0")
print("------------------------------------------------------------")
q0,q1 = cirq.LineQubit.range(2)
qc = cirq.Circuit(cirq.H(q0), cirq.measure(q0, key='qbit'))

print(qc)

simulator = cirq.Simulator()

for i in range(15):
    result = simulator.run(qc)
    print(f"{result} ", end='\n------\n')
    time.sleep(0.5)