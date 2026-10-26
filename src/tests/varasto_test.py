import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_konstruktori_oikein_negatiivisen_tilan_varaston(self):
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_konstruktori_oikein_negatiivisen_alku_saldon(self):
        self.varasto = Varasto(10, -1)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_oikein_suuremman_alku_saldon_kuin_varasto(self):
        self.varasto = Varasto(10, 11)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivinen_lisays_ei_lisaa_mitaan(self):
        self.varasto.lisaa_varastoon(-2)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_lisaa_vain_varastoon_mahtuva_maara(self)     :
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivinen_ottaminen_palauttaa_oikean_maaran(self):
        saatu_maara = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_liika_ottaminen_palauttaa_vain_varastossa_olevan_maaran(self):
        self.varasto.saldo = 1
        saatu_maara = self.varasto.ota_varastosta(8)
        self.assertAlmostEqual(saatu_maara, 1)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

def test_zero_equals_one():
    assert 1 == 0