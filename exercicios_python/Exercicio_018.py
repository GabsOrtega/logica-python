# import math

from math import radians, sin, cos, tan

angulo = int(input('Digite o angulo do triângulo: '))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O valor do seno é de {:.2f} \n O valor do cosseno é de {:.2f} \n E o valor da tangente é de {:.2f}'.format(seno,
                                                                                                                  cos,
                                                                                                                  tan))
