from genetic_algorithm import GeneticAlgorithm


def test_danych():
    # wielkość populacji
    population_size = 10

    # długość bitowa chromosomu
    chromosome_size = 32

    # zaakres przeszukiwania
    scope_range = (-4, 2)

    # wielkość turnieju
    tournament_size = 3

    # rodzaje mutacji
    single = "single_bit_mutation"
    swap = "swap_bit_mutation"
    reverse = 'reverse_mutation'
    selected_mutation = [reverse, single, swap]

    # ilość generacji
    generations = 50
    result = []
    for i in range(1000):
        genetic = GeneticAlgorithm(population_size=population_size,
                                   chromosome_size=chromosome_size,
                                   scope_range=scope_range,
                                   tournament_size=tournament_size,
                                   mutation=selected_mutation,
                                   if_generate_chart=False)
        value = genetic.evolve(generations)
        result.append(value)
    print(sum(result)/len(result))


def generate_chart():
    # wielkość populacji
    population_size = 10

    # długość bitowa chromosomu
    chromosome_size = 32

    # zaakres przeszukiwania
    scope_range = (-4, 2)

    # wielkość turnieju
    tournament_size = 3

    # rodzaje mutacji
    single = "single_bit_mutation"
    swap = "swap_bit_mutation"
    reverse = 'reverse_mutation'
    selected_mutation = [swap, reverse]

    # ilość generacji
    generations = 50

    genetic = GeneticAlgorithm(population_size=population_size,
                               chromosome_size=chromosome_size,
                               scope_range=scope_range,
                               tournament_size=tournament_size,
                               mutation=selected_mutation,
                               if_generate_chart=True)
    genetic.evolve(generations)


def main():

    # wyświetlanie działania wraz z tworzeniem gifu
    generate_chart()

    # testowanie danych i uzyskiwanie średniej wyników
    # test_danych()


if __name__ == '__main__':
    main()
