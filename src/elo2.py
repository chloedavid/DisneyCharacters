K = 10

class Elo(object):

    def match(self, p1, p2):
        algo_func=self.__match_algo_strict
        return algo_func(p1, p2)

    @staticmethod
    def __match_algo_strict(winner, looser):
        #elo algorithm - simple modifications
        r1 = max(min(looser['score'] - winner['score'], 400), -400)
        r2 = max(min(winner['score'] - looser['score'], 400), -400)
        e1 = 1.0 / (1+10**(r1 / 400))
        e2 = 1.0 / (1+10**(r2 / 400))

        s1 = 1
        s2 = 0

        winner['score'] = winner['score'] + K*(s1-e1)
        looser['score'] = looser['score'] + K*(s2-e2)
        # formatting
        winner['score'] = format(winner['score'], '.2f')
        looser['score'] = format(looser['score'], '.2f')

        #increase wincounter        
        winner['wins'] +=1

        #increase matchcounter
        winner['matches'] +=1
        looser['matches'] +=1

        return winner, looser
