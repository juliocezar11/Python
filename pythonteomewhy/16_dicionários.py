# %%
lista = [2, 132, "julio", ["da", "de", "di"], True] 

lista[2]

# %%
# pares de chave/valor -> int e str 

dados_julio = {"nome":"julio",
                "filhos": True,
                "idade": 22,
                "sobrenome":"monteiro",
                "formação":["engenharia eletrica", "engenharia de dados"], 
                "times":[
                {"nome": "real madrid", "local":"espanha", "estadio":"santiago bernabeu"},
                {"nome": "CRB", "local":"Maceió", "estadio":"Trapichão"},
                {"nome": "Flamengo", "local":"Rio de Janeiro", "estadio":"Maracanã"}
             ]
}

print(dados_julio)
print(dados_julio["times"][-1]["local"])
print(dados_julio["times"][-3]["estadio"])

# %%
dados_julio["estado civil"] = "casado"

print(dados_julio)
print(dados_julio.values())
print("Chaves:", dados_julio.keys())

# %%
