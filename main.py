# Import the required libraries
import time
from tests.test_BJ_ElGringo.test_BJ_ElGringo import test_BJ_ElGringo
from tests.test_StK.test_StK import test_StK
from tests.test_bang_mancato_barilo_vulcanic_CJ_WtK.main import test_bang_mancato_barilo_vulcanic_CJ_WtK
from tests.test_bart_cassidy.test_bart_cassidy import test_bart_cassidy
from tests.test_distances.test_distances import test_distances
from tests.test_emporio_KC_LD.test_emporio_KC_LD import test_emporio_KC_LD
from tests.test_indiani_gatling_duel.test_indiani_gatling_duel_jourdonnais import test_indiani_gatling_duel_jourdonnais
from tests.test_panico_cat_ballou.test_panico_cat_ballou import test_panico_cat_ballou
from globals import *
from tests.test_prigione_dynamite.test_prigione_dynamite import test_prigione_dynamite

# Navigate to the webpage
driver.get(ROUTE)

# test_bang_mancato_barilo_vulcanic_CJ_WtK()

# test_bang_mancato_barilo_vulcanic_CJ_WtK()
# test_indiani_gatling_duel_jourdonnais()
# test_panico_cat_ballou()
# test_prigione_dynamite()
# test_emporio_KC_LD()
# test_StK()
# test_bart_cassidy()
# test_BJ_ElGringo()
test_distances()
input()

# Close the web window
driver.quit()
