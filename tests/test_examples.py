# -*- coding: utf-8 -*-
import sys
import os.path
import unittest
import contextlib


class TestExamples(unittest.TestCase):
    '''
    Test examples' models.  This creates a model object and iterates it through
    some steps.  The idea is to get code coverage, rather than to test the
    details of each example's model.
    '''

    @contextlib.contextmanager
    def active_example_dir(self, example):
        'save and restore sys.path and sys.modules'
        old_sys_path = sys.path[:]
        old_sys_modules = sys.modules.copy()
        old_cwd = os.getcwd()
        example_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../examples', example))
        try:
            sys.path.insert(0, example_path)
            os.chdir(example_path)
            yield
        finally:
            os.chdir(old_cwd)
            added = [m for m in sys.modules.keys() if m not in old_sys_modules]
            for mod in added:
                del sys.modules[mod]
            sys.modules.update(old_sys_modules)
            sys.path[:] = old_sys_path

    def test_schelling(self):
        with self.active_example_dir('Schelling'):
            from model import SchellingModel
            model = SchellingModel(height=20, width=20, density=0.8,
                minority_pc=0.2, homophily=3)
            (model.step() for _ in range(100))

    def test_bank_reserves(self):
        with self.active_example_dir('bank_reserves'):
            from bank_reserves.model import BankReservesModel
            model = BankReservesModel()
            (model.step() for _ in range(100))

    def test_boid_flockers(self):
        with self.active_example_dir('boid-flockers'):
            from boidflockers.model import BoidModel
            model = BoidModel()
            (model.step() for _ in range(100))

    def test_boltzmann_wealth_model(self):
        with self.active_example_dir('boltzmann_wealth_model'):
            from wealth_model.model import MoneyModel
            model = MoneyModel(100, 20, 20)
            (model.step() for _ in range(100))

    def test_boltzmann_wealth_model_network(self):
        with self.active_example_dir('boltzmann_wealth_model_network'):
            from wealth_model.model import MoneyModel
            model = MoneyModel(100, 100)
            (model.step() for _ in range(100))

    def test_color_patches(self):
        with self.active_example_dir('color_patches'):
            from color_patches.model import ColorPatchModel
            model = ColorPatchModel(100, 100)
            (model.step() for _ in range(100))

    def test_conways_game_of_life(self):
        with self.active_example_dir('conways_game_of_life'):
            from game_of_life.model import GameOfLife
            model = GameOfLife(100, 100)
            (model.step() for _ in range(100))

    def test_epstein_civil_violence(self):
        with self.active_example_dir('epstein_civil_violence'):
            from civil_violence.model import CivilViolenceModel
            model = CivilViolenceModel(
                height=40,
                width=40,
                citizen_density=.7,
                cop_density=.074,
                citizen_vision=7,
                cop_vision=7,
                legitimacy=.8,
                max_jail_term=1000)
            (model.step() for _ in range(100))

    def test_forest_fire(self):
        with self.active_example_dir('forest_fire'):
            from forest_fire.model import ForestFire
            model = ForestFire(100, 100, 0.65)
            (model.step() for _ in range(100))

    def test_hex_snowflake(self):
        with self.active_example_dir('hex_snowflake'):
            from hex_snowflake.model import HexSnowflake
            model = HexSnowflake(100, 100)
            (model.step() for _ in range(100))

    def test_pd_grid(self):
        with self.active_example_dir('pd_grid'):
            from pd_grid.model import PDModel
            model = PDModel(100, 100, "Random")
            (model.step() for _ in range(100))

    def test_shape_example(self):
        with self.active_example_dir('shape_example'):
            from shape_model.model import ShapesModel
            model = ShapesModel(100, 100, 100)
            (model.step() for _ in range(100))

    def test_sugarscape_cg(self):
        with self.active_example_dir('sugarscape_cg'):
            from sugarscape.model import Sugarscape2ConstantGrowback
            model = Sugarscape2ConstantGrowback()
            (model.step() for _ in range(100))

    def test_virus_on_network(self):
        with self.active_example_dir('virus_on_network'):
            from virus_on_network.model import VirusModel
            model = VirusModel(
                num_nodes=10,
                avg_node_degree=3,
                initial_outbreak_size=1,
                virus_spread_chance=0.4,
                virus_check_frequency=0.4,
                recovery_chance=0.3,
                gain_resistance_chance=0.5)
            (model.step() for _ in range(100))

    def test_wolf_sheep(self):
        with self.active_example_dir('wolf_sheep'):
            from wolf_sheep.model import WolfSheepPredation
            model = WolfSheepPredation()
            (model.step() for _ in range(100))
