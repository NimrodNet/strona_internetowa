class W_grze:

    def uruchom(self, instancja):
        pygame = instancja
        uruchomiono = True
        while uruchomiono:
            for zdarzenie in pygame.event.get():
                graczNaciskaCzerwonyX = zdarzenie.type == pygame.QUIT
                if graczNaciskaCzerwonyX:
                    uruchomiono = False
            pygame.display.flip()
