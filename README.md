# Wprowadzenie
  Gra Spaceship Simulator polega na poprowadzeniu przez gracza statku kosmicznego przez pole asteroid oraz jak najdłuższemu unikaniu zderzenia z nimi.

# Uruchomienie gry
## Wymagania
  Gra do poprawnego działania wymaga interpretera Python w wersji 3 (rekomendowany Python 3.11) wraz w zainstalowaną biblioteką pyGame.
  Jeżeli uruchamiasz grę przez venv (preferowane), wykonaj: `pip install pygame` lub, jeżeli gra uruchamiana bezpośrednio w systemie: 
  `<Twój manager pakietów> python-pygame` lub podobne, w zależności od dystrybucji Linuxa.

## Uruchomienie
  Aby uruchomić grę wystarczy uruchomić interpreter Pythona ze wskazanym plikiem skryptu w parametrze: `python3 spaceship_sim.py`

## Sterowanie
  Gracz może sterować statkiem za pomocą klawiatury. Strzałki lewa i prawa powodują obrót, odpowiednio przeciwnie i zgodnie z ruchem
wskazówek zegara. Strzałki góra i dół powodują przyspieszenie lub zwolnienie statku.

# Cel i zasady gry
## Cel gry
  Celem gracza jest zebranie jak największej ilości punktów. 

## Zasady gry
  Punkty naliczane są zgodnie z upływającym czasem przemnożone przez prędkość statku.
Zatem, jeżeli statek gracza nie będzie się poruszał, wynik nie będzie się zwiększał.
  W trakcie gry gracz powinien unikać zderzenia z asteroidami, które poruszają się z losowymi prędkościami i w losowych kierunkach.
Dodatkowo, co każde 15 sekund w grze pojawia się kolejna asteroida. 
Asteroidy poruszają się, jeżeli statek gracza ma niezerową prędkość. W przeciwnym razie również się zatrzymują.

## Zakończenie gry
  Gra kończy się w momencie kolizji statku gracza z asteroidą.

# Wykonanie i autorzy
  Aplikacja została wygenerowana przez ChatGPT i jest pracą konkursową z przedmiotu: "Uczenie maszynowe w Pythonie", 
Uniwersytet WSB Merito w Chorzowie, w semetrze letnim roku akadeckiego 2022/23.
  Zespół projektowy: Grażyna Górka, Tomasz Juszkiewicz

