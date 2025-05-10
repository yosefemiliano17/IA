from tkinter import *
from pyswip import Prolog

prolog = Prolog()
prolog.consult("Sistema_Experto_Enfermedades_Respiratorias.pl")

sintomas = [
    'fiebre', 'tos', 'dolor_garganta', 'dolor_muscular', 'secrecion_nasal',
    'estornudos', 'dificultad_respirar', 'dolor_pecho', 'cansancio_extremo',
    'dolor_cabeza', 'perdida_olfato', 'perdida_gusto', 'escalofrios',
    'sibilancias', 'tos_con_flema', 'nauseas', 'vomitos', 'fatiga',
    'tos_seca', 'ronquera', 'ojos_llorosos', 'contacto_con_infectado',
    'dificultad_para_tragar', 'alergico_a_algo', 'diarrea'
]

root = Tk()
root.title("Sistema Experto - Diagnóstico Respiratorio")
root.geometry("500x700")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True)

header_frame = Frame(main_frame)
header_frame.pack(fill=X, pady=10)

title_label = Label(header_frame, text="Sistema Experto de Diagnóstico Respiratorio", 
                    font=("Arial", 16, "bold"))
title_label.pack()

checkbutton_canvas_frame = Frame(main_frame)
checkbutton_canvas_frame.pack(fill=BOTH, expand=True)

scrollbar = Scrollbar(checkbutton_canvas_frame)
scrollbar.pack(side=RIGHT, fill=Y)

canvas = Canvas(checkbutton_canvas_frame)
canvas.pack(fill=BOTH, expand=True)

scrollbar.config(command=canvas.yview)
canvas.config(yscrollcommand=scrollbar.set)

frame_sintomas = Frame(canvas)
canvas.create_window((0, 0), window=frame_sintomas, anchor="nw")


variables = {}
for sintoma in sintomas:
    var = IntVar()
    chk = Checkbutton(frame_sintomas, text=sintoma.replace("_", " ").capitalize(), variable=var)
    chk.pack(anchor="w")
    variables[sintoma] = var


frame_sintomas.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))


bottom_frame = Frame(main_frame)
bottom_frame.pack(fill=X, side=BOTTOM, pady=20)


btn = Button(bottom_frame, text="Diagnosticar", command=lambda: diagnosticar())
btn.pack(pady=10)


resultado_frame = Frame(bottom_frame, bd=2, relief=GROOVE)
resultado_frame.pack(fill=X, padx=20, pady=10)


Label(resultado_frame, text="RESULTADO:", font=("Arial", 12, "bold")).pack(pady=5)
"""resultado_label = Label(resultado_frame, text="Esperando diagnóstico...", 
                        wraplength=400, justify="center", font=("Arial", 12), fg="black",
                        height=3)  # Especificar altura mínima"""
resultado_label = Label(resultado_frame, text="Esperando diagnóstico...", 
                        wraplength=400, justify="left", anchor="w",  # mejor alineado
                        font=("Arial", 12), fg="black")

resultado_label.pack(pady=10, fill=X)


def diagnosticar():

    list(prolog.query("retractall(sintoma_usuario(_))"))
   
    sintomas_seleccionados = []
    for sintoma, var in variables.items():
        if var.get():
            sintomas_seleccionados.append(sintoma)
            list(prolog.query(f"assertz(sintoma_usuario({sintoma}))"))
    
    if not sintomas_seleccionados:
        resultado_label.config(text="Por favor, seleccione al menos un síntoma")
        return
    
    resultado = list(prolog.query("diagnosticar(Diagnosticos)"))

    if resultado and resultado[0]['Diagnosticos']:
        diagnosticos = resultado[0]['Diagnosticos']
        texto_final = ""

        for d in diagnosticos:
            info = list(prolog.query(f"mostrar_info({d}, Info)"))  
            if info:
                detalles = info[0]['Info']
                detalles_texto = "\n".join(d.decode() if isinstance(d, bytes) else str(d) for d in detalles)
                texto_final += f"{detalles_texto}\n\n"
            else:
                texto_final += f"Diagnóstico: {d}\n(No hay información adicional disponible)\n\n"

        resultado_label.config(text=texto_final.strip())
    else:
        resultado_label.config(text="No se pudo determinar un diagnóstico exacto.")
    
    """if resultado and resultado[0]['Diagnosticos']:
        diagnosticos = resultado[0]['Diagnosticos']
        print("Diagnóstico en consola:", diagnosticos)
        resultado_texto = ", ".join(str(d) for d in diagnosticos)
        resultado_label.config(text=resultado_texto)
    else:
        resultado_label.config(text="No se pudo determinar un diagnóstico exacto.")"""

root.mainloop()