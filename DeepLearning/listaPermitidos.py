class flabianos:
    """ Lista de invitados a la cena del señor en el laboratorio """

    def __init__(self):
        self.permitidos=['Bryan_Sierra','Dylan_Sierra',
               'Lupita Tejeda','Ian Ibarria']

    def TuSiTuNo(self,EllosSi):        
        if EllosSi in self.permitidos:
            print('Bienvenido {}'.format(EllosSi))
        else:
            print('Lo siento {}, aun no trais el omnitrix'.format(EllosSi))
