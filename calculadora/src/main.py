import flet as ft
import math


def main(page: ft.Page):
    page.title="Calculadora Simple"
    page.bgcolor=ft.Colors.BLACK87
    
    titulo=ft.Text(
        "🧮 Calculadora Basica",
        size=28,
        color=ft.Colors.WHITE54,
        text_align="center",
        weight="bold"
    )
    
    num1=ft.TextField(
        label="Numero 1",
        width=200,
        text_style=ft.TextStyle(ft.Colors.GREEN)
    )
    
    num2=ft.TextField(
        label="Numero 2",
        width=200,
        text_style=ft.TextStyle(ft.Colors.GREEN)
    )
    
    resultado=ft.Text(
        value="Resultado",
        size=20,
        color=ft.Colors.YELLOW,
        text_align="center"
    )
   
    info=ft.Container(
    content=ft.Text(
        "📊 Para el boton porcentaje: el campo de arriba es el número base y el de abajo es el porcentaje(%) que quieres calcular",
        size=13,
        color=ft.Colors.YELLOW,
        text_align="center",
        italic=True,
        max_lines=2,
        overflow="clip"
    ),
    alignment=ft.alignment="center",
    width=400,
    padding=5  
    )
    
    
    def mostrar_resultado(value):
        resultado.value=f"Resultado: {valor}",
        page.update()
        
        
    def suma(e):
        try:
            res=float(num1.value)+float(num2.value)
            mostrar_resultado(res)
        except:
            mostrar_resultado("Error")
            
    def resta(e):
        try:
            res=float(num1.value)-float(num2.value)
            mostrar_resultado(res)
        except:
            mostrar_resultado("Error")
        
   
    page.add()


ft.app(main)
