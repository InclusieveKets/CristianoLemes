---
layout: default
title: Section 04 - Basic of electronics
use_math: true
---

# Basic of electronics

The class took place by Zoom where Bruce Helsen could share his knowledge and experience with everyone.
Basically the class was organazied in the following parts: (i) Basics concepts in electronics circuits; (ii) Measurements tools that supports electronics; (iii) Basics components used to design a circuit; and (iv) How to apply the theory in practice to choose the correct component when designing a circuit including some examples of Transistor and Mosfet.
Shortly we got the idea of (vi) Motors and (vii) Buzzers.

## Basics concepts

| Concept    | Symbol | Unit   | Symbol  |
|------------|--------|--------|---------|
| Resistence | R      | Ohm    | &#x3a9; |
| Voltage    | U      | Volts  | V       |
| Current    | I      | Ampere | A       |
| Eletrical power | P | .      | .       |
| Induction  | L      | Henry  | H       |

It was presented the resistence values for different types or materials.

Important equations was introduced as well.

* U = R * I
* P = U * I
* P = U^2 / R


## Measurements tools

### Power supply

* Generate power for the electronic circuit.
* It can be from different types, from old power supply for computers, to a phone charger.

### Multimeter

* Used to measure the voltage, current, or resistence of a circuit.
* It is necessary to connect the wires correctly to get the right measurements.

### Oscilloscope

* Measure only voltage but in real time.
* It shows the waves of its variation over the time.

### Functie generator


## Basic components

It was shown several components that can be embedded into the eletronic circuit including and pratical simulation of how each component iteracts in the circuit.

### Resistor (Weerstanden)

* It consumes the voltage in a circuit.
* Exist several types of resistors.
	* Adjustable resistor - potentiometer
	* Flexible resistors
* LDR - Light Dependent Resistor.
* An important property is its temperature as consequence of consuming the voltage.
* The colors code for resistor indicate how strong they are. It was shown a table with different colors and their values.

### Power supply (Bron)

* It can be batteries or any energy source.

### Switches (Schakelaar)

* Used to close or open the electronic circuit.
* Types
	* normal open/close.
	* bistabiel/drukknop.
	* meer polig;
	* wisselschakelaar (SPDT - single pin)

### Inductors (Spoel)

### Capacitors (Condensator)

* Used to save (little) energy to perform functionalities when there is not power supply.

### Relay (Relais)

* Switch that can be controled using energy;

### Diode

* Let the current flow only in one direction;
* Exist different kinds of diodes
	* zenerdiode(stabilsator)
	* schotkeydiode()
	* photodiode
* LED is a common exampe of diode.

### Transistor

* Used to amplify and control the current.
* It needs a protective resistor.
* Important equations:
	* I_c = I_b * H_fe
	* I_e = I_c + I_b
* The transistor most used is the BC547.
* Summary
	* H_fe DC current gain
	* V_be Base emitter forward voltage
	* I_c Collector Currentor

### Mosfet()

* Voltage controller for the current flowing;
* The mosfet most common is of the type _N channe_
	* Enhancement
	* Enhancement no bulk semi
	* Depletion
* Summary
	* V_ds drain'source breakdown voltage
	* V_gs(th) gate threshold voltage
	* V_gs(on) static drain-source on-

### Spanningsregelaar

* Voltage regulator.
* It consumes the excedent voltage used in the component.

### Spanningsdeler

* Voltage dividor.

## Pratical examples

* How to calculate the resistor to not burn a LED
	U_r = U_bronspanning - U_LED / stroom door LED

	U_b = 12V; U_led=1.78V; I_led=10mA
	U_r = 12V - 1.78 = 10.22
	R = U / I = 10.22 / 0.01 = 1022&#x3a9;

* How to use transistor/mosfet
	See example for Transistor and calculation done during class.
	See example for Mosfet.

* Important use a diode to avoid burn the relay;
* Calculate the resistor in order to turn on the relay;

## Motors (Motoren)

* DC motoren - normal motor (turn around in circle)
* Servo Motoren - like an arm
* Stappen motoren - control how the motor turn around in circle.

## Buzzer

* Change shape and create voltage;

## Opdracht (task for next week)
* Try to design a circuit.

# Websites

* Software for seeing electronic circuits: falstad circuit simulator (https://www.falstad.com/circuit/)
* voltage divider calculator
* www.mouser.be/semiconductors/

