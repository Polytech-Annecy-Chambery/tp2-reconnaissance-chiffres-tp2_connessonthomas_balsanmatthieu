from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    
    similitude_comparaison = 0
    indice = 0
    
    image_binarisee = image.binarisation(S)
    image_localisee = image_binarisee.localisation()
    
    
    for i in range(len(liste_modeles)):
        
        image_resizee = image_localisee.resize(liste_modeles[i].H, liste_modeles[i].W)
        image_similitude = image_resizee.similitude(liste_modeles[i])
        
        if similitude_comparaison < image_similitude:
            similitude_comparaison = image_similitude
            indice = i
            
            
    return indice
