import gmpy2
import time
def CRT(items):
    N = reduce(lambda x, y: x * y, (i[1] for i in items))
    result = 0
    for a, n in items:
        m = N / n
        d, r, s = gmpy2.gcdext(n, m)
        if d != 1: raise Exception("Input not pairwise co-prime")
        result += a * s * m
    return result % N, N
e = 3
n = [155266493936043103849855199987896813716831986416707080645036022909153373110367007140301635144950634879983289720164117794783088845393686109145443728632527874768524615377182297125716276153800765906014206797548230661764274997562670900115383324605843933035314110752560290540848152237316752573471110899212429555149, 112306066601652819062206435724795595603085908011001671184332227488970057128128821831260649058569739569103298091727188365019228385820143813415009397359257831092635374404034997011441653286642458431865026213129412677064308342580757248577955071384972714557250468686599901682728173096745710849318629959223270431039, 147733349387696521015664992396355145811249793103958464053225389476050097503928022819269482555955365534137156079172704297584033078453033637103720972881068435459202133846880715879894340131656691631756162323422868846616160423755883726450486845175227682329583615739797782025647376042249605775433971714513081755709]
c = [124929943232081828105808318993257526364596580021564021377503915670544445679836588765369503919311404328043203272693851622132258819278328852726005776082575583793735570095307898828254568015886630010269615546857335790791577865565021730890364239443651479580968112031521485174068731577348690810906553798608040451024, 108387832390337770947361518376552702503741092284778824448943971792044922720461955035726863109418657218498659460663504872870862538725835055240750735576735249122665348803252691221869146679004017916359067454693701495389784159620341860394035373599823801288442604273046729873467936004227013186659110262247417571857, 52253817590056116368273294519761274350847193477090280916373828903718796358618956145225746496960677477661151583828604021049936963779103440560630451125137344639503705880024677345063113240530798352727432768980751992926293801206779839157443722614687126711272753610923903360818026083573711899014859313677159790039]
print '[+]Detecting m...'
data = zip(c, n)
x, n = CRT(data)
realnum = gmpy2.iroot(gmpy2.mpz(x), e)[0].digits()
print '  [-]m is: ' + '{:x}'.format(int(realnum)).decode('hex')
print '[!]All Done!'