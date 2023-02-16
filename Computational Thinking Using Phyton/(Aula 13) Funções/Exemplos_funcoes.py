#!/usr/bin/env python
# coding: utf-8

# In[1]:


def mostra_texto():
    print("Minha primeira função")


# In[2]:


mostra_texto()


# In[3]:


def mostra_texto_person(texto):
    print(texto)


# In[4]:


palavra = "Fiap"
mostra_texto_person(palavra)


# In[5]:


mostra_texto_person("Fiap")


# In[6]:


def checa_numero(num):
    if (num % 2 ==0):
        print("Par")
    else:
        print("Ímpar")


# In[8]:


numero = int(input("Digite um número"))
checa_numero (numero)


# In[9]:


def carrega_lista (lista):
    for i in range (0,5):
        lista.append(int(input("Elemento: ")))


# In[10]:


listaA = []
carrega_lista(listaA)


# In[11]:


listaA




# In[17]:


def calculo (a,b):
    soma = a + b
    mult = (a * b) + a
    return (soma,mult)


# In[18]:


x = int(input("Digite x: "))
y = int(input("Digite y: "))

soma, mult = calculo (x,y)

print(soma, " ", mult)


# In[19]:


soma, mult = calculo (6,9)
print(soma, mult)


# In[20]:


def soma_numeros (a,b):
    soma = a + b
    return(soma)


# In[21]:


x = int(input("Digite x: "))
y = int(input("Digite y: "))

soma = soma_numeros (x,y)

print(soma)
print(soma_numeros (x,y))





