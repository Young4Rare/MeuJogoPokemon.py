import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class Pokemon:
    def __init__(self, nome, tipo, ataques):
        self.nome = nome
        self.tipo = tipo
        self.ataques = ataques
        self.hp_max = 100  # Pontos de vida máximos
        self.hp_atual = self.hp_max  # Pontos de vida atuais

class JogoPokemon:
    def __init__(self):
        self.pokemons = {
            'Água': [],
            'Fogo': [],
            'Planta': [],
            'Voador': [],
            'Lutador': []
        }

        # Adicionando mais Pokémons de exemplo com nomes de ataques em português
        self.criar_pokemon("Magikarp", "Água", ["Salpicar", "Investida"])
        self.criar_pokemon("Vaporeon", "Água", ["Cauda Aqua", "Jato de Água"])
        self.criar_pokemon("Psyduck", "Água", ["Jato de Água", "Confusão"])

        self.criar_pokemon("Vulpix", "Fogo", ["Brasinha", "Giro de Fogo"])
        self.criar_pokemon("Growlithe", "Fogo", ["Lança-Chamas", "Mordida"])
        self.criar_pokemon("Ponyta", "Fogo", ["Explosão de Fogo", "Pisoteio"])

        self.criar_pokemon("Oddish", "Planta", ["Absorver", "Pó Venenoso"])
        self.criar_pokemon("Bellsprout", "Planta", ["Chicote de Vinha", "Pó Sonífero"])
        self.criar_pokemon("Exeggcute", "Planta", ["Semente Sanguessuga", "Confusão"])

        self.criar_pokemon("Pidgeotto", "Voador", ["Rajada de Vento", "Ataque Rápido"])
        self.criar_pokemon("Spearow", "Voador", ["Bicada", "Ás Áereo"])
        self.criar_pokemon("Farfetch'd", "Voador", ["Corte", "Voo"])

        self.criar_pokemon("Mankey", "Lutador", ["Golpe Karatê", "Chute Baixo"])
        self.criar_pokemon("Hitmonlee", "Lutador", ["Chute Salto Alto", "Mega Chute"])
        self.criar_pokemon("Machoke", "Lutador", ["Rasteira", "Submissão"])

        self.janela = tk.Tk()
        self.janela.title("Jogo de Pokémon")

        self.label_seu_pokemon = tk.Label(self.janela, text="Seu Pokémon: ")
        self.label_seu_pokemon.grid(row=0, column=0, padx=10, pady=10)

        self.label_pokemon_inimigo = tk.Label(self.janela, text="Pokémon Inimigo: ")
        self.label_pokemon_inimigo.grid(row=1, column=0, padx=10, pady=10)

        label_tipo = tk.Label(self.janela, text="Escolha um tipo:")
        label_tipo.grid(row=2, column=0, padx=10, pady=10)

        tipos = list(self.pokemons.keys())
        combo_tipo = tk.StringVar()
        combo_tipo.set(tipos[0])

        dropdown_tipo = tk.OptionMenu(self.janela, combo_tipo, *tipos)
        dropdown_tipo.grid(row=2, column=1, padx=10, pady=10)

        botao_escolher = tk.Button(self.janela, text="Escolher Pokémon", command=lambda: self.escolher_e_batalhar(combo_tipo.get()))
        botao_escolher.grid(row=2, column=2, padx=10, pady=10)

        self.janela.mainloop()

    def criar_pokemon(self, nome, tipo, ataques):
        pokemon = Pokemon(nome, tipo, ataques)
        self.pokemons[tipo].append(pokemon)

    def escolher_pokemon(self, tipo):
        pokemon_escolhido = random.choice(self.pokemons[tipo])
        return pokemon_escolhido

    def batalhar(self, seu_pokemon, pokemon_inimigo, ataque_escolhido):
        if ataque_escolhido in seu_pokemon.ataques:
            dano_causado = random.randint(10, 20)  # Ajuste conforme necessário
            pokemon_inimigo.hp_atual -= dano_causado

            self.atualizar_interface_batalha(seu_pokemon, pokemon_inimigo, ataque_escolhido, dano_causado)

            if pokemon_inimigo.hp_atual <= 0:
                resultado = "vitória"
                mensagem = f"Você derrotou {pokemon_inimigo.nome}!"
                self.mostrar_mensagem_batalha("Batalha de Pokémon", mensagem)
            else:
                resultado = "continuar"
        else:
            self.mostrar_mensagem_batalha("Ataque Inválido", "Seu Pokémon não conhece esse ataque!")
            resultado = "ataque_inválido"

        return resultado

    def escolher_e_batalhar(self, tipo):
        seu_pokemon = self.escolher_pokemon(tipo)
        pokemon_inimigo = self.escolher_pokemon(tipo)

        self.mostrar_pokemon_batalha(seu_pokemon, pokemon_inimigo)

        while seu_pokemon.hp_atual > 0 and pokemon_inimigo.hp_atual > 0:
            ataque_escolhido = self.escolher_ataque(seu_pokemon)
            if ataque_escolhido is None:
                # O usuário cancelou a escolha do ataque
                break

            resultado = self.batalhar(seu_pokemon, pokemon_inimigo, ataque_escolhido)

            if resultado == "ataque_inválido":
                continue  # Permitir que o usuário escolha outro ataque se o anterior foi inválido

            # Simulação do ataque do Pokémon adversário
            if pokemon_inimigo.hp_atual > 0:
                dano_causado_inimigo = random.randint(5, 15)  # Ajuste conforme necessário
                seu_pokemon.hp_atual -= dano_causado_inimigo

                self.atualizar_interface_batalha(seu_pokemon, pokemon_inimigo, "Ataque Inimigo", dano_causado_inimigo)

        if resultado == "vitória":
            self.mostrar_mensagem_batalha("Batalha de Pokémon", "Você venceu a batalha!")
        elif resultado == "derrota":
            self.mostrar_mensagem_batalha("Batalha de Pokémon", "Você foi derrotado. Tente novamente!")

    def escolher_ataque(self, pokemon):
        ataque_escolhido = simpledialog.askstring("Escolha de Ataque", f"Escolha um ataque para {pokemon.nome}:\n{', '.join(pokemon.ataques)}")
        return ataque_escolhido

    def mostrar_pokemon_batalha(self, seu_pokemon, pokemon_inimigo):
        self.label_seu_pokemon.config(text=f"Seu Pokémon: {seu_pokemon.nome} ({seu_pokemon.tipo}) - HP: {seu_pokemon.hp_atual}/{seu_pokemon.hp_max}")
        self.label_pokemon_inimigo.config(text=f"Pokémon Inimigo: {pokemon_inimigo.nome} ({pokemon_inimigo.tipo}) - HP: {pokemon_inimigo.hp_atual}/{pokemon_inimigo.hp_max}")

    def atualizar_interface_batalha(self, seu_pokemon, pokemon_inimigo, ataque, dano):
        mensagem = f"{seu_pokemon.nome} usou {ataque} e causou {dano} de dano!\n"
        mensagem += f"{pokemon_inimigo.nome} agora tem {pokemon_inimigo.hp_atual} de HP restante."

        self.mostrar_pokemon_batalha(seu_pokemon, pokemon_inimigo)
        self.mostrar_mensagem_batalha("Batalha de Pokémon", mensagem)

    def mostrar_mensagem_batalha(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

if __name__ == "__main__":
    jogo = JogoPokemon()
