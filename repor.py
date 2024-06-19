import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import Tk, Frame, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Cargar los datos
df = pd.read_csv('C:/Users/RONALD/Downloads/data/dataset.csv', encoding='latin1')

# Eliminar duplicados y llenar valores faltantes
df.drop_duplicates(inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)

# Funciones de visualización
def mostrar_distribucion_popularity():
    plt.figure(figsize=(10, 6))
    sns.histplot(df['popularity'], bins=50, kde=True)
    plt.title('Distribución de Popularidad')
    plt.xlabel('Popularidad')
    plt.ylabel('Frecuencia')
    mostrar_grafico()

def mostrar_distribucion_danceability():
    plt.figure(figsize=(10, 6))
    sns.histplot(df['danceability'], bins=50, kde=True)
    plt.title('Distribución de Danceability')
    plt.xlabel('Danceability')
    plt.ylabel('Frecuencia')
    mostrar_grafico()

def mostrar_matriz_correlacion():
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title('Matriz de Correlación')
    mostrar_grafico()

def mostrar_top_tracks_popularity():
    top_tracks_popularity = df.sort_values(by='popularity', ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_tracks_popularity, x='popularity', y='track_name', hue='artists')
    plt.title('Top 10 Tracks por Popularidad')
    plt.xlabel('Popularidad')
    plt.ylabel('Track')
    mostrar_grafico()

def mostrar_top_artistas_tracks():
    top_artists_tracks = df['artists'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(y=top_artists_tracks.index, x=top_artists_tracks.values)
    plt.title('Top 10 Artistas por Cantidad de Tracks')
    plt.xlabel('Cantidad de Tracks')
    plt.ylabel('Artista')
    mostrar_grafico()

def mostrar_top_tracks_duration():
    top_tracks_duration = df.sort_values(by='duration_ms', ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_tracks_duration, x='duration_ms', y='track_name', hue='artists')
    plt.title('Top 10 Tracks por Duración')
    plt.xlabel('Duración (ms)')
    plt.ylabel('Track')
    mostrar_grafico()

def mostrar_grafico():
    fig = plt.gcf()
    for widget in frame.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
    # Agregar botón "Regresar" para volver al menú principal
    btn_regresar = Button(frame, text="Regresar", command=mostrar_menu_principal)
    btn_regresar.pack(pady=10)

def mostrar_menu_principal():
    for widget in frame.winfo_children():
        widget.destroy()
    # Botón para mostrar distribución de popularidad
    btn_distribucion_popularity = Button(frame, text="Distribución de Popularidad", command=mostrar_distribucion_popularity)
    btn_distribucion_popularity.pack(pady=5)
    # Botón para mostrar distribución de danceability
    btn_distribucion_danceability = Button(frame, text="Distribución de Danceability", command=mostrar_distribucion_danceability)
    btn_distribucion_danceability.pack(pady=5)
    # Botón para mostrar la matriz de correlación
    btn_matriz_correlacion = Button(frame, text="Matriz de Correlación", command=mostrar_matriz_correlacion)
    btn_matriz_correlacion.pack(pady=5)
    # Botón para mostrar los top 10 tracks por popularidad
    btn_top_tracks_popularity = Button(frame, text="Top 10 Tracks por Popularidad", command=mostrar_top_tracks_popularity)
    btn_top_tracks_popularity.pack(pady=5)
    # Botón para mostrar los top 10 artistas por cantidad de tracks
    btn_top_artistas_tracks = Button(frame, text="Top 10 Artistas por Tracks", command=mostrar_top_artistas_tracks)
    btn_top_artistas_tracks.pack(pady=5)
    # Botón para mostrar los top 10 tracks por duración
    btn_top_tracks_duration = Button(frame, text="Top 10 Tracks por Duración", command=mostrar_top_tracks_duration)
    btn_top_tracks_duration.pack(pady=5)

# Configuración de la interfaz gráfica
root = Tk()
root.title("Reportes de Música")
root.geometry("800x600")

frame = Frame(root)
frame.pack(pady=20)

# Mostrar el menú principal al iniciar la aplicación
mostrar_menu_principal()

root.mainloop()
