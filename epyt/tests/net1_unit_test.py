from epyt import epanet
import numpy as np
import unittest


class TestGetSetLinksCase(unittest.TestCase):
    def setUp(self):
        """Call before every test case."""
        # Create EPANET object using the INP file
        inpname = 'Net1.inp'
        self.epanetClass = epanet(inpname)

    def tearDown(self):
        """Call after every test case."""
        self.epanetClass.unload()

    """ ------------------------------------------------------------------------- """

    # *Get Links Data (EXAMPLES)*

    def testDiameterAll(self):
        assert all(self.epanetClass.getLinkDiameter() == [18.0, 14.0, 10.0, 10.0, 12.0, 6.0,
                                                          18.0, 10.0, 12.0, 8.0, 8.0, 6.0,
                                                          0.0]), "Wrong diameter output"

    def testDiameterIndices(self):
        assert all(self.epanetClass.getLinkDiameter([1, 5, 10]) == [18.0, 12.0, 8.0]), "Wrong diameter output"

    def testDiameterIndex(self):
        assert self.epanetClass.getLinkDiameter(10) == 8.0, "Wrong diameter output"

    """ ------------------------------------------------------------------------- """

    def testLengthAll(self):
        assert all(self.epanetClass.getLinkLength() == [10530.0, 5280.0, 5280.0, 5280.0, 5280.0,
                                                        5280.0, 200.0, 5280.0, 5280.0, 5280.0, 5280.0, 5280.0,
                                                        0.0]), "Wrong length output"

    def testLengthIndices(self):
        assert all(self.epanetClass.getLinkLength([1, 5, 10]) == [10530.0, 5280.0, 5280.0]), "Wrong length output"

    def testLengthIndex(self):
        assert self.epanetClass.getLinkLength(10) == 5280.0, "Wrong length output"

    """ ------------------------------------------------------------------------- """

    def testRoughnessCoeffAll(self):
        assert all(self.epanetClass.getLinkRoughnessCoeff() == [100.0, 100.0, 100.0, 100.0, 100.0, 100.0,
                                                                100.0, 100.0, 100.0, 100.0, 100.0, 100.0,
                                                                0.0]), "Wrong RoughnessCoeff output"

    def testRoughnessCoeffIndices(self):
        assert all(self.epanetClass.getLinkRoughnessCoeff([1, 5, 10]) == [100.0, 100.0,
                                                                          100.0]), "Wrong RoughnessCoeff output"

    def testRoughnessCoeffIndex(self):
        assert self.epanetClass.getLinkRoughnessCoeff(10) == 100.0, "Wrong RoughnessCoeff output"

    """ ------------------------------------------------------------------------- """

    def testMinorLossCoeffAll(self):
        assert all(self.epanetClass.getLinkMinorLossCoeff() == [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                                                0.0, 0.0, 0.0, 0.0, 0.0]), "Wrong MinorLossCoeff output"

    def testMinorLossCoeffIndices(self):
        assert all(self.epanetClass.getLinkMinorLossCoeff([1, 5, 10]) == [0.0, 0.0, 0.0]), "Wrong MinorLossCoeff output"

    def testMinorLossCoeffIndex(self):
        assert self.epanetClass.getLinkMinorLossCoeff(10) == 0.0, "Wrong MinorLossCoeff output"

    """ ------------------------------------------------------------------------- """

    def testInitialStatusAll(self):
        assert all(self.epanetClass.getLinkInitialStatus() == [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                                               1.0, 1.0, 1.0, 1.0, 1.0]), "Wrong InitialStatus output"

    def testInitialStatusIndices(self):
        assert all(self.epanetClass.getLinkInitialStatus([1, 5, 10]) == [1.0, 1.0, 1.0]), "Wrong InitialStatus output"

    def testInitialStatusIndex(self):
        assert self.epanetClass.getLinkInitialStatus(10) == 1.0, "Wrong InitialStatus output"

    """ ------------------------------------------------------------------------- """

    def testInitialSettingfAll(self):
        assert all(self.epanetClass.getLinkInitialSetting() == [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0,
                                                                100.0, 100.0, 100.0, 100.0, 100.0,
                                                                1.0]), "Wrong InitialSetting output"

    def testInitialSettingIndices(self):
        assert all(self.epanetClass.getLinkInitialSetting([1, 5, 10]) == [100.0, 100.0,
                                                                          100.0]), "Wrong InitialSetting output"

    def testInitialSettingIndex(self):
        assert self.epanetClass.getLinkInitialSetting(10) == 100.0, "Wrong InitialSetting output"

    """ ------------------------------------------------------------------------- """

    def testBulkReactionCoeffAll(self):
        assert all(self.epanetClass.getLinkBulkReactionCoeff() == [-0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,
                                                                   -0.5, -0.5, -0.5, -0.5,
                                                                   0.0]), "Wrong BulkReactionCoeff output"

    def testBulkReactionCoeffIndices(self):
        assert all(self.epanetClass.getLinkBulkReactionCoeff([1, 5, 10]) == [-0.5, -0.5,
                                                                             -0.5]), "Wrong BulkReactionCoeff output"

    def testBulkReactionCoeffIndex(self):
        assert self.epanetClass.getLinkBulkReactionCoeff(10) == -0.5, "Wrong BulkReactionCoeff output"

    """ ------------------------------------------------------------------------- """

    def testWallReactionCoeffAll(self):
        assert all(self.epanetClass.getLinkWallReactionCoeff() == [-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0,
                                                                   -1.0, -1.0, -1.0, -1.0,
                                                                   0.0]), "Wrong WallReactionCoeff output"

    def testWallReactionCoeffIndices(self):
        assert all(self.epanetClass.getLinkWallReactionCoeff([1, 5, 10]) == [-1.0, -1.0,
                                                                             -1.0]), "Wrong WallReactionCoeff output"

    def testWallReactionCoeffIndex(self):
        assert self.epanetClass.getLinkWallReactionCoeff(10) == -1.0, "Wrong WallReactionCoeff output"

    """ ------------------------------------------------------------------------- """

    def testLinkTypeAll(self):
        assert self.epanetClass.getLinkType() == ['PIPE', 'PIPE', 'PIPE', 'PIPE', 'PIPE', 'PIPE', 'PIPE',
                                                  'PIPE', 'PIPE', 'PIPE', 'PIPE', 'PIPE',
                                                  'PUMP'], "Wrong LinkType output"

    def testLinkTypeIndices(self):
        assert self.epanetClass.getLinkType([1, 5, 10]) == ['PIPE', 'PIPE', 'PIPE'], "Wrong LinkType output"

    def testLinkTypeIndex(self):
        assert self.epanetClass.getLinkType(13) == 'PUMP', "Wrong LinkType output"

    """ ------------------------------------------------------------------------- """

    def testLinkTypeIndexAll(self):
        assert self.epanetClass.getLinkTypeIndex() == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                                       1, 1, 2], "Wrong LinkTypeIndex output"

    def testLinkTypeIndexIndices(self):
        assert self.epanetClass.getLinkTypeIndex(list(range(5, self.epanetClass.getLinkCount() + 1))) == \
               [1, 1, 1, 1, 1, 1, 1, 1, 2], "Wrong LinkTypeIndex output"

    def testLinkTypeIndexIndex(self):
        assert self.epanetClass.getLinkTypeIndex(13) == 2, "Wrong LinkTypeIndex output"

    """ ------------------------------------------------------------------------- """

    def testLinkStatusAll(self):
        assert all(
            self.epanetClass.getLinkStatus() == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "Wrong LinkStatus output"

    def testLinkStatusIndices(self):
        assert all(self.epanetClass.getLinkStatus(list(range(5, self.epanetClass.getLinkCount() + 1))) == \
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]), "Wrong LinkStatus output"

    def testLinkStatusIndex(self):
        assert self.epanetClass.getLinkStatus(13) == 0, "Wrong LinkStatus output"

    """ ------------------------------------------------------------------------- """

    def testStepbyStepAnalysis(self):
        # Runs hydraulics Step-by-step
        self.epanetClass.openHydraulicAnalysis()
        self.epanetClass.initializeHydraulicAnalysis()
        tstep, T, V, H, F = 1, list(), list(), list(), list()
        index = 1
        while (tstep > 0):
            t = self.epanetClass.runHydraulicAnalysis()
            V.append(self.epanetClass.getLinkVelocity(index))
            H.append(self.epanetClass.getLinkHeadloss(index))
            F.append(self.epanetClass.getLinkFlows(index))
            T.append(t)
            tstep = self.epanetClass.nextHydraulicAnalysisStep()
        self.epanetClass.closeHydraulicAnalysis()
        V_desired = np.array(
            [2.352866658167868, 2.3306833593092215, 2.3166632197802377, 2.3014354684962814, 2.294465806401654,
             2.286139935062943, 2.2859850879557047, 2.284396185662495, 2.2748389650812535, 2.266909416977331,
             2.251123423567716,
             2.2370345272054206, 2.215263054711122, 1.0662692976018556e-06, 1.0566736415735937e-06,
             1.0371486202278355e-06,
             1.015528522999284e-06, 9.971882904769073e-07, 9.829639436645328e-07, 9.704692261235375e-07,
             9.55911660310027e-07,
             9.452347598503036e-07, 9.28221894076609e-07, 9.084721628771827e-07, 2.416368471024177,
             2.4073945733540967,
             2.3857323225219194])
        np.testing.assert_array_almost_equal(V, V_desired, err_msg="Wrong Velocity output")
        H_desired = np.array(
            [19.117018607743262, 18.784557106294415, 18.575821630530413, 18.350323106559813, 18.247536420722895,
             18.125096976393024, 18.12282340051479, 18.099494697653654, 17.95951292501252, 17.843745116056084,
             17.61430252411742, 17.410680708749624,
             17.098168734109322, 3.410605131648481e-11, 3.353761712787673e-11, 3.240074875066057e-11,
             3.115019353572279e-11, 3.012701199622825e-11,
             2.9331204132176936e-11, 2.864908310584724e-11, 2.7853275241795927e-11, 2.7284841053187847e-11,
             2.637534635141492e-11,
             2.5352164811920375e-11, 20.08353269330769, 19.945617762391066,
             19.61450487894149])
        np.testing.assert_array_almost_equal(H, H_desired, err_msg="Wrong HeadLoss output")
        F_desired = [np.array(1866.17582999), np.array(1848.5811499), np.array(1837.46107838)]
        np.testing.assert_array_almost_equal(F[0:3], F_desired, err_msg="Wrong Flows output")

    """ ------------------------------------------------------------------------- """

    def testLinkSettingAll(self):
        assert all(self.epanetClass.getLinkSettings() == [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0,
                                                          100.0, 100.0, 100.0, 100.0, 0.0]), "Wrong LinkSetting output"

    def testLinkSettingIndices(self):
        assert all(self.epanetClass.getLinkSettings(list(range(5, self.epanetClass.getLinkCount() + 1))) == \
                   [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 0.0]), "Wrong LinkSetting output"

    def testLinkSettingIndex(self):
        assert self.epanetClass.getLinkSettings(13) == 0.0, "Wrong LinkSetting output"

    """ ------------------------------------------------------------------------- """

    # *Set Links Data (EXAMPLES)*

    def testSetLinkDiameterAll(self):
        self.epanetClass.setLinkDiameter([2 * i for i in self.epanetClass.getLinkDiameter()])
        assert all(self.epanetClass.getLinkDiameter() == [36.0, 28.0, 20.0, 20.0, 24.0, 12.0, 36.0,
                                                          20.0, 24.0, 16.0, 16.0, 12.0,
                                                          0.0]), "Wrong SetLinkDiameter output"

    def testSetLinkDiameterIndices(self):
        self.epanetClass.setLinkDiameter([2, 3, 4], [200, 250, 350])  # index,  value
        assert all(self.epanetClass.getLinkDiameter([2, 3, 4]) == [200, 250, 350]), "Wrong SetLinkDiameter output"

    def testSetLinkDiameterIndex(self):
        self.epanetClass.setLinkDiameter(2, 200)  # index,  value
        assert self.epanetClass.getLinkDiameter(2) == 200, "Wrong SetLinkDiameter output"

    """ ------------------------------------------------------------------------- """

    def testSetLinkLengthAll(self):
        self.epanetClass.setLinkLength([2 * i for i in self.epanetClass.getLinkLength()])
        assert all(self.epanetClass.getLinkLength() == [21060.0, 10560.0, 10560.0, 10560.0, 10560.0, 10560.0,
                                                        400.0, 10560.0, 10560.0, 10560.0, 10560.0, 10560.0,
                                                        0.0]), "Wrong SetLinkLength output"

    def testSetLinkLengthIndices(self):
        self.epanetClass.setLinkLength([2, 3, 4], [200, 250, 350])  # index,  value
        assert all(self.epanetClass.getLinkLength([2, 3, 4]) == [200, 250, 350]), "Wrong SetLinkLength output"

    def testSetLinkLengthIndex(self):
        self.epanetClass.setLinkLength(2, 500)  # index,  value
        assert self.epanetClass.getLinkLength(2) == 500, "Wrong SetLinkLength output"

    """ ------------------------------------------------------------------------- """

    def testSetLinkRoughnessCoeffAll(self):
        self.epanetClass.setLinkRoughnessCoeff([2 * i for i in self.epanetClass.getLinkRoughnessCoeff()])
        assert all(self.epanetClass.getLinkRoughnessCoeff() == [200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0, 200.0,
                                                                200.0, 200.0, 200.0, 200.0,
                                                                0.0]), "Wrong SetLinkRoughnessCoeff output"

    def testSetLinkRoughnessCoeffIndices(self):
        self.epanetClass.setLinkRoughnessCoeff([2, 3, 4], [200, 250, 350])  # index,  value
        assert all(self.epanetClass.getLinkRoughnessCoeff([2, 3, 4]) == [200, 250,
                                                                         350]), "Wrong SetLinkRoughnessCoeff output"

    def testSetLinkRoughnessCoeffIndex(self):
        self.epanetClass.setLinkRoughnessCoeff(2, 500)  # index,  value
        assert self.epanetClass.getLinkRoughnessCoeff(2) == 500, "Wrong SetLinkRoughnessCoeff output"

    """ ------------------------------------------------------------------------- """

    def testSetLinkMinorLossCoeffAll(self):
        self.epanetClass.setLinkMinorLossCoeff([1.2 for i in self.epanetClass.getLinkMinorLossCoeff()])
        assert all(self.epanetClass.getLinkMinorLossCoeff() == [1.2, 1.2000000000000002, 1.2000000000000002,
                                                                1.2000000000000002, 1.2, 1.2,
                                                                1.2, 1.2000000000000002, 1.2, 1.2, 1.2, 1.2,
                                                                0.0]), "Wrong SetLinkMinorLossCoeff output"

    def testSetLinkMinorLossCoeffIndices(self):
        self.epanetClass.setLinkMinorLossCoeff([2, 3, 4], [1.01, 1.02, 1.01])  # index,  value
        assert all(self.epanetClass.getLinkMinorLossCoeff([2, 3, 4]) == [1.01, 1.02,
                                                                         1.01]), "Wrong SetLinkMinorLossCoeff output"

    def testSetLinkMinorLossCoeffIndex(self):
        self.epanetClass.setLinkMinorLossCoeff(2, 1.01)  # index,  value
        assert self.epanetClass.getLinkMinorLossCoeff(2) == 1.01, "Wrong SetLinkMinorLossCoeff output"

    """ ------------------------------------------------------------------------- """

    def testSetLinkInitialStatusAll(self):
        self.epanetClass.setLinkInitialStatus([0 for i in self.epanetClass.getLinkInitialStatus()])
        assert all(self.epanetClass.getLinkInitialStatus() == [0] * 13), "Wrong SetLinkInitialStatus output"

    def testSetLinkInitialStatusIndices(self):
        self.epanetClass.setLinkInitialStatus([2, 3, 4], [0] * 3)  # index,  value
        assert all(self.epanetClass.getLinkInitialStatus([2, 3, 4]) == [0] * 3), "Wrong SetLinkInitialStatus output"

    def testSetLinkInitialStatusIndex(self):
        self.epanetClass.setLinkInitialStatus(2, 0)  # index,  value
        assert self.epanetClass.getLinkInitialStatus(2) == 0, "Wrong SetLinkInitialStatus output"

    """ ------------------------------------------------------------------------- """

    def testSetLinkBulkReactionCoeffAll(self):
        self.epanetClass.setLinkBulkReactionCoeff([i - 0.055 for i in self.epanetClass.getLinkBulkReactionCoeff()])
        assert all(
            self.epanetClass.getLinkBulkReactionCoeff() == [-0.555, -0.555, -0.555, -0.555, -0.555, -0.555, -0.555,
                                                            -0.555, -0.555, -0.555, -0.555, -0.555,
                                                            0.0]), "Wrong SetLinkBulkReactionCoeff output"

    def testSetLinkBulkReactionCoeffIndices(self):
        self.epanetClass.setLinkBulkReactionCoeff([2, 3, 13], [0.1] * 3)  # index,  value
        assert all(self.epanetClass.getLinkBulkReactionCoeff([2, 3, 13]) == [0.1, 0.1,
                                                                             0.0]), "Wrong SetLinkBulkReactionCoeff " \
                                                                                    "output"

    def testSetLinkBulkReactionCoeffIndex(self):
        self.epanetClass.setLinkBulkReactionCoeff(1, 0.2)  # index,  value
        assert self.epanetClass.getLinkBulkReactionCoeff(1) == 0.2, "Wrong SetLinkBulkReactionCoeff output"

    """ ------------------------------------------------------------------------- """

    def testSetLinkWallReactionCoeffAll(self):
        self.epanetClass.setLinkWallReactionCoeff([i * (-1.1) for i in self.epanetClass.getLinkWallReactionCoeff()])
        assert all(self.epanetClass.getLinkWallReactionCoeff() == [1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1,
                                                                   1.1, 1.1,
                                                                   0.0]), "Wrong SetLinkWallReactionCoeff output"

    def testSetLinkWallReactionCoeffIndices(self):
        self.epanetClass.setLinkWallReactionCoeff([2, 3, 13], [-2] * 3)  # index,  value
        assert all(self.epanetClass.getLinkWallReactionCoeff([2, 3, 13]) == [-2.0, -2.0,
                                                                             0.0]), "Wrong SetLinkWallReactionCoeff " \
                                                                                    "output"

    def testSetLinkWallReactionCoeffIndex(self):
        self.epanetClass.setLinkWallReactionCoeff(2, -2)  # index,  value
        assert self.epanetClass.getLinkWallReactionCoeff(2) == -2, "Wrong SetLinkWallReactionCoeff output"

    """ ------------------------------------------------------------------------- """

    def testSetLinkInitialSettingAll(self):
        linkset = self.epanetClass.getLinkInitialSetting()
        if self.epanetClass.getLinkValveCount():
            linkset[self.epanetClass.getLinkValveIndex()] = 0
        self.epanetClass.setLinkInitialSetting([i * 10 for i in linkset])
        assert all(self.epanetClass.getLinkInitialSetting() == [1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0,
                                                                1000.0, 1000.0, 1000.0, 1000.0, 1000.0,
                                                                10.0]), "Wrong SetLinkInitialSetting output"

    def testSetLinkInitialSettingIndices(self):
        self.epanetClass.setLinkInitialSetting([2, 3, 13], [2] * 3)  # index,  value
        assert all(self.epanetClass.getLinkInitialSetting([2, 3, 13]) == [2] * 3), "Wrong SetLinkInitialSetting output"

    def testSetLinkInitialSettingIndex(self):
        self.epanetClass.setLinkInitialSetting(2, 10)  # index,  value
        assert self.epanetClass.getLinkInitialSetting(2) == 10, "Wrong SetLinkInitialSetting output"

    """ ------------------------------------------------------------------------- """

    def testSetLinkStatusAll(self):
        self.epanetClass.setLinkStatus([1 for i in self.epanetClass.getLinkStatus()])
        assert all(self.epanetClass.getLinkStatus() == [1] * 13), "Wrong SetLinkStatus output"

    def testSetLinkStatusIndices(self):
        self.epanetClass.setLinkStatus([2, 3, 13], [1] * 3)  # index,  value
        assert all(self.epanetClass.getLinkStatus([2, 3, 13]) == [1] * 3), "Wrong SetLinkStatus output"

    def testSetLinkStatusIndex(self):
        self.epanetClass.setLinkStatus(2, 1)  # index,  value
        assert self.epanetClass.getLinkStatus(2) == 1, "Wrong SetLinkStatus output"

    """ ------------------------------------------------------------------------- """

    def testSetLinkSettingsAll(self):
        self.epanetClass.setLinkSettings([i + 10 for i in self.epanetClass.getLinkSettings()])
        assert all(self.epanetClass.getLinkSettings() == [110.0, 110.0, 110.0, 110.0, 110.0, 110.0, 110.0,
                                                          110.0, 110.0, 110.0, 110.0, 110.0,
                                                          10.0]), "Wrong SetLinkSettings output"

    def testSetLinkSettingsIndices(self):
        self.epanetClass.setLinkSettings([2, 3, 13], [10, 15, 20])  # index,  value
        assert all(self.epanetClass.getLinkSettings([2, 3, 13]) == [10, 15, 20]), "Wrong SetLinkSettings output"

    def testSetLinkSettingsIndex(self):
        self.epanetClass.setLinkSettings(2, 10)  # index,  value
        assert self.epanetClass.getLinkSettings(2) == 10, "Wrong SetLinkSettings output"

    """ ------------------------------------------------------------------------- """


if __name__ == "__main__":
    unittest.main()  # run all tests
