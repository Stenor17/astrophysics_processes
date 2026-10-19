import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 11
})

# Griglia di punti per l'impulso p
p = np.linspace(-3, 3, 500)
E_min = -1.0
E_max = 3.0

mc = 1.0
# Relazione di dispersione relativistica per particella massiva: E/c = sqrt(p^2 + (mc)^2)
E_massive = np.sqrt(p**2 + mc**2)

p_abs = np.abs(p)

plt.figure(figsize=(6, 6))

# 2. Regione non permessa / non causale (E/c < |p|)
plt.fill_between(p, E_min, p_abs, 
                 color='salmon', alpha=0.3, label=r'Regione non permessa')

# Rette di luce per fotoni (m = 0 -> E/c = |p|)
plt.plot(p, p_abs, 'k--', linewidth=1.2, label=r'Relazione per fotoni')
plt.plot(p, -p_abs, 'k--', linewidth=0.8, alpha=0.4)

# Curva per la particella massiva
plt.plot(p, E_massive, 'b-', linewidth=2.0, label=r'Particella massiva ($E/c = \sqrt{p^2 + m^2c^2}$)')

# Assi coordinati
plt.axhline(0, color='black', linestyle='-', linewidth=0.8)
plt.axvline(0, color='black', linestyle='-', linewidth=0.8)

# Etichette assi e titolo
plt.xlabel(r'Impulso $p$')
plt.ylabel(r'Energia $\frac{E}{c}$')
plt.title(r'Relazione di dispersione e regioni permesse nello spazio $(p, E/c)$')
plt.xlim(-3, 3)
plt.ylim(-1, 3)
plt.grid(True, alpha=0.25)
plt.legend(loc='upper right', fontsize=10, framealpha=0.9)

plt.tight_layout()
plt.savefig('spazio_tempo_energia_impulso.pdf')
plt.show()