from abstractFactory import *
from builder import *

print("\nPADRÃO ABSTRACT FACTORY\n\nVamos testar a fabrica concreta de bolo de casamento: \n")
requisicao(FabricaBoloCasamento())
print("\n\nVamos testar a fabrica concreta de bolo de aniversario: \n")
requisicao(FabricaBoloAniversario())
print("\n\nVamos testar a fabrica concreta de bolo de festa informal: \n")
requisicao(FabricaBoloFestaInformal())

print("\n\n\nPADRAO BUILDER\n")

director = Director()

builder = BoloCenouraCasamentoBuilder()
director.builder = builder
print("\nConstruindo Bolo de Cenoura para Casamento: ")
director.fazer_bolo()
builder.product.descricao_bolo()

builder = BoloMandiocaCasamentoBuilder()
director.builder = builder
print("\nConstruindo Bolo de Mandioca para Casamento: ")
director.fazer_bolo()
builder.product.descricao_bolo()

builder = BoloChocolateCasamentoBuilder()
director.builder = builder
print("\nConstruindo Bolo de Chocolate para Casamento: ")
director.fazer_bolo()
builder.product.descricao_bolo()

builder = BoloCenouraAniversarioBuilder()
director.builder = builder
print("\nConstruindo Bolo de Cenoura para Aniversario: ")
director.fazer_bolo()
builder.product.descricao_bolo()

builder = BoloMandiocaAniversarioBuilder()
director.builder = builder
print("\nConstruindo Bolo de Mandioca para Aniversario: ")
director.fazer_bolo()
builder.product.descricao_bolo()

builder = BoloChocolateAniversarioBuilder()
director.builder = builder
print("\nConstruindo Bolo de Chocolate para Aniversario: ")
director.fazer_bolo()
builder.product.descricao_bolo()

builder = BoloCenouraFestaInformalBuilder()
director.builder = builder
print("\nConstruindo Bolo de Cenoura para Festa Informal: ")
director.fazer_bolo()
builder.product.descricao_bolo()

builder = BoloMandiocaFestaInformalBuilder()
director.builder = builder
print("\nConstruindo Bolo de Mandioca para Festa Informal: ")
director.fazer_bolo()
builder.product.descricao_bolo()

builder = BoloChocolateFestaInformalBuilder()
director.builder = builder
print("\nConstruindo Bolo de Chocolate para Festa Informal: ")
director.fazer_bolo()
builder.product.descricao_bolo()