#--coding: utf-8 --

import telebot #importa a biblioteca do pyTelegramBotAPI
from telebot import types #Seleciona a lib types
import json #importa biblioteca json
import urllib #importa biblioteca urllib

API_TOKEN = '' #Chave da api do telegram

bot = telebot.TeleBot(API_TOKEN) #telebot-sumário e TeleBot(comando) aplica o token

#inicio

@bot.message_handler(commands=['start'])
def send_welcome(message):
	msg = bot.reply_to(message, "Sou um bot de busca de CEP digite /cep para continuar!") #responde do comando CEP
	cid = message.chat.id #pega o ID da conversa

@bot.message_handler(commands=['cep'])
def send_cep(message):
	msg = bot.reply_to(message, "Digite o CEP que deseja consultar (Apenas números):) ") #responde do comando CEP
	cid = message.chat.id #pega o ID da conversa
	bot.register_next_step_handler(msg, send_cep_step) #Armazena a informação digita e joga para o proximo passo

def send_cep_step(message):
	cid = message.chat.id #pega o ID da conversa
	message_cep = message.text #Mensagem digitada
	url = "https://viacep.com.br/ws/" + message_cep + "/json/" #url da api JSON
	response = urllib.urlopen(url) #abre a variavel URL contendo o JSON
	
	data = json.loads(response.read()) #carrega e lê os valores do json
	
	cep = data['cep']
	logradouro = data['logradouro']
	bairro = data['bairro']
	localidade = data['localidade']
	uf = data['uf']
	bot.send_message(cid, "CEP: " + cep + "\nLogradouro: " + logradouro + "\nBairro: " + bairro + "\nLocalidade: " + localidade + "\nUF: " + uf)





bot.polling() #Coloca o bot em escuta