from django.db import models

class category(models.Model):
    nome_category = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_category

class obra(models.Model):
    insc_obra = models.CharField(max_length=20)
    nome_obra = models.CharField(max_length=300)
    category_obra = models.ForeignKey('category', on_delete=models.CASCADE, related_name='category_obra')
    foto_obra = models.ImageField(upload_to='obra_fotos')

    def __str__(self):
        return self.nome_obra

class pessoa(models.Model):
    email_pessoa = models.EmailField(max_length=150, unique=True)
    pessoa_votou = models.IntegerField(default=0)


    def __str__(self):
        return self.email_pessoa

class pessoaVoto(models.Model):
    pessoa = models.ForeignKey('pessoa', on_delete=models.CASCADE, related_name='pessoa')
    obra1 = models.ForeignKey('obra', on_delete=models.CASCADE, related_name='obra1')
    obra2 = models.ForeignKey('obra', on_delete=models.CASCADE, related_name='obra2')
    obra3 = models.ForeignKey('obra', on_delete=models.CASCADE, related_name='obra3')
    obra4 = models.ForeignKey('obra', on_delete=models.CASCADE, related_name='obra4')
    obra5 = models.ForeignKey('obra', on_delete=models.CASCADE, related_name='obra5')
    obra6 = models.ForeignKey('obra', on_delete=models.CASCADE, related_name='obra6')
    obra7 = models.ForeignKey('obra', on_delete=models.CASCADE, related_name='obra7')
    obra8 = models.ForeignKey('obra', on_delete=models.CASCADE, related_name='obra8')
    hora_voto = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.pessoa.email_pessoa

class voto(models.Model):
    obraVotada = models.ForeignKey('obra', on_delete=models.CASCADE)
    category_obra = models.ForeignKey('category', on_delete=models.CASCADE)
    quantidadeVotos = models.IntegerField(default=0)

    def __str__(self):
        return self.obraVotada.nome_obra
