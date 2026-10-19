import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 11
})

# Griglia di punti per x e limiti ct
x = np.linspace(-3, 3, 500)
ct_max = 3.0
ct_min = -3.0

ct_abs = np.abs(x)

plt.figure(figsize=(6, 6))

# 1. Futuro Causale (ct >= |x|)
plt.fill_between(x, ct_abs, ct_max, 
                 color='skyblue', alpha=0.3, label=r'Futuro causale')

# 2. Passato Causale (ct <= -|x|)
plt.fill_between(x, ct_min, -ct_abs, 
                 color='lightgreen', alpha=0.3, label=r'Passato causale')

# 3. Regione Non Permessa Causalmente / Spacelike (-|x| < ct < |x|)
plt.fill_between(x, -ct_abs, ct_abs, 
                 color='salmon', alpha=0.3, label=r'Regione non permessa')

# Disegno delle linee di luce (ct = x e ct = -x)
plt.plot(x, x, 'k--', linewidth=1.2, label=r'Cono di luce ($ct = \pm x$)')
plt.plot(x, -x, 'k--', linewidth=1.2)

# Assi coordinati
plt.axhline(0, color='black', linestyle='-', linewidth=0.8)
plt.axvline(0, color='black', linestyle='-', linewidth=0.8)

# Etichette di testo sul grafico per maggiore chiarezza
plt.text(0, 1.8, 'FUTURO', fontsize=12, fontweight='bold', ha='center', color='black')
plt.text(0, -1.8, 'PASSATO', fontsize=12, fontweight='bold', ha='center', color='black')

# Etichette assi e titolo
plt.xlabel(r'Posizione $x$')
plt.ylabel(r'Tempo $ct$')
plt.title(r'Diagramma Spazio-Tempo con Struttura Causale')
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.grid(True, alpha=0.2)
plt.legend(loc='upper right', fontsize=12, framealpha=0.9)

plt.tight_layout()
plt.savefig('spazio_tempo_tempo_posizione.pdf')
plt.show()