name = input("Digite seu nome: ")
idade = int(input("Insira sua idade: "))    
febre = input("Você tem febre?(Sim ou Não): ").lower()
def sint_febre(febre):
     if febre == "sim":
          tempe = float(input("Qual a sua temperatura?: "))
          if tempe < 37.5:
               class_febre = "Normal"
          elif tempe >= 37.5 and tempe <= 38.9:
               class_febre = "Febre Moderada(observação)"
          else:
               class_febre = "Febre Alta(Atenção Urgente)"
     else:
          class_febre = "Sem Febre"
     return class_febre
class_febre = sint_febre(febre)
dor_cabeca = input("Você tem dor de cabeça?(Sim ou Não): ").lower()
def sint_cabeca(dor_cabeca):
     if dor_cabeca == "sim":
          grau = int(input("Qual sua dor numa escala de 0-10 ?: "))
          if grau >= 0 and  grau <= 4:
               class_cabeca = "Leve(autocuidado)"
          elif grau >=5 and  grau <=7:
               class_cabeca = "Moderada(repouso)"
          else:
               class_cabeca = "Intensa(consulta médica)"
     else:
          class_cabeca = "Sem dor de cabeça"
     return class_cabeca
class_cabeca = sint_cabeca(dor_cabeca)
tosse = input("Você tem tosse?(Sim ou Não): ").lower()
def sint_tosse(tosse):
     if tosse == "sim":
          tipo = input("Qual o seu tipo de tosse?(Seca ou Com Catarro): ").lower()
          if tipo == "seca":
               class_tosse = "Hidratação"
          else:
               class_tosse = "Possível Infecção"
     else:
          class_tosse = "Sem tosse"
     return class_tosse
class_tosse = sint_tosse(tosse)
def recomend(class_febre):
     if class_febre =="Normal":
          recomendation_febre = "Descansar,Evitar roupas e cobertores em excesso,Utilizar medicamentos antipiréticos"
     elif class_febre == "Febre Moderada(observação)":
          recomendation_febre = "Beber muitos líquidos,Tomar banhos mornos e Utilizar medicamentos antipiréticos"
     elif class_febre == "Febre Alta(Atenção Urgente)":
          recomendation_febre = "Beba muita água,Descanse em grande quantidade,Utilize medicamentos antipiréticos e caso os sintomas persistirem por mais de 3 dias,consulte um médico"
     else:
          recomendation_febre = "Nenhuma,você está saudável"
     return recomendation_febre
recomendation_febre = recomend(class_febre)
def recomendor(class_cabeca):
     if class_cabeca == "Leve(autocuidado)":
          recomendation_cabeca = "Tomar um analgésico de venda livre, como paracetamol ou ibuprofeno, e Aplicar uma compressa fria nas têmporas ou testa"
     elif class_cabeca == "Moderada(repouso)":
          recomendation_cabeca = "Usar analgésicos de venda livre, como paracetamol ou ibuprofeno,Aplicar compressas frias na testa,Descansar em um ambiente escuro e silencioso,Fazer massagens na região da dor"
     elif class_cabeca == "Intensa(consulta médica)":
          recomendation_cabeca = "Usar analgésicos de venda livre, como paracetamol ou ibuprofeno,Aplicar compressas frias na testa,Descansar em um ambiente escuro e silencioso,Fazer massagens na região da dor.Caso não resolver consultar um médico"
     else:
          recomendation_cabeca = "Nenhuma,você está saudável"
     return recomendation_cabeca
recomendation_cabeca = recomendor(class_cabeca)
def recomentos(class_tosse):
     if class_tosse == "Hidratação":
          recomendation_tosse = "Beba muita água e poupe sua voz"
     elif class_tosse == "Possível Infecção":
          recomendation_tosse = "Beba muita água,Faça inalações com soro fisiológico ou água quente e Use um umidificador de ar"
     else:
          recomendation_tosse = "Nenhuma,você está saudável"
     return recomendation_tosse
recomendation_tosse = recomentos(class_tosse)
def diagnosis(febre,dor_cabeca,tosse):
     if febre == "sim":
          diagnosis_ind = "Infecção Viral"
     elif tosse == "sim":
          diagnosis_ind = "Infeccção Respiratória ou Clima seco"
     elif dor_cabeca == "sim":
          diagnosis_ind = "Cansaço ou Estresse Mental"
     else:
          diagnosis_ind = "Você está saudável"
     return diagnosis_ind
diagnosis_ind = diagnosis(febre,dor_cabeca,tosse)
def diagnosis_per(class_febre,class_cabeca,class_tosse):
     if class_febre == "Normal" and class_cabeca == "Leve(autocuidado)":
          diagnosis_cm = "Resfriado Comum"
     elif class_febre == "Febre Moderada(observação)" and class_cabeca == "Moderada(repouso)":
          diagnosis_cm = "Sinusite Aguda"
     elif class_febre == "Febre Alta(Atenção Urgente)" and class_cabeca == "Intensa(consulta médica)" :
          diagnosis_cm = "Amigdalite bacteriana ou Dengue ou Pneumonia"
     elif class_febre == "Normal" and class_tosse == "Hidratação":
          diagnosis_cm = "Resfriado Comum ou Covid-19 leve"
     elif class_febre == "Febre Moderada(observação)" and class_tosse == "Hidratação":
          diagnosis_cm = "Gripe ou Bronquite viral"
     elif class_febre == "Febre Alta(Atenção Urgente)" and class_tosse =="Hidratação":
          diagnosis_cm = "Pneumonia viral ou Coqueluche"
     elif class_febre == "Normal" and class_tosse == "Possível Infecção":
          diagnosis_cm = "Infecção viral das vias aéreas ou Bronquite Aguda"
     elif class_febre == "Febre Moderada(observação)" and class_tosse == "Possível Infecção":
          diagnosis_cm = "Pneumonia bacteriana ou Sinusite aguda"
     elif class_febre == "Febre Alta(Atenção Urgente)" and class_tosse == "Possível Infecção":
          diagnosis_cm = "Bronquite Aguda ou Tuberculose"
     elif class_tosse == "Hidratação" and class_cabeca == "Leve(autocuidado)":
          diagnosis_cm = "Resfriado comum"
     elif class_tosse == "Hidratação" and class_cabeca == "Moderada(repouso)":
          diagnosis_cm = "Sinusite Viral"
     elif class_tosse =="Hidratação" and class_cabeca == "Intensa(consulta médica)":
          diagnosis_cm = "Sinusite Aguda ou Enxaqueca"
     elif class_tosse == "Possível Infecção" and class_cabeca == "Leve(autocuidado)":
          diagnosis_cm = "Faringite viral"
     elif class_tosse == "Possível Infecção" and class_cabeca == "Moderada(repouso)":
          diagnosis_cm = "Gripe ou Sinusite Bacteriana"
     elif class_tosse == "Possível Infecção" and class_cabeca == "Intensa(consulta médica)":
          diagnosis_cm = "Influenza complicada ou Sinusite Bacteriana Grave"
     elif class_febre == "Normal" and class_cabeca == "Leve(autocuidado)" and class_tosse == "Hidratação":
          diagnosis_cm = "Resfriado comum, rinite alérgica"
     elif class_febre == "Febre Moderada(observação)" and  class_cabeca == "Leve(autocuidado)" and class_tosse == "Hidratação":
          diagnosis_cm = "Gripe Leve, Faringite viral"
     elif class_febre == "Febre Moderada(observação)" and class_cabeca == "Moderada(repouso)" and class_tosse == "Hidratação":
          diagnosis_cm = "Sinusite bacteriana leve, Influenza"
     elif class_febre == "Febre Moderada(observação)" and class_cabeca == "Moderada(repouso)" and class_tosse == "Possível Infecção":
          diagnosis_cm = "Influenza ou Bronquite Aguda"
     elif class_febre == "Normal" and class_cabeca == "Moderada(repouso)" and class_tosse == "Hidratação":
          diagnosis_cm = "Sinusite viral inicial ou Cefaleia Tensional"
     elif class_febre == "Febre Moderada(observação)" and class_cabeca == "Leve(autocuidado)" and class_tosse == "Possível Infecção":
          diagnosis_cm = "Gripe ou Bronquite Viral"
     elif class_febre == "Febre Alta(Atenção Urgente)" and class_cabeca == "Intensa(consulta médica)" and class_tosse == "Hidratação":
          diagnosis_cm = "Meningite viral/bacteriana"
     elif class_febre == "Febre Alta(Atenção Urgente)" and class_cabeca == "Leve(autocuidado)" and class_tosse == "Possível Infecção":
          diagnosis_cm = "Pneumonia bacteriana, Coqueluche Complicada"
     elif class_febre == "Normal" and class_cabeca == "Intensa(consulta médica)" and class_tosse == "Possível Infecção":
          diagnosis_cm = "Tosse crônica + cefaleia"
     elif class_febre == "Febre Alta(Atenção Urgente)" and class_cabeca == "Intensa(consulta médica)" and class_tosse == "Possível Infecção":
          diagnosis_cm = "Pneumonia grave, Tuberculose avançada ou meningite"
     else:
          diagnosis_cm = "Saudável :)"
     return diagnosis_cm
diagnosis_cm = diagnosis_per(class_febre,class_cabeca,class_tosse)
print(f"{name},{idade}\nFebre:{febre},{class_febre}\nDor de cabeça:{dor_cabeca},{class_cabeca}\nTosse:{tosse},{class_tosse}\nRecomendações dos sintomas individuais:\nFebre:{recomendation_febre}\nDor de cabeça:{recomendation_cabeca}\nTosse:{recomendation_tosse}\nDiagnóstico individual:{diagnosis_ind}\nDiagnóstico combinado:{diagnosis_cm}\nEste algoritmo não suprimi a nescessidade de consultar um médico,caso tenha estes sintomas por favor vá a unidade de saúde mais próxima e se previna")
def trata(febre,dor_cabeca,tosse):
     if febre == "sim":
          print("Febre: Você precisa de um antipirético")
     if dor_cabeca == "sim": 
          print("Dor de cabeça: Você precisa de um analgésico")
     if tosse == "sim":
          print("Tosse: Você precisa de um xarope para tosse")
     else:
          print("Nenhuma recomendação ou somente as citadas")
     return
tratamento = trata(febre,dor_cabeca,tosse)

          
               



          
     









     

          
    
     
     





    
