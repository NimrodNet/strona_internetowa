class W_grze:

    def uruchom(self, instancja, okno):
        pygame = instancja
        uruchomiono = True
        while uruchomiono:
            for zdarzenie in pygame.event.get():
                graczNaciskaCzerwonyX = zdarzenie.type == pygame.QUIT
                if graczNaciskaCzerwonyX:
                    uruchomiono = False
            okno.ustaw_tlo((255, 255, 255))
            pygame.display.flip()
