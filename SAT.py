from random    import sample, choice, shuffle, randint
from itertools import product
from numpy     import arange
from time      import time


class SAT():
    def __init__(self):
        ''' Initialize an empty 3SAT instance: phi '''
        self.variables = []     # Names of the variables :1,2,... -> x1,x2,...
        self.clauses   = []     # Clauses, e.g. [1,2,-3]  -> x1 and x2 and not x3
        self.nv        = 30      # Number of variabes = len(self.variables)
        self.nc        = 10      # Number of clauses  = len(self.clauses)
        self.configuration = [] # Current value assignment of the variabes

    def __repr__(self):
        ''' To print out the SAT instance in readable form '''
        r = "SAT instance with "+str(self.nv)+" variables and "+str(self.nc)+" clauses: \n"
        for c in self.clauses:
            r+= str(c) + "\n"
        return r

    def set_variable(self, variable, value):
        ''' Set the given 'variable' to the giben  'value' '''
        self.configuration[ abs(variable)-1 ] = value

    def flip_variable(self,variable):
        '''
        Flip the value of 'variable'
        '''
        self.configuration[ abs(variable)-1 ] = not self.configuration[ abs(variable)-1 ]

    def get_variable(self,variable):
        ''' Return the value assigned to 'variable' '''
        return self.configuration[ abs(variable)-1 ]

    #    Evaluations
    #    ===========
    
    def clause_value(self, clause):
        ''' Return the value of 'clause' '''
        x1 = self.get_variable( clause[0] )
        x2 = self.get_variable( clause[1] )
        x3 = self.get_variable( clause[2] )
        # if negative then negate boolean value of the variable
        if clause[0]<0: x1 = not x1
        if clause[1]<0: x2 = not x2
        if clause[2]<0: x3 = not x3
        return (x1 or x2 or x3)

    def value(self):
        ''' evaluate phi - stop as soon as a clause is False '''
        for c in self.clauses:
            if self.clause_value( c ) == False: # if any clause is False then phi is not satisfied
                return False
        return True                             # if no clause is False then phi is satisfied

    def value_full(self):
        ''' evaluate phi - do not stop until we evalaute all clauses '''
        val = True
        for c in self.clauses:
            val &= self.clause_value( c )
        return val

    def ratio_unsatisfied(self):
        ''' calculate ratio of satisfied clauses '''
        count = 0
        for c in self.clauses:
            if self.clause_value( c ) == False:
                count += 1
        return count/self.nc

    #    Methods for random constructions
    #    ================================

    def random_clause(self):
        ''' helper function to generate a clause randomly '''
        c = sample(self.variables,3)
        c[0] *= choice([-1,1])
        c[1] *= choice([-1,1])
        c[2] *= choice([-1,1])
        return c

    def random_instance(self, nv, nc):
        ''' build a random 3SAT instance with nv variables and nc clauses '''
        self.nv = nv
        self.variables = list(range(1,nv+1))
        self.configuration = [False]*nv
        self.nc = nc
        # generate nc clauses: (... or ... or ...)
        self.clauses = []
        for c in range(nc):
            self.clauses.append( self.random_clause() )

    def random_configuration(self):
        '''
        Build a random configuration (= assignment of the variables)
        Return value of objective function.
        '''
        self.configuration = [choice([True,False]) for nv in range(self.nv)]

    def random_yes_instance(self, nv, nc):
        ''' build a random 'yes' 3SAT instance with nv variables and nc clauses '''
        # choose a random configuration to be satisfied
        self.nv = nv
        self.variables = list(range(1,nv+1))
        self.random_configuration()
        # choose satisfying clauses
        self.nc = nc
        self.clauses = []
        for nc in range(self.nc):
            c = self.random_clause() #sample(self.variables,3)
            while self.clause_value(c) == False: # alter c until it becomes satisfying
                c[ choice([0,1,2]) ] *= -1  # by flipping terminals (negating)
            self.clauses.append(c)
        if self.value() != True:
            print("something has gone wrong!")

    #    Solution methods
    #    ================
        
    def greedy(self):
        '''
        Solve in the 3SAT problem instance using a simple greedy search.
        Find the variable that appears most often and assign it accordingly to maximize ...
        '''
        literals_occurance = [[i,0] for i in range(-self.nv,self.nv+1)]
        for c in self.clauses:
            for v in c:
                literals_occurance[ v+self.nv ][1] += 1
        literals_occurance.sort( key=lambda a:a[1] )
        for v in literals_occurance:
            self.set_variable( v[0] , v[0]>0 )
        return self.ratio_unsatisfied()

    def greedy_randomized(self, block_size=2):
        '''
        Solve in the 3SAT problem instance using a randomized greedy search.
        Find the variable that appears most often and assign it accordingly to maximize ...
        Same as greedy() but randomizes the order of 'literals_occurance' a bit
        '''
        literals_occurance = [[i,0] for i in range(-self.nv,self.nv+1)]
        for c in self.clauses:
            for v in c:
                literals_occurance[ v+self.nv ][1] += 1
        literals_occurance.sort( key=lambda a:a[1] )
        for i in range(0,len(literals_occurance), block_size): # randomize list block by block
            tmp = literals_occurance[i:i+block_size]
            shuffle( tmp )
            literals_occurance[i:i+block_size] = tmp
        for v in literals_occurance:
            self.set_variable( v[0] , v[0]>0 )
        return self.ratio_unsatisfied()

    def GRASP(self, max_repetition=100):
        ''' Solve the 3SAT problem instance using the GRASP meta-heuristic '''
        best = 1 # i.e. start with the worst solution that satisfies no clauses
        for i in range(max_repetition):
            candidate = self.greedy_randomized( choice([2,3,4]) ) # random block_size from {2,3,4}
            # local search: flip variable assignment and see if things improve
            # Choose the best one from the flipped attempts
            best_v = 0
            for v in self.variables:
                self.flip_variable(v)          # try changing variable v
                neighbour = self.ratio_unsatisfied()
                if neighbour < candidate:
                    candidate = neighbour
                    best_v = v
                self.flip_variable(v) # undo, to try flipping next variable
            if candidate < best:
                best = candidate
        return best

#
#-----  TESTING  -----
#

instance = SAT() # global variable... [TODO?]

def report_print( file, line ):
    print( line )
    file.write( line + '\n' )

def test_Approximation():
    with open("data_approx.csv","w") as f:
        # test greedy search
        report_print( f, "rho\tGreedy\tGRASP" )
        max_repeats = 50
        nv = 20
        for rho in arange(1,50,1):  # rho = nc/nv
            nc = int(rho*nv)
            q = [0]*3        # to measure 'quality'
            for repeat in range(max_repeats):
                instance.random_yes_instance(nv, nc)
                q[0] += instance.greedy()
                q[1] += instance.GRASP()
            for i in range(3): q[i] = '{:1.4f}'.format(1-q[i]/max_repeats)
            report_print( f, str(rho)+'\t'+"\t".join(q) )

test_Approximation()
