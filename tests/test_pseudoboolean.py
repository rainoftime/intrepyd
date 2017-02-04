import intrepyd as ip
from intrepyd.engine import EngineResult
import intrepyd.pseudoboolean
import unittest

class TestPseudoBoolean(unittest.TestCase):

    def setUp(self):
        self.ctx = ip.Context()

    def create_and_run_nets(self, n):
        nets = []
        bt = self.ctx.mk_boolean_type()
        for i in range(n):
            nets.append(self.ctx.mk_input("n" + str(i), bt))
        eo = ip.pseudoboolean.mk_exactly_one(self.ctx.ctx, nets, "eo")
        bmc = self.ctx.mk_bmc()
        bmc.add_target(eo)
        result = bmc.reach_targets()
        self.assertEqual(EngineResult.REACHABLE, result)
        reachedNets = bmc.get_last_reached_targets()
        self.assertEqual(1, len(list(reachedNets)))

    def test_exactly_one_01(self):
        self.create_and_run_nets(1)

    def test_exactly_one_02(self):
        self.create_and_run_nets(2)

    def test_exactly_one_03(self):
        self.create_and_run_nets(3)

    def test_exactly_one_04(self):
        self.create_and_run_nets(4)

    def test_exactly_one_05(self):
        self.create_and_run_nets(10)

    def test_exactly_one_06(self):
        self.create_and_run_nets(11)

    def test_exactly_one_07(self):
        self.create_and_run_nets(12)

    def test_exactly_one_08(self):
        self.create_and_run_nets(43)

    def test_exactly_one_09(self):
        nets = []
        bt = self.ctx.mk_boolean_type()
        i1 = self.ctx.mk_input("i1", bt)
        i2 = self.ctx.mk_input("i2", bt)
        i3 = self.ctx.mk_input("i3", bt)
        nets.append(self.ctx.mk_or(i1, i2))
        nets.append(self.ctx.mk_or(i1, i3))
        nets.append(self.ctx.mk_or(i2, i3))
        eo = ip.pseudoboolean.mk_exactly_one(self.ctx.ctx, nets, "eo")
        bmc = self.ctx.mk_bmc()
        bmc.add_target(eo)
        result = bmc.reach_targets()
        self.assertEqual(EngineResult.UNREACHABLE, result)